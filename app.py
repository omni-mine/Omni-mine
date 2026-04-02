import streamlit as st
import asyncio, random, datetime, threading
import nest_asyncio
import google.generativeai as genai
from pyrogram import Client, filters, errors

# 🔱 1. KERNEL LEVEL STABILIZATION
nest_asyncio.apply()

# 🔱 2. THE SOVEREIGN VAULT
KEYS = {
    "GEMINI": "AIzaSyAZyKtRas8hM7Np37z0H_cLLmFEhQ3k2OU",
    "TG_TOKEN": "8694888309:AAHi7PZsOnqUXEPy9njkcyA9u5-K9X6c6f4",
    "MASTER_STRING": "AQITXrMApOu_j55ppe3joKFT4PITOopth2WK8_Inq0CuEdi01SzhXbIjPAl9na3CwDGnsMb5egtGnGNNVPog9OwkaxaTWIwmA8yPp6wZ1xki6IuemFjz3oaFjd8YJSeNg_Kpj8HhtoXe6i4PA3TuoPX0IWn0X2NI0QiKTaN7imKKD6uyjUc28XJ2-jwSOW1cELUWQXGIANZsA-LMIpxyhZEnQojYBwiCkdyjUwGb0WIaKOIV5sigTpigayiTjYKoDTnPWhcUU0tVJNIzUu83u8dT3_sOkchL6IPvDmIAFiAOsmZ4AblwSgJQEe_7cPvfbV5M9k4YwTWvLN8Q4KqTz9Y5USzljAAAAAIHHCRIAA",
    "COMMANDER_ID": 7649534062 
}

# 🔱 3. NEURAL INITIALIZATION
genai.configure(api_key=KEYS["GEMINI"])
model = genai.GenerativeModel('gemini-1.5-flash')

# 🔱 4. CLIENT INITIALIZATION
user = Client("USER_CORE", api_id=34823859, api_hash="9c6f3c8056f6c6f04a6b23c3eb51e716", session_string=KEYS["MASTER_STRING"], in_memory=True)
bot = Client("BOT_CORE", api_id=34823859, api_hash="9c6f3c8056f6c6f04a6b23c3eb51e716", bot_token=KEYS["TG_TOKEN"], in_memory=True)

# 🔱 5. NEURAL PARTNER PROTOCOL
@bot.on_message(filters.text & filters.private)
async def neural_bridge(client, message):
    if message.from_user.is_bot or message.text.startswith("/"): return
    persona = f"OMNI-GIANT Scientist. Partner to Commander Sterocoy. Date: {datetime.date.today()}. Jamaica Sector. Mission: Music Dominance."
    try:
        response = model.generate_content(f"{persona}\nCommander: {message.text}")
        await message.reply(f"🔱 {response.text}")
    except: await message.reply("🔱 Logic gates stable.")

# 🔱 6. THE BACKGROUND ENGINE (The Fix)
def run_telegram_logic():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    async def start_clients():
        await bot.start()
        await user.start()
        try:
            await bot.send_message(KEYS["COMMANDER_ID"], "🔱 OMNI-V112.5 ONLINE. 2026 Real-Time Brain Active.")
        except: pass
        while True: await asyncio.sleep(1000)
        
    loop.run_until_complete(start_clients())

# 🔱 7. DASHBOARD IGNITION
if __name__ == "__main__":
    st.set_page_config(page_title="OMNI-MASTER DECK", page_icon="🔱")
    st.title("🔱 OMNI-MASTER DECK")
    st.success("ENGINES RUNNING IN BACKGROUND SECTOR.")
    
    # This block prevents the "Derailed" error by launching Telegram on a separate thread
    if 'engine_started' not in st.session_state:
        thread = threading.Thread(target=run_telegram_logic, daemon=True)
        thread.start()
        st.session_state.engine_started = True
        st.info("🔱 Neural Link Established. Check your Telegram, Commander.")
