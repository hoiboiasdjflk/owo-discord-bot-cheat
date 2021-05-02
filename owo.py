import time
import random
import random, string
import discord
import asyncio
token="   "

client=discord.Client()
tire="-"*14
@client.event
async def on_connect():
  global chan
  print(f"{tire}\n Logged in as \n {str(client.user)}\n{tire}")
  channel=channelid
  chan=client.get_channel(channel)
async def function2():
  global chan
  await client.wait_until_ready()
  x=True
  with chan.typing():
    while x:
      await asyncio.sleep(3600)
async def function1():
  global chan
  await client.wait_until_ready()
  runCondition = True;
  text1 = "owo hunt"
  text2 = "owo battle"
  n = 0
  timesToRun = 0
  while runCondition == True:
    await chan.send(text1)
    shortVariant = random.random()
    time.sleep(.3)
    time.sleep(shortVariant)
    await chan.send(text2)
    await asyncio.sleep(12)
    timeVariant = random.randint(1, 5)
    time.sleep(timeVariant)
    randomJunk = "".join(random.choices(string.ascii_letters + string.digits, k=random.randint(5, 13)))
    await chan.send(randomJunk)
    time.sleep(random.randint(2, 3))
    owoUwu = ["owo", "uwu", "owo owo owo"]
    await chan.send(random.choice(owoUwu))
    time.sleep(random.random() + random.random())
    time.sleep(random.random())
    varChance = random.randint(1, 20)
    timesToRun += 1
    if varChance == 1:
        await asyncio.sleep(15)
        while n <= random.randint(5, 17):
            longRandomJunk = "".join(random.choices(string.ascii_letters + string.digits, k=random.randint(3, 17)))                                      
            await chan.send(longRandomJunk+ " "*n)
            n += 1
        await asyncio.sleep(random.randint(10, 12))
        
                                                
client.loop.create_task(function1())
client.loop.create_task(function2())
client.run(token, bot=False)
