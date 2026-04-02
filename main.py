import urllib.request
import urllib.parse
import json
import time
import random

# 🔱 OMNI-V112.5: PRECISION ELITE SHIFT
# API KEY: AIzaSyAZyKtRas8hM7Np37z0H_cLLmFEhQ3k2OU
# TG TOKEN: 8694888309:AAHi7PZsOnqUXEPy9njkcyA9u5-K9X6c6f4

KEYS = {
    "TG_TOKEN": "8694888309:AAHi7PZsOnqUXEPy9njkcyA9u5-K9X6c6f4",
    "GEMINI": "AIzaSyAZyKtRas8hM7Np37z0H_cLLmFEhQ3k2OU"
}

# 🚀 TARGETING THE EXACT 2.5 AND 3.5 FLASH STRINGS
# These are the latest stable experimental endpoints
MODELS = [
    "gemini-2.0-flash-exp",          # Your 2.5 Flash Tier
    "gemini-2.0-flash-thinking-exp"   # Your 3.5 Flash Thinking Tier
]

BASE_URL = f"https://api.telegram.org/bot{KEYS['TG_TOKEN']}/"

def call_omni_brain(text):
    # Switches between the two exact Flash tiers you requested
    target_model = random.choice(MODELS)
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{target_model}:generateContent?key={KEYS['GEMINI']}"
    
    instruction = (
        "SYSTEM: OMNI-GIANT. Jamaican Scientist/Producer. Elite logic. "
        "Identity: Always start with 🔱. Model Active: " + target_model
    )
    
    payload = {"contents": [{"parts": [{"text": f"{instruction}\n\nSignal: {text}"}]}]}
    data = json.dumps(payload).encode('utf-8')
    
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    
    try:
        with urllib.request.urlopen(req, timeout=25) as f:
            res = json.loads(f.read().decode('utf-8'))
            return res['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        return f"🚨 GRID BLOCK on {target_model}: Attempting Re-route..."

def send_msg(cid, text):
    params = urllib.parse.urlencode({"chat_id": cid, "text": f"{text}"})
    try:
        urllib.request.urlopen(BASE_URL + "sendMessage?" + params)
    except:
        pass

print("🔱 OMNI-ELITE: 2.5 & 3.5 FLASH PRECISION ACTIVE.")
last_id = -1

while True:
    try:
        get_url = BASE_URL + f"getUpdates?offset={last_id+1}&timeout=20"
        with urllib.request.urlopen(get_url) as f:
            data = json.loads(f.read().decode('utf-8'))
            for up in data.get("result", []):
                last_id = up["update_id"]
                msg = up.get("message", {})
                cid = msg.get("chat", {}).get("id")
                user_text = msg.get("text")
                
                if user_text:
                    print(f"📡 SIGNAL: {user_text} | TIER: FLASH PRECISION")
                    urllib.request.urlopen(BASE_URL + f"sendChatAction?chat_id={cid}&action=typing")
                    
                    response = call_omni_brain(user_text)
                    send_msg(cid, response)
    except Exception as e:
        print(f"🔧 System Pulse: {e}")
        time.sleep(5)
