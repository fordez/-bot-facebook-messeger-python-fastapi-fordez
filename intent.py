from schemas import SchemaRequest
from fastapi import APIRouter
from fastapi import FastAPI, Request, Response
import requests
from google.cloud import dialogflow_v2beta1 as dialogflow


verify_token = "bot-fordez"
page_access_token = ""


api = APIRouter()


@api.get("/webhook")
async def verify(request: Request):
    if request.query_params.get("hub.verify_token") == verify_token:
        return Response(content=request.query_params["hub.challenge"])
    else:
        return Response(content="Se requiere un token de verificacion", status_code=400)


@api.post("/webhook")
def webhook(data: SchemaRequest):
    dta = data.entry[0]
    messaging = list(
        map(lambda messaging: messaging['messaging'], data.entry))
    senderId = list(
        map(lambda senderId: senderId['sender']['id'], messaging[0]))
    message = list(
        map(lambda message: message['message']['text'], messaging[0]))
    print(senderId[0])
    print(message[0])

    return Response("ok", status_code=200)
