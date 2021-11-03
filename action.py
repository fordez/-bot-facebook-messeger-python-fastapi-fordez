from sheets import query_sheets
import httpx

SPREADSHEET_ID = '1honsjXD0qIiF50-KDjDFFpw79Wa_-nbXPE4yUEdj0WY'
range = 'Menu!A1:B5'

menu_persistent = query_sheets(SPREADSHEET_ID, range)


async def send_message(
    page_access_token: str,
    recipient_id: str,
    message_text: str,
    message_type: str = "RESPONSE",
):
    r = httpx.post(
        "https://graph.facebook.com/v12.0/me/messages",
        params={"access_token": page_access_token},
        headers={"Content-Type": "application/json"},
        json={
            "recipient": {"id": recipient_id},
            "message": {"text": message_text},
            "messaging_type": message_type,
        },
    )
    r.raise_for_status()
