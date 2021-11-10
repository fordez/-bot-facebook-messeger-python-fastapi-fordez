from fastapi import APIRouter, Request, Response
from pydantic import BaseModel
from typing import List
from bot.post import post
from bot.action import action


api = APIRouter()

verify_token = "bot-fordez"


@api.get("/webhook")
async def verify(request: Request):
    if request.query_params.get("hub.verify_token") == verify_token:
        return Response(content=request.query_params["hub.challenge"])
    else:
        return Response(content="Se requiere un token de verificacion", status_code=400)


class SchemaRequest(BaseModel):
    entry: List = []


@api.post("/webhook")
async def webhook(data: SchemaRequest):
    messaging = data.entry[0]["messaging"]
    senderId = messaging[0]["sender"]["id"]
    await post(senderId, message="sender_action", payload="typing_on")

    if messaging[0].get("message"):
        intent = messaging[0]["message"]["text"]
    else:
        intent = messaging[0]["postback"]["payload"]
        await action(senderId, intent)

    return Response(status_code=200)
