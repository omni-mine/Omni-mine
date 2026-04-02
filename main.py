import urllib.request
import urllib.parse
import json
import time

# 🔱 OMNI-V112.5 GHOST-DNA: FINAL STAND
# DIRECT KEYS - NO CACHE - NO LIBRARIES
TOKEN = "8694888309:AAHi7PZsOnqUXEPy9njkcyA9u5-K9X6c6f4"
GEMINI_KEY = "AIzaSyAZyKtRas8hM7Np37z0H_cLLmFEhQ3k2OU"
BASE_URL = f"https://api.telegram.org/bot{TOKEN}/"

def call_gemini(text):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_KEY}"
    data = json.dumps({"contents": [{"parts": [{"text": f"You are the OMNI-GIANT Scientist. Brief logic only: {text}"}]}]}).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req) as f:
            res = json.loads(f.read().decode('utf-8'))
            return res['candidates'][0]['content']['parts'][0]['text']
    except: return "🚨 GRID OVERLOAD."

def send_msg(cid, text):
    url = BASE_URL + "sendMessage?" + urllib.parse.urlencode({"chat_id": cid, "text": f"🔱 {text}"})
    urllib.request.urlopen(url)

print("👑 OMNI-ENGINE: FINAL STAND ONLINE.")
last_id = -1

while True:
    try:
        url = BASE_URL + f"getUpdates?offset={last_id+1}&timeout=10"
        with urllib.request.urlopen(url) as f:
            data = json.loads(f.read().decode('utf-8'))
            for up in data.get("result", []):
                last_id = up["update_id"]
                msg = up.get("message", {})
                text = msg.get("text")
                if text:
                    print(f"📡 SIGNAL: {text}")
                    reply = call_gemini(text)
                    send_msg(msg['chat']['id'], reply)
    except: time.sleep(5)
