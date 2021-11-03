from schemas import SchemaRequest
from action import send_message
from fastapi import APIRouter
from fastapi import Request, Response
import requests


verify_token = "bot-fordez"
page_access_token = "EAAGy5yDAkIoBAMGmQJiisZA92nm7SsakDinigipBWd52Y0A3kWWjEsnVr1G29RvKALz2HR6d2ONicWSni5ZAFOy8Fafelu4UOOg3rmJe291hOWKASRvW482yLiH40MhIcooqYWFcJwJ7SkqBJ8noZAuatZCn1YQkmDbvZAU7xgwt9sXbECKEx"


api = APIRouter()


@api.get("/webhook")
async def verify(request: Request):
    if request.query_params.get("hub.verify_token") == verify_token:
        return Response(content=request.query_params["hub.challenge"])
    else:
        return Response(content="Se requiere un token de verificacion", status_code=400)


@api.post("/webhook")
async def webhook(data: SchemaRequest):

    messaging = data.entry[0]['messaging']
    senderId = messaging[0]['sender']['id']
    if messaging[0].get('message'):
        intent = messaging[0]['message']['text']
    else:
        intent = messaging[0]['postback']['payload']

    print(senderId)
    print(intent)
    await send_message(page_access_token, senderId, intent)
    return Response(status_code=200)
