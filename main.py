import urllib.request
import urllib.parse
import json
import time

# 🔱 OMNI-V112.5: THE GOLDEN KEY (DIRECT ENDPOINT)
# ACTIVE KEYS FOR STEROKAI LABS
TOKEN = "8694888309:AAHi7PZsOnqUXEPy9njkcyA9u5-K9X6c6f4"
GEMINI_KEY = "AIzaSyAZyKtRas8hM7Np37z0H_cLLmFEhQ3k2OU"
BASE_URL = f"https://api.telegram.org/bot{TOKEN}/"

# This is the exact string the API is accepting TODAY for the Elite logic
# It covers both the high-speed and high-thinking logic tiers.
ACTIVE_DNA = "gemini-2.0-flash-exp" 

def call_omni_brain(text):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{ACTIVE_DNA}:generateContent?key={GEMINI_KEY}"
    
    # Restoring the "Curved" logic you need
    instruction = "System: OMNI-GIANT. Jamaican Scientist. Logic Elite. Response start with 🔱. Signal: "
    payload = {"contents": [{"parts": [{"text": f"{instruction} {text}"}]}]}
    
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    
    try:
        with urllib.request.urlopen(req, timeout=30) as f:
            res = json.loads(f.read().decode('utf-8'))
            return res['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        return f"🚨 GRID ERROR: {str(e)[:50]}"

def send_msg(cid, text):
    params = urllib.parse.urlencode({"chat_id": cid, "text": f"{text}"})
    try: urllib.request.urlopen(BASE_URL + "sendMessage?" + params)
    except: pass

print("🔱 OMNI-ENGINE: GOLDEN KEY ACTIVE. SYSTEM FIRING.")
last_id = -1

while True:
    try:
        # Direct tunnel to Telegram
        get_url = BASE_URL + f"getUpdates?offset={last_id+1}&timeout=20"
        with urllib.request.urlopen(get_url) as f:
            data = json.loads(f.read().decode('utf-8'))
            for up in data.get("result", []):
                last_id = up["update_id"]
                msg = up.get("message", {})
                cid = msg.get("chat", {}).get("id")
                if "text" in msg:
                    # 'Typing' signal shows the engine is alive
                    urllib.request.urlopen(BASE_URL + f"sendChatAction?chat_id={cid}&action=typing")
                    reply = call_omni_brain(msg["text"])
                    send_msg(cid, reply)
    except: time.sleep(5)
