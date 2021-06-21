import discord
import os
import requests
from discord.ext import commands
from random import choice

my_secret = os.environ['BOT_KEY'] #here goes you r own bot token
api_key = os.environ['GMAP_API']  #here goes your own gmap api code
url = 'https://maps.googleapis.com/maps/api/streetview?size=600x400'

bot=commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    print(f'{bot.user} is online.')



@bot.command(name='hey',help='gives random rick roll Hi!')
async def rick_roll(ctx):
    rick_rolls=('Loser','Nerd','Swine','Sucker','Lazy')
    response='Hi! '+ choice(rick_rolls)
    await ctx.send(response)

@bot.command(name='find',help='Helps find places')
async def find(ctx, x: str):
    y = x.replace(' ', '+')
    r = requests.get(url + "location=" + y + "&key=" + api_key)
    await ctx.send(r.text)

@bot.command(name='baseball', help='Plays a game of base ball. Bot selects a random number \{ 1,2,3\}')
async def bb(ctx):
    await ctx.send(f'{ctx.author.mention} has started a base ball game choose one from 1,2,3')
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    strike=0
    score=0
    while strike<3:
        msg = await bot.wait_for("message", check=check)
        if msg.content in ('1','2','3'):
            if choice(('1','2','3')) == msg.content:
                strike+=1
                await ctx.send(f'{ctx.author.mention} Strike {strike}')
            else:
                score+=int(msg.content)
                await ctx.send(f'{ctx.author.mention} Score {score}')
        else:
            break
    
    await ctx.send(f'Good Game! {ctx.author.mention} Your score was {score}')

bot.run(my_secret)
