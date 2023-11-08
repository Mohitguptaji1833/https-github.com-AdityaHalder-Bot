from pyrogram import Client, idle
from pyrogram import filters

api_id = 12380656
api_hash = "d927c13beaaf5110f25c505b7c071273"
bot_token = "6626130097:AAG5iab-L1-7xYfaDUo57jnANPJj-PhPx0M"

app = Client(
    name = "KAALWARE",
    api_id = api_id,
    api_hash = api_hash,
    bot_token = bot_token,
)


@app.on_message(filters.command("start") & filters.private)
async def start_message(client, message):
    message.reply_text(f"Hello, {message.from_user.mention}")





app.start()
print("Bot Started")
idle()
