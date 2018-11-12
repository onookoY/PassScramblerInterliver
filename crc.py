class Crc16CCITT(object):

    def crc16(self, message):
        crc = 0x0000
        for i in message:
            crc ^= (ord(i)<<8)
            for j in range(8):
                if crc & 0x0001 != 0:
                    crc <<= 1
                    crc ^= 0x1021
                else:
                    crc <<= 1
        return(crc)