# 🧠 Discord Brainrot Translator

Translates your messages into Gen Z brainrot using Claude AI.

---

## Selfbot (Auto-translates everything you type)

⚠️ Selfbots violate Discord ToS. Risk of account ban. Use only on personal/test accounts.

### Get your user token
1. Open Discord in browser (discord.com/app)
2. Press F12 → Console tab
3. Paste this and hit Enter:
```javascript
window.webpackChunkdiscord_app.push([[Math.random()],{},req=>{for(const m of Object.values(req.c)){try{const token=m.exports?.default?.getToken?.();if(token)console.log(token);}catch{}}});
```
4. Copy the token that prints

### Run
```bash
pip install discord.py-self anthropic
DISCORD_USER_TOKEN=your_token ANTHROPIC_API_KEY=your_key python brainrot_selfbot.py
```

### Controls
- Auto-translates: everything you type gets brainrot'd after sending
- Skip translation: prefix with `!real your message`

---

## Tips
- Each translation costs ~1-3 Claude API credits (very cheap)
- The selfbot edits your message ~1 second after sending
- Restrict to specific channels by filling `ALLOWED_CHANNELS` in the script

