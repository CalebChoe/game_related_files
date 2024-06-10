import time
import random
import pygame

pygame.init()

pygame.mixer.music.load('bgmusicchill.mp3')
pygame.mixer.music.play()

user = ""
coins = 0
cpc = 1
apples = 0
apc = 0

def save():
    with open(f"rgames{user}.txt", "w") as output:
        output.write(str(f"{coins}\n{cpc}\n{apples}\n{apc}"))

print("Welcome to random games!")

check = input("Have you played before and want to load up your game? Type Y if you would like to. ")

if check.upper() == "Y":
    user = input("Please enter your saved game's username: ")
    count = 0
    file = open(f"rgames{user}.txt", "r")
    lines = file.readlines()
    for line in lines:
        if count == 0:
            plug = line.strip()
            coins = int(plug)
        elif count == 1:
            plug = line.strip()
            cpc = int(plug)
        elif count == 2:
            plug = line.strip()
            apples = int(plug)
        elif count == 3:
            plug = line.strip()
            apc = int(plug)
        count += 1
else:
    user = input("You are new to the game! What will be your username? ")

print(f"Coins: {coins} Coins per click: {cpc} Apples: {apples} Apples per click: {apc}")

save()

print("Type info to see commands.")

while True:
    typed = input()
    if typed == "":
        coins += cpc
        apples += apc
        print(f"Coins: {coins} Apples: {apples}")

    elif typed.lower() == "stat":
        print(f"Coins: {coins} Coins per click: {cpc} Apples: {apples} Apples per click:{apc}")

    elif typed.lower() == "info":
        print("Click (or hold but thats no fun :[ ) enter while in the input system to gain a coin.")
        print("Type stat and click enter in the input system to see your stat info.")
        print("Type upg to see and buy upgrades.")
        print("Type info to see commands.")

    elif typed.lower() == "upg":
        print(f"Coins: {coins} Apples: {apples}")
        print("+1 coins per click: 50 coins. Type A to buy: ")
        print("+5 coins per click: 225 coins. Type B to buy. ")
        print("+1 apples per click: 1000 coins. Type C to buy.")
        print("+10 apples per click: 5000 coins and 100 apples. Type D to buy.")
        print("+25 coins per click: 100 apples. Type E to buy.")
        typed = input("Type the character(s) for the upgrade you would like to buy. ")
        char = typed.upper()
        if char == "A":
            if coins >= 50:
                coins -= 50
                cpc += 1
                print(f"Coins: {coins} Coins per click: {cpc}")
            else:
                print("Cannot Afford!")
        if char == "B":
            if coins >= 225:
                coins -= 225
                cpc += 5
                print(f"Coins: {coins} Coins per click: {cpc}")
            else:
                print("Cannot Afford!")
        if char == "C":
            if coins >= 1000:
                coins -= 1000
                apc += 1
                print(f"Coins: {coins} Apples per click: {apc}")
            else:
                print("Cannot Afford!")
        if char == "D":
            if coins >= 5000 and apples >= 100:
                coins -= 5000
                apples -= 100
                apc += 10
                print(f"Coins: {coins} Apples: {apples} Apples per click: {cpc}")
            else:
                print("Cannot Afford!")
        if char == "E":
            if apples >= 100:
                apples -= 100
                cpc += 25
                print(f"Coins per click: {cpc} Apples: {apples}")
            else:
                print(f"Cannot Afford!")

    save()
