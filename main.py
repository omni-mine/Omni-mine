import requests
import time
import os
import smtplib
import random
import re
import threading
from datetime import datetime
from email.message import EmailMessage

# 🔱 MASTER VAULT: DIRECT INJECTION
KEYS = {
    "GEMINI": "AIzaSyAZyKtRas8hM7Np37z0H_cLLmFEhQ3k2OU",
    "TG_TOKEN": "8694888309:AAHi7PZsOnqUXEPy9njkcyA9u5-K9X6c6f4",
    "EMAIL": "johnbrownw89@gmail.com",
    "EMAIL_PASS": "pqxjwojwiuuflctc"
}

T_URL = f"https://api.telegram.org/bot{KEYS['TG_TOKEN']}/"
TRACKS = ["Donald Trump", "Straw"]
LINKS = ["https://linktr.ee/sterocoy", "https://music.apple.com/us/album/danal-trump-single/1839213239"]

# --- THE GHOST ENGINE (SHIELDED) ---
def ghost_scrape(keyword):
    search_url = f"https://www.google.com/search?q={keyword}+site:facebook.com+%22%40gmail.com%22"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        # Added a 5-second timeout to prevent hanging
        r = requests.get(search_url, headers=headers, timeout=5)
        emails = re.findall(r'[a-zA-Z0-9._%+-]+@gmail\.com', r.text)
        return list(set(emails))
    except Exception as e:
        print(f"📡 Grid Blocked by Google: {e}")
        return []

def beam_email(target):
    try:
        dna = "\u200b" + "".join(random.choices('ACGT', k=16))
        msg = EmailMessage()
        msg.set_content(f"Greetings,\n\nNew music from Sterocoy.\n🔥 DROP: {random.choice(TRACKS)}\n🔗 STREAM: {random.choice(LINKS)}\n\n{dna}")
        msg['Subject'] = "STEROCOY: NEW DROP"; msg['From'] = KEYS["EMAIL"]; msg['To'] = target
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(KEYS["EMAIL"], KEYS["EMAIL_PASS"])
            smtp.send_message(msg)
        return True
    except: return False

# 🚀 AUTO-PILOT (Background)
def auto_pilot_engine():
    while True:
        try:
            leads = ghost_scrape("dancehall fans")
            if leads:
                for target in leads[:3]:
                    beam_email(target)
                    time.sleep(60)
        except: pass
        time.sleep(3600) # Wait 1 hour before trying again

threading.Thread(target=auto_pilot_engine, daemon=True).start()

# --- THE COMMAND CENTER ---
print("👑 OMNI-V900 INVINCIBLE: ONLINE.")
last_id = -1
while True:
    try:
        # Long polling to keep connection stable
        updates = requests.get(f"{T_URL}getUpdates?offset={last_id+1}&timeout=20").json()
        for up in updates.get("result", []):
            last_id = up["update_id"]
            msg = up.get("message", {}); cid = msg.get("chat", {}).get("id")
            text = msg.get("text", "")

            if text == "/ping":
                requests.post(f"{T_URL}sendMessage", data={"chat_id": cid, "text": "🏓 PONG. Ghost is active."})

            if text.startswith("/ghost"):
                query = text[7:].strip() or "dancehall fans"
                requests.post(f"{T_URL}sendMessage", data={"chat_id": cid, "text": f"👻 Scanning Grid for '{query}'..."})
                found = ghost_scrape(query)
                if found:
                    requests.post(f"{T_URL}sendMessage", data={"chat_id": cid, "text": f"🎯 Found {len(found)}. Beaming..."})
                    for target in found[:3]:
                        if beam_email(target):
                            requests.post(f"{T_URL}sendMessage", data={"chat_id": cid, "text": f"✅ Beamed: {target}"})
                        time.sleep(30)
                else:
                    requests.post(f"{T_URL}sendMessage", data={"chat_id": cid, "text": "🚨 Grid Blocked. Manual intervention required."})
    except Exception as e:
        print(f"🔧 System Loop: {e}")
        time.sleep(2)
