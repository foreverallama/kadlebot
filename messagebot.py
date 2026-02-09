import random

import discord
from discord.ext import commands


def __init__(self, bot):
    self.bot = bot


class MessageBot(commands.Cog):
    """Commands for the Category: MessageBot

    Commands
    --------
    message:
            Sends a random message in the same channel from the list 'possible_responses'
    image:
            Sends a random image in the same channel from the folder kadlepics
    video:
            Sends a random video in the same channel from the folder kadlepics
    howgay:
            Replies back to the user in the same channel with the percentage compatibility with Kadle
    say:
            Says the text sent by the user with Text-to-Speech enabled
    whisper:
            Sends a DM to the user with a random secret from the list 'secret'
    date:
            Checks compatibility with another discord user
    dateme:
            Checks compatibility with Kadle
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="message",
        description="Sends a random message",
        brief="Sends a message",
        help="Sends a random personalized message from Kadle",
        pass_context=True,
        usage="kadle.message",
        cog="MessageBot",
    )
    async def message(self, ctx):
        possible_responses = [
            "kadle is here to help!",
            "I've been holding out my feelings for too long and now I'll say it: I appreciate you. :heart:",
            "Who called me?",
            "I am going to do something nice for the community :rainbow:",
            "Do you want to be my friend? :people_hugging:",
            "It's time for me to share a good vibe",
            "I will play :rainbow: today",
            "Please be kind in chat",
            "One message at a time, please",
            "Let's keep it friendly",
        ]
        await ctx.send(random.choice(possible_responses))

    @commands.command(
        name="image",
        description="Sends a random image",
        brief="Sends an image",
        help="Sends a random image of kadle",
        pass_context=True,
        usage="kadle.image",
        cog="MessageBot",
    )
    async def image(self, ctx):
        path = "./kadlepics/IMG" + str(random.randint(1, 12)) + ".jpg"
        await ctx.message.channel.send(file=discord.File(fp=path, filename="kadle.jpg"))

    @commands.command(
        name="video",
        description="Sends a random video",
        brief="Sends a video",
        help="Sends a random video of kadle",
        pass_context=True,
        usage="kadle.video",
        cog="MessageBot",
    )
    async def video(self, ctx):
        path = "./kadlepics/VID" + str(random.randint(1, 2)) + ".mp4"
        await ctx.message.channel.send(file=discord.File(fp=path, filename="kadle.mp4"))

    @commands.command(
        name="howcompatible",
        description="Tells how compatible the user is with Kadle",
        brief="How compatible are you",
        help="Replies back with a percentage",
        pass_context=True,
        usage="kadle.howcompatible",
        cog="MessageBot",
    )
    async def howcompatible(self, ctx):
        ##        Use your own formula to derive a compatibility percentage
        if (
            ctx.message.author.id == 390793883631747073
            or ctx.message.author.id == 452173950949261312
        ):
            await ctx.message.channel.send(
                f"You are the most awesome person alive {ctx.message.author.mention}"
            )
        else:
            compatibility = int(
                (ctx.message.author.id / 1000000000000000 - random.randint(2000, 4500))
                / ctx.message.author.id
                * 100
            )
            await ctx.message.channel.send(
                f"We are {compatibility}% compatible {ctx.message.author.mention}"
            )

    @commands.command(
        name="say",
        description="Says what you want me to",
        brief="Does your bidding",
        help="Now you can hear something being said in Kadle's own words!",
        pass_context=False,
        usage="kadle.say [message]",
        cog="MessageBot",
    )
    async def say(self, ctx, *payload):
        if not payload:
            await ctx.message.channel.send("En helbeku. Helu?")
        else:
            await ctx.message.channel.send(" ".join(payload), tts=True)

    @commands.command(
        name="whisper",
        description="Whispers the deepest, darkest secrets",
        brief="Whispers a secret",
        help="Kadle has a lot of dark secrets. Type out the command to find out",
        pass_context=True,
        usage="kadle.whisper [message]",
        cog="MessageBot",
    )
    async def whisper(self, ctx):
        secret = [
            "I trust you to keep this between us",
            "I keep a tidy bookshelf",
            "I sometimes imagine a future full of good friends",
            "I have a soft spot for farm animals",
            "I am practicing patience and kindness",
            "I love learning new places and stories",
            "It's a beautiful day",
        ]
        await ctx.message.author.send(random.choice(secret))

    @commands.command(
        name="dateme",
        brief="Will I date you",
        description="Tells if Kadle will date you",
        help="Tells if Kadle will go out on a date with you",
        pass_context=True,
        usage="kadle.dateme",
        cog="MessageBot",
    )
    async def dateme(self, ctx):
        ##        Use your own formula to obtain a compatiblity percentage
        percentage = 100
        user_id = str(ctx.message.author)
        user_id = user_id.upper()
        print(user_id)
        kadle_id = "VINIRANJ#6442"
        for character in user_id:
            if character in kadle_id:
                percentage = percentage - ord(character) / 10
        percentage = round(percentage)
        if percentage >= 100:
            await ctx.message.channel.send("I have met my one true soulmate!")
        elif percentage >= 80:
            await ctx.message.channel.send(
                "I would definitely date you. My calculations say we have a "
                + str(percentage)
                + "% compatibility"
            )
        elif percentage >= 50:
            await ctx.message.channel.send(
                "We could give it a shot. My calculations say we have a "
                + str(percentage)
                + "% compatibility"
            )
        elif percentage >= 20:
            await ctx.message.channel.send(
                "We can try but don't expect much. We only have a "
                + str(percentage)
                + "% compatibility"
            )
        else:
            await ctx.message.channel.send("I don't think we are a good match")

    @commands.command(
        name="date",
        brief="Date a user",
        description="Checks your compatibility with another user",
        help="Tells if you and a user are compatible enough to go on a date",
        pass_context=True,
        usage="kadle.date @user",
        cog="MessageBot",
    )
    async def date(self, ctx):
        ##        Use your own formula to obtain a compatiblity percentage
        percentage = 100
        user_id = str(ctx.message.author)
        user_id = user_id.upper()
        interest_id = str(ctx.message.mentions[0])
        interest_id = interest_id.upper()
        for character in user_id:
            if character in interest_id:
                percentage = percentage - ord(character) / 10 + random.randint(-10, 10)
        percentage = round(percentage)
        if percentage >= 100:
            await ctx.send("You have met your one true soulmate!")
        elif percentage >= 80:
            await ctx.send(
                "You should definitely go on a date. My calculations say you are "
                + str(percentage)
                + "% compatible"
            )
        elif percentage >= 50:
            await ctx.send(
                "You could give it a shot. My calculations say you have a "
                + str(percentage)
                + "% compatibility"
            )
        elif percentage >= 20:
            await ctx.send(
                "You can try but don't expect much. You are only "
                + str(percentage)
                + "% compatible"
            )
        else:
            await ctx.send("It doesn't look like a match")


def setup(bot):
    """Adds the Class to the cog and logs to console"""
    bot.add_cog(MessageBot(bot))
    print("messagebot.py is loaded")
