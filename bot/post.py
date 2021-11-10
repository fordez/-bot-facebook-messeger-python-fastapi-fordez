from typing import Any
import httpx

access_token = "EAAGy5yDAkIoBANeBCTqamKyhdkgZCVZBtrAuN8LU6s42SjerpkmTCNJzZChCFVGuPrmDZBvVvHKELZC7jDAYfCHpmMtRnaBvO36JFLDhKfstbiHOCBFyMsuyVJc4gBVSeskCUYFhZCApubpMEVaPEgGmCs953o6pMdbN3pEditN00YcPLjVcea"


async def post(
    senderId: str,
    message: str,
    payload: Any,
):
    response = httpx.post(
        "https://graph.facebook.com/v12.0/me/messages",
        params={"access_token": access_token},
        headers={"Content-Type": "application/json"},
        json={
            "recipient": {"id": senderId},
            "messaging_type": "RESPONSE",
            message: payload,
        },
    )
    response.raise_for_status()
