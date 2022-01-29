from fastapi import FastAPI
from models.Translation import Translation
from lib.kuduairo_translator.entrypoint import Entrypoint
import uvicorn

app = FastAPI()

@app.post("/pt-to-kd/")
def brazilian_portuguese_to_kuduairo(translation: Translation):
    kuduairo_phonemes = [
        "uro"
    ]
        
    brazilian_portuguese_phonemes = [
        "uairo"
    ]
    current_sentence = translation.sentence


    return {'message': current_sentence.replace('uro', 'uairo')}

@app.post("/kd-to-pt/")                             
def kuduairo_to_brazilian_portuguese(translation: Translation):
    return {'message': 'not available yet'}

if __name__=='__main__':
    uvicorn.run(app)