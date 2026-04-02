import requests
import time
import base64
import json

# 🔱 MASTER VAULT: DIRECT INJECTION
KEYS = {
    "GEMINI": "AIzaSyAZyKtRas8hM7Np37z0H_cLLmFEhQ3k2OU",
    "TG_TOKEN": "8694888309:AAHi7PZsOnqUXEPy9njkcyA9u5-K9X6c6f4"
}

T_URL = f"https://api.telegram.org/bot{KEYS['TG_TOKEN']}/"

def call_gemini(prompt, img_b64=None):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={KEYS['GEMINI']}"
    content_part = [{"text": f"You are the OMNI-GIANT. Jamaican Scientist/Producer. Elite logic. Respond to: {prompt}"}]
    if img_b64:
        content_part.append({"inline_data": {"mime_type": "image/png", "data": img_b64}})
    payload = {"contents": [{"parts": content_part}]}
    try:
        r = requests.post(url, json=payload, timeout=20).json()
        return r['candidates'][0]['content']['parts'][0]['text']
    except:
        return "🚨 GRID OVERLOAD: Signal weak."

print("👑 OMNI-ENGINE: ONLINE. READY FOR COMMANDS.")
last_id = -1

while True:
    try:
        updates = requests.get(f"{T_URL}getUpdates?offset={last_id+1}&timeout=20").json()
        for up in updates.get("result", []):
            last_id = up["update_id"]
            msg = up.get("message", {})
            cid = msg.get("chat", {}).get("id")
            text = msg.get("text", "")
            
            img_b64 = None
            if "photo" in msg:
                fid = msg["photo"][-1]["file_id"]
                f_info = requests.get(f"{T_URL}getFile?file_id={fid}").json()
                img_raw = requests.get(f"https://api.telegram.org/file/bot{KEYS['TG_TOKEN']}/{f_info['result']['file_path']}").content
                img_b64 = base64.b64encode(img_raw).decode("utf-8")
                text = msg.get("caption", "Analyze this image.")

            if text:
                requests.post(f"{T_URL}sendChatAction", data={"chat_id": cid, "action": "typing"})
                reply = call_gemini(text, img_b64)
                requests.post(f"{T_URL}sendMessage", data={"chat_id": cid, "text": f"🔱 {reply}"})
                
    except Exception as e:
        print(f"🔧 System Pulse: {e}")
        time.sleep(2)
