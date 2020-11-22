
###################
####python 3.x#####
#discord.py==1.4.0#
###################

import discord

client = discord.Client()

@client.event
async def on_ready():
    print("봇이 성공적으로 실행되었습니다.")
    game = discord.Game('★~하는중에 표시될 네임 작성★')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith('봉순아 한강온도'): #requ,bs4
        url = "https://hangang.life"
        res = requests.get(url)

        soup = BeautifulSoup(res.text, "lxml")

        temp = soup.find("h1", attrs={"class":"white"}) #한강온도
        date = soup.find("font", attrs={"style":"font-weight: 700; font-size: 10pt;"}) #측정날짜

        hanembed = discord.Embed(title="💧 한강온도", description=f"{temp.get_text()}", colour=discord.Colour.blue())
        hanembed.set_footer(text=date.get_text())
        await message.channel.send(embed=hanembed)


client.run('★TOKEN★')
