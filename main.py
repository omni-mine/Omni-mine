import requests
import time
import os
import smtplib
import random
import re
import threading
from datetime import datetime
from email.message import EmailMessage

# 🔱 MASTER VAULT: DIRECT INJECTION (No Variables Needed)
KEYS = {
    "GEMINI": "AIzaSyAZyKtRas8hM7Np37z0H_cLLmFEhQ3k2OU",
    "TG_TOKEN": "8694888309:AAHi7PZsOnqUXEPy9njkcyA9u5-K9X6c6f4",
    "EMAIL": "johnbrownw89@gmail.com",
    "EMAIL_PASS": "pqxjwojwiuuflctc"
}

T_URL = f"https://api.telegram.org/bot{KEYS['TG_TOKEN']}/"
TRACKS = ["Donald Trump", "Straw"]
LINKS = ["https://linktr.ee/sterocoy", "https://music.apple.com/us/album/danal-trump-single/1839213239"]

# --- THE GHOST ENGINE (LEAD HARVESTER) ---
def ghost_scrape(keyword):
    search_url = f"https://www.google.com/search?q={keyword}+site:facebook.com+OR+site:instagram.com+%22%40gmail.com%22"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        r = requests.get(search_url, headers=headers, timeout=10)
        emails = re.findall(r'[a-zA-Z0-9._%+-]+@gmail\.com', r.text)
        return list(set(emails))
    except: return []

def beam_email(target):
    try:
        dna = "\u200b" + "".join(random.choices('ACGT', k=16))
        track = random.choice(TRACKS)
        bio = (f"Greetings,\n\nYou've been selected for an exclusive listen from Sterocoy.\n"
               f"Direct from Jamaica.\n\n🔥 DROP: {track}\n🔗 STREAM: {random.choice(LINKS)}\n\n{dna}")
        msg = EmailMessage()
        msg.set_content(bio)
        msg['Subject'] = f"STEROCOY: {track}"; msg['From'] = KEYS["EMAIL"]; msg['To'] = target
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(KEYS["EMAIL"], KEYS["EMAIL_PASS"])
            smtp.send_message(msg)
        return True
    except: return False

# 🚀 AUTO-PILOT (Background Harvester)
def auto_pilot_engine():
    while True:
        leads = ghost_scrape("dancehall fans")
        for target in leads[:5]:
            beam_email(target)
            time.sleep(120)
        time.sleep(21600) # Wait 6 hours before next harvest

threading.Thread(target=auto_pilot_engine, daemon=True).start()

# --- THE COMMAND CENTER ---
print("👑 OMNI-V900 INVINCIBLE: ONLINE.")
last_id = -1
while True:
    try:
        updates = requests.get(f"{T_URL}getUpdates?offset={last_id+1}&timeout=5").json()
        for up in updates.get("result", []):
            last_id = up["update_id"]
            msg = up.get("message", {}); cid = msg.get("chat", {}).get("id")
            text_prompt = msg.get("text", "")

            if text_prompt == "/ping":
                requests.post(f"{T_URL}sendMessage", data={"chat_id": cid, "text": "🏓 PONG. Engine is active."})

            if text_prompt.startswith("/ghost"):
                query = text_prompt[7:].strip() or "dancehall fans"
                requests.post(f"{T_URL}sendMessage", data={"chat_id": cid, "text": f"👻 Ghosting '{query}'..."})
                found = ghost_scrape(query)
                if found:
                    requests.post(f"{T_URL}sendMessage", data={"chat_id": cid, "text": f"🎯 Found {len(found)}. Beaming..."})
                    for target in found[:5]:
                        if beam_email(target):
                            requests.post(f"{T_URL}sendMessage", data={"chat_id": cid, "text": f"✅ Beamed: {target}"})
                        time.sleep(120)
    except Exception:
        time.sleep(1)
