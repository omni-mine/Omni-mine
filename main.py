import requests
import time
import base64

# 🔱 OMNI-V112.5 GHOST-DNA (V.7-GOLD)
KEYS = {
    "GEMINI": "AIzaSyAZyKtRas8hM7Np37z0H_cLLmFEhQ3k2OU",
    "TG_TOKEN": "8694888309:AAHi7PZsOnqUXEPy9njkcyA9u5-K9X6c6f4"
}

T_URL = f"https://api.telegram.org/bot{KEYS['TG_TOKEN']}/"

def call_gemini(prompt, img_b64=None):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={KEYS['GEMINI']}"
    content_part = [{"text": f"You are the OMNI-GIANT. Jamaican Scientist. Logic only. Respond to: {prompt}"}]
    if img_b64:
        content_part.append({"inline_data": {"mime_type": "image/png", "data": img_b64}})
    try:
        r = requests.post(url, json={"contents": [{"parts": content_part}]}, timeout=20).json()
        return r['candidates'][0]['content']['parts'][0]['text']
    except:
        return "🚨 GRID OVERLOAD."

print("🔱 V.7-GOLD: ENGINE STARTING...")

last_id = -1
while True:
    try:
        # The 'timeout=20' here keeps the connection open without flooding Telegram
        updates = requests.get(f"{T_URL}getUpdates?offset={last_id+1}&timeout=20").json()
        for up in updates.get("result", []):
            last_id = up["update_id"]
            msg = up.get("message", {})
            cid = msg.get("chat", {}).get("id")
            text = msg.get("text", "")
            
            if text:
                print(f"📡 Signal Received: {text}")
                requests.post(f"{T_URL}sendChatAction", data={"chat_id": cid, "action": "typing"})
                reply = call_gemini(text)
                requests.post(f"{T_URL}sendMessage", data={"chat_id": cid, "text": f"🔱 {reply}"})
    except Exception as e:
        print(f"🔧 System Pulse: {e}")
        time.sleep(5)
