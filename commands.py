
CMD_DEVICE_INFO                                                  = 0x0000
CMD_SETUP_WRITE                                                  = 0x0001
CMD_FINISH_WRITE                                                 = 0x0003
CMD_HARDWARE_RESET                                               = 0x0004
CMD_START_FLASH                                                  = 0x0005
CMD_NACK                                                         = 0x00fe
CMD_ACK                                                          = 0x00ff

#For general mucking around
CMD_DEBUG_PRINT_STRING                                           = 0x0100
CMD_DEBUG_PRINT_INTEGERS                                         = 0x0101
CMD_DEBUG_PRINT_BYTES                                            = 0x0102
CMD_LCD_RESET                                                    = 0x0103
CMD_LCD                                                          = 0x0104
CMD_BUFF_CLEAR                                                   = 0x0105
CMD_READ_MEM                                                     = 0x0106
CMD_VERSION                                                      = 0x0107

# For low-frequency tags
CMD_READ_TI_TYPE                                                 = 0x0202
CMD_WRITE_TI_TYPE                                                = 0x0203
CMD_DOWNLOADED_RAW_BITS_TI_TYPE                                  = 0x0204
CMD_ACQUIRE_RAW_ADC_SAMPLES_125K                                 = 0x0205
CMD_MOD_THEN_ACQUIRE_RAW_ADC_SAMPLES_125K                        = 0x0206
CMD_DOWNLOAD_RAW_ADC_SAMPLES_125K                                = 0x0207
CMD_DOWNLOADED_RAW_ADC_SAMPLES_125K                              = 0x0208
CMD_DOWNLOADED_SIM_SAMPLES_125K                                  = 0x0209
CMD_SIMULATE_TAG_125K                                            = 0x020A
CMD_HID_DEMOD_FSK                                                = 0x020B
CMD_HID_SIM_TAG                                                  = 0x020C
CMD_SET_LF_DIVISOR                                               = 0x020D
CMD_LF_SIMULATE_BIDIR                                            = 0x020E
CMD_SET_ADC_MUX                                                  = 0x020F
CMD_HID_CLONE_TAG                                                = 0x0210
CMD_EM410X_WRITE_TAG                                             = 0x0211
CMD_INDALA_CLONE_TAG                                             = 0x0212
# for 224 bits UID
CMD_INDALA_CLONE_TAG_L                                           = 0x0213

# CMD_SET_ADC_MUX: ext1 is 0 for lopkd 1 for loraw 2 for hipkd 3 for hiraw 

# For the 13.56 MHz tags
CMD_ACQUIRE_RAW_ADC_SAMPLES_ISO_15693                            = 0x0300
CMD_ACQUIRE_RAW_ADC_SAMPLES_ISO_14443                            = 0x0301
CMD_READ_SRI512_TAG                                              = 0x0303
CMD_READ_SRIX4K_TAG                                              = 0x0304
CMD_READER_ISO_15693                                             = 0x0310
CMD_SIMTAG_ISO_15693                                             = 0x0311
CMD_RECORD_RAW_ADC_SAMPLES_ISO_15693                             = 0x0312
CMD_ISO_15693_COMMAND                                            = 0x0313
CMD_ISO_15693_COMMAND_DONE                                       = 0x0314
CMD_ISO_15693_FIND_AFI                                           = 0x0315
CMD_ISO_15693_DEBUG                                              = 0x0316

# For Hitag2 transponders
CMD_SNOOP_HITAG                                                  = 0x0370
CMD_SIMULATE_HITAG                                               = 0x0371
CMD_READER_HITAG                                                 = 0x0372

CMD_SIMULATE_TAG_HF_LISTEN                                       = 0x0380
CMD_SIMULATE_TAG_ISO_14443                                       = 0x0381
CMD_SNOOP_ISO_14443                                              = 0x0382
CMD_SNOOP_ISO_14443a                                             = 0x0383
CMD_SIMULATE_TAG_ISO_14443a                                      = 0x0384
CMD_READER_ISO_14443a                                            = 0x0385
CMD_SIMULATE_TAG_LEGIC_RF                                        = 0x0387
CMD_READER_LEGIC_RF                                              = 0x0388
CMD_WRITER_LEGIC_RF                                              = 0x0389
CMD_EPA_PACE_COLLECT_NONCE                                       = 0x038A

CMD_SNOOP_ICLASS                                                 = 0x0392
CMD_SIMULATE_TAG_ICLASS                                          = 0x0393
CMD_READER_ICLASS                                                = 0x0394

# For measurements of the antenna tuning
CMD_MEASURE_ANTENNA_TUNING                                       = 0x0400
CMD_MEASURE_ANTENNA_TUNING_HF                                    = 0x0401
CMD_MEASURED_ANTENNA_TUNING                                      = 0x0410
CMD_LISTEN_READER_FIELD                                          = 0x0420

# For direct FPGA control
CMD_FPGA_MAJOR_MODE_OFF                                          = 0x0500

# For mifare commands
CMD_MIFARE_SET_DBGMODE                                           = 0x0600
CMD_MIFARE_EML_MEMCLR                                            = 0x0601
CMD_MIFARE_EML_MEMSET                                            = 0x0602
CMD_MIFARE_EML_MEMGET                                            = 0x0603
CMD_MIFARE_EML_CARDLOAD                                          = 0x0604
CMD_MIFARE_EML_CSETBLOCK                                         = 0x0605
CMD_MIFARE_EML_CGETBLOCK                                         = 0x0606

CMD_SIMULATE_MIFARE_CARD                                         = 0x0610

CMD_READER_MIFARE                                                = 0x0611
CMD_MIFARE_NESTED                                                = 0x0612

CMD_MIFARE_READBL                                                = 0x0620
CMD_MIFARE_READSC                                                = 0x0621
CMD_MIFARE_WRITEBL                                               = 0x0622
CMD_MIFARE_CHKKEYS                                               = 0x0623

CMD_MIFARE_SNIFFER                                               = 0x0630

CMD_VTA_PLAY                                                     = 0x0700
CMD_VTA_NEWCARD                                                  = 0x0701
CMD_VTA_APDU_REQ                                                 = 0x0702
CMD_VTA_APDU_RES                                                 = 0x0703

CMD_UNKNOWN                                                      = 0xFFFF

