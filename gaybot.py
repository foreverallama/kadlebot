import asyncio
import random
import discord
from discord.ext import commands

def __init__(self, bot):
        self.bot = bot

class GayStuff:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='message',
                      description='Sends a random message',
                      brief='Sends a message',
                      help='Sends a random personalized message from Kadle',
                      pass_context=False,
                      no_pm=True)
    async def message(self):
        possible_responses = ['kadle is gay!',
         'I\'ve been holding out my feelings for too long and now I\'ll come out and say it. I am gay :heart:',
         'Did someone call me?',
         'I am going to do something for the LGBT community :gay_pride_flag:',
         'Do you want to be my.... boyfriend? :couple_mm:',
         'It\'s time for me to come out of the closet',
         'I will play :rainbow: today',
         'Nodu... bai muchko illa andre dengbidthini',
         'Innondu sala message madu andre dengbidthini',
         'Sumne iru! Nan thante ge barbeda',
         ]
        await self.bot.say(random.choice(possible_responses))

    @commands.command(name='image',
                      description='Sends a random image',
                      brief='Sends an image',
                      help='Sends a random gay image of kadle',
                      pass_context=True,
                      no_pm=True)
    async def image(self, ctx):
        path = ['./kadlepics/IMG1.jpg',
                './kadlepics/IMG2.png',
                './kadlepics/IMG3.jpg',
                './kadlepics/IMG4.jpg',
                './kadlepics/IMG5.jpg',
                './kadlepics/IMG6.jpg',
                './kadlepics/IMG7.jpg',
                './kadlepics/IMG8.jpg',
                './kadlepics/IMG9.jpg',
                './kadlepics/IMG11.jpg',
                './kadlepics/IMG12.jpg',
                ]
        await self.bot.send_file(ctx.message.channel, random.choice(path))

    @commands.command(name='video',
                      description='Sends a random video',
                      brief='Sends a video',
                      help='Sends a random gay video of kadle',
                      pass_context=True,
                      no_pm=True)
    async def video(self, ctx):
        path = ['./kadlepics/VID1.mp4',
                './kadlepics/VID2.mp4',
                ]
        await self.bot.send_file(ctx.message.channel, random.choice(path))

    @commands.command(name='howgay',
                      description='Tells how gay the user is',
                      brief='How gay are you',
                      help='Replies back with the Gayness in percentage',
                      pass_context=True,
                      no_pm=True)
    async def howgay(self, ctx):
        if ctx.message.author.id == '390793883631747073' or ctx.message.author.id == '452173950949261312':
            await self.bot.say('You are absolutely 100% gay ' + ctx.message.author.mention)
        else:
            await self.bot.say('You are completely straight ' + ctx.message.author.mention)

    @commands.command(name='say',
                      description='Says what you want me to',
                      brief='Does your bidding',
                      help='Now you can hear something being said in Kadle\'s own words!',
                      pass_context=False,
                      no_pm=True)
    async def say(self, *, payload=None):
        if (payload == None):
            await self.bot.say('You need to specify something for me to say')
        else:
            await self.bot.say(payload, tts=True);

    @commands.command(name='whisper',
                      description='Whispers the deepest, darkest secrets',
                      brief='Whispers a secret',
                      help='Kadle has a lot of dark secrets. Type out the command to find out',
                      pass_context=True,
                      no_pm=True)
    async def whisper(self, ctx):
        secret = ['I don\t trust you to keep my secrets so please stop asking',
              'I first got married at the age of 6',
              'I sometimes imagine a future for you and me',
              'I have 12 cows whom I love everyday',
              'My second wife doesn\'t seem to love me anymore',
              'I originally migrated from Nepal through Uttarkhand and changed my surname from \'Bhatt\' to \'Bhat\'',
              'It\'s a beautful day',
              ]
        await self.bot.send_message(ctx.message.author, random.choice(secret))
  
def setup(bot):
    bot.add_cog(GayStuff(bot))
    print('gaybot is loaded')
