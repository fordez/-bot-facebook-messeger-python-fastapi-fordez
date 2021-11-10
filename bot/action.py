import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from bot.post import post

cred = credentials.Certificate("bot/keys/keys.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


async def action(senderId: str, intent: str):
        match intent:
            case 'menu':
                data = db.collection("template").document("generic").get()
            case 'orden':
                print('orden listo')

        await post(senderId, message='message', payload=data.to_dict())


