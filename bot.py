import discord
import responses
import spotipytest
import os
from dotenv import load_dotenv

load_dotenv()
TKN = os.getenv("TOKEN")

# Send messages
async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    #Prompts a bad request error when said something that's unrecognizable by the bot. Hence printing a blank string instead of the exeption
    except Exception as e:
        print("")


def run_discord_bot():
    TOKEN = TKN
    client = discord.Client(intents=discord.Intents.all())

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        # Make sure bot doesn't get stuck in an infinite loop
        if message.author == client.user:
            return

        # Get data about the user
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # Debug printing
        print(f"{username} said: '{user_message}' ({channel})")
       
        await send_message(message, user_message, is_private=False)

        if user_message.startswith("https://open.spotify.com/track/"):
            spotipytest.addSong(user_message)

    # Remember to run your bot with your personal TOKEN
    client.run(TOKEN)
