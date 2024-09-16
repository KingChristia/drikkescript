from time import sleep
import numpy as np
import pyttsx3
from datetime import datetime, timedelta

#names = ['John-John', 'Bent dick', 'Hoe con', 'Cry stuffer', 'Thor-Yay', 'Air in', 'Will I am', 'See Gert', 'Everyone']
names = ['John-John', 'Bent dick', 'Cry stuffer', 'Air in', 'Christ Ian', 'Will I am', 'Semen', 'Everyone']
extra_names = ['Everyone', 'Christ Ian']
multiplier = np.array([3 if name in extra_names else 1 for name in names])
indices = [*range(len(names))]
min_time = 10
max_time = 60
w = np.array([1 for name in names])
engine = pyttsx3.init()
weight_reduce = 5

for voice in engine.getProperty('voices'):
    # if voice.name == 'Microsoft Jon - Norwegian (Bokmål)':
    #     engine.setProperty('voice', voice.id)
    #     break
    if voice.name == 'Microsoft Zira Desktop - English (United States)':
        engine.setProperty('voice', voice.id)
        break
    # if voice.name == 'Microsoft Hazel Desktop - English (Great Britain)':
    #     engine.setProperty('voice', voice.id)
    #     break


def say(text):
    engine.say(text)
    engine.runAndWait()


def choose():
    global w
    i = np.random.choice(indices, 1, p=w / w.sum())[0]
    w += multiplier
    w[i] = max(w[i] - weight_reduce, 1)
    return names[i]


if __name__ == '__main__':
    length = max((len(name) for name in names))
    while True:
        say('New loser in five, four, three, two, one')
        name = choose()
        say(f'{name} has to drink')
        print(f'{name} has to drink')
        wait = np.random.randint(min_time, max_time)
        print(f'New name in {wait} seconds, at {(datetime.now() + timedelta(seconds=wait)).time():%H:%M:%S}')
        total = w.sum()
        weight_reduce = max(round(total/10), 5)
        for name, weight in zip(names, w):
            print(f'{name:{length}}: {weight / total:.2%}')
        print("-------------------")
        print("\n")
        sleep(wait)
