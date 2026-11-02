
from transformers import pipeline

MODEL_NAME = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"

print("Loading Hugging Face model...")

classifier = pipeline(
    task="text-classification",
    model=MODEL_NAME,
    device=-1
)

print("Model loaded successfully!")

texts = [
    "I love this movie. It is amazing!",
    "This movie is terrible. I hate it."
]

for text in texts:
    result = classifier(text)[0]

    print("\nInput:", text)
    print("Sentiment:", result["label"])
    print("Confidence:", round(result["score"], 4))
