from form import Ui_Form
from crc import Crc16CCITT
from interclass import Interl
from scrclass import Scrumble
from generator import Generate

class events(Ui_Form):
    def GeneratorPass(self):
        self.txteditMessage.clear()
        PassString = Generate.passwrd(None)
        self.txteditMessage.insertPlainText(PassString)

    def AllCalc(self):
        InputMessage = self.txteditMessage.toPlainText()

        self.txteditCrc.clear()
        InputCrc = Crc16CCITT.crc16(None, InputMessage)
        self.txteditCrc.insertPlainText(str(InputCrc))

        self.txteditScr.clear()
        InputScr = Scrumble.RealScrumble(None, InputMessage)
        self.txteditScr.insertPlainText(InputScr)

        self.txteditInter.clear()
        InputInter, count = Interl.NormalInterl(None, InputScr)
        result = int(InputInter, 2) # Представляем строку числом
        decode_string = result.to_bytes((result.bit_length()+7) // 8, 'big').decode(encoding='UTF-8',errors='ignore') # Конвертируем
        self.txteditInter.insertPlainText(decode_string)

        self.txteditDeint.clear()
        OutputInter = Interl.NormalDeinterl(None, InputInter, count)
        deint_result = int(OutputInter, 2) # Представляем строку числом
        deint_decode_string = deint_result.to_bytes((deint_result.bit_length()+7) // 8, 'big').decode(encoding='UTF-8',errors='ignore') # Конвертируем обратно
        self.txteditDeint.insertPlainText(deint_decode_string)

        self.txteditDescr.clear()
        OutputDescr = Scrumble.RealUnScrumble(None, deint_decode_string)
        self.txteditDescr.insertPlainText(OutputDescr)

        self.txteditCrcRes.clear()
        OutputCrc = Crc16CCITT.crc16(None, OutputDescr)
        self.txteditCrcRes.insertPlainText(str(OutputCrc))


