import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from bot.post import getUser, post

cred = credentials.Certificate("bot/keys/keys.json")
firebase_admin.initialize_app(cred)

db = firestore.client()



async def action(senderId: str, intent: str):

        data = db.collection("customer").document(senderId).get()
        if(data.to_dict() == None):
            user = getUser(senderId)
            data = db.collection("customer").document(senderId).set(user)

        match intent:
            case 'MENU':
                data = db.collection("template").document("generic").get()
            case 'ORDER':
                data = db.collection("template").document("generic").get() 
            case 'STARTED':
                data = db.collection("template").document("generic").get()
        
        await post(senderId, message="message", payload=data.to_dict())

