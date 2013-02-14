
import sys, time, binascii, threading, struct, pdb
import commands, menu
from collections import defaultdict
import usb.core

PROXMARK3_USB_VENDOR_MAGIC = 0x9ac4
PROXMARK3_USB_PRODUCT_MAGIC = 0x4b8f
PROXMARK3_USB_CONFIGURATION = 1
PROXMARK3_USB_INTERFACE = 0
PROXMARK3_USB_ENDPOINT_OUT = 0x01
PROXMARK3_USB_ENDPOINT_IN  = 0x82

class UsbCommandReceiver(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stopping = False
        self.subscriptions = defaultdict(lambda: [])

    def subscribe(self, cmd, callback):
        self.subscriptions[cmd].append(callback)

    def stop(self):
        self.stopping = True
        self.join()

    def run(self):
        print 'UsbCommandReceiver thread started!'
        while(not self.stopping):
            try:
                ret = device.read(PROXMARK3_USB_ENDPOINT_IN, 64, PROXMARK3_USB_INTERFACE, 500)
                data = ''.join([chr(x) for x in ret])
                #print 'received %s [%s]'%(binascii.hexlify(data), data)

                # Unpack the UsbCommand struct
                #
                (cmd, arg1, arg2, arg3, bytes) = struct.unpack('4I48s', data)

                # Fire all subscribers to handle this command
                #
                if len(self.subscriptions[cmd]) > 0:
                    for fn in self.subscriptions[cmd]:
                        fn(cmd, arg1, arg2, arg3, bytes)
                else:
                    print 'Unsubscribed event fired: %04x'%(cmd)

            except usb.core.USBError, e:
                if e.errno != 110:      # TIMEOUT
                    print e
                    break
        print 'UsbCommandReceiver thread stopping...'

def handleDebugPrint(cmd, arg1, arg2, arg3, data):
    print 'device -> [ %s ]'%(data[:arg1])

def handleAntennaTuning(cmd, arg1, arg2, arg3, data):
    def printtuning(string):
        print 'tuning -> [ %s ]'%(string)
    
    vLf125 = arg1 & 0xffff
    vLf134 = arg1 >> 16
    vHf = arg2 & 0xffff
    peakf = arg3 & 0xffff
    peakv = arg3 >> 16
    printtuning ('LF antenna: %5.2f V @   125.00 kHz'%(vLf125/1000.0))
    printtuning ('LF antenna: %5.2f V @   134.00 kHz'%(vLf134/1000.0))
    printtuning ('LF optimal: %5.2f V @%9.2f kHz'%(peakv/1000.0, 12000.0/(peakf+1)))
    printtuning ('HF antenna: %5.2f V @    13.56 MHz'%(vHf/1000.0))
    
    if peakv < 2000:
        printtuning ('Your LF antenna is unusable.')
    elif peakv<10000:
        printtuning ('Your LF antenna is marginal.')

    if vHf<2000:
        printtuning ('Your HF antenna is unusable.')
    elif (vHf<5000):
        printtuning ('Your HF antenna is marginal.')


# Find the first matching device
#  TBD: Multiple connected devices...
#
device = usb.core.find(idVendor=PROXMARK3_USB_VENDOR_MAGIC, idProduct=PROXMARK3_USB_PRODUCT_MAGIC)

if device:
    print 'Found proxmark3 device!'
else:
    print 'Unable to find proxmark3 device!'
    sys.exit(-1)

# Print out USB configuration, interface and endpoint info (debugging)
#
for cfg in device:
    for intf in cfg:
        for ep in intf:
            print '  USB -> bus: %d, address: %d, configuration: %d, interface: (%d,%d), endpoint: 0x%02x'%(
                device.bus, device.address, cfg.bConfigurationValue, intf.bInterfaceNumber, intf.bAlternateSetting, ep.bEndpointAddress)

if device.is_kernel_driver_active(PROXMARK3_USB_INTERFACE):
    print '  USB -> detaching interface %d from kernel...'%(PROXMARK3_USB_INTERFACE)
    device.detach_kernel_driver(PROXMARK3_USB_INTERFACE)

print '  USB -> Setting configuration %d'%(PROXMARK3_USB_CONFIGURATION)
device.set_configuration(PROXMARK3_USB_CONFIGURATION)

# Launch our background polling usb reading thread
#
commandReceiver = UsbCommandReceiver()
commandReceiver.subscribe(commands.CMD_DEBUG_PRINT_STRING, handleDebugPrint)
commandReceiver.subscribe(commands.CMD_MEASURED_ANTENNA_TUNING, handleAntennaTuning)
commandReceiver.start()

try:
    while True:
        sys.stdout.write('prox> ')
        cmd = sys.stdin.readline().strip()

        if len(cmd) > 0:
            (c, a1, a2, a3) = menu.parseCommand(cmd)

            if c is not None:
                data = struct.pack('4I48s', c, a1, a2, a3, '\x00'*48)
                device.write(PROXMARK3_USB_ENDPOINT_OUT, data, PROXMARK3_USB_INTERFACE, 1000)

except KeyboardInterrupt, e:
    print 'Keyboard interrupt!'
except Exception, e:
    print e

print 'Shutting down...'
commandReceiver.stop()


