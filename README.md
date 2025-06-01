# 🐶 Veterinary Dog Microservice

This is a FastAPI-based microservice for managing dog data in a veterinary clinic.  
The API is built based on the provided OpenAPI specification (`clinic.yaml`).

## 🌐 Deployed Version

The service is deployed on Render and publicly available at:

👉 https://vet-clinic-3r2z.onrender.com/docs

## 📦 Features

- List all dogs or filter by breed (`/dog`)
- Create a new dog entry (`POST /dog`)
- Get or update a dog by ID (`/dog/{pk}`)
- Return server timestamp (`POST /post`)
- Simple root endpoint (`GET /`)

## 🚀 Tech Stack

- Python 3.10+
- FastAPI
- Uvicorn (for ASGI server)

## 📂 Project Structure
pets/

└── main.py        # FastAPI app

clinic.yaml         # OpenAPI 3.0 spec

requirements.txt    # Python dependencies

README.md

LICENCE       # MIT License. Feel free to use and modify.
