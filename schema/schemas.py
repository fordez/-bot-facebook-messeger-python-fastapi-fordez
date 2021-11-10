import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("keys.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

doc_ref = db.collection("template").document("generic")
doc_ref.set(
    {
        "attachment": {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Welcome!",
                        "image_url": "https://petersfancybrownhats.com/company_image.png",
                        "subtitle": "We have the right hat for everyone.",
                        "buttons": [
                            {
                                "type": "web_url",
                                "url": "https://petersfancybrownhats.com",
                                "title": "View Website",
                            },
                            {
                                "type": "postback",
                                "title": "Start Chatting",
                                "payload": "DEVELOPER_DEFINED_PAYLOAD",
                            },
                        ],
                    }
                ],
            },
        }
    }
)
