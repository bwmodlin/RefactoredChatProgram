CLOCKSPEED = 0.05

BIT_RATE = 2000

LINK_MODE = "WAVE"

BIT_STUFF_RUN_LENGTH = 3

START_SEQUENCE = "0101001001110111"

STOP_SEQUENCE = "0101100101110111"

TABLE_HEADER = "0101000010001000100010"

HEADER_LENGTH = len(TABLE_HEADER)

GPIO_TRANSMITTER_NUMBER = lambda port: 27 - (2 * (port - 1))

GPIO_RECEIVER_NUMBER = lambda port : 26 - (2 * (port - 1))

UPDATE_TABLE_INTERVAL = 15
