from lib.kuduairo_translator.phonemestable import phonemes_dict

class Entrypoint:
    @staticmethod
    def pt_to_kd(text):
        for i, j in phonemes_dict.items():
            text = text.replace(i, j)
        return text
    

