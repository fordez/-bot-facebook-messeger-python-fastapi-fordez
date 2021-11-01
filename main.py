from fastapi import FastAPI
from intent import api


bot = FastAPI()

bot.include_router(api)
