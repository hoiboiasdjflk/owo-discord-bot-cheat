from pynput.keyboard import Key,Controller
import time
import random
import random, string

runCondition  = (input("how many times should it loop? (just press enter for forever) "))
if runCondition == "":
    runCondition = True;
else:
    runCondition = int(runCondition)               
time.sleep(3)
text1 = "owo hunt"
text2 = "owo battle"
n = 0
timesToRun = 0
Keyboard = Controller()
time.sleep(1)
while runCondition == True or timesToRun < runCondition:
    Keyboard.type(text1)
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)
    shortVariant = random.random()
    time.sleep(.3)
    time.sleep(shortVariant)
    Keyboard.type(text2)
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)
    time.sleep(12)
    timeVariant = random.randint(1, 5)
    time.sleep(timeVariant)
    randomJunk = "".join(random.choices(string.ascii_letters + string.digits, k=random.randint(5, 13)))
    Keyboard.type(randomJunk)
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)
    time.sleep(random.randint(2, 3))
    owoUwu = ["owo", "uwu"]
    Keyboard.type(random.choice(owoUwu))
    time.sleep(random.random() + random.random())
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)
    time.sleep(random.random())
    varChance = random.randint(1, 20)
    timesToRun += 1
    if varChance == 1:
        time.sleep(15)
        while n <= random.randint(5, 17):
            longRandomJunk = "".join(random.choices(string.ascii_letters + string.digits, k=random.randint(3, 17)))                                      
            Keyboard.type(longRandomJunk)
            Keyboard.press(Key.space)
            n += 1
        Keyboard.press(Key.enter)
        Keyboard.release(Key.enter)
        time.sleep(random.randint(10, 12))
        
                                                
