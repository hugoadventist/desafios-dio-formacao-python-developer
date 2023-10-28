"""API to convert currencies at BRL to another one.

Returns:
    dict: a json file currencies converted from BRL.
"""
from fastapi import FastAPI
import uvicorn
from . import convert

app = FastAPI()

app.include_router(convert.router)

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
