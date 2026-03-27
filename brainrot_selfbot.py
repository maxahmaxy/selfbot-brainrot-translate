"""
Discord Brainrot Selfbot (Auto-translate everything you type)
WARNING: Selfbots violate Discord ToS. Use at your own risk.
Only works on your OWN account. Never use on others.

HOW IT WORKS:
1. You type normally in Discord
2. The bot detects your message AFTER it's sent
3. It immediately edits it with the brainrot translation
"""

import discord
import anthropic
import os

# Your Discord USER token (not bot token - get from browser devtools)
DISCORD_USER_TOKEN = os.getenv("DISCORD_USER_TOKEN")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# Only translate in these channel IDs (leave empty to translate everywhere)
ALLOWED_CHANNELS = []  # e.g. [123456789, 987654321]

# Prefix to SKIP translation (type !real before message to send normally)
SKIP_PREFIX = "!real"

BRAINROT_SYSTEM_PROMPT = """You are a Gen Z brainrot translator. Convert any message into peak Gen Z brainrot language.

Rules:
- Use terms like: no cap, fr fr, bussin, rizz, slay, based, lowkey/highkey, NPC, W/L, goated, mid, rent free, ate and left no crumbs, understood the assignment, it's giving, sigma, alpha, caught in 4k, sussy, the ick, main character, delulu, situationship, beige flag, era, understood the assignment, real, the streets, chronically online, core (as suffix), type beat, pov:, I'm dead 💀, not me doing X, ratio, touch grass, we don't gatekeep here, mother, bestie, sheeesh, periodt
- Replace "very" with "absolutely unhinged level of"  
- Add random skibidi, rizz, sigma references where fitting
- Use excessive abbreviations: ngl, imo, tbh, istg, iykyk, lfg
- End statements with "no cap", "fr", "real", "periodt", or "slay"
- Use 💀😭🙏✨🔥💅🫡🤌 emojis liberally
- Keep the core meaning but make it sound like a chronically online teenager
- Keep it SHORT and punchy. Match original message length roughly.
- Output ONLY the translated message, nothing else."""

anth = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

class SelfBot(discord.Client):
    async def on_message(self, message):
        # Only process YOUR messages
        if message.author.id != self.user.id:
            return

        # Skip if not in allowed channels (if list is set)
        if ALLOWED_CHANNELS and message.channel.id not in ALLOWED_CHANNELS:
            return

        # Skip if using bypass prefix
        if message.content.startswith(SKIP_PREFIX):
            await message.edit(content=message.content[len(SKIP_PREFIX):].strip())
            return

        # Skip commands, mentions starting with !, or very short messages
        if message.content.startswith("!") or len(message.content) < 3:
            return

        # Skip if message is only emojis or special chars
        if all(not c.isalpha() for c in message.content):
            return

        try:
            response = anth.messages.create(
                model="claude-opus-4-5",
                max_tokens=500,
                system=BRAINROT_SYSTEM_PROMPT,
                messages=[{"role": "user", "content": message.content}]
            )
            brainrot_text = response.content[0].text
            await message.edit(content=brainrot_text)
        except Exception as e:
            print(f"Error translating: {e}")

selfbot = SelfBot()
selfbot.run(DISCORD_USER_TOKEN)
