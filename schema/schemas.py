import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("keys.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

doc_ref = db.collection("presentation").document("persistent_menu")
doc_ref.set(
    {
        "persistent_menu": [
            {
                "locale": "default",
                "composer_input_disabled": false,
                "call_to_actions": [
                    {"type": "postback", "title": "🛵 Pedido", "payload": "ORDER"},
                    {"type": "postback", "title": "🍔 Menu", "payload": "MENU"},
                    {
                        "type": "postback",
                        "title": "🔖 Promoción",
                        "payload": "PROMOTION",
                    },
                    {
                        "type": "web_url",
                        "title": "⛳ Dirección",
                        "url": "https://www.google.com/maps/place/Burger+King+-+Calima+Bogot%C3%A1/@4.6183277,-74.0881089,17z/data=!3m1!4b1!4m5!3m4!1s0x8e3f997af53516ef:0x22dda215cfc17c9d!8m2!3d4.6183224!4d-74.0859202",
                        "webview_height_ratio": "tall",
                    },
                    {
                        "type": "web_url",
                        "title": "👤 Contacto",
                        "url": "https://api.whatsapp.com/send?phone=3234497863&text=Deseo%20contactarme%20con%20una%20persona",
                        "webview_height_ratio": "full",
                    },
                ],
            }
        ]
    }
)
