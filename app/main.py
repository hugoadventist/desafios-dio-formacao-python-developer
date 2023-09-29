"""API to convert currencies at BRL to another one.

Returns:
    dict: a json file currencies converted from BRL.
"""
from fastapi import FastAPI
import uvicorn
from src.routers import convert

app = FastAPI()


if __name__ == "__main__":
    uvicorn.run(convert.app, port=8000)
