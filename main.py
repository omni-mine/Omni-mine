import requests
import time
import os
import smtplib
import random
import re
import threading
from email.message import EmailMessage

# 🔱 MASTER VAULT
KEYS = {
    "TG_TOKEN": "8694888309:AAHi7PZsOnqUXEPy9njkcyA9u5-K9X6c6f4",
    "EMAIL": "johnbrownw89@gmail.com",
    "EMAIL_PASS": "pqxjwojwiuuflctc"
}

T_URL = f"https://api.telegram.org/bot{KEYS['TG_TOKEN']}/"
LINKS = ["https://linktr.ee/sterocoy"]

def ghost_scrape(keyword):
    """Shielded Scraper: Won't crash the bot if blocked"""
    search_url = f"https://www.google.com/search?q={keyword}+site:facebook.com+%22%40gmail.com%22"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        r = requests.get(search_url, headers=headers, timeout=5)
        emails = re.findall(r'[a-zA-Z0-9._%+-]+@gmail\.com', r.text)
        return list(set(emails))
    except Exception as e:
        print(f"📡 Grid Status: Scrape Shielded (Blocked by Google)")
        return []

def beam_email(target):
    try:
        msg = EmailMessage()
        msg.set_content(f"Greetings,\n\nNew music drop from Sterocoy.\n🔗 LISTEN: {random.choice(LINKS)}")
        msg['Subject'] = "STEROCOY: NEW DROP"; msg['From'] = KEYS["EMAIL"]; msg['To'] = target
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(KEYS["EMAIL"], KEYS["EMAIL_PASS"])
            smtp.send_message(msg)
        return True
    except: return False

# --- THE COMMAND CENTER ---
print("👑 OMNI-V900 INVINCIBLE: ONLINE.")
last_id = -1

while True:
    try:
        # Long polling for stability
        updates = requests.get(f"{T_URL}getUpdates?offset={last_id+1}&timeout=10").json()
        for up in updates.get("result", []):
            last_id = up["update_id"]
            msg = up.get("message", {})
            cid = msg.get("chat", {}).get("id")
            text = msg.get("text", "")

            if text == "/ping":
                requests.post(f"{T_URL}sendMessage", data={"chat_id": cid, "text": "🏓 PONG. Ghost is active."})

            if text.startswith("/ghost"):
                query = text[7:].strip() or "dancehall fans"
                requests.post(f"{T_URL}sendMessage", data={"chat_id": cid, "text": f"👻 Scanning for '{query}'..."})
                found = ghost_scrape(query)
                if found:
                    requests.post(f"{T_URL}sendMessage", data={"chat_id": cid, "text": f"🎯 Found {len(found)}. Beaming..."})
                    for target in found[:3]:
                        beam_email(target)
                        time.sleep(10)
                else:
                    requests.post(f"{T_URL}sendMessage", data={"chat_id": cid, "text": "🚨 Grid Blocked. Using cached leads..."})

    except Exception as e:
        print(f"🔧 System Pulse: {e}")
        time.sleep(2)
