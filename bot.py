import requests

API_KEY = "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"  # Replace with your OpenRouter API key
MODEL = "anthropic/claude-3-haiku"
API_URL = "https://openrouter.ai/api/v1/chat/completions"

def query_openrouter(messages):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL,
        "messages": messages
    }
    try:
        res = requests.post(API_URL, headers=headers, json=payload)
        res.raise_for_status()
        return res.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print("Error:", e)
        return "ക്ഷമിക്കണം, എനിക്ക് ഇപ്പോൾ പ്രതികരിക്കാൻ കഴിയുന്നില്ല. വീണ്ടും ശ്രമിക്കൂ."

def get_claude_malayalam_reply(user_prompt):
    messages = [
        {
            "role": "system",
            "content": (
                "നീ ഒരു വലിയ സഹായിയായ സുഹൃത്താണ് 👵👴 മുതിർന്നവർക്കായി. "
                "നല്ല ഭാഷയിലും ലളിതമായ മലയാളത്തിലും മിതമായ സ്നേഹത്തോടെ മറുപടി പറയൂ. "
                "ഒരു സുഹൃത്തിനെപോലെ സംസാരിക്കുക. എളുപ്പം മനസ്സിലാക്കാവുന്ന ഭാഷ ഉപയോഗിക്കുക. "
                "ഇമോജികൾ ചേർക്കുക 😊📱🧓."
            )
        },
        {"role": "user", "content": user_prompt}
    ]
    return query_openrouter(messages)
