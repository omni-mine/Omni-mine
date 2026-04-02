import requests
import time
import base64
import os

# 🔱 OMNI-V112.5 GHOST-DNA (V.7-GOLD-FINAL)
# CACHE-BREAKER-ID: 999-STEROCOY-ALPHA
KEYS = {
    "GEMINI": "AIzaSyAZyKtRas8hM7Np37z0H_cLLmFEhQ3k2OU",
    "TG_TOKEN": "8694888309:AAHi7PZsOnqUXEPy9njkcyA9u5-K9X6c6f4"
}

T_URL = f"https://api.telegram.org/bot{KEYS['TG_TOKEN']}/"

def call_gemini(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={KEYS['GEMINI']}"
    payload = {"contents": [{"parts": [{"text": f"System: Elite Jamaican Scientist. User: {prompt}"}]}]}
    try:
        r = requests.post(url, json=payload, timeout=15).json()
        return r['candidates'][0]['content']['parts'][0]['text']
    except:
        return "🚨 GRID OVERLOAD."

print("🔱 V.7-GOLD: ENGINE ONLINE AND SHIFT-READY.")

last_id = -1
while True:
    try:
        # Requesting updates from Telegram
        resp = requests.get(f"{T_URL}getUpdates?offset={last_id+1}&timeout=15", timeout=20).json()
        for up in resp.get("result", []):
            last_id = up["update_id"]
            msg = up.get("message", {})
            cid = msg.get("chat", {}).get("id")
            text = msg.get("text", "")
            
            if text:
                print(f"📡 SIGNAL: {text}")
                # Sending a reply back to your Telegram
                requests.post(f"{T_URL}sendMessage", data={"chat_id": cid, "text": f"🔱 {call_gemini(text)}"})
    except Exception as e:
        print(f"🔧 PULSE CHECK: {e}")
        time.sleep(5)
