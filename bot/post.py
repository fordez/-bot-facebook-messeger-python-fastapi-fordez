from typing import Any
import httpx, requests

access_token = "EAAGy5yDAkIoBAJPgAkeGYSCKZChoN708kdRGUlejrs5EgZBUINZAZABZCQZC1mNwjNRuFFII2IU5rkPSZA3UjAP9WhJWzuhJbrslUS4xvzEsq0F7DYVvXARbMNMqEYDRJdOY1CINYCXSR2JzeZCqsdZBflCdjWlCTkHi2YVBZAXtq922zvTaOkL4uA"


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


def getUser(senderId: str):
    response = requests.get(
        f"https://graph.facebook.com/{senderId}?fields=first_name,last_name&access_token={access_token}"
    )
    user = response.json()
    return user
