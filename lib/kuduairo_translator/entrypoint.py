from lib.kuduairo_translator.phonemestable import PhonemesTable

class Entrypoint:
    def __init__(self, sentence, current_language, target_language):
        self.sentence = sentence
        self.current_language = current_language
        self.target_language = target_language
        self.phonemes = PhonemesTable()

    def set_sentence(self, sentence):
        self.sentence = sentence
    
    def get_sentence(self):
        return self.sentence

    def translate(self):
        pt_KD = self.phonemes.get_kuduairo_phonemes
        pt_BR = self.phonemes.get_brazilian_portuguese_phonemes

        for index in range(pt_BR.len()):
            self.set_sentence = self.sentence.replace(pt_BR[index], pt_KD[index])

        return self.sentence

