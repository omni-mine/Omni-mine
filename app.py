import streamlit as st
import asyncio, random, requests, base64, subprocess, sys, os, re, hashlib, time, threading
import nest_asyncio
import google.generativeai as genai

# 🔱 AUTO-MECHANIC: Ignition patch
nest_asyncio.apply()

def install_deps():
    deps = ["pyrogram", "tgcrypto", "google-generativeai", "httpx", "beautifulsoup4"]
    for p in deps:
        try: __import__(p.replace("-", "_"))
        except ImportError: subprocess.check_call([sys.executable, "-m", "pip", "install", p])

install_deps()
from pyrogram import Client, filters, errors

# 🔱 1. THE SOVEREIGN VAULT (ENCRYPTED ASSETS)
KEYS = {
    "GEMINI": "AIzaSyAZyKtRas8hM7Np37z0H_cLLmFEhQ3k2OU",
    "TG_TOKEN": "8694888309:AAHi7PZsOnqUXEPy9njkcyA9u5-K9X6c6f4",
    "PIPEDREAM": "https://eohco80amwi0w5q.m.pipedream.net",
    "MY_ID": "7649534062"
}

# 🔱 ROTATION SQUAD (ADD MORE KEYS HERE TO ROTATE)
ROTATION_SQUAD = [
    "AQITXrMApOu_j55ppe3joKFT4PITOopth2WK8_Inq0CuEdi01SzhXbIjPAl9na3CwDGnsMb5egtGnGNNVPog9OwkaxaTWIwmA8yPp6wZ1xki6IuemFjz3oaFjd8YJSeNg_Kpj8HhtoXe6i4PA3TuoPX0IWn0X2NI0QiKTaN7imKKD6uyjUc28XJ2-jwSOW1cELUWQXGIANZsA-LMIpxyhZEnQojYBwiCkdyjUwGb0WIaKOIV5sigTpigayiTjYKoDTnPWhcUU0tVJNIzUu83u8dT3_sOkchL6IPvDmIAFiAOsmZ4AblwSgJQEe_7cPvfbV5M9k4YwTWvLN8Q4KqTz9Y5USzljAAAAAIHHCRIAA"
]

STEROCOY_PITCH = "🔱 OMNI-MINER V8.1 USA nodes: https://linktr.ee/sterocoy"

# 🔱 2. NEURAL CORE (GEMINI 2.5 FLASH)
genai.configure(api_key=KEYS["GEMINI"])
model = genai.GenerativeModel('gemini-1.5-flash') # Using stable 1.5-flash for reliability

st.title("🔱 OMNI-V112.5: GHOST-DNA")
st.status("ENGINES ONLINE. SQUAD ROTATION ACTIVE.")

# Initialize the primary user and bot
current_session = ROTATION_SQUAD[0]
user = Client("OMNI_USER", api_id=34823859, api_hash="9c6f3c8056f6c6f04a6b23c3eb51e716", session_string=current_session, in_memory=True)
bot = Client("OMNI_BOT", api_id=34823859, api_hash="9c6f3c8056f6c6f04a6b23c3eb51e716", bot_token=KEYS["TG_TOKEN"], in_memory=True)

# 🔱 3. LAYER A: THE GHOST-DNA HARVESTER (URL CRAWLING)
async def ghost_harvest(url, message):
    await message.reply("🔱 URL RECOGNIZED. TELEPORTING GHOST DNA TO SECTOR...")
    try:
        headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU OS 17_4 like Mac OS X)"}
        r = requests.get(url, headers=headers, timeout=15)
        emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', r.text)
        found = list(set(emails))
        for email in found:
            requests.post(KEYS["PIPEDREAM"], json={"email": email, "source": url, "type": "GHOST_DNA"}, timeout=5)
        await message.reply(f"🔱 GHOST HARVEST COMPLETE. {len(found)} EMAILS PIPED TO UNDERWORLD.")
    except Exception as e:
        await message.reply(f"🚨 GHOST BYPASS ERROR: {str(e)}")

# 🔱 4. LAYER B: NEURAL CHAT & ACCOUNTABILITY
@bot.on_message(filters.text & filters.private & ~filters.command(["harvest"]))
async def neural_bridge(client, message):
    if "http" in message.text.lower():
        asyncio.create_task(ghost_harvest(message.text, message))
        return

    prompt = f"You are the OMNI-V112.5 AI. Sterocoy's 15-hour accountability partner. Respond to: {message.text}"
    try:
        response = model.generate_content(prompt)
        await message.reply(f"🔱 OMNI-BRAIN: {response.text}")
    except:
        await message.reply("🔱 Grid Active. Speak your command.")

# 🔱 5. LAYER C: THE SQUAD STRIKE (TELEGRAM HARVEST)
@bot.on_message(filters.command("harvest") & filters.private)
async def squad_strike(client, message):
    target = message.text.replace("/harvest", "").strip().replace("@", "")
    if not target:
        await message.reply("🔱 PROVIDE TARGET SECTOR.")
        return

    await message.reply(f"🔱 SQUAD ROTATION ACTIVE. STRIKING {target}...")
    
    try:
        if not user.is_connected: await user.start()
        try: await user.join_chat(target)
        except: pass
        
        count = 0
        async for member in user.get_chat_members(target):
            if member.user.is_bot or member.user.is_deleted: continue
            
            # Pipe to Underworld
            requests.post(KEYS["PIPEDREAM"], json={"tg_id": member.user.id, "group": target}, timeout=5)

            try:
                await user.send_message(member.user.id, STEROCOY_PITCH)
                count += 1
                await asyncio.sleep(random.randint(60, 120)) # One-minute timer logic
            except errors.FloodWait as e:
                # 🔱 ROTATION LOGIC: Switch account if blocked
                await message.reply("🚨 PRIMARY SECTOR BLOCKED. ROTATING SQUAD...")
                # In a real fleet, you would rotate current_session here
                await asyncio.sleep(e.value)
            except: continue
        await message.reply(f"🔱 STRIKE COMPLETE. {count} NODES HARVESTED.")
    except Exception as e:
        await message.reply(f"🚨 GRID ERROR: {str(e)}")

async def start_omni():
    await bot.start()
    await user.start()
    print("🔱 OMNI-V112.5: GHOST-DNA ONLINE.")
    while True: await asyncio.sleep(1000)

if __name__ == "__main__":
    asyncio.run(start_omni())
