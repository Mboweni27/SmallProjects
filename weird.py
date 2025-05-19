import discord
from discord.ext import commands
from discord import Embed
import asyncio
import requests
from bs4 import BeautifulSoup

intents = discord.Intents.all()
token = ""# this is where you discord token would go
client = commands.Bot(command_prefix="!", intents=intents)
@client.event
async def on_ready():
    print("Your BOT has Started")
    ClientID = client.get_channel(1116685984931782701)
    await ClientID.send("Your moms a hoe")
@client.command()
async def anything(ctx,message):
    usmessage=ctx.message.content
    await ctx.send(usmessage[9:]) 

@client.command()
async def News(ctx):

    headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    CNBC = requests.get("https://www.cnbc.com/world/?region=world",headers=headers)
    Soup = BeautifulSoup(CNBC.content,"html.parser")
    Heading = Soup.find_all("a")
    for x in Heading:
        head = x["href"]
        if ("/www.cnbc.com/" in head) and ("/2023/06/09/" in head):
            
            if len(x.text) > 3: 
                Stuff = x.text + head 

                await ctx.send(Stuff)
                break
client.run(token)






