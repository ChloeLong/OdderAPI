from fastapi import FastAPI
from os import listdir, getcwd
import random

app = FastAPI()

@app.get("/Otter")
def getOtter():
    return {'url': random.choice(listdir(getcwd() + "/Images"))}
