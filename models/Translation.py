from pydantic import BaseModel, validator

class Translation(BaseModel):
    sentence: str
    current_language: str
    target_language: str
    @validator('current_language', 'target_language')
    def current_language_must_be_in_languages(cls, language):
        languages=["pt-BR", "pt-KD"]
        if language not in languages:
            raise ValueError(f'must be in {languages}')
        return language
