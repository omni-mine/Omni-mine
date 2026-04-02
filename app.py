import os, asyncio, random, requests, base64, subprocess, sys
from pyrogram import Client, filters, errors

# 🔱 AUTO-MECHANIC: Installs the right parts for Railway parity
def install_deps():
    for p in ["pyrogram", "tgcrypto", "requests"]:
        try: __import__(p)
        except ImportError: subprocess.check_call([sys.executable, "-m", "pip", "install", p])

install_deps()

# 🔱 1. MASTER KEYS & SYNCED STRING
API_ID = 34823859
API_HASH = "9c6f3c8056f6c6f04a6b23c3eb51e716"
BOT_TOKEN = "8694888309:AAHi7PZsOnqUXEPy9njkcyA9u5-K9X6c6f4"
# BOLTED DIRECTLY FROM YOUR SAVED MESSAGES SCREENSHOT
MASTER_STRING = "AQITXrMAJnae15kTJdR2YWoBmCnqJiHBm4odQ667QTTABePRYqcDLy_hkz43xg5fxxoHXOfyaaF0evsNHktL3LC47M7dFlKaay_bcZGcpAZI1U1UCZ-yrCyR2GgJamR6fEj8w60IAnHSoon0J90pe-xQ1xzSDVTyvHW6hP8LmNr2JwgumlptEdb-ShQmHX8cZzbOlwe69l5Yms0CN2GJC0cIcavZtoUgdMHhNgMkTl-nKPsHV5UzVl_ozyNlu1viegJRgl7c5CKqQD2dNaIgbBOMkyWxThRQlCvxcatkynIIQy71c3xqo1VmWfRhPNd2_4M6tHEe8Gvc0UStPiPkEjnoaxcIDQAAAAIHHCRIAA"

# 🔱 2. DUAL-ENGINE IGNITION (STALWART MODE)
user = Client("OMNI_USER", api_id=API_ID, api_hash=API_HASH, session_string=MASTER_STRING, in_memory=True)
bot = Client("OMNI_BOT", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, in_memory=True)

# 🔱 3. THE HARVESTER COMMAND
@bot.on_message(filters.command("harvest") & filters.private)
async def run_harvest(client, message):
    target = message.text.replace("/harvest", "").strip().replace("@", "")
    if not target:
        await message.reply("🔱 PROVIDE A TARGET CHANNEL.")
        return

    await message.reply(f"🔱 OMNI-V112.5: STRIKING TARGET {target}...")
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
                await asyncio.sleep(random.randint(30, 60)) # Anti-Ban Delay
            except errors.FloodWait as e: await asyncio.sleep(e.value)
            except: continue
        await message.reply(f"🔱 STRIKE COMPLETE. {count} NODES HIT.")
    except Exception as e:
        await message.reply(f"🚨 GRID ERROR: {str(e)}")

# 🔱 4. THE NEURAL-LINK FIX (FOR RAILWAY THREADS)
async def start_omni():
    print("🔱 OMNI-V112.5: IGNITION...")
    await bot.start()
    await user.start()
    print("🔱 ENGINES ONLINE. NO RUNTIME ERROR.")
    await asyncio.Event().wait()

if __name__ == "__main__":
    try:
        asyncio.run(start_omni())
    except RuntimeError:
        # Fixes the 'ScriptRunner' loop error from your screenshot
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(start_omni())
