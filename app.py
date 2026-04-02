import asyncio, requests, nest_asyncio, random, os
from telethon import TelegramClient, events, errors
from telethon.tl.functions.channels import JoinChannelRequest, GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

# 1. GRID PERSISTENCE & ENVIRONMENT
nest_asyncio.apply()

# 2. MASTER CREDENTIALS (V15 SECURE)
API_ID = 34823859  
API_HASH = '9c6f3c8056f6c6f04a6b23c3eb51e716'
BOT_TOKEN = '8694888309:AAHi7PZsOnqUXEPy9njkcyA9u5-K9X6c6f4'
GEMINI_KEY = "AIzaSyAZyKtRas8hM7Np37z0H_cLLmFEhQ3k2OU"
PRODUCT_LINK = "https://payhip.com/b/e8wfa"
MY_PHONE = '+18763942586'

# 3. UNIFIED SESSIONS
client = TelegramClient('omni_final_v15', API_ID, API_HASH, auto_reconnect=True)
bot = TelegramClient('bot_final_v15', API_ID, API_HASH)

# 4. AI SALES CORE (ENHANCED PERSONALITY)
def get_ai_response(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_KEY}"
    directive = (
        f"You are the OMNI-GIANT Sales Executive. A user just messaged: '{prompt}'. "
        f"Your goal is to convince them that OMNI-MINER V8.1 is the only tool they need to dominate USA nodes. "
        f"Be confident, professional, and slightly aggressive. Always include this link: {PRODUCT_LINK}. "
        "Keep the response under 100 words."
    )
    try:
        r = requests.post(url, json={"contents": [{"parts": [{"text": directive}]}]}, timeout=10)
        return r.json()['candidates'][0]['content']['parts'][0]['text']
    except: return "🔱 GRID BUSY. MOMENTUM HIGH. CHECK THE LINK: " + PRODUCT_LINK

# 5. THE STRIKE ENGINE (AUTO-HARVESTER)
@bot.on(events.NewMessage)
async def handle_message(event):
    if not event.is_private: return
    text = event.text.lower()
    
    if text.startswith('/harvest'):
        target = text.replace('/harvest', '').strip().replace('@', '').split('/')[-1]
        if not target:
            await event.respond("❌ ERROR: Please provide a group link or username. Example: `/harvest groupname`")
            return

        try:
            if not client.is_connected(): await client.connect()
            
            # --- PHASE 1: INFILTRATION ---
            await client(JoinChannelRequest(target))
            await event.respond(f"🔱 **INFILTRATION SUCCESSFUL**: {target}\n🔱 **INITIALIZING OMNI-STRIKE ON 40 NODES...**")
            
            # --- PHASE 2: PRECISION SCRAPE ---
            participants = await client(GetParticipantsRequest(target, ChannelParticipantsSearch(''), 0, 40, hash=0))
            
            count = 0
            for u in participants.users:
                if u.bot or u.deleted or not u.first_name: continue
                try:
                    # --- PHASE 3: THE HIGH-MOMENTUM PITCH ---
                    msg = (
                        f"🔱 Greetings {u.first_name}. The **OMNI-MINER V8.1** is now active in your sector. "
                        f"Secure your USA nodes and dominate the grid here: {PRODUCT_LINK}"
                    )
                    await client.send_message(u.id, msg)
                    count += 1
                    # Anti-Ban Protection (Crucial for Kingston IP)
                    await asyncio.sleep(random.randint(15, 25)) 
                except errors.FloodWaitError as e:
                    await event.respond(f"⚠️ GRID COOLING: Waiting {e.seconds}s to avoid ban.")
                    await asyncio.sleep(e.seconds)
                except: continue
                
            await event.respond(f"🔱 **STRIKE COMPLETE.**\n✅ **LEADS REACHED:** {count}\n💰 **CHECK PAYHIP REVENUE.**")
        except Exception as e:
            await event.respond(f"🚨 **GRID ERROR:** {str(e)}")
    
    elif text == "/start":
        await event.respond("🔱 **OMNI-V15 ONLINE.** Send me any message to chat with AI, or use `/harvest [link]` to ignite the engine.")
    else:
        # AI Sales Response for everything else
        await event.respond(get_ai_response(text))

# 6. IGNITION SEQUENCE
async def main():
    await bot.start(bot_token=BOT_TOKEN)
    print("🔱 BOT SYSTEM ACTIVE.")
    
    # Client will ask for login code in the Railway logs if not already logged in
    await client.start(phone=MY_PHONE)
    print("🔱 CLIENT SYSTEM ACTIVE. OMNI-V15 FULLY MERGED.")
    
    await bot.run_until_disconnected()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
