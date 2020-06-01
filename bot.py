import discord
from discord.ext import commands
import requests
from PIL import Image
import creds
from os import remove
description = '''I stole the framework from the discord.py example because I didn't want to face having to write all the base stuff out because I'd get confused by it'''
bot = commands.Bot(command_prefix='?', description=description)
bot.remove_command('help')
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(status=discord.Status.online,activity=discord.Game(name='?help | Happy Pride!'))
@bot.command()
async def rainbowme(ctx):
    avi = ctx.message.author.avatar_url_as(format='png')
    author = ctx.message.author.id
    r = requests.get(avi,allow_redirects=True)
    with open(f'cache{author}.png','wb') as cache:
        cache.write(r.content)
    base = Image.open('rainbow.png')
    image = Image.open(f'cache{author}.png')
    newimage = image.resize((500,500))
    newimage.paste(base,(0,0),base)
    newimage.save(f'final{author}.png')
    with open(f'final{author}.png','rb') as final:
        await ctx.send(file=discord.File(final,filename=f"final{author}.png"))
    remove(f'cache{author}.png')
    remove(f'final{author}.png')
@bot.command()
async def help(ctx):
    await ctx.send('Welcome to RainbowMe! To add a rainbow border to your profile picture, just type ?rainbowme. This bot stores your profile picture temporarily when you do it, as well as the final product before it gets sent off and then deleted. This bot was written by @heyimdaf on Twitter.')
bot.run(creds.token)