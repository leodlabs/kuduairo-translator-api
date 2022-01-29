from fastapi import FastAPI
from models.Translation import Translation
from lib.kuduairo_translator.entrypoint import Entrypoint as Translator
import uvicorn

app = FastAPI()
translator = Translator()

@app.get("/")
def index():
    return { 'status': 'OK' }

@app.post("/pt-to-kd/")
def brazilian_portuguese_to_kuduairo(translation: Translation):
    return {
        'status': 'success',
        'current_language': translation.target_language,
        'original_language': translation.current_language,
        'translation': translator.pt_to_kd(translation.sentence)
    }

@app.post("/kd-to-pt/")                             
def kuduairo_to_brazilian_portuguese(translation: Translation):
    return {'message': 'not available yet'}

if __name__=='__main__':
    uvicorn.run(app)