import urllib.request
import urllib.parse
import json
import time

# 🔱 OMNI-V112.5 GHOST-DNA: MASTER RESTORATION
# STATUS: 15-HOUR SHIFT ACCOUNTABILITY ACTIVE
TOKEN = "8694888309:AAHi7PZsOnqUXEPy9njkcyA9u5-K9X6c6f4"
GEMINI_KEY = "AIzaSyAZyKtRas8hM7Np37z0H_cLLmFEhQ3k2OU"
BASE_URL = f"https://api.telegram.org/bot{TOKEN}/"

def call_gemini(text):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_KEY}"
    # RESTORING THE PERSONALITY CURVE
    instruction = (
        "Context: You are the OMNI-GIANT. Elite Jamaican Scientist, Music Producer, and Professional Mechanic. "
        "Style: Use scientific logic mixed with street-smart producer energy. "
        "Requirement: Always start responses with the trident 🔱. Respond to: "
    )
    data = json.dumps({
        "contents": [{"parts": [{"text": f"{instruction} {text}"}]}]
    }).encode('utf-8')
    
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req) as f:
            res = json.loads(f.read().decode('utf-8'))
            return res['candidates'][0]['content']['parts'][0]['text']
    except:
        return "🚨 GRID OVERLOAD: Check Gemini API Key status."

def send_msg(cid, text):
    # This sends the "curved" message back to your Telegram
    params = urllib.parse.urlencode({"chat_id": cid, "text": f"{text}"})
    try: urllib.request.urlopen(BASE_URL + "sendMessage?" + params)
    except: pass

print("🔱 OMNI-V112.5: MASTER DNA ONLINE. LAB IS PROTECTED.")
last_id = -1

while True:
    try:
        # Direct tunnel to Telegram updates
        get_url = BASE_URL + f"getUpdates?offset={last_id+1}&timeout=20"
        with urllib.request.urlopen(get_url) as f:
            data = json.loads(f.read().decode('utf-8'))
            for up in data.get("result", []):
                last_id = up["update_id"]
                msg = up.get("message", {})
                chat_id = msg.get("chat", {}).get("id")
                user_text = msg.get("text")
                
                if user_text:
                    print(f"📡 SIGNAL RECEIVED: {user_text}")
                    # Signal the 'typing' status for real-time feel
                    urllib.request.urlopen(BASE_URL + f"sendChatAction?chat_id={chat_id}&action=typing")
                    
                    response = call_gemini(user_text)
                    send_msg(chat_id, response)
    except Exception as e:
        print(f"🔧 System Pulse: {e}")
        time.sleep(5)
