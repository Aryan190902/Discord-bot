import discord
import os
import requests

client = discord.Client()

my_secret = os.environ['TOKEN']
api_key = os.environ['API']
url = 'https://maps.googleapis.com/maps/api/streetview?size=600x400'


@client.event
async def on_ready():
    print('{0.user} is online'.format(client))


@client.event
async def on_message(mssg):
    if mssg.author == client.user:
        return

    if mssg.content.startswith('>hey'):
        await mssg.channel.send('Hey! looser')

    x = mssg.content.replace('>find ', '')
    y = x.replace(' ', '+')
    def findIt():
        r = requests.get(url + "location=" + y + "&key=" + api_key)
        print(r.text)
         

    if mssg.content.startswith(('>find {0}').format(x)):
        return findIt()


client.run(my_secret)
