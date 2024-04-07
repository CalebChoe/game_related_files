import turtle
import random
# import keyboard

#hello world
w = 0
l = 0
t = 0
g = 0
teswt = 192
experience = 0
level = 1

class player:
    def __init__(self, wins, losses, ties, games, lvl, exp):
        self.w = wins
        self.l = losses
        self.t = ties
        self.g = games
        self.lvl = lvl
        self.exp = exp


name2 = input("Name? Type only your first. ")
if name2 == "joshua":
    print("I SEE YOU JOSH. he he he he he")
if name2 == "caleb":
    print("coolest man")
file_true = input("Have you played before? Type Y or N: ")
if file_true == "Y":
    delete = input("If you've played before and want to restart, type Y, else type N. ")
    if delete != "Y":
        file1 = open(f"score_{name2}.txt", "r")
        lines = file1.readlines()
        print(lines)
        count = 0
        for line in lines:
            if count == 0:
                w = line.strip()
                count += 1
            elif count == 1:
                l = line.strip()
                count += 1
            elif count == 2:
                t = line.strip()
                count += 1
            elif count == 3:
                g = line.strip()
                count += 1
            elif count == 4:
                experience = line.strip()
                count += 1
            elif count == 5:
                level = line.strip()
                count += 1
        print(f"{w}{l}{t}{g}{experience}{level}")

        # w = str(w[0])
        # l = str(w[1])
        # t = str(w[2])
        # g = str(w[3])
    else:
        file1 = open(f"score_{name2}.txt", "w")
        file1.write("0\n0\n0\n0\n0\n0")

player1 = player(w, l, t, g, level, experience)

name3 = input("Name? Type only your first. ")
if name3 == "joshua":
    print("I SEE YOU JOSH. he he he he he")
if name3 == "caleb":
    print("coolest man")
file_true = input("Have you played before? Type Y or N: ")
if file_true == "Y":
    delete = input("If you've played before and want to restart, type Y, else type N. ")
    if delete != "Y":
        file1 = open(f"score_{name3}.txt", "r")
        lines = file1.readlines()
        print(lines)
        count = 0
        for line in lines:
            if count == 0:
                w = line.strip()
                count += 1
            elif count == 1:
                l = line.strip()
                count += 1
            elif count == 2:
                t = line.strip()
                count += 1
            elif count == 3:
                g = line.strip()
                count += 1
            elif count == 4:
                experience = line.strip()
                count += 1
            elif count == 5:
                level = line.strip()
                count += 1
        print(f"{w}{l}{t}{g}{experience}{level}")

        # w = str(w[0])
        # l = str(w[1])
        # t = str(w[2])
        # g = str(w[3])
    else:
        file1 = open(f"score_{name3}.txt", "w")
        file1.write("0\n0\n0\n0\n0\n0")

player2 = player(w, l, t, g, level, experience)

print("Loading simulation...")

wn = turtle.Screen()
wn.title("NFL SIMULATOR BY CALEB CHOE")

wn.register_shape(r"C:\Users\pooki\Desktop\Nfl\Giants.gif")
wn.register_shape(r"C:\Users\pooki\Desktop\Nfl\cardinals.gif")
wn.register_shape(r"C:\Users\pooki\Desktop\Nfl\steelers.gif")
wn.register_shape(r"C:\Users\pooki\Desktop\Nfl\cowboy.gif")
wn.register_shape(r"C:\Users\pooki\Desktop\Nfl\bengals.gif")
wn.register_shape(r"C:\Users\pooki\Desktop\Nfl\browns.gif")
wn.register_shape(r"C:\Users\pooki\Desktop\Nfl\chiefs.gif")
wn.register_shape(r"C:\Users\pooki\Desktop\Nfl\ravens.gif")

skin = random.randint(1, 8)
name = 0

team = turtle.Turtle()
team.speed(0)

pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.color("black")

