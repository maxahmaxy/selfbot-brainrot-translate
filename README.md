# 🧠 Discord Brainrot Translator

Translates your messages into Gen Z brainrot using Claude AI.

---

## Option 1: Slash Command Bot (Recommended, ToS-safe)

### Setup
1. Go to https://discord.com/developers/applications
2. Create a new application → Bot → copy the TOKEN
3. Enable "applications.commands" scope and "bot" permissions
4. Invite bot to your server with this URL (replace CLIENT_ID):
   `https://discord.com/oauth2/authorize?client_id=CLIENT_ID&scope=bot+applications.commands&permissions=2048`

### Run
```bash
pip install -r requirements.txt
DISCORD_TOKEN=your_token ANTHROPIC_API_KEY=your_key python brainrot_bot.py
```

### Usage
Type `/brainrot <your message>` in any channel.

---

## Option 2: Selfbot (Auto-translates everything, ToS risk)

⚠️ Selfbots violate Discord ToS. Risk of account ban. Use only on personal/test accounts.

### Get your user token
1. Open Discord in browser (discord.com/app)
2. Press F12 → Network tab
3. Refresh the page
4. Filter for "api" requests → find any request → Headers → Authorization header

### Run
```bash
pip install -r requirements.txt
DISCORD_USER_TOKEN=your_token ANTHROPIC_API_KEY=your_key python brainrot_selfbot.py
```

### Controls
- Sends normally: type `!real your message` (strips the prefix, no translation)
- Auto-translates: everything else gets brainrot'd after sending

---

## Tips
- Each translation costs ~1-3 Claude API credits (very cheap)
- The selfbot edits your message ~1 second after sending
- You can restrict selfbot to specific channels by filling ALLOWED_CHANNELS in the script
