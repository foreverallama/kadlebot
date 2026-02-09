import asyncio
import random

import discord
from discord.ext import commands


def __init__(self, bot):
    self.bot = bot


class Love(commands.Cog):
    """Commands for the Category: Rainbow

    Commands
    --------

    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="date",
        brief="Checks compatibility",
        description="Checks your compatibility with another user",
        help="Tells if you and a user are compatible enough to go on a date",
        pass_context=True,
    )
    async def date(self, ctx):
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
            await ctx.send("It does not look like a match")

    @commands.command(
        name="eqtest",
        brief="How dateable you are",
        description="Checks how dateable you are by assessing your personality",
        help="Asks 5 questions to determine your personality and tells how dateable you are",
        pass_context=True,
        no_pm=True,
    )
    async def eqtest(self, ctx):
        await ctx.send(
            f"{ctx.message.author.mention}, I will ask you 5 yes-no questions to determine your personality."
            "Answer honestly, please.\n\n"
            "__Instructions__\n\n"
            "1. Type `kadle.start` to start the test\n"
            "2. Answer each question with `kadle.yes` or `kadle.no`\n"
            "3. Wait for results\n"
            "4. You can cancel anytime by not answering for 60 seconds"
        )

        def check(m):
            if (
                m.content == "kadle.start"
                and m.author == ctx.message.author
                and m.channel == ctx.message.channel
            ):
                return True

        msg = await self.bot.wait_for("message", timeout=60, check=check)
        if msg:
            list_of_questions = [
                [
                    "`Consider a scenario where you can save only two people, including yourself. Will you save your oldest friend?`",
                    "`Will you save your newest friend?`",
                    "`Would you go out of your way to help a friend in need?`",
                    "`Do you keep a consistent daily routine?`",
                    "`Would you support your team when it matters most?`",
                ]
            ]
            question_bank = random.randint(0, 0)
            current_questions = list_of_questions[question_bank]
            answers = []

            def check1(m):
                print(str(m.author))
                print(str(ctx.message.author))
                if m.author == ctx.message.author and m.channel == ctx.message.channel:
                    if str(m.content) == "kadle.yes":
                        return "YES"
                    elif str(m.content) == "kadle.no":
                        return "NO"

            for i in range(0, 5):
                await ctx.send(current_questions[i])
                msg = await self.bot.wait_for(timeout=60, check=check1)
                if msg:
                    answers.append(str(msg.content))
                else:
                    await ctx.send(
                        f"{ctx.message.author.mention}, Please don't waste my time."
                    )

            if question_bank == 0:
                if (
                    answers[0] == "kadle.yes"
                    and answers[1] == "kadle.yes"
                    and answers[2] == "kadle.yes"
                    and answers[3] == "kadle.yes"
                    and answers[4] == "kadle.yes"
                ):
                    msg = "Thanks for sharing. Compatibility rating: 7/10."
                    await ctx.send(ctx.message.author.mention + msg)
                elif (
                    answers[0] == "kadle.yes"
                    and answers[1] == "kadle.yes"
                    and answers[2] == "kadle.yes"
                    and answers[3] == "kadle.yes"
                    and answers[4] == "kadle.no"
                ):
                    msg = "Thanks for sharing. Compatibility rating: 5/10."
                    await ctx.send(ctx.message.author.mention + msg)
                elif (
                    answers[0] == "kadle.yes"
                    and answers[1] == "kadle.yes"
                    and answers[2] == "kadle.yes"
                    and answers[3] == "kadle.no"
                    and answers[4] == "kadle.yes"
                ):
                    msg = "Thanks for sharing. Compatibility rating: 6/10."
                    await ctx.send(ctx.message.author.mention + msg)
                elif (
                    answers[0] == "kadle.yes"
                    and answers[1] == "kadle.yes"
                    and answers[2] == "kadle.yes"
                    and answers[3] == "kadle.no"
                    and answers[4] == "kadle.no"
                ):
                    msg = "Thanks for sharing. Compatibility rating: 10/10."
                    await ctx.send(ctx.message.author.mention + msg)
                elif (
                    answers[0] == "kadle.yes"
                    and answers[1] == "kadle.yes"
                    and answers[2] == "kadle.no"
                    and answers[3] == "kadle.yes"
                    and answers[4] == "kadle.yes"
                ):
                    msg = "Thanks for sharing. Compatibility rating: 5/10."
                    await ctx.send(ctx.message.author.mention + msg)
                elif (
                    answers[0] == "kadle.yes"
                    and answers[1] == "kadle.yes"
                    and answers[2] == "kadle.no"
                    and answers[3] == "kadle.yes"
                    and answers[4] == "kadle.no"
                ):
                    msg = "Thanks for sharing. Compatibility rating: 3/10."
                    await ctx.send(ctx.message.author.mention + msg)
                elif (
                    answers[0] == "kadle.yes"
                    and answers[1] == "kadle.yes"
                    and answers[2] == "kadle.no"
                    and answers[3] == "kadle.no"
                    and answers[4] == "kadle.yes"
                ):
                    msg = "Thanks for sharing. Compatibility rating: 5/10."
                    await ctx.send(ctx.message.author.mention + msg)
                elif (
                    answers[0] == "kadle.yes"
                    and answers[1] == "kadle.yes"
                    and answers[2] == "kadle.no"
                    and answers[3] == "kadle.no"
                    and answers[4] == "kadle.no"
                ):
                    msg = "Thanks for sharing. Compatibility rating: 4/10."
                    await ctx.send(ctx.message.author.mention + msg)
                elif (
                    answers[0] == "kadle.yes"
                    and answers[1] == "kadle.no"
                    and answers[2] == "kadle.yes"
                    and answers[3] == "kadle.yes"
                    and answers[4] == "kadle.yes"
                ):
                    msg = "Thanks for sharing. Compatibility rating: 6/10."
                    await ctx.send(ctx.message.author.mention + msg)
                elif (
                    answers[0] == "kadle.yes"
                    and answers[1] == "kadle.no"
                    and answers[2] == "kadle.yes"
                    and answers[3] == "kadle.yes"
                    and answers[4] == "kadle.no"
                ):
                    msg = "Thanks for sharing. Compatibility rating: 3/10."
                    await ctx.send(ctx.message.author.mention + msg)
                elif (
                    answers[0] == "kadle.yes"
                    and answers[1] == "kadle.no"
                    and answers[2] == "kadle.yes"
                    and answers[3] == "kadle.no"
                    and answers[4] == "kadle.yes"
                ):
                    msg = "Thanks for sharing. Compatibility rating: 7/10."
                    await ctx.send(ctx.message.author.mention + msg)
                elif (
                    answers[0] == "kadle.yes"
                    and answers[1] == "kadle.no"
                    and answers[2] == "kadle.yes"
                    and answers[3] == "kadle.no"
                    and answers[4] == "kadle.no"
                ):
                    msg = "Thanks for sharing. Compatibility rating: 6/10."
                    await ctx.send(ctx.message.author.mention + msg)
                elif (
                    answers[0] == "kadle.yes"
                    and answers[1] == "kadle.no"
                    and answers[2] == "kadle.no"
                    and answers[3] == "kadle.yes"
                    and answers[4] == "kadle.yes"
                ):
                    msg = "Thanks for sharing. Compatibility rating: 3/10."
                    await ctx.send(ctx.message.author.mention + msg)
                elif (
                    answers[0] == "kadle.yes"
                    and answers[1] == "kadle.no"
                    and answers[2] == "kadle.no"
                    and answers[3] == "kadle.yes"
                    and answers[4] == "kadle.no"
                ):
                    msg = "Thanks for sharing. Compatibility rating: 1/10."
                    await ctx.send(ctx.message.author.mention + msg)
                elif (
                    answers[0] == "kadle.yes"
                    and answers[1] == "kadle.no"
                    and answers[2] == "kadle.no"
                    and answers[3] == "kadle.no"
                    and answers[4] == "kadle.yes"
                ):
                    msg = "Thanks for sharing. Compatibility rating: 2/10."
                    await ctx.send(ctx.message.author.mention + msg)
                elif (
                    answers[0] == "kadle.yes"
                    and answers[1] == "kadle.no"
                    and answers[2] == "kadle.no"
                    and answers[3] == "kadle.no"
                    and answers[4] == "kadle.no"
                ):
                    msg = "Thanks for sharing. Compatibility rating: 1/10."
                    await ctx.send(ctx.message.author.mention + msg)
                elif (
                    answers[0] == "kadle.no"
                    and answers[1] == "kadle.yes"
                    and answers[2] == "kadle.yes"
                    and answers[3] == "kadle.yes"
                    and answers[4] == "kadle.yes"
                ):
                    msg = "Thanks for sharing. Compatibility rating: 4/10."
                    await ctx.send(ctx.message.author.mention + msg)
                elif (
                    answers[0] == "kadle.no"
                    and answers[1] == "kadle.yes"
                    and answers[2] == "kadle.yes"
                    and answers[3] == "kadle.yes"
                    and answers[4] == "kadle.no"
                ):
                    msg = "Thanks for sharing. Compatibility rating: 2/10."
                    await ctx.send(ctx.message.author.mention + msg)
                elif (
                    answers[0] == "kadle.no"
                    and answers[1] == "kadle.yes"
                    and answers[2] == "kadle.yes"
                    and answers[3] == "kadle.no"
                    and answers[4] == "kadle.yes"
                ):
                    msg = "Thanks for sharing. Compatibility rating: 7/10."
                    await ctx.send(ctx.message.author.mention + msg)
                elif (
                    answers[0] == "kadle.no"
                    and answers[1] == "kadle.yes"
                    and answers[2] == "kadle.yes"
                    and answers[3] == "kadle.no"
                    and answers[4] == "kadle.no"
                ):
                    msg = "Thanks for sharing. Compatibility rating: 6/10."
                    await ctx.send(ctx.message.author.mention + msg)
                elif (
                    answers[0] == "kadle.no"
                    and answers[1] == "kadle.yes"
                    and answers[2] == "kadle.no"
                    and answers[3] == "kadle.yes"
                    and answers[4] == "kadle.yes"
                ):
                    msg = "Thanks for sharing. Compatibility rating: 1/10."
                    await ctx.send(ctx.message.author.mention + msg)
                elif (
                    answers[0] == "kadle.no"
                    and answers[1] == "kadle.yes"
                    and answers[2] == "kadle.no"
                    and answers[3] == "kadle.yes"
                    and answers[4] == "kadle.no"
                ):
                    msg = "Thanks for sharing. Compatibility rating: 2/10."
                    await ctx.send(ctx.message.author.mention + msg)
                elif (
                    answers[0] == "kadle.no"
                    and answers[1] == "kadle.yes"
                    and answers[2] == "kadle.no"
                    and answers[3] == "kadle.no"
                    and answers[4] == "kadle.yes"
                ):
                    msg = "Thanks for sharing. Compatibility rating: 6/10."
                    await ctx.send(ctx.message.author.mention + msg)
                elif (
                    answers[0] == "kadle.no"
                    and answers[1] == "kadle.yes"
                    and answers[2] == "kadle.no"
                    and answers[3] == "kadle.no"
                    and answers[4] == "kadle.no"
                ):
                    msg = "Thanks for sharing. Compatibility rating: 6/10."
                    await ctx.send(ctx.message.author.mention + msg)
                elif (
                    answers[0] == "kadle.no"
                    and answers[1] == "kadle.no"
                    and answers[2] == "kadle.yes"
                    and answers[3] == "kadle.yes"
                    and answers[4] == "kadle.yes"
                ):
                    msg = "Thanks for sharing. Compatibility rating: 2/10."
                    await ctx.send(ctx.message.author.mention + msg)
                elif (
                    answers[0] == "kadle.no"
                    and answers[1] == "kadle.no"
                    and answers[2] == "kadle.yes"
                    and answers[3] == "kadle.yes"
                    and answers[4] == "kadle.no"
                ):
                    msg = "Thanks for sharing. Compatibility rating: 0/10."
                    await ctx.send(ctx.message.author.mention + msg)
                elif (
                    answers[0] == "kadle.no"
                    and answers[1] == "kadle.no"
                    and answers[2] == "kadle.yes"
                    and answers[3] == "kadle.no"
                    and answers[4] == "kadle.yes"
                ):
                    msg = "Thanks for sharing. Compatibility rating: 10/10."
                    await ctx.send(ctx.message.author.mention + msg)
                elif (
                    answers[0] == "kadle.no"
                    and answers[1] == "kadle.no"
                    and answers[2] == "kadle.yes"
                    and answers[3] == "kadle.no"
                    and answers[4] == "kadle.no"
                ):
                    msg = "Thanks for sharing. Compatibility rating: 0/10."
                    await ctx.send(ctx.message.author.mention + msg)
                elif (
                    answers[0] == "kadle.no"
                    and answers[1] == "kadle.no"
                    and answers[2] == "kadle.no"
                    and answers[3] == "kadle.yes"
                    and answers[4] == "kadle.yes"
                ):
                    msg = "Thanks for sharing. Compatibility rating: 1/10."
                    await ctx.send(ctx.message.author.mention + msg)
                elif (
                    answers[0] == "kadle.no"
                    and answers[1] == "kadle.no"
                    and answers[2] == "kadle.no"
                    and answers[3] == "kadle.yes"
                    and answers[4] == "kadle.no"
                ):
                    msg = "Thanks for sharing. Compatibility rating: -10/10."
                    await ctx.send(ctx.message.author.mention + msg)
                elif (
                    answers[0] == "kadle.no"
                    and answers[1] == "kadle.no"
                    and answers[2] == "kadle.no"
                    and answers[3] == "kadle.no"
                    and answers[4] == "kadle.yes"
                ):
                    msg = "Thanks for sharing. Compatibility rating: 7/10."
                    await ctx.send(ctx.message.author.mention + msg)
                elif (
                    answers[0] == "kadle.no"
                    and answers[1] == "kadle.no"
                    and answers[2] == "kadle.no"
                    and answers[3] == "kadle.no"
                    and answers[4] == "kadle.no"
                ):
                    msg = "Thanks for sharing. Compatibility rating: 1/10."
                    await ctx.send(ctx.message.author.mention + msg)

        else:
            await ctx.send(
                ctx.message.author.mention
                + " Please respond next time so we can finish the test"
            )


def setup(bot):
    """Adds the Class to the cog and logs to console"""
    bot.add_cog(Love(bot))
    print("lovebot is loaded")
