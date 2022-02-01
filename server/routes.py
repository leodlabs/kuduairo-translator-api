from fastapi import APIRouter
from models.Translation import Translation
from lib.kuduairo_translator.entrypoint import translate

router = APIRouter()

@router.post("/pt-to-kd/")
def brazilian_portuguese_to_kuduairo(translation: Translation):
    return {
        'status': 'success',
        'current_language': translation.target_language,
        'original_language': translation.current_language,
        'translation': translate(translation.sentence)
    }
