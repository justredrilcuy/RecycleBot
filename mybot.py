import discord
from discord.ext import commands
from botlogic import pass_gen
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def passgen(ctx):
    await ctx.send('halo berikut pw anda:')
    await ctx.send(pass_gen(8))

@bot.command()
async def pangkat(ctx):
    await ctx.send('Masukkan angka bebas, nanti aku hitung pangkat 2 nya')
    message = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
    await ctx.send(f'Pangkat dua dari angka yang kamu kirimkan adalah {(int(message.content)**2)}')

@bot.command()
async def meme(ctx):
    import random, os
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

daur_ulang = ["botol plastik", "botol kaca", "kaleng aluminium", "pelapis alumunium", 
              "baterai", "limbah elektronik", "kertas", "majalah", "koran"]

@bot.command()
async def cek_sampah(ctx):
    await ctx.send('Sampah apa yang mau Anda periksa?')
    message = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
    message = str(message.content)
    #proses pemeriksaan
    if message.lower() in daur_ulang:
        await ctx.send('Sampah tersebut harus di daur ulang, berikut adalah tips untuk Anda!')
        await ctx.send('https://www.youtube.com/watch?v=ts0DYCU5cM8')
    else:
        await ctx.send('Sampah tersebut bisa dibuang/dimusnahkan dengan bijak!')
        await ctx.send('https://www.youtube.com/watch?v=CGd3lgxReFE')
