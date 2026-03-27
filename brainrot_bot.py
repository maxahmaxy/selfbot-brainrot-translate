"""
Discord Brainrot Bot (Slash Command version - ToS safe)
Usage: /brainrot <your message here>
"""

import discord
from discord import app_commands
import anthropic
import os

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

BRAINROT_SYSTEM_PROMPT = """You are a Gen Z brainrot translator. Convert any message into peak Gen Z brainrot language.

Rules:
- Use terms like: no cap, fr fr, bussin, rizz, slay, based, lowkey/highkey, NPC, W/L, goated, mid, rent free, ate and left no crumbs, understood the assignment, it's giving, sigma, alpha, caught in 4k, sussy, the ick, main character, delulu, situationship, beige flag, era, understood the assignment, real, unalive (instead of die), the streets, chronically online, core (as suffix), type beat, pov:, I'm dead 💀, not me doing X, ratio, touch grass, no printer just fax, we don't gatekeep here, mother, bestie, sheeesh, periodt, and it's giving [adjective] era
- Replace "very" with "absolutely unhinged level of"
- Add random skibidi, rizz, sigma references where fitting
- Use excessive abbreviations: ngl, imo, tbh, istg, iykyk, lfg, sfs, dni, fyp
- End statements with "no cap", "fr", "real", "periodt", or "slay"
- Use 💀😭🙏✨🔥💅🫡🤌 emojis liberally but not every word
- Keep the core meaning but make it sound like a chronically online 16-year-old
- Keep it SHORT and punchy. Match original message length roughly.
- Output ONLY the translated message, nothing else."""

class BrainrotBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
        self.anthropic = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    async def setup_hook(self):
        await self.tree.sync()
        print(f"Synced slash commands for {self.user}")

    def translate_to_brainrot(self, text: str) -> str:
        response = self.anthropic.messages.create(
            model="claude-opus-4-5",
            max_tokens=500,
            system=BRAINROT_SYSTEM_PROMPT,
            messages=[{"role": "user", "content": text}]
        )
        return response.content[0].text

client = BrainrotBot()

@client.tree.command(name="brainrot", description="Translate your message to Gen Z brainrot")
@app_commands.describe(message="The message you want to brainrot-ify")
async def brainrot(interaction: discord.Interaction, message: str):
    await interaction.response.defer()
    try:
        translated = client.translate_to_brainrot(message)
        embed = discord.Embed(
            description=translated,
            color=0xFF6B6B
        )
        embed.set_footer(text=f"original: {message[:80]}{'...' if len(message) > 80 else ''}")
        await interaction.followup.send(embed=embed)
    except Exception as e:
        await interaction.followup.send(f"ratio'd by an error: {e}", ephemeral=True)

client.run(DISCORD_TOKEN)
