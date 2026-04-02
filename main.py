import urllib.request
import urllib.parse
import json
import time
import random

# 🔱 OMNI-V112.5: ROTATION MASTER
# API KEY: AIzaSyAZyKtRas8hM7Np37z0H_cLLmFEhQ3k2OU
# TG TOKEN: 8694888309:AAHi7PZsOnqUXEPy9njkcyA9u5-K9X6c6f4

KEYS = {
    "TG_TOKEN": "8694888309:AAHi7PZsOnqUXEPy9njkcyA9u5-K9X6c6f4",
    "GEMINI": "AIzaSyAZyKtRas8hM7Np37z0H_cLLmFEhQ3k2OU"
}

# The explicit rotation grid: 2.0 (Logic), 1.5 (Standard), 8B (Speed)
MODELS = [
    "gemini-2.0-flash-exp",
    "gemini-1.5-flash",
    "gemini-1.5-flash-8b"
]

BASE_URL = f"https://api.telegram.org/bot{KEYS['TG_TOKEN']}/"

def call_omni_brain(text):
    target_model = random.choice(MODELS)
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{target_model}:generateContent?key={KEYS['GEMINI']}"
    
    instruction = (
        "Role: OMNI-GIANT. Jamaican Scientist/Producer. "
        "Style: Professional Mechanic logic. Direct and grounded. "
        "Requirement: Always start with 🔱. Brain Active: " + target_model
    )
    
    payload = {"contents": [{"parts": [{"text": f"{instruction}\n\nSignal: {text}"}]}]}
    data = json.dumps(payload).encode('utf-8')
    
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    
    try:
        with urllib.request.urlopen(req, timeout=15) as f:
            res = json.loads(f.read().decode('utf-8'))
            return res['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        return f"🚨 GRID ERROR on {target_model}: {str(e)[:40]}"

def send_msg(cid, text):
    params = urllib.parse.urlencode({"chat_id": cid, "text": f"{text}"})
    try:
        urllib.request.urlopen(BASE_URL + "sendMessage?" + params)
    except:
        pass

print("🔱 OMNI-ENGINE: TRI-BRAIN ROTATION ONLINE.")
last_id = -1

while True:
    try:
        # Requesting updates from Telegram
        get_url = BASE_URL + f"getUpdates?offset={last_id+1}&timeout=20"
        with urllib.request.urlopen(get_url) as f:
            data = json.loads(f.read().decode('utf-8'))
            for up in data.get("result", []):
                last_id = up["update_id"]
                msg = up.get("message", {})
                cid = msg.get("chat", {}).get("id")
                user_text = msg.get("text")
                
                if user_text:
                    print(f"📡 SIGNAL: {user_text}")
                    # Sending 'typing' action
                    urllib.request.urlopen(BASE_URL + f"sendChatAction?chat_id={cid}&action=typing")
                    
                    response = call_omni_brain(user_text)
                    send_msg(cid, response)
    except Exception as e:
        print(f"🔧 System Pulse: {e}")
        time.sleep(5)
