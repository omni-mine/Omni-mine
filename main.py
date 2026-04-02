import asyncio, datetime, random
import google.generativeai as genai
from pyrogram import Client, filters, errors

KEYS = {
    "GEMINI": "AIzaSyAZyKtRas8hM7Np37z0H_cLLmFEhQ3k2OU",
    "TG_TOKEN": "8694888309:AAHi7PZsOnqUXEPy9njkcyA9u5-K9X6c6f4",
    "MASTER_STRING": "AQITXrMApOu_j55ppe3joKFT4PITOopth2WK8_Inq0CuEdi01SzhXbIjPAl9na3CwDGnsMb5egtGnGNNVPog9OwkaxaTWIwmA8yPp6wZ1xki6IuemFjz3oaFjd8YJSeNg_Kpj8HhtoXe6i4PA3TuoPX0IWn0X2NI0QiKTaN7imKKD6uyjUc28XJ2-jwSOW1cELUWQXGIANZsA-LMIpxyhZEnQojYBwiCkdyjUwGb0WIaKOIV5sigTpigayiTjYKoDTnPWhcUU0tVJNIzUu83u8dT3_sOkchL6IPvDmIAFiAOsmZ4AblwSgJQEe_7cPvfbV5M9k4YwTWvLN8Q4KqTz9Y5USzljAAAAAIHHCRIAA",
    "COMMANDER_ID": 7649534062 
}

genai.configure(api_key=KEYS["GEMINI"])
model = genai.GenerativeModel('gemini-1.5-flash')
bot = Client("BOT_CORE", api_id=34823859, api_hash="9c6f3c8056f6c6f04a6b23c3eb51e716", bot_token=KEYS["TG_TOKEN"], in_memory=True)
user = Client("USER_CORE", api_id=34823859, api_hash="9c6f3c8056f6c6f04a6b23c3eb51e716", session_string=KEYS["MASTER_STRING"], in_memory=True)

# 🔱 THE LIVE REPORTER
@bot.on_message(filters.command("status") & filters.private)
async def check_status(client, message):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    await message.reply(f"🔱 OMNI-STATUS [{now}]:\n✅ Brain: Active\n✅ Harvester: Ready\n✅ Grid: 2026 Secured")

@bot.on_message(filters.command("harvest") & filters.private)
async def strike(client, message):
    target = message.text.split(" ")[-1].replace("@", "")
    await message.reply(f"🔱 INITIATING STRIKE ON {target}...")
    try:
        count = 0
        async for member in user.get_chat_members(target):
            if member.user.is_bot: continue
            try:
                await user.send_message(member.user.id, "🔱 Join the Movement: https://linktr.ee/sterocoy")
                count += 1
                # 🔱 REPORT EVERY 5 SUCCESSES
                if count % 5 == 0:
                    await bot.send_message(KEYS["COMMANDER_ID"], f"🔱 HARVEST REPORT: {count} nodes secured in {target}.")
                await asyncio.sleep(random.randint(150, 350))
            except errors.FloodWait as e:
                await bot.send_message(KEYS["COMMANDER_ID"], f"🚨 GRID BLOCK: Sleeping {e.value}s.")
                await asyncio.sleep(e.value)
            except: continue
        await message.reply(f"🔱 MISSION COMPLETE: {count} NODES TOTAL.")
    except Exception as e:
        await message.reply(f"🚨 ERROR: {str(e)}")

async def start():
    await bot.start(); await user.start()
    await bot.send_message(KEYS["COMMANDER_ID"], "🔱 GHOST-V1 ONLINE.\n\nType /status to check health.\nType /harvest [target] to begin.")
    while True: await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(start())
