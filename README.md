# 🧠 Discord Brainrot Translator

Automatically translates everything you type in Discord into Gen Z brainrot language, using Claude AI.

⚠️ This uses a Discord selfbot, which violates Discord ToS. Risk of account ban is low for personal use but exists. Use on personal/test accounts only.

---

## Step 1 — Get your Anthropic API key

This is what powers the AI translation.

1. Go to **console.anthropic.com** and sign up / log in
2. In the left sidebar click **API Keys**
3. Click **Create Key** → give it a name → copy the key (starts with `sk-ant-...`)
4. Save it somewhere — you won't see it again

> You'll need to add a payment method. Usage for this bot is very cheap (~$0.01 per few hundred messages).

---

## Step 2 — Get your Discord user token

1. Open Discord in your **browser** at discord.com/app (not the desktop app)
2. Press **F12** to open DevTools
3. Go to the **Console** tab
4. If you see a warning about pasting, type `allow pasting` and press Enter first
5. Paste the following and press Enter:

```javascript
window.webpackChunkdiscord_app.push([
  [Math.random()],
  {},
  req => {
    for (const m of Object.values(req.c)) {
      try {
        const token = m.exports?.default?.getToken?.();
        if (token) console.log(token);
      } catch {}
    }
  }
]);
```

6. Your token will appear in the console — copy it

> ⚠️ Never share this token with anyone. It gives full access to your Discord account.

---

## Step 3 — Set up Python

Make sure you have Python 3.8+ installed. Check with:

```bash
python3 --version
```

Then create a project folder and install dependencies:

```bash
mkdir brainrot && cd brainrot
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install discord.py-self anthropic
```

---

## Step 4 — Download the script

```bash
curl -O https://raw.githubusercontent.com/maxahmaxy/selfbot-brainrot-translate/main/brainrot_selfbot.py
```

Or just download `brainrot_selfbot.py` manually from this repo.

---

## Step 5 — Run it

**Mac/Linux:**
```bash
DISCORD_USER_TOKEN=your_token_here ANTHROPIC_API_KEY=your_key_here python brainrot_selfbot.py
```

**Windows:**
```cmd
set DISCORD_USER_TOKEN=your_token_here
set ANTHROPIC_API_KEY=your_key_here
python brainrot_selfbot.py
```

If it doesn't crash, it's running.

---

## Step 6 — Test it

Go to any Discord channel and type a normal message. After ~1 second it will auto-edit into brainrot.

---

## Controls

| What you want | How |
|---|---|
| Translate everything | Just type normally |
| Skip translation for one message | Start with `!real` e.g. `!real hey be serious for a sec` |
| Limit to specific channels only | Edit `ALLOWED_CHANNELS` in the script with channel IDs |

### How to get a channel ID
1. In Discord go to **Settings → Advanced → enable Developer Mode**
2. Right-click any channel → **Copy Channel ID**
3. Add it to the script: `ALLOWED_CHANNELS = [123456789]`

---

## Keeping it running

The bot stops when you close the terminal. Options:

- **Leave the terminal open** — simplest
- **tmux** (Linux/Mac): `tmux new -s brainrot` → run the script → `Ctrl+B D` to detach
- **Host on a VPS** — Hetzner CX11 is ~€4/month and works great