if skin == 1:
    team.shape(r"C:\Users\pooki\Desktop\Nfl\Giants.gif")
    name = "New York Giants"
    wn.bgcolor("blue")
elif skin == 2:
    team.shape(r"C:\Users\pooki\Desktop\Nfl\cardinals.gif")
    name = "Arizona Cardinals"
    wn.bgcolor("red")
elif skin == 3:
    team.shape(r"C:\Users\pooki\Desktop\Nfl\steelers.gif")
    name = "Pittsburgh Steelers"
    wn.bgcolor("yellow")
elif skin == 4:
    team.shape(r"C:\Users\pooki\Desktop\Nfl\cowboy.gif")
    name = "Dallas Cowboys"
    wn.bgcolor("dark blue")
    pen.color("white")
elif skin == 5:
    team.shape(r"C:\Users\pooki\Desktop\Nfl\bengals.gif")
    name = "Cincinnati Bengals"
    wn.bgcolor("orange")
elif skin == 6:
    team.shape(r"C:\Users\pooki\Desktop\Nfl\browns.gif")
    name = "Cleveland Browns"
    wn.bgcolor("orange")
elif skin == 7:
    team.shape(r"C:\Users\pooki\Desktop\Nfl\chiefs.gif")
    name = "Kansas City Chiefs"
    wn.bgcolor("red")
elif skin == 8:
    team.shape(r"C:\Users\pooki\Desktop\Nfl\ravens.gif")
    name = "Baltimore Ravens"
    wn.bgcolor("purple")
    pen.color("white")

play = turtle.Turtle()
play.penup()
play.shape("square")
play.color("green")
play.goto(-250, 0)

play.shapesize(4, 5)
play.speed(0)
play.hideturtle()

r = turtle.Turtle()
r.penup()
r.shape("square")

r.goto(270, 0)
r.hideturtle()
r.shapesize(4, 5)
r.speed(0)
r.pencolor("black")
r.write(f"Record: {player1.w}-{player1.l}-{player1.t}", align="center", font=("Courier", 17, "normal"))
r.goto(270, -60)
r.write(f"Record: {player2.w}-{player2.l}-{player2.t}", align="center", font=("Courier", 17, "normal"))

back = turtle.Turtle()
back.penup()
back.shape("square")
back.color("green")
back.goto(0, -200)

back.shapesize(4, 5)
back.speed(0)
back.hideturtle()

play.shapesize(4, 5)
play.showturtle()
pen.write("Enter a match by clicking the green button, \n it will automate your game.", align="center",
          font=("Courier", 12, "normal"))
pen.goto(-250, -100)
pen.write(f"Experience: {experience}/10 Level: {level}", align="center",
          font=("Courier", 8, "normal"))


