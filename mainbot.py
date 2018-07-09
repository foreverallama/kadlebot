import asyncio
import discord
from discord.voice_client import VoiceClient
from discord.ext.commands import Bot
from discord.ext import commands
import os

startup_extensions = ["gaybot", "musicbot"]
TOKEN = os.environ.get('TOKEN', None)
# Get at discordapp.com/developers/applications/me

client = Bot(command_prefix='kadle.', description='Kadle says GAY!')
client.remove_command('help')    
@client.event
async def on_message(message):
    swear_words = ['FUCK', 'BASTARD', 'AMMAN', 'SULE', 'MOTHERFUCKER',
                   'ASSHOLE', 'DENGIBDTHINI', 'TIKKA', 'SHIT', 'CRAP',
                    ]
    if message.author == client.user:
        return #Prevents the bot from replying to itself
    if message.content.startswith('kadle.'):
        await client.process_commands(message)
    elif any(word in message.content.upper() for word in swear_words):
        await client.send_message(message.channel,'Hari Om')
    elif 'WONDERLA' in message.content.upper():
        await client.send_message(message.channel,'Only gay people go to Wonderla')

@client.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.CommandOnCooldown):
        await client.send_message(ctx.message.channel, content='`You can use this command only after %.2fs seconds. Spam madidre dengbidthini`' % error.retry_after)

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='kadle.help',type=2))
    print('Logged in as ' + client.user.name + ': ' + client.user.id)
    print('--------------------------------------')

class Utility:
    @commands.command(pass_context=True)
    async def help(self, ctx, *args: str):
        return await commands.bot._default_help_command(ctx, *args)
    
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__,e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

client.add_cog(Utility())
client.run(TOKEN)

