import asyncio
import discord
import random
from discord.ext import commands
if not discord.opus.is_loaded():
    # the 'opus' library here is opus.dll on windows
    # or libopus.so on linux in the current directory
    # you should replace this with the location the
    # opus library is located in and with the proper filename.
    # note that on windows this DLL is automatically provided for you
    discord.opus.load_opus('./libopus.so')

def __init__(self, bot):
        self.bot = bot

class VoiceEntry:
    """Contains the player information"""
    def __init__(self, message, player):
        self.requester = message.author
        self.channel = message.channel
        self.player = player

    def __str__(self):
        fmt = ' {0.title}'
        duration = self.player.duration
        return fmt.format(self.player)

class VoiceState:
    """Contains the player details"""
    def __init__(self, bot):
        self.current = None
        self.voice = None
        self.bot = bot
        self.play_next_song = asyncio.Event()
        self.songs = asyncio.Queue()
        self.skip_votes = set() # a set of user_ids that voted
        self.audio_player = self.bot.loop.create_task(self.audio_player_task())

    def is_playing(self):
        if self.voice is None or self.current is None:
            return False

        player = self.current.player
        return not player.is_done()

    @property
    def player(self):
        return self.current.player

    def skip(self):
        self.skip_votes.clear()
        if self.is_playing():
            self.player.stop()

    def toggle_next(self):
        self.bot.loop.call_soon_threadsafe(self.play_next_song.set)

    async def audio_player_task(self):
        while True:
            self.play_next_song.clear()
            self.current = await self.songs.get()
            await self.bot.send_message(self.current.channel, 'Now playing' + str(self.current))
            self.current.player.start()
            await self.play_next_song.wait()
            
class Music:
    """Commands for the Category: Music
    Works in multiple servers at once

    Commands
    --------
    join:
            Joins the same voice channel as the user who requested it
    play:
            If a search term is specified, it plays the first search result (from YouTube)
            Else it plays a random Bhajan from the list 'url'
            If a song is already playing, then it is added to queue
    volume:
            Adjusts the volume of the playback as an integer between 0 to 100
    pause:
            Pauses the player
    resume:
            Resumes the player
    stop:
            Stops the player and disconnects from the Voice Channel
    """
    def __init__(self, bot):
        self.bot = bot
        self.voice_states = {}

    def get_voice_state(self, server):
        state = self.voice_states.get(server.id)
        if state is None:
            state = VoiceState(self.bot)
            self.voice_states[server.id] = state

        return state

    async def create_voice_client(self, channel):
        voice = await self.bot.join_voice_channel(channel)
        state = self.get_voice_state(channel.server)
        state.voice = voice

    def __unload(self):
        for state in self.voice_states.values():
            try:
                state.audio_player.cancel()
                if state.voice:
                    self.bot.loop.create_task(state.voice.disconnect())
            except:
                pass

    @commands.command(name='join',
                      description='Joins the voice channel the user is in',
                      brief='Join voice channel',
                      help='This command allows the bot to join the same voice channel as the user who invoked the command',
                      pass_context=True,
                      no_pm=True)
    async def join(self, ctx):
        summoned_channel = ctx.message.author.voice_channel
        if summoned_channel is None:
            await self.bot.say('You need to join a voice channel first')
            return False

        state = self.get_voice_state(ctx.message.server)
        if state.voice is None:
            state.voice = await self.bot.join_voice_channel(summoned_channel)
        else:
            await state.voice.move_to(summoned_channel)
            
        return True

    @commands.command(name='play',
                      description='Plays a random soulful piece of music',
                      brief='Plays a song',
                      help='If a search term is specified, it plays the the first YouTube result. Otherwise it plays a random Bhajan',
                      pass_context=True,
                      no_pm=True)
    @commands.cooldown(3, 120, commands.BucketType.user)
    async def play(self, ctx, *, song=None):
        
        state = self.get_voice_state(ctx.message.server)
        opts = {
            'default_search': 'auto',
            'quiet': True,
        }

        if state.voice is None:
            success = await ctx.invoke(self.join)
            if not success:
                return
        url = ['https://www.youtube.com/watch?v=iW16WWmWZL4',
               'https://www.youtube.com/watch?v=2yAzgg3zEjM',
               'https://www.youtube.com/watch?v=Ezhdk82sR1Y',
               ]
        try:
            if song is None:
                player = await state.voice.create_ytdl_player(random.choice(url), after=state.toggle_next)
            else:
                player = await state.voice.create_ytdl_player(song, ytdl_options=opts, after=state.toggle_next)
        except Exception as e:
            fmt = 'An error occurred while processing this request: ```py\n{}: {}\n```'
            await self.bot.send_message(ctx.message.channel, fmt.format(type(e).__name__, e))
        else:
            player.volume = 0.6
            entry = VoiceEntry(ctx.message, player)
            await state.songs.put(entry)
    
            

    @commands.command(name='volume',
                      description='Adjusts the volume',
                      brief='Adjust volume',
                      help='Can set the volume of the music being played as an integer between 0 to 100', 
                      pass_context=True,
                      no_pm=True)
    async def volume(self, ctx, value : int):
        if value is None:
            await self.bot.say("You need to specify a value between 0 to 100")
        else:
            state = self.get_voice_state(ctx.message.server)
            if state.is_playing():
                player = state.player
                player.volume = value / 100
                await self.bot.say('Volume set to {:.0%}'.format(player.volume))

    @commands.command(name='resume',
                      description='Resumes the song',
                      brief='Resumes playing',
                      help='Resumes playing the song, if paused previously',
                      pass_context=True,
                      no_pm=True)
    async def resume(self, ctx):
        state = self.get_voice_state(ctx.message.server)
        if state.is_playing():
            player = state.player
            player.resume()

    @commands.command(name='pause',
                      description='Pauses the song',
                      brief='Pauses music',
                      help='Pauses the music, if already playing',
                      pass_context=True,
                      no_pm=True)
    async def pause(self, ctx):
        state = self.get_voice_state(ctx.message.server)
        if state.is_playing():
            player = state.player
            player.pause()

    @commands.command(name='stop',
                      description='Regretfully stops playing the music',
                      brief='Stops playing',
                      help='Stops playing the music and leaves the voice channel',
                      pass_context=True,
                      no_pm=True)
    async def stop(self, ctx):
        server = ctx.message.server
        state = self.get_voice_state(server)

        if state.is_playing():
            player = state.player
            player.stop()

        try:
            state.audio_player.cancel()
            del self.voice_states[server.id]
            await state.voice.disconnect()
            await self.bot.say("Cleared the queue and disconnected from voice channel ")
        except:
            pass
      
def setup(bot):
    bot.add_cog(Music(bot))
    print('Bhajans is loaded')
