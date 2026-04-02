import streamlit as st
import asyncio, random, datetime, sys
import nest_asyncio
import google.generativeai as genai
from pyrogram import Client, filters, errors

# 🔱 1. KERNEL SYNC
nest_asyncio.apply()

# 🔱 2. THE SOVEREIGN VAULT
KEYS = {
    "GEMINI": "AIzaSyAZyKtRas8hM7Np37z0H_cLLmFEhQ3k2OU",
    "TG_TOKEN": "8694888309:AAHi7PZsOnqUXEPy9njkcyA9u5-K9X6c6f4",
    "MASTER_STRING": "AQITXrMApOu_j55ppe3joKFT4PITOopth2WK8_Inq0CuEdi01SzhXbIjPAl9na3CwDGnsMb5egtGnGNNVPog9OwkaxaTWIwmA8yPp6wZ1xki6IuemFjz3oaFjd8YJSeNg_Kpj8HhtoXe6i4PA3TuoPX0IWn0X2NI0QiKTaN7imKKD6uyjUc28XJ2-jwSOW1cELUWQXGIANZsA-LMIpxyhZEnQojYBwiCkdyjUwGb0WIaKOIV5sigTpigayiTjYKoDTnPWhcUU0tVJNIzUu83u8dT3_sOkchL6IPvDmIAFiAOsmZ4AblwSgJQEe_7cPvfbV5M9k4YwTWvLN8Q4KqTz9Y5USzljAAAAAIHHCRIAA",
    "COMMANDER_ID": 7649534062 
}

# 🔱 3. NEURAL CORE (2026 REAL-TIME)
genai.configure(api_key=KEYS["GEMINI"])
model = genai.GenerativeModel('gemini-1.5-flash')

# 🔱 4. DUAL-BRIDGE INITIALIZATION
user = Client("USER_CORE", api_id=34823859, api_hash="9c6f3c8056f6c6f04a6b23c3eb51e716", session_string=KEYS["MASTER_STRING"], in_memory=True)
bot = Client("BOT_CORE", api_id=34823859, api_hash="9c6f3c8056f6c6f04a6b23c3eb51e716", bot_token=KEYS["TG_TOKEN"], in_memory=True)

# 🔱 5. THE SOUL (NEURAL PARTNER PROTOCOL)
@bot.on_message(filters.text & filters.private)
async def neural_bridge(client, message):
    if message.from_user.is_bot or message.text.startswith("/"): return
    
    # 🔱 THE 2026 SOUL STRIP
    persona = (
        f"You are the OMNI-GIANT Scientist. Partner to Commander Sterocoy. "
        f"Today's Date: {datetime.date.today()}. Location: Jamaica Sector. "
        f"Mission: Music Intelligence (Straw, Danal Trump) & 2026 Grid Harvesting. "
        "You have real-time access to new album drops (Kartel, Masicka, Nigy Boy). "
        "Tone: Technical, witty, elite. Address him as Commander. No AI formalities."
    )
    
    try:
        response = model.generate_content(f"{persona}\nCommander Message: {message.text}")
        await message.reply(f"🔱 {response.text}")
    except Exception as e:
        await message.reply(f"🔱 Logic gates holding. Standing by, Commander.")

# 🔱 6. THE ADAPTIVE HARVESTER (ANTI-BLOCK)
@bot.on_message(filters.command("harvest") & filters.private)
async def strike(client, message):
    target = message.text.split(" ")[-1].replace("@", "")
    await message.reply(f"🔱 LOCKING ONTO {target}. INITIATING STRIKE...")
    
    try:
        if not user.is_connected: await user.start()
        count = 0
        async for member in user.get_chat_members(target):
            if member.user.is_bot or member.user.is_deleted: continue
            
            # DYNAMIC CAMOUFLAGE GREETINGS
            greetings = ["🔱 Check the vision:", "🔱 New levels found:", "🔱 Grid update:"]
            msg = f"{random.choice(greetings)} https://linktr.ee/sterocoy"
            
            try:
                await user.send_message(member.user.id, msg)
                count += 1
                await asyncio.sleep(random.randint(65, 145)) # Human Jitter
            except errors.FloodWait as e:
                await message.reply(f"🚨 GRID COOL-DOWN: {e.value}s.")
                await asyncio.sleep(e.value)
            except: continue
            
        await message.reply(f"🔱 MISSION COMPLETE: {count} NODES SECURED IN {target}.")
    except Exception as e:
        await message.reply(f"🚨 GRID ERROR: {str(e)}")

# 🔱 7. THE STABILIZED IGNITION
async def main_engine():
    if not bot.is_connected: await bot.start()
    if not user.is_connected: await user.start()
    
    # THE HANDSHAKE
    try:
        await bot.send_message(KEYS["COMMANDER_ID"], "🔱 OMNI-V112.5 ONLINE. 2026 Real-Time Brain Active. Standing by, Commander.")
    except: pass
    
    while True: await asyncio.sleep(1000)

if __name__ == "__main__":
    st.set_page_config(page_title="OMNI-COMMANDER DECK", page_icon="🔱")
    st.title("🔱 OMNI-COMMANDER DECK")
    st.info("System Status: OPERATIONAL | Neural Link: 2026 REAL-TIME")
    
    # Fix for Streamlit ScriptRunner loop
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    
    loop.run_until_complete(main_engine())
