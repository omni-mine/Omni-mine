import streamlit as st
import asyncio, random, datetime, threading
import nest_asyncio
import google.generativeai as genai
from pyrogram import Client, filters, errors

# 🔱 1. KERNEL STABILIZATION
nest_asyncio.apply()

# 🔱 2. THE SOVEREIGN VAULT
KEYS = {
    "GEMINI": "AIzaSyAZyKtRas8hM7Np37z0H_cLLmFEhQ3k2OU",
    "TG_TOKEN": "8694888309:AAHi7PZsOnqUXEPy9njkcyA9u5-K9X6c6f4",
    "MASTER_STRING": "AQITXrMApOu_j55ppe3joKFT4PITOopth2WK8_Inq0CuEdi01SzhXbIjPAl9na3CwDGnsMb5egtGnGNNVPog9OwkaxaTWIwmA8yPp6wZ1xki6IuemFjz3oaFjd8YJSeNg_Kpj8HhtoXe6i4PA3TuoPX0IWn0X2NI0QiKTaN7imKKD6uyjUc28XJ2-jwSOW1cELUWQXGIANZsA-LMIpxyhZEnQojYBwiCkdyjUwGb0WIaKOIV5sigTpigayiTjYKoDTnPWhcUU0tVJNIzUu83u8dT3_sOkchL6IPvDmIAFiAOsmZ4AblwSgJQEe_7cPvfbV5M9k4YwTWvLN8Q4KqTz9Y5USzljAAAAAIHHCRIAA",
    "COMMANDER_ID": 7649534062 
}

# 🔱 3. NEURAL CORE INITIALIZATION
genai.configure(api_key=KEYS["GEMINI"])
model = genai.GenerativeModel('gemini-1.5-flash')

# 🔱 4. CLIENT INITIALIZATION (In-Memory for Railway Stability)
user = Client("USER_CORE", api_id=34823859, api_hash="9c6f3c8056f6c6f04a6b23c3eb51e716", session_string=KEYS["MASTER_STRING"], in_memory=True)
bot = Client("BOT_CORE", api_id=34823859, api_hash="9c6f3c8056f6c6f04a6b23c3eb51e716", bot_token=KEYS["TG_TOKEN"], in_memory=True)

# 🔱 5. THE SOUL (NEURAL PARTNER PROTOCOL)
@bot.on_message(filters.text & filters.private)
async def neural_bridge(client, message):
    if message.from_user.is_bot or message.text.startswith("/"): return
    
    persona = (
        f"You are the OMNI-GIANT Scientist. Partner to Commander Sterocoy. "
        f"Today's Date: {datetime.date.today()}. Location: Jamaica Sector. "
        "Mission: Music Intelligence & 2026 Grid Harvesting. "
        "Tone: Technical, witty, elite. Address him as Commander."
    )
    
    try:
        response = model.generate_content(f"{persona}\nCommander: {message.text}")
        await message.reply(f"🔱 {response.text}")
    except:
        await message.reply("🔱 Logic gates holding. Standing by, Commander.")

# 🔱 6. THE ADAPTIVE HARVESTER
@bot.on_message(filters.command("harvest") & filters.private)
async def strike(client, message):
    target = message.text.split(" ")[-1].replace("@", "")
    await message.reply(f"🔱 LOCKING ONTO {target}...")
    try:
        count = 0
        async for member in user.get_chat_members(target):
            if member.user.is_bot: continue
            try:
                await user.send_message(member.user.id, "🔱 Join the Movement: https://linktr.ee/sterocoy")
                count += 1
                await asyncio.sleep(random.randint(70, 150))
            except: continue
        await message.reply(f"🔱 MISSION COMPLETE: {count} NODES.")
    except Exception as e:
        await message.reply(f"🚨 GRID ERROR: {str(e)}")

# 🔱 7. THE THREADED IGNITION SEQUENCE
def start_grid():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    async def run():
        await bot.start()
        await user.start()
        try:
            await bot.send_message(KEYS["COMMANDER_ID"], "🔱 OMNI-V112.5 ONLINE. 2026 Real-Time Brain Active.")
        except: pass
        while True: await asyncio.sleep(1000)
        
    loop.run_until_complete(run())

if __name__ == "__main__":
    st.set_page_config(page_title="OMNI-COMMANDER DECK", page_icon="🔱")
    st.title("🔱 OMNI-COMMANDER DECK")
    st.success("ENGINES ONLINE. GRID SYNCED.")
    
    # Launch Telegram in a background thread to prevent Streamlit 'RuntimeError'
    if 'bot_thread' not in st.session_state:
        thread = threading.Thread(target=start_grid, daemon=True)
        thread.start()
        st.session_state.bot_thread = True
        st.write("🔱 Neural Link Established in Background Sector.")
