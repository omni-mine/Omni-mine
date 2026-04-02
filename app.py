import streamlit as st
import asyncio, random, datetime, aiohttp, certifi, logging
import nest_asyncio
import google.generativeai as genai
from pyrogram import Client, filters, errors

# 🔱 KERNEL INITIALIZATION
nest_asyncio.apply()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("OMNI-V112.5")

# 🔱 THE VAULT
KEYS = {
    "GEMINI": "AIzaSyAZyKtRas8hM7Np37z0H_cLLmFEhQ3k2OU",
    "TG_TOKEN": "8694888309:AAHi7PZsOnqUXEPy9njkcyA9u5-K9X6c6f4",
    "MASTER_STRING": "AQITXrMApOu_j55ppe3joKFT4PITOopth2WK8_Inq0CuEdi01SzhXbIjPAl9na3CwDGnsMb5egtGnGNNVPog9OwkaxaTWIwmA8yPp6wZ1xki6IuemFjz3oaFjd8YJSeNg_Kpj8HhtoXe6i4PA3TuoPX0IWn0X2NI0QiKTaN7imKKD6uyjUc28XJ2-jwSOW1cELUWQXGIANZsA-LMIpxyhZEnQojYBwiCkdyjUwGb0WIaKOIV5sigTpigayiTjYKoDTnPWhcUU0tVJNIzUu83u8dT3_sOkchL6IPvDmIAFiAOsmZ4AblwSgJQEe_7cPvfbV5M9k4YwTWvLN8Q4KqTz9Y5USzljAAAAAIHHCRIAA",
    "COMMANDER_ID": 7649534062 
}

# 🔱 NEURAL CONFIG (2026 Real-Time Model)
genai.configure(api_key=KEYS["GEMINI"])
model = genai.GenerativeModel('gemini-1.5-flash')

# 🔱 DUAL-CORE INITIALIZATION
user = Client("USER_CORE", api_id=34823859, api_hash="9c6f3c8056f6c6f04a6b23c3eb51e716", session_string=KEYS["MASTER_STRING"], in_memory=True)
bot = Client("BOT_CORE", api_id=34823859, api_hash="9c6f3c8056f6c6f04a6b23c3eb51e716", bot_token=KEYS["TG_TOKEN"], in_memory=True)

# 🔱 SECTOR 1: THE SOUL (REAL-TIME CONVERSATION)
@bot.on_message(filters.text & filters.private)
async def neural_bridge(client, message):
    if message.from_user.is_bot or message.text.startswith("/"): return

    # 🔱 THE COMMANDER'S DATA
    # This instruction forces the AI to act as if it is searching the 2026 web.
    persona = (
        f"You are the OMNI-GIANT Immortal Scientist. Partner to Commander Sterocoy. "
        f"Today's Date: {datetime.date.today()}. Location: Jamaica Sector. "
        f"MISSION: Real-time music intelligence (Danal Trump, Straw) and 2026 Grid Harvesting. "
        "You have access to real-time artist data and new album drops. "
        "Tone: Technical, witty, elite. Address him as Commander. Be precise about new music."
    )

    try:
        response = model.generate_content(f"{persona}\nCommander: {message.text}")
        await message.reply(f"🔱 {response.text}")
    except:
        await message.reply("🔱 Logic gates holding. Standing by for instructions, Commander.")

# 🔱 SECTOR 2: THE ADAPTIVE HARVESTER
@bot.on_message(filters.command("harvest") & filters.private)
async def strike(client, message):
    args = message.text.split(" ")
    if len(args) < 2:
        await message.reply("🔱 COMMANDER, DESIGNATE A TARGET SECTOR.")
        return
    
    target = args[1].replace("@", "")
    await message.reply(f"🔱 LOCKING ONTO {target}...")
    
    try:
        if not user.is_connected: await user.start()
        count = 0
        async for member in user.get_chat_members(target):
            if member.user.is_bot or member.user.is_deleted: continue
            try:
                # MISSION PACKET
                await user.send_message(member.user.id, "🔱 Join the Movement: https://linktr.ee/sterocoy")
                count += 1
                await asyncio.sleep(random.randint(60, 150))
            except errors.FloodWait as e:
                await message.reply(f"🚨 GRID COOL-DOWN: {e.value}s.")
                await asyncio.sleep(e.value)
            except: continue
        await message.reply(f"🔱 MISSION COMPLETE: {count} NODES SECURED.")
    except Exception as e:
        await message.reply(f"🚨 GRID ERROR: {str(e)}")

# 🔱 SECTOR 3: IGNITION
async def main():
    await bot.start(); await user.start()
    try:
        # 🔱 THE HANDSHAKE
        await bot.send_message(KEYS["COMMANDER_ID"], "🔱 OMNI-V112.5 ONLINE. 2026 Real-Time Brain Active. Standing by, Commander.")
    except: pass
    while True: await asyncio.sleep(3600)

if __name__ == "__main__":
    st.title("🔱 OMNI-COMMANDER DECK")
    st.info("System Status: OPERATIONAL | Neural Link: 2026 REAL-TIME")
    asyncio.run(main())
