# kadlebot
A simple Discord Bot based on Kadle using Python

Requirements
===========
* Python 3.4.2+
* `discord` library: `pip install discord`
* `youtube-dl` library: `pip install youtube-dl`
* `PyNaCl` library: `pip install pynacl` (optional, for voice only)
* `libopus.so` opus library if you're using linux (included by default for windows)(optional, voice only)
* FFmpeg is required to stream audio. It can be downloaded from [here](https://www.ffmpeg.org/download.html "FFmpeg")
**Note**: To host the bot on Heroku, you need the ffmpeg buildpack. Click [here](https://elements.heroku.com/buildpacks/jonathanong/heroku-buildpack-ffmpeg-latest) and follow the instructions to add the buildpack

`mainbot.py`
===========
* Creates the bot with prefix **kadle.**
* Loads files `gaybot.py` and `musicbot.py`
* Also runs a chat filter for certain _swear words_ and _wonderla_
* The default help command has been removed and a new one was created and added to a cog **Utility** which returns the default help command itself
* `on_command_error` handles the `CommandOnCooldown` exception (can also be used to handle other errors)

`gaybot.py`
==========
**Cog:** GayStuff

Commands
--------------
- **kadle.message**
Sends a random message from given list into the same channel as requested by the user

- **kadle.image**
Sends a random image from the given list into the same channel as requested by the user

- **kadle.video**
Sends a random video from the given list into the same channel as requested by the user

- **kadle.howgay**
Replies back to the user saying how gay they are (Replies with 100% gay only for kadle)

- **kadle.say**
Repeats back the text entered by the user

- **kadle.whisper**
DM's the user with a random secret defined in the list

`musicbot.py`
==========
**Cog:** Bhajans

Commands
--------------
- **kadle.join**
Joins the voice channel the user is in

- **kadle.play**
Joins the voice channel the user is in (if not already joined) and plays a random bhajan given in the list of URLs

- **kadle.volume**
Adjusts the volume of the music being played 
(An integer between 0 to 100)

- **kadle.pause**
Pauses the music

- **kadle.resume**
Resumes the music

- **kadle.stop**
Stops playing the music and leaves the voice channel

Thanks to [**YetiGuy!**](https://www.youtube.com/channel/UCkPxP6J6LPBm6Ce-XAeojXQ "Channel: YetiGuy!") for his [video](https://www.youtube.com/watch?v=FpRzDY0-I1o "YetiGuy!: Create a working music bot! Discord.py & python") on how to make the music player bot.

_The files_ `requirements.txt`_,_ `Procfile` _and_ `libopus.so` _are required to deploy it on Heroku_
