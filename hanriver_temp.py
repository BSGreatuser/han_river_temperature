import discord
import requests

client = discord.Client()

@client.event
async def on_ready():
    print("봇이 성공적으로 실행되었습니다.")
    game = discord.Game('★~하는중에 표시될 네임 작성★')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith('봉순아 한강온도'):
        json = requests.get('http://hangang.dkserver.wo.tc/').json()
        temp = json.get("temp") # 한강온도
        time = json.get("time") # 측정시간

        embed = discord.Embed(title='💧 한강온도', description=f'{temp}°C', colour=discord.Colour.blue())
        embed.set_footer(text=f'{time}에 측정됨')

        await message.channel.send(embed=embed)

client.run('★TOKEN★')
