import discord
from discord.ext import commands
import json
from discord.utils import get

with open ("settings.json",mode="r",encoding="utf8") as jfile:
    jdata= json.load(jfile)

from C_M_event import CM1,CM2,CM3,CMex

bot = commands.Bot(command_prefix="/")

@bot.event
async def on_ready():
    print(">>>LogIn as :",bot)

@bot.command()
async def 烙人(ctx):
            await ctx.channel.send("輸入身份組：以'@'開頭")
            @bot.event
            async def on_message(ctx):
                if ctx.content.startswith("@")==True:
                    msg=ctx.content[1:]
                    print(msg)
                    i=0
                    role=0
                    while msg!=role:
                        i=i+1
                        role = get(guild.roles, id = i)
                        role2= get(guild.roles,name=msg)
                        if role==role2:
                            await ctx.channel.send("@"+msg)
                            break
@bot.command()
async def 烙全人(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.channel.send("@everyone")
@bot.command()
async def 戳狗偵測(ctx):
     await ctx.channel.send("輸入名稱與成績")
     await ctx.channel.send('''(名稱與成績之間使用半形冒號分開)(人與人之間以空格分開)''')
     @bot.event
     async def on_message(ctx):
         if ctx.author!=bot:
             a,b,c=map(str,ctx.content.split(" "))
             msg=[]
             a=a.split(":")
             b=b.split(":")
             c=c.split(":")
             print(a,b,c)
             i=0
             l=[]
             l2=[]
             g1=int(a[1])
             g2=int(b[1])
             g3=int(c[1])
             await ctx.channel.purge(limit=4)
             if g3<g2:
                 if g3<g1:
                     await ctx.channel.send("%s戳狗，嘖嘖"%(c[0]))
                 else :
                      await ctx.channel.send("%s戳狗，嘖嘖"%(a[0]))
             elif g1<g2:
                  if g1<g3:
                      await ctx.channel.send("%s戳狗，嘖嘖"%(a[0]))
                  else :
                      await ctx.channel.send("%s戳狗，嘖嘖"%(c[0]))
             elif g2<g3 :
                   if g2<g1:
                       await ctx.channel.send("%s戳狗，嘖嘖"%(b[0]))

bot.run(jdata["TOKEN"])