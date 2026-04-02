import os
import asyncio
from telethon import TelegramClient, events

# --- CONFIGURATION WRAPPERS ---
# Using int() to force numerical format and .get() to prevent 'KeyError' crashes
try:
    API_ID = int(os.environ.get("API_ID", 0))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    # Wrapped to ensure this is always a number
    COMMANDER_ID = int(os.environ.get("COMMANDER_ID", 0))
except ValueError:
    print("❌ ERROR: API_ID or COMMANDER_ID must be a number in Railway Variables!")

# Initialize the Client
client = TelegramClient('ghost_session', API_ID, API_HASH)

# --- BRAIN 1: THE RESPONDER ---
@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.reply("🔱 GHOST-V1 ONLINE. System is active, Commander.")

@client.on(events.NewMessage)
async def handle_all(event):
    # Logic to prevent the bot from responding to itself or double-responding
    if event.is_private and event.message.text != '/start':
        await event.reply("Message received. The 16-brain hierarchy is listening.")

# --- THE ENGINE CORE ---
async def main():
    print("🛰️ Booting Ghost Engine...")
    
    await client.start(bot_token=BOT_TOKEN)
    print("✅ Connection to Telegram established.")

    # --- THE SAFETY WRAPPER ---
    # This prevents the 'resolve_peer' crash from killing the bot
    try:
        if COMMANDER_ID != 0:
            await client.send_message(COMMANDER_ID, "🔱 GHOST-V1 ONLINE")
            print(f"🚀 Startup signal sent to Commander: {COMMANDER_ID}")
    except Exception as e:
        print(f"⚠️ Startup signal bypassed: {e}. (Bot is still running!)")

    print("📡 Ghost Engine is now idling in the cloud. Waiting for commands...")
    await client.run_until_disconnected()

if __name__ == '__main__':
    # Standard Python loop for asynchronous scripts
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Engine stopped by user.")
