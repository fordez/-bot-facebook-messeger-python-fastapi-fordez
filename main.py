from fastapi import FastAPI
from bot.intent import api


bot = FastAPI()

bot.include_router(api)
