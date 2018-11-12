class Scrumble(object):

    def RealScrumble(self, polyA):       
        polyB = 0b11111111 #устанавливаем исходное значение
        return ''.join([chr(ord(c) ^ ((polyB & 0b00000010) ^ (polyB & 0b00000001))) for c in polyA])
        # устанавливаем старший и последующий регистр в 1
        # это все складываем с битом сообщения
        # соединяем в строку и выводим

 
    def RealUnScrumble(self, polyA):    
        polyB = 0b11111111
        return ''.join([chr(ord(c) ^ ((polyB & 0b00000010) ^ (polyB & 0b00000001))) for c in polyA])
        # дескремблируем в обратную сторону