def automate(x, y):
    print(x, y)
    pen.goto(0, 0)
    pen.write("FOLLOW THE\n CONSOLE\n INSTRUCTIONS.", align="center", font=("Courier", 30, "normal"))
    r.clear()
    team.hideturtle()
    play.hideturtle()
    pen.goto(-200, 100)
    q1 = random.randrange(0, 4)
    qs1 = 0
    q2 = random.randrange(0, 4)
    qs2 = 0
    q3 = random.randrange(0, 4)
    qs3 = 0
    q4 = random.randrange(0, 4)
    qs4 = 0
    dq1 = random.randrange(0, 4)
    dqs1 = 0
    dq2 = random.randrange(0, 4)
    dqs2 = 0
    dq3 = random.randrange(0, 4)
    dqs3 = 0
    dq4 = random.randrange(0, 4)
    dqs4 = 0
    if player1.lvl <= 2 and q4 > 0:
        q4 -= 1
    if player1.lvl <= 4 and q3 > 0:
        q3 -= 1
    if player1.lvl <= 5 and q2 > 0:
        q2 -= 1
        if dq2 < 4:
            dq2 += 1
    if player1.lvl <= 7 and q1 > 0:
        q1 -= 1
        if dq1 < 4:
            dq1 += 1
    if player1.lvl >= 10 and q4 < 4:
        q4 += 1
    if player1.lvl >= 14 and q3 < 4:
        q3 += 1
    if player1.lvl >= 17 and q2 < 4:
        q2 += 1
    if player1.lvl >= 20 and q1 < 4:
        q1 += 1
    if q1 != 4:
        track = random.randint(1, 5)
        chance = input("Choose a number between 1 and 5.")
        if track == chance:
            print("You got it right!")
            q1 += 1
        else:
            print("WRONG.")
    if q2 != 4:
        track = random.randint(1, 5)
        chance = input("Choose a number between 1 and 5.")
        if track == chance:
            print("You got it right!")
            q2 += 1
        else:
            print("WRONG.")
    if q3 != 4:
        track = random.randint(1, 5)
        chance = input("Choose a number between 1 and 5.")
        if track == chance:
            print("You got it right!")
            q3 += 1
        else:
            print("WRONG.")
    if q4 != 4:
        track = random.randint(1, 5)
        chance = input("Choose a number between 1 and 5.")
        if track == chance:
            print("You got it right!")
            q4 += 1
        else:
            print("WRONG.")
    """
    else:
        space = 0
        timer = 10
        print("spam enter key")
        while timer > 0:
            if keyboard.read_key() == "enter":
                space += 1
            time.sleep(1)
            timer -= 1
        if space > 20 and q1 < 4:
            q1 += 1
    """
    if q1 == 1:
        qs1 = 0
    if q2 == 1:
        qs2 = 0
    if q3 == 1:
        qs3 = 0
    if q4 == 1:
        qs4 = 0
    if q1 == 2:
        qs1 = 3
    if q2 == 2:
        qs2 = 3
    if q3 == 2:
        qs3 = 3
    if q4 == 2:
        qs4 = 3
    if q1 == 3:
        qs1 = 7
    if q2 == 3:
        qs2 = 7
    if q3 == 3:
        qs3 = 7
    if q4 == 3:
        qs4 = 7
    if q1 == 4:
        qs1 = 8
    if q2 == 4:
        qs2 = 8
    if q3 == 4:
        qs3 = 8
    if q4 == 4:
        qs4 = 8
    if q1 == 0:
        dqs1 += 3
    if q2 == 0:
        dqs2 += 3
    if q3 == 0:
        dqs3 += 3
    if q4 == 0:
        dqs4 += 3

    if player2.lvl <= 2 and q4 > 0:
        dq4 -= 1
    if player2.lvl <= 4 and q3 > 0:
        dq3 -= 1
    if player2.lvl <= 5 and q2 > 0:
        dq2 -= 1
        if dq2 < 4:
            dq2 += 1
    if player2.lvl <= 7 and q1 > 0:
        dq1 -= 1
        if dq1 < 4:
            dq1 += 1
    if player2.lvl >= 10 and dq4 < 4:
        dq4 += 1
    if player2.lvl >= 14 and dq3 < 4:
        dq3 += 1
    if player2.lvl >= 17 and dq2 < 4:
        dq2 += 1
    if player2.lvl >= 20 and dq1 < 4:
        dq1 += 1

    if dq1 != 4:
        track = random.randint(1, 5)
        chance = input("Choose a number between 1 and 5.")
        if track == chance:
            print("You got it right!")
            dq1 += 1
        else:
            print("WRONG.")
    if dq2 != 4:
        track = random.randint(1, 5)
        chance = input("Choose a number between 1 and 5.")
        if track == chance:
            print("You got it right!")
            dq2 += 1
        else:
            print("WRONG.")
    if dq3 != 4:
        track = random.randint(1, 5)
        chance = input("Choose a number between 1 and 5.")
        if track == chance:
            print("You got it right!")
            dq3 += 1
        else:
            print("WRONG.")
    if dq4 != 4:
        track = random.randint(1, 5)
        chance = input("Choose a number between 1 and 5.")
        if track == chance:
            print("You got it right!")
            dq4 += 1
        else:
            print("WRONG.")
    if dq1 == 1:
        dqs1 = 3
    if dq2 == 1:
        dqs2 = 0
    if dq3 == 1:
        dqs3 = 0
    if dq4 == 1:
        dqs4 = 0
    if dq1 == 2:
        dqs1 = 3
    if dq2 == 2:
        dqs2 = 3
    if dq3 == 2:
        dqs3 = 3
    if dq4 == 2:
        dqs4 = 3
    if dq1 == 3:
        dqs1 = 7
    if dq2 == 3:
        qs2 = 7
    if dq3 == 3:
        dqs3 = 7
    if dq4 == 3:
        dqs4 = 7
    if dq1 == 4:
        dqs1 = 8
    if dq2 == 4:
        dqs2 = 8
    if dq3 == 4:
        dqs3 = 8
    if q4 == 4:
        dqs4 = 8
    if dq1 == 0:
        qs1 += 3
    if dq2 == 0:
        qs2 += 3
    if dq3 == 0:
        qs3 += 3
    if dq4 == 0:
        qs4 += 3
    score = qs1 + qs2 + qs3 + qs4
    e_score = dqs1 + dqs2 + dqs3 + dqs4
    """
    if wild:
        if div:
            if conf:
                if super:
                    if level <= 25 and q4 > 0:
                        q4 -= 1
                    if level <= 30 and q3 > 0:
                        q3 -= 1
                    if level <= 33 and q2 > 0:
                        q2 -= 1
                    if level <= 36 and q1 > 0:
                        q1 -= 1
                    if level >= 40 and q4 < 4:
                        q4 += 1
                    if level >= 43 and q3 < 4:
                        q3 += 1
                    if level >= 46 and q2 < 4:
                        q2 += 1
                    if level >= 50 and q1 < 4:
                        q1 += 1
                else:
                    if level <= 20 and q4 > 0:
                        q4 -= 1
                    if level <= 24 and q3 > 0:
                        q3 -= 1
                    if level <= 27 and q2 > 0:
                        q2 -= 1
                    if level <= 30 and q1 > 0:
                        q1 -= 1
                    if level >= 33 and q4 < 4:
                        q4 += 1
                    if level >= 35 and q3 < 4:
                        q3 += 1
                    if level >= 38 and q2 < 4:
                        q2 += 1
                    if level >= 40 and q1 < 4:
                        q1 += 1
            else:
                if level <= 15 and q4 > 0:
                    q4 -= 1
                if level <= 18 and q3 > 0:
                    q3 -= 1
                if level <= 20 and q2 > 0:
                    q2 -= 1
                if level <= 23 and q1 > 0:
                    q1 -= 1
                if level >= 27 and q4 < 4:
                    q4 += 1
                if level >= 30 and q3 < 4:
                    q3 += 1
                if level >= 34 and q2 < 4:
                    q2 += 1
                if level >= 38 and q1 < 4:
                    q1 += 1
        else:
            if level <= 10 and q4 > 0:
                q4 -= 1
            if level <= 13 and q3 > 0:
                q3 -= 1
            if level <= 15 and q2 > 0:
                q2 -= 1
            if level <= 18 and q1 > 0:
                q1 -= 1
            if level >= 20 and q4 < 4:
                q4 += 1
            if level >= 23 and q3 < 4:
                q3 += 1
            if level >= 26 and q2 < 4:
                q2 += 1
            if level >= 30 and q1 < 4:
                q1 += 1
    """
    pen.clear()
    pen.goto(0, 100)
    pen.write(f"You scored {qs1} points in quarter 1. Second player scored {dqs1}.", align="center", font=("Courier", 15, "normal"))
    pen.goto(0, 50)
    pen.write(f"You scored {qs2} points in quarter 2. Second player scored {dqs1}.", align="center", font=("Courier", 15, "normal"))
    pen.goto(0, 0)
    pen.write(f"You scored {qs3} points in quarter 3. Second player scored {dqs1}.", align="center", font=("Courier", 15, "normal"))
    pen.goto(0, -50)
    pen.write(f"You scored {qs4} points in quarter 4. Second player scored {dqs1}.", align="center", font=("Courier", 15, "normal"))
    pen.goto(0, -100)
    pen.write(f"You got {score} total points, and 2nd player got {e_score}.", align="center",
              font=("Courier", 10, "normal"))
    pen.goto(0, -150)

    experience1 = player1.exp
    experience2 = player2.exp
    if score == e_score:
        pen.write(f"It ended in a tie.", align="center", font=("Courier", 15, "normal"))
        experience1 += 1.5
        experience2 += 1.5
        player1.t += 1
        player2.t += 1
    elif score > e_score:
        pen.write(f"It ended in a win, by player one! Nice!", align="center", font=("Courier", 15, "normal"))
        experience1 += 3
        experience2 += 1.5
        player1.w += 1
        player2.l += 1
    else:
        pen.write(f"It ended in a win, by player two! Nice!", align="center", font=("Courier", 15, "normal"))
        experience1 += 1.5
        experience2 += 3
        player1.l += 1
        player2.w += 1
    if experience1 >= 10:
        player1.lvl += 1
        experience1 -= 10
    if experience2 >= 10:
        player2.lvl += 1
        experience2 -= 10
    player1.g += 1
    player2.g += 1
    pen.goto(0, -270)
    pen.write("Click the green button to go back.", align="center", font=("Courier", 10, "normal"))
    back.showturtle()

    # print("Beginning")
    # print("d is ", d)
    # print("w is ", w)
    # print("l is ", l)
    # print("t is ", t)
    # print("After one game round")
    # print("w is ", w)
    # print("l is ", l)
    # print("t is ", t)


