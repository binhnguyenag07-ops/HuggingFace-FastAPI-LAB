
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator
from transformers import pipeline

app = FastAPI(
    title="Sentiment Analysis API",
    description="Sentiment analysis using Hugging Face DistilBERT",
    version="1.0.0"
)

MODEL_NAME = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"

classifier = pipeline(
    task="text-classification",
    model=MODEL_NAME,
    device=-1
)


class PredictRequest(BaseModel):
    text: str = Field(min_length=1, max_length=2000)

    @field_validator("text")
    @classmethod
    def validate_text(cls, value):
        value = value.strip()

        if not value:
            raise ValueError("Text cannot be empty")

        return value


@app.get("/")
def home():
    return {
        "message": "Welcome to Sentiment Analysis API",
        "model": MODEL_NAME
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "model_loaded": classifier is not None
    }


@app.post("/predict")
def predict(request: PredictRequest):
    try:
        result = classifier(
            request.text,
            truncation=True,
            max_length=512
        )[0]

        return {
            "input": request.text,
            "label": result["label"],
            "score": round(float(result["score"]), 4)
        }

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="Model inference failed"
        ) from exc
