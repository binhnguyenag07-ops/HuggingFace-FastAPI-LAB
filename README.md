
# Sentiment Analysis API

## 1. Student Information

- Full Name: Nguyễn Cao An Bình
- Student ID: 25127183
- Course: Computational Thinking
- Assignment: Lab 2 - API

## 2. Project Description

This project implements a Sentiment Analysis API
using FastAPI and a pretrained Hugging Face model.

The API accepts English text and predicts whether
the sentiment is POSITIVE or NEGATIVE.

## 3. Hugging Face Model

Model: DistilBERT (SST-2)

Model URL:
https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english

Task: Text Classification / Sentiment Analysis

## 4. Technologies

- Python
- FastAPI
- Hugging Face Transformers
- PyTorch
- Requests
- Uvicorn

## 5. Installation

Clone the repository:

    git clone https://github.com/binhnguyenag07-ops/HuggingFace-FastAPI-LAB.git

Navigate to the project directory:

    cd HuggingFace-FastAPI-LAB

Create a virtual environment (Windows):

    python -m venv .venv

Install dependencies (CPU version):

    .\.venv\Scripts\python.exe -m pip install -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cpu

## 6. Running the Application

Start the FastAPI server:

    .\.venv\Scripts\python.exe -m uvicorn main:app --reload

API URL:

http://127.0.0.1:8000

Swagger UI:

http://127.0.0.1:8000/docs

The Hugging Face model is downloaded automatically
when the application starts for the first time.

## 7. API Endpoints

### GET /

Returns basic information about the API.

### GET /health

Returns the operational status of the application.

### POST /predict

Accepts text and returns the predicted sentiment.

Example Request:

    {
      "text": "I love this movie!"
    }

Example Response:

    {
      "input": "I love this movie!",
      "label": "POSITIVE",
      "score": 0.9999
    }

The score may vary depending on the input.

## 8. Input Validation

The API validates incoming requests.

Invalid requests return HTTP 422.

Examples include:

- Missing text field
- Empty text
- Whitespace-only text
- Invalid data type
- Text longer than 2000 characters
- Malformed JSON

Model inference failures return HTTP 500.

## 9. API Testing

Make sure the FastAPI server is running.

Run the API tests:

    .\.venv\Scripts\python.exe test_api.py

Run the additional validation tests:

    .\.venv\Scripts\python.exe test_validation.py

## 10. Demonstration Video

Video URL: https://drive.google.com/drive/u/0/folders/1a1sSM0p8MZuvaVxFf9UobNg8QBiIHHJ3

The video demonstrates:

- Introduction to the Hugging Face model
- Source code structure
- Running the FastAPI application
- Testing the API with different inputs
- Explanation of prediction results