def setup(x, y):
    back.hideturtle()
    pen.clear()
    print(x, y)
    play.showturtle()
    team.showturtle()
    pen.goto(0, 260)
    pen.write("Enter a match by clicking the green button, it will automate your game.", align="center",
              font=("Courier", 12, "normal"))
    if player1.g > 16:
        player1.w = 0
        player1.l = 0
        player1.t = 0
        # if w >= 10:
        #     wild = True
        # else:
        #     w = 0
        #     l = 0
        #     t = 0
        #     g = 0
    if player2.g > 16:
        player2.w = 0
        player2.l = 0
        player2.t = 0
        # if w >= 10:
        #     wild = True
        # else:
        #     w = 0
        #     l = 0
        #     t = 0
        #     g = 0
    with open(f"score_{name2}.txt", "w") as output:
        output.write(str(f"{player1.w}\n{player1.l}\n{player1.t}\n{player1.g}\n{player1.exp}\n{player1.lvl}"))
    with open(f"score_{name3}.txt", "w") as output:
        output.write(str(f"{player2.w}\n{player2.l}\n{player2.t}\n{player2.g}\n{player2.exp}\n{player2.lvl}"))
    pen.goto(0, 100)
    r.write(f"Record: \n {player1.w}-{player1.l}-{player1.t}", align="center", font=("Courier", 17, "normal"))
    pen.goto(0, 200)
    r.write(f"Record: \n {player2.w}-{player2.l}-{player2.t}", align="center", font=("Courier", 17, "normal"))
    pen.goto(-250, -100)
    pen.write(f"Experience: {player1.exp}/10 Level: {player1.lvl}", align="center",
              font=("Courier", 10, "normal"))
    pen.goto(-250, -160)
    pen.write(f"Experience: {player2.exp}/10 Level: {player2.lvl}", align="center",
              font=("Courier", 10, "normal"))
    pen.goto(0, -200)
    pen.write("Remember, the higher level, the better you play!", align="center",
              font=("Courier", 11, "normal"))
    pen.goto(0, -250)


play.onclick(automate)
back.onclick(setup)

wn.mainloop()
