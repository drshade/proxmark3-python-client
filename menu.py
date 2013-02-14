
import commands
from collections import namedtuple

menu = {
    'hw' : {
        'tune'      : commands.CMD_MEASURE_ANTENNA_TUNING,
        'tunehf'    : commands.CMD_MEASURE_ANTENNA_TUNING_HF,
    },

    'hf'            : {},
    'lf'            : {},
    'data'          : {},

    'vta' : {
        'play'      : commands.CMD_VTA_PLAY,
    },
}

def parseCommand(cmd_string):

    def walk(cmd_list, current_item):
        if len(cmd_list) == 0:

            if isinstance(current_item, (int, long)):
                # Hit an actual command
                #
                return (current_item, None)
            else:
                # Hit a menu
                #
                return (None, current_item)

        if not current_item.has_key(cmd_list[0]):
            print '* Unknown command "%s"!'%(cmd_list[0])
            return (None, current_item)
        else:
            return walk(cmd_list[1:], current_item[cmd_list[0]])

    (cmd, current_item) = walk(cmd_string.split(' '), menu)
    if cmd is not None:
        return (cmd, 0, 0, 0)

    else:
        print 'Help: %s'%(current_item)
        return (None, None, None, None)



