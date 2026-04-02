import streamlit as st
import asyncio, random, requests, base64, subprocess, sys, os
import nest_asyncio

# 🔱 AUTO-MECHANIC: Ignition patch for Streamlit/Railway
nest_asyncio.apply()

def install_deps():
    for p in ["pyrogram", "tgcrypto"]:
        try: __import__(p)
        except ImportError: subprocess.check_call([sys.executable, "-m", "pip", "install", p])

install_deps()
from pyrogram import Client, filters, errors

# 🔱 1. MASTER ASSETS (PERMANENTLY BOLTED)
API_ID = 34823859
API_HASH = "9c6f3c8056f6c6f04a6b23c3eb51e716"
BOT_TOKEN = "8694888309:AAHi7PZsOnqUXEPy9njkcyA9u5-K9X6c6f4"
# YOUR MASTER KEY FROM SAVED MESSAGES
MASTER_STRING = "AQITXrMAJnae15kTJdR2YWoBmCnqJiHBm4odQ667QTTABePRYqcDLy_hkz43xg5fxxoHXOfyaaF0evsNHktL3LC47M7dFlKaay_bcZGcpAZI1U1UCZ-yrCyR2GgJamR6fEj8w60IAnHSoon0J90pe-xQ1xzSDVTyvHW6hP8LmNr2JwgumlptEdb-ShQmHX8cZzbOlwe69l5Yms0CN2GJC0cIcavZtoUgdMHhNgMkTl-nKPsHV5UzVl_ozyNlu1viegJRgl7c5CKqQD2dNaIgbBOMkyWxThRQlCvxcatkynIIQy71c3xqo1VmWfRhPNd2_4M6tHEe8Gvc0UStPiPkEjnoaxcIDQAAAAIHHCRIAA"

st.title("🔱 OMNI-V112.5 HYPER-BRIDGE")
st.status("ENGINES ONLINE. GRID SYNCED.")

# 🔱 2. DUAL-ENGINE IGNITION
user = Client("OMNI_USER", api_id=API_ID, api_hash=API_HASH, session_string=MASTER_STRING, in_memory=True)
bot = Client("OMNI_BOT", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, in_memory=True)

# 🔱 3. HARVESTER LOGIC
@bot.on_message(filters.command("harvest") & filters.private)
async def run_harvest(client, message):
    target = message.text.replace("/harvest", "").strip().replace("@", "")
    if not target:
        await message.reply("🔱 PROVIDE A TARGET CHANNEL.")
        return

    await message.reply(f"🔱 OMNI-V112.5: STRIKING {target}...")
    try:
        if not user.is_connected: await user.start()
        await user.join_chat(target)
        count = 0
        async for member in user.get_chat_members(target):
            if member.user.is_bot or member.user.is_deleted: continue
            try:
                pitch = f"🔱 OMNI-MINER V8.1 USA nodes: https://linktr.ee/sterocoy"
                await user.send_message(member.user.id, pitch)
                count += 1
                await asyncio.sleep(random.randint(30, 60))
            except errors.FloodWait as e: await asyncio.sleep(e.value)
            except: continue
        await message.reply(f"🔱 STRIKE COMPLETE. {count} NODES HIT.")
    except Exception as e:
        await message.reply(f"🚨 GRID ERROR: {str(e)}")

# 🔱 4. STARTUP SEQUENCE
async def start_omni():
    if not bot.is_connected: await bot.start()
    if not user.is_connected: await user.start()
    print("🔱 OMNI-V112.5: FULLY SYNCED.")
    # Keep the bridge open
    while True:
        await asyncio.sleep(1000)

if __name__ == "__main__":
    # Ignition call that bypasses the Streamlit Thread error
    asyncio.run(start_omni())
