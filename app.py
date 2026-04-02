import os, time, requests, base64, json, random, asyncio, httpx, threading, re, sys, subprocess
from datetime import datetime

# 🔱 AUTO-MECHANIC: Installs the "Harvester" parts automatically
def install_deps():
    for p in ["pyrogram", "tgcrypto"]:
        try: __import__(p)
        except ImportError: subprocess.check_call([sys.executable, "-m", "pip", "install", p])

install_deps()
from pyrogram import Client, filters, errors

# --- 1. THE IMMORTAL CORE ASSETS ---
KEYS = {
    "GEMINI": "AIzaSyAZyKtRas8hM7Np37z0H_cLLmFEhQ3k2OU",
    "TG_TOKEN": "8694888309:AAHi7PZsOnqUXEPy9njkcyA9u5-K9X6c6f4",
    "PIPEDREAM": "https://eohco80amwi0w5q.m.pipedream.net",
    "API_ID": 34823859,
    "API_HASH": "9c6f3c8056f6c6f04a6b23c3eb51e716"
}

# 🔱 YOUR MASTER STRING (BOLTED FROM YOUR SCREENSHOT)
MASTER_STRING = "AQITXrMAJnaeYvHwZ5k5H2r5U-mH9D6v9Y8X7C6B5A4S3D2F1G0HjK" # REPLACE THIS WITH YOUR FULL STRING FROM SAVED MESSAGES

PORTFOLIO = "https://linktr.ee/sterocoy"
SONGS = {
    "STRAW": "https://youtu.be/Wy-HpTGuHxs", 
    "DANAL_TRUMP": "https://music.apple.com/us/album/danal-trump-single/1839213239"
}

# --- 2. DUAL-ENGINE IGNITION ---
# Engine A: The Bot (Neural Link)
bot = Client("OMNI_BOT", api_id=KEYS["API_ID"], api_hash=KEYS["API_HASH"], bot_token=KEYS["TG_TOKEN"], in_memory=True)
# Engine B: The User (The Harvester)
user = Client("OMNI_USER", api_id=KEYS["API_ID"], api_hash=KEYS["API_HASH"], session_string=MASTER_STRING, in_memory=True)

# --- 3. THE HARVESTER COMMAND (/harvest [group]) ---
@bot.on_message(filters.command("harvest") & filters.private)
async def run_harvest(client, message):
    target = message.text.replace("/harvest", "").strip().replace("@", "")
    if not target:
        await message.reply("🔱 PROVIDE A TARGET CHANNEL OR GROUP.")
        return

    await message.reply(f"🔱 OMNI-V112.5: TARGETING {target}...")
    
    try:
        if not user.is_connected: await user.start()
        await user.join_chat(target)
        count = 0
        async for member in user.get_chat_members(target):
            if member.user.is_bot or member.user.is_deleted: continue
            try:
                pitch = f"🔱 Secure OMNI-MINER V8.1 USA nodes here: {PORTFOLIO}\nTrack: {SONGS['STRAW']}"
                await user.send_message(member.user.id, pitch)
                count += 1
                await asyncio.sleep(random.randint(25, 45)) # Anti-Ban Delay
            except errors.FloodWait as e: await asyncio.sleep(e.value)
            except: continue
        await message.reply(f"🔱 STRIKE COMPLETE. {count} NODES HIT.")
    except Exception as e:
        await message.reply(f"🚨 GRID ERROR: {str(e)}")

# --- 4. THE NEURAL-LINK (GEMINI AI) ---
@bot.on_message(filters.private & ~filters.command("harvest"))
async def neural_link(client, message):
    prompt = message.text or message.caption or "Analyze."
    
    # Visual analysis check
    img_b64 = None
    if message.photo:
        file = await client.download_media(message.photo, in_memory=True)
        img_b64 = base64.b64encode(file.getvalue()).decode()

    # AI Request
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={KEYS['GEMINI']}"
    sys_msg = "Role: OMNI-GIANT. Kingston 2026 Grid. Answer with mechanical authority."
    parts = [{"text": f"{sys_msg}\n\nPROMPT: {prompt}"}]
    if img_b64: parts.append({"inline_data": {"mime_type": "image/png", "data": img_b64}})
    
    try:
        r = requests.post(url, json={"contents": [{"parts": parts}]}, timeout=25)
        reply = r.json()['candidates'][0]['content']['parts'][0]['text']
        await message.reply(reply)
    except:
        await message.reply("🚨 NEURAL-LINK DISRUPTED.")

# --- 5. STARTUP ---
async def start_omni():
    print("🔱 OMNI-V112.5 HYPER-BRIDGE: ONLINE.")
    await bot.start()
    await user.start()
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(start_omni())
