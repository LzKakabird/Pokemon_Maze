# 2019.12 - 2020.1 CS final project
#Pokemon Maze
#1. let the user input their name
#2. print the instructions
#3. open a picture window which is frame 1
#4. frame1: the conversation with the professor
#5. open another frame
#6. draw a maze and points
#7. control the character by using key press
#8. if the character step on the points, the info will be collected
#9. frames with pokemon will change all the time to simulate the move of pokemon
#10. if the character goes out of the maze without 4 pieces information of 
#    pokemon, the researcher will say you lose the game 
#11 if you collect 4 pieces of information, you win



#setup
print("you have 2 endings in this program")
print("")
import turtle
import time
turtle.title("pokemon maze")
turtle.setup(1000,1000,0,0)
turtle_w = turtle.Turtle()
turtle_w.speed(0)
turtle.speed(0)
turtle.ht()
turtle_m = turtle.Turtle()
red = turtle.Turtle()
go = True
steps = 25
t_wf = turtle.Turtle()
t_ww = turtle.Turtle()
t_wg = turtle.Turtle()
t_wp = turtle.Turtle()
t_wf.speed(0)
t_ww.speed(0)
t_wg.speed(0)
t_wp.speed(0)
t_wf_dis = turtle.Turtle()
t_ww_dis = turtle.Turtle()
t_wg_dis = turtle.Turtle()
t_wp_dis = turtle.Turtle()

global findf
global findw
global findg
global findp
findf = 0
findw = 0
findg = 0
findp = 0



#import images
turtle.register_shape("back.gif")
turtle.register_shape("back go left.gif")
turtle.register_shape("back go right.gif")
turtle.register_shape("front.gif")
turtle.register_shape("front go left.gif")
turtle.register_shape("front go right.gif")
turtle.register_shape("right.gif")
turtle.register_shape("right go left.gif")
turtle.register_shape("right go right.gif")
turtle.register_shape("left.gif")
turtle.register_shape("left go right.gif")
turtle.register_shape("left go left.gif")
turtle.register_shape("findf.gif")
turtle.register_shape("findg.gif")
turtle.register_shape("findw.gif")
turtle.register_shape("findp.gif")
turtle.register_shape("findg n.gif")
turtle.register_shape("findg d.gif")
turtle.register_shape("findw n.gif")
turtle.register_shape("findw d.gif")
turtle.register_shape("findf n.gif")
turtle.register_shape("findf d.gif")
turtle.register_shape("findp n.gif")
turtle.register_shape("findp d.gif")


def clear_turtle_w():
    turtle_w.penup()
    turtle_w.goto(90,100)
    for _ in range(2):
        turtle_w.fillcolor("#FFFFFF")
        turtle_w.begin_fill()
        turtle_w.forward(400)
        turtle_w.left(90)
        turtle_w.forward(100)
        turtle_w.left(90)
        turtle_w.end_fill()
    turtle_w.goto(100,100)


x = turtle.xcor()
y = turtle.ycor()
x = round(x,0)
y = round(y,0)



#how to move in this maze
def up():
    turtle.setheading(90)
    go = True
    steps = 25
    turtle.shape("front.gif")
    global findf
    global findw
    global findg
    global findp
    while (go == True) and (steps > 0):
        x = turtle.xcor()
        y = turtle.ycor()
        x = round(x,0)
        y = round(y,0)

        if 13 < steps <= 25 :
            turtle.shape("front go left.gif")
        if 1 < steps <= 13 :
            turtle.shape("front go right.gif")
        elif steps == 1 :
            turtle.shape("front.gif")
            
        if (-264 <= y <= -236) and (-350 <= x <= -300):
            go = False
        elif (-264 <= y <= -236) and (-275 <= x <= 350):
            go = False
        elif (-164 <= y <= -136) and (-300 <= x <= -250):
            go = False
        elif (-164 <= y <= -136) and (100 <= x <= 300):
            go = False
        elif (-114 <= y <= -86) and (-250 <= x <= -100):
            go = False
        elif (-214 <= y <= -186) and (-200 <= x <= -100):
            go = False
        elif (-64 <= y <= -36) and (-250 <= x <= -100):
            go = False
        elif (-64 <= y <= -36) and (50 <= x <= 100):
            go = False
        elif (36 <= y <= 64) and (-250 <= x <= -150):
            go = False
        elif (36 <= y <= 64) and (100 <= x <= 150):
            go = False
        elif (86 <= y <= 114) and (-300 <= x <= -250):
            go = False
        elif (86 <= y <= 114) and (0 <= x <= 50):
            go = False
        elif (86 <= y <= 114) and (100 <= x <= 150):
            go = False
        elif (116 <= y <= 134) and (-200 <= x <= -50):
            go = False
        elif (136 <= y <= 164) and (-350 <= x <= -250):
            go = False
        elif (141 <= y <= 159) and (-150 <= x <= 50):
            go = False
        elif (136 <= y <= 164) and (100 <= x <= 150):
            go = False
        elif (161 <= y <= 189) and (-200 <= x <= -100):
            go = False
        elif (161 <= y <= 189) and (50 <= x <= 150):
            go = False
        elif (186 <= y <= 214) and (200 <= x <= 250):
            go = False
        elif (216 <= y <= 234) and (-250 <= x <= 300):
            go = False
        elif (241 <= y <= 259) and (-350 <= x <= 300):
            go = False
        elif (241 <= y <= 259) and (325 <= x <= 350):
            go = False
        elif (-250 <= y <= 250) and (-359 <= x <= -341):
            go = False
        elif (100 <= y <= 225) and (-259 <= x <= -241):
            go = False
        elif (-50 <= y <= 0) and (-259 <= x <= -241):
            go = False
        elif (-250 <= y <= -100) and (-259 <= x <= -241):
            go = False
        elif (125 <= y <= 175) and (-209 <= x <= -191):
            go = False
        elif (-200 <= y <= -150) and (-209 <= x <= -191):
            go = False
        elif (50 <= y <= 100) and (-159 <= x <= -141):
            go = False
        elif (150 <= y <= 175) and (-109 <= x <= -91):
            go = False
        elif (-50 <= y <= 125) and (-109 <= x <= -91):
            go = False
        elif (-200 <= y <= -100) and (-109 <= x <= -91):
            go = False
        elif (150 <= y <= 225) and (-59 <= x <= -41):
            go = False
        elif (-200 <= y <= 125) and (-59 <= x <= -41):
            go = False
        elif (-250 <= y <= 50) and (-9 <= x <= 9):
            go = False
        elif (100 <= y <= 175) and (41 <= x <= 59):
            go = False
        elif (-50 <= y <= 50) and (41 <= x <= 59):
            go = False
        elif (150 <= y <= 175) and (91 <= x <= 109):
            go = False
        elif (50 <= y <= 100) and (91 <= x <= 109):
            go = False
        elif (-50 <= y <= 225) and (241 <= x <= 259):
            go = False
        elif (-150 <= y <= 225) and (291 <= x <= 309):
            go = False
        elif (-250 <= y <= 250) and (341 <= x <= 359):
            go = False
        if (-87.5 <= x <= -62.5) and (150 <= y <= 175):
            findf = findf + 1
            if findf == 1:
                go = False
                t_wf.fillcolor("#ffffff")
                t_wf.ht()
                t_wf_dis.ht()
                t_wf.up()
                t_wf_dis.up()
                t_wf.goto(-500,500)
                t_wf_dis.goto(0,-250)
                t_wf.begin_fill()
                for _ in range(4):
                    t_wf.forward(1000)
                    t_wf.right(90)
                t_wf.end_fill()
                t_wf.goto(0,0)
                t_wf.st()
                t_wf_dis.st()
                t_wf.shape("findf.gif")
                t_wf_dis.shape("findf n.gif")
                time.sleep(3)
                t_wf_dis.shape("findf d.gif")
                time.sleep(9)
                t_wf.ht()
                t_wf_dis.ht()
                t_wf.clear()
                go = True
                break
        if (-137.5 <= x <= -112.5) and (150 <= y <= 175):
            findp = findp + 1
            if findp == 1:
                go = False
                t_wp.fillcolor("#ffffff")
                t_wp.ht()
                t_wp_dis.ht()
                t_wp.up()
                t_wp_dis.up()
                t_wp.goto(-500,500)
                t_wp_dis.goto(0,-250)
                t_wp.begin_fill()
                for _ in range(4):
                    t_wp.forward(1000)
                    t_wp.right(90)
                t_wp.end_fill()
                t_wp.goto(0,0)
                t_wp.st()
                t_wp_dis.st()
                t_wp.shape("findp.gif")
                t_wp_dis.shape("findp n.gif")
                time.sleep(3)
                t_wp_dis.shape("findp d.gif")
                time.sleep(9)
                t_wp.ht()
                t_wp_dis.ht()
                t_wp.clear()
                go = True
                break
        if (-312.5 <= x <= -287.5) and (162.5 <= y <= 187.5):
            findg = findg + 1
            if findg == 1:
                go = False
                t_wg.fillcolor("#ffffff")
                t_wg.ht()
                t_wg_dis.ht()
                t_wg.up()
                t_wg_dis.up()
                t_wg.goto(-500,500)
                t_wg_dis.goto(0,-250)
                t_wg.begin_fill()
                for _ in range(4):
                    t_wg.forward(1000)
                    t_wg.right(90)
                t_wg.end_fill()
                t_wg.goto(0,0)
                t_wg.st()
                t_wg_dis.st()
                t_wg.shape("findg.gif")
                t_wg_dis.shape("findg n.gif")
                time.sleep(3)
                t_wg_dis.shape("findg d.gif")
                time.sleep(9)
                t_wg.ht()
                t_wg_dis.ht()
                t_wg.clear()
                go = True
                break
        if (262.5 <= x <= 287.5) and (187.5 <= y <= 212.5):
            findw = findw + 1
            if findw == 1:
                go = False
                t_ww.fillcolor("#ffffff")
                t_ww.ht()
                t_ww_dis.ht()
                t_ww.up()
                t_ww_dis.up()
                t_ww.goto(-500,500)
                t_ww_dis.goto(0,-250)
                t_ww.begin_fill()
                for _ in range(4):
                    t_ww.forward(1000)
                    t_ww.right(90)
                t_ww.end_fill()
                t_ww.goto(0,0)
                t_ww.st()
                t_ww_dis.st()
                t_ww.shape("findw.gif")
                t_ww_dis.shape("findw n.gif")
                time.sleep(3)
                t_ww_dis.shape("findw d.gif")
                time.sleep(9)
                t_ww.ht()
                t_ww_dis.ht()
                t_ww.clear()
                go = True
                break
        if go == False:
            turtle.backward(1)
            go = True
            break
        turtle.forward(1)
        steps = steps - 1
        if (findf >= 1) and (findg >= 1) and (findw >= 1) and(findp >= 1):
            info = True
        else:
            info = False
        if (info == True) and (y >= 250):
            print("congratulation")
            t.ht()
            turtle.ht()
            t.clear()
            turtle_w.write("Congratulation, young trainer",move = False,font = ("Arial",15,"normal"))
            time.sleep(2)
            clear_turtle_w()
            turtle_w.write("you successfully complete the mission")
            time.sleep(2)
            clear_turtle_w()
            turtle.done()
        elif (info == False) and (y >= 250):
            print("congratulation")
            t.ht()
            turtle.ht()
            t.clear()
            turtle_w.write("Congratulation, young trainer",move = False,font = ("Arial",15,"normal"))
            time.sleep(2)
            clear_turtle_w()
            turtle_w.write("You go out of the maze",move = False,font = ("Arial",15,"normal"))
            time.sleep(2)
            clear_turtle_w()
            turtle_w.write("But you did not collect all the information",move = False,font = ("Arial",15,"normal"))
            time.sleep(2)
            clear_turtle_w()
            turtle_w.write("So in this game, you lose",move = False,font = ("Arial",15,"normal"))
            turtle.done()
        #turtle.onkey(stop_up,"Down")
        
def left():
    turtle.setheading(180)
    go = True
    steps = 25
    global findf
    global findw
    global findg
    global findp
    turtle.shape("left.gif")
    while (go == True) and (steps > 0):
        x = turtle.xcor()
        y = turtle.ycor()
        x = round(x,0)
        y = round(y,0)

        if 13 < steps <= 25 :
            turtle.shape("left go left.gif")
        if 1 < steps <= 13  :
            turtle.shape("left go right.gif")
        elif steps == 1 :
            turtle.shape("left.gif")
            
        if (-264 <= y <= -236) and (-350 <= x <= -300):
            go = False
        elif (-264 <= y <= -236) and (-275 <= x <= 350):
            go = False
        elif (-164 <= y <= -136) and (-300 <= x <= -250):
            go = False
        elif (-164 <= y <= -136) and (100 <= x <= 300):
            go = False
        elif (-114 <= y <= -86) and (-250 <= x <= -100):
            go = False
        elif (-214 <= y <= -186) and (-200 <= x <= -100):
            go = False
        elif (-64 <= y <= -36) and (-250 <= x <= -100):
            go = False
        elif (-64 <= y <= -36) and (50 <= x <= 100):
            go = False
        elif (36 <= y <= 64) and (-250 <= x <= -150):
            go = False
        elif (36 <= y <= 64) and (100 <= x <= 150):
            go = False
        elif (86 <= y <= 114) and (-300 <= x <= -250):
            go = False
        elif (86 <= y <= 114) and (0 <= x <= 50):
            go = False
        elif (86 <= y <= 114) and (100 <= x <= 150):
            go = False
        elif (116 <= y <= 134) and (-200 <= x <= -50):
            go = False
        elif (136 <= y <= 164) and (-350 <= x <= -250):
            go = False
        elif (141 <= y <= 159) and (-150 <= x <= 50):
            go = False
        elif (136 <= y <= 164) and (100 <= x <= 150):
            go = False
        elif (161 <= y <= 189) and (-200 <= x <= -100):
            go = False
        elif (161 <= y <= 189) and (50 <= x <= 150):
            go = False
        elif (186 <= y <= 214) and (200 <= x <= 250):
            go = False
        elif (216 <= y <= 234) and (-250 <= x <= 300):
            go = False
        elif (241 <= y <= 259) and (-350 <= x <= 300):
            go = False
        elif (241 <= y <= 259) and (325 <= x <= 350):
            go = False
        elif (-250 <= y <= 250) and (-359 <= x <= -341):
            go = False
        elif (100 <= y <= 225) and (-259 <= x <= -241):
            go = False
        elif (-50 <= y <= 0) and (-259 <= x <= -241):
            go = False
        elif (-250 <= y <= -100) and (-259 <= x <= -241):
            go = False
        elif (125 <= y <= 175) and (-209 <= x <= -191):
            go = False
        elif (-200 <= y <= -150) and (-209 <= x <= -191):
            go = False
        elif (50 <= y <= 100) and (-159 <= x <= -141):
            go = False
        elif (150 <= y <= 175) and (-109 <= x <= -91):
            go = False
        elif (-50 <= y <= 125) and (-109 <= x <= -91):
            go = False
        elif (-200 <= y <= -100) and (-109 <= x <= -91):
            go = False
        elif (150 <= y <= 225) and (-59 <= x <= -41):
            go = False
        elif (-200 <= y <= 125) and (-59 <= x <= -41):
            go = False
        elif (-250 <= y <= 50) and (-9 <= x <= 9):
            go = False
        elif (100 <= y <= 175) and (41 <= x <= 59):
            go = False
        elif (-50 <= y <= 50) and (41 <= x <= 59):
            go = False
        elif (150 <= y <= 175) and (91 <= x <= 109):
            go = False
        elif (50 <= y <= 100) and (91 <= x <= 109):
            go = False
        elif (-50 <= y <= 225) and (241 <= x <= 259):
            go = False
        elif (-150 <= y <= 225) and (291 <= x <= 309):
            go = False
        elif (-250 <= y <= 250) and (341 <= x <= 359):
            go = False
        if (-87.5 <= x <= -62.5) and (150 <= y <= 175):
            findf = findf + 1
            if findf == 1:
                go = False
                t_wf.fillcolor("#ffffff")
                t_wf.ht()
                t_wf_dis.ht()
                t_wf.up()
                t_wf_dis.up()
                t_wf.goto(-500,500)
                t_wf_dis.goto(0,-250)
                t_wf.begin_fill()
                for _ in range(4):
                    t_wf.forward(1000)
                    t_wf.right(90)
                t_wf.end_fill()
                t_wf.goto(0,0)
                t_wf.st()
                t_wf_dis.st()
                t_wf.shape("findf.gif")
                t_wf_dis.shape("findf n.gif")
                time.sleep(3)
                t_wf_dis.shape("findf d.gif")
                time.sleep(9)
                t_wf.ht()
                t_wf_dis.ht()
                t_wf.clear()
                go = True
                break
        if (-137.5 <= x <= -112.5) and (150 <= y <= 175):
            findp = findp + 1
            if findp == 1:
                go = False
                t_wp.fillcolor("#ffffff")
                t_wp.ht()
                t_wp_dis.ht()
                t_wp.up()
                t_wp_dis.up()
                t_wp.goto(-500,500)
                t_wp_dis.goto(0,-250)
                t_wp.begin_fill()
                for _ in range(4):
                    t_wp.forward(1000)
                    t_wp.right(90)
                t_wp.end_fill()
                t_wp.goto(0,0)
                t_wp.st()
                t_wp_dis.st()
                t_wp.shape("findp.gif")
                t_wp_dis.shape("findp n.gif")
                time.sleep(3)
                t_wp_dis.shape("findp d.gif")
                time.sleep(9)
                t_wp.ht()
                t_wp_dis.ht()
                t_wp.clear()
                go = True
                break
        if (-312.5 <= x <= -287.5) and (162.5 <= y <= 187.5):
            findg = findg + 1
            if findg == 1:
                go = False
                t_wg.fillcolor("#ffffff")
                t_wg.ht()
                t_wg_dis.ht()
                t_wg.up()
                t_wg_dis.up()
                t_wg.goto(-500,500)
                t_wg_dis.goto(0,-250)
                t_wg.begin_fill()
                for _ in range(4):
                    t_wg.forward(1000)
                    t_wg.right(90)
                t_wg.end_fill()
                t_wg.goto(0,0)
                t_wg.st()
                t_wg_dis.st()
                t_wg.shape("findg.gif")
                t_wg_dis.shape("findg n.gif")
                time.sleep(3)
                t_wg_dis.shape("findg d.gif")
                time.sleep(9)
                t_wg.ht()
                t_wg_dis.ht()
                t_wg.clear()
                go = True
                break
        if (262.5 <= x <= 287.5) and (187.5 <= y <= 212.5):
            findw = findw + 1
            if findw == 1:
                go = False
                t_ww.fillcolor("#ffffff")
                t_ww.ht()
                t_ww_dis.ht()
                t_ww.up()
                t_ww_dis.up()
                t_ww.goto(-500,500)
                t_ww_dis.goto(0,-250)
                t_ww.begin_fill()
                for _ in range(4):
                    t_ww.forward(1000)
                    t_ww.right(90)
                t_ww.end_fill()
                t_ww.goto(0,0)
                t_ww.st()
                t_ww_dis.st()
                t_ww.shape("findw.gif")
                t_ww_dis.shape("findw n.gif")
                time.sleep(3)
                t_ww_dis.shape("findw d.gif")
                time.sleep(9)
                t_ww.ht()
                t_ww_dis.ht()
                t_ww.clear()
                go = True
                break
        if go == False:
            turtle.backward(1)
            go = True
            break
        turtle.forward(1)
        steps = steps - 1
        if (findf >= 1) and (findg >= 1) and (findw >= 1) and(findp >= 1):
            info = True
        else:
            info = False
        if (info == True) and (y >= 250):
            print("congratulation")
            t.ht()
            turtle.ht()
            t.clear()
            turtle_w.write("Congratulation, young trainer",move = False,font = ("Arial",15,"normal"))
            time.sleep(2)
            clear_turtle_w()
            turtle_w.write("you successfully complete the mission")
            time.sleep(2)
            clear_turtle_w()
            turtle.done()
        elif (info == False) and (y >= 250):
            print("congratulation")
            t.ht()
            turtle.ht()
            t.clear()
            turtle_w.write("Congratulation, young trainer",move = False,font = ("Arial",15,"normal"))
            time.sleep(2)
            clear_turtle_w()
            turtle_w.write("You go out of the maze",move = False,font = ("Arial",15,"normal"))
            time.sleep(2)
            clear_turtle_w()
            turtle_w.write("But you did not collect all the information",move = False,font = ("Arial",15,"normal"))
            time.sleep(2)
            clear_turtle_w()
            turtle_w.write("So in this game, you lose",move = False,font = ("Arial",15,"normal"))
            turtle.done()
        #turtle.onkey(stop_left,"Right")
        
def right():
    turtle.setheading(0)
    go = True
    steps = 25
    global findf
    global findw
    global findg
    global findp
    turtle.shape("right.gif")
    while (go == True) and (steps > 0):
        x = turtle.xcor()
        y = turtle.ycor()
        x = round(x,0)
        y = round(y,0)

        if 13 < steps <= 25 :
            turtle.shape("right go left.gif")
        if 1 < steps <= 13 :
            turtle.shape("right go right.gif")
        elif steps == 1 :
            turtle.shape("right.gif")
            
        if (-264 <= y <= -236) and (-350 <= x <= -300):
            go = False
        elif (-264 <= y <= -236) and (-275 <= x <= 350):
            go = False
        elif (-164 <= y <= -136) and (-300 <= x <= -250):
            go = False
        elif (-164 <= y <= -136) and (100 <= x <= 300):
            go = False
        elif (-114 <= y <= -86) and (-250 <= x <= -100):
            go = False
        elif (-214 <= y <= -186) and (-200 <= x <= -100):
            go = False
        elif (-64 <= y <= -36) and (-250 <= x <= -100):
            go = False
        elif (-64 <= y <= -36) and (50 <= x <= 100):
            go = False
        elif (36 <= y <= 64) and (-250 <= x <= -150):
            go = False
        elif (36 <= y <= 64) and (100 <= x <= 150):
            go = False
        elif (86 <= y <= 114) and (-300 <= x <= -250):
            go = False
        elif (86 <= y <= 114) and (0 <= x <= 50):
            go = False
        elif (86 <= y <= 114) and (100 <= x <= 150):
            go = False
        elif (116 <= y <= 134) and (-200 <= x <= -50):
            go = False
        elif (136 <= y <= 164) and (-350 <= x <= -250):
            go = False
        elif (141 <= y <= 159) and (-150 <= x <= 50):
            go = False
        elif (136 <= y <= 164) and (100 <= x <= 150):
            go = False
        elif (161 <= y <= 189) and (-200 <= x <= -100):
            go = False
        elif (161 <= y <= 189) and (50 <= x <= 150):
            go = False
        elif (186 <= y <= 214) and (200 <= x <= 250):
            go = False
        elif (216 <= y <= 234) and (-250 <= x <= 300):
            go = False
        elif (241 <= y <= 259) and (-350 <= x <= 300):
            go = False
        elif (241 <= y <= 259) and (325 <= x <= 350):
            go = False
        elif (-250 <= y <= 250) and (-359 <= x <= -341):
            go = False
        elif (100 <= y <= 225) and (-259 <= x <= -241):
            go = False
        elif (-50 <= y <= 0) and (-259 <= x <= -241):
            go = False
        elif (-250 <= y <= -100) and (-259 <= x <= -241):
            go = False
        elif (125 <= y <= 175) and (-209 <= x <= -191):
            go = False
        elif (-200 <= y <= -150) and (-209 <= x <= -191):
            go = False
        elif (50 <= y <= 100) and (-159 <= x <= -141):
            go = False
        elif (150 <= y <= 175) and (-109 <= x <= -91):
            go = False
        elif (-50 <= y <= 125) and (-109 <= x <= -91):
            go = False
        elif (-200 <= y <= -100) and (-109 <= x <= -91):
            go = False
        elif (150 <= y <= 225) and (-59 <= x <= -41):
            go = False
        elif (-200 <= y <= 125) and (-59 <= x <= -41):
            go = False
        elif (-250 <= y <= 50) and (-9 <= x <= 9):
            go = False
        elif (100 <= y <= 175) and (41 <= x <= 59):
            go = False
        elif (-50 <= y <= 50) and (41 <= x <= 59):
            go = False
        elif (150 <= y <= 175) and (91 <= x <= 109):
            go = False
        elif (50 <= y <= 100) and (91 <= x <= 109):
            go = False
        elif (-50 <= y <= 225) and (241 <= x <= 259):
            go = False
        elif (-150 <= y <= 225) and (291 <= x <= 309):
            go = False
        elif (-250 <= y <= 250) and (341 <= x <= 359):
            go = False
        if (-87.5 <= x <= -62.5) and (150 <= y <= 175):
            findf = findf + 1
            if findf == 1:
                go = False
                t_wf.fillcolor("#ffffff")
                t_wf.ht()
                t_wf_dis.ht()
                t_wf.up()
                t_wf_dis.up()
                t_wf.goto(-500,500)
                t_wf_dis.goto(0,-250)
                t_wf.begin_fill()
                for _ in range(4):
                    t_wf.forward(1000)
                    t_wf.right(90)
                t_wf.end_fill()
                t_wf.goto(0,0)
                t_wf.st()
                t_wf_dis.st()
                t_wf.shape("findf.gif")
                t_wf_dis.shape("findf n.gif")
                time.sleep(3)
                t_wf_dis.shape("findf d.gif")
                time.sleep(9)
                t_wf.ht()
                t_wf_dis.ht()
                t_wf.clear()
                go = True
                break
        if (-137.5 <= x <= -112.5) and (150 <= y <= 175):
            findp = findp + 1
            if findp == 1:
                go = False
                t_wp.fillcolor("#ffffff")
                t_wp.ht()
                t_wp_dis.ht()
                t_wp.up()
                t_wp_dis.up()
                t_wp.goto(-500,500)
                t_wp_dis.goto(0,-250)
                t_wp.begin_fill()
                for _ in range(4):
                    t_wp.forward(1000)
                    t_wp.right(90)
                t_wp.end_fill()
                t_wp.goto(0,0)
                t_wp.st()
                t_wp_dis.st()
                t_wp.shape("findp.gif")
                t_wp_dis.shape("findp n.gif")
                time.sleep(3)
                t_wp_dis.shape("findp d.gif")
                time.sleep(9)
                t_wp.ht()
                t_wp_dis.ht()
                t_wp.clear()
                go = True
                break
        if (-312.5 <= x <= -287.5) and (162.5 <= y <= 187.5):
            findg = findg + 1
            if findg == 1:
                go = False
                t_wg.fillcolor("#ffffff")
                t_wg.ht()
                t_wg_dis.ht()
                t_wg.up()
                t_wg_dis.up()
                t_wg.goto(-500,500)
                t_wg_dis.goto(0,-250)
                t_wg.begin_fill()
                for _ in range(4):
                    t_wg.forward(1000)
                    t_wg.right(90)
                t_wg.end_fill()
                t_wg.goto(0,0)
                t_wg.st()
                t_wg_dis.st()
                t_wg.shape("findg.gif")
                t_wg_dis.shape("findg n.gif")
                time.sleep(3)
                t_wg_dis.shape("findg d.gif")
                time.sleep(9)
                t_wg.ht()
                t_wg_dis.ht()
                t_wg.clear()
                go = True
                break
        if (262.5 <= x <= 287.5) and (187.5 <= y <= 212.5):
            findw = findw + 1
            if findw == 1:
                go = False
                t_ww.fillcolor("#ffffff")
                t_ww.ht()
                t_ww_dis.ht()
                t_ww.up()
                t_ww_dis.up()
                t_ww.goto(-500,500)
                t_ww_dis.goto(0,-250)
                t_ww.begin_fill()
                for _ in range(4):
                    t_ww.forward(1000)
                    t_ww.right(90)
                t_ww.end_fill()
                t_ww.goto(0,0)
                t_ww.st()
                t_ww_dis.st()
                t_ww.shape("findw.gif")
                t_ww_dis.shape("findw n.gif")
                time.sleep(3)
                t_ww_dis.shape("findw d.gif")
                time.sleep(9)
                t_ww.ht()
                t_ww_dis.ht()
                t_ww.clear()
                go = True
                break
        if go == False:
            turtle.backward(1)
            go = True
            break
        turtle.forward(1)
        steps = steps - 1
        if (findf >= 1) and (findg >= 1) and (findw >= 1) and(findp >= 1):
            info = True
        else:
            info = False
        if (info == True) and (y >= 250):
            print("congratulation")
            t.ht()
            turtle.ht()
            t.clear()
            turtle_w.write("Congratulation, young trainer",move = False,font = ("Arial",15,"normal"))
            time.sleep(2)
            clear_turtle_w()
            turtle_w.write("you successfully complete the mission")
            time.sleep(2)
            clear_turtle_w()
            turtle.done()
        elif (info == False) and (y >= 250):
            print("congratulation")
            t.ht()
            turtle.ht()
            t.clear()
            turtle_w.write("Congratulation, young trainer",move = False,font = ("Arial",15,"normal"))
            time.sleep(2)
            clear_turtle_w()
            turtle_w.write("You go out of the maze",move = False,font = ("Arial",15,"normal"))
            time.sleep(2)
            clear_turtle_w()
            turtle_w.write("But you did not collect all the information",move = False,font = ("Arial",15,"normal"))
            time.sleep(2)
            clear_turtle_w()
            turtle_w.write("So in this game, you lose",move = False,font = ("Arial",15,"normal"))
            turtle.done()
        #turtle.onkey(stop_right,"Left")

def down():
    turtle.setheading(270)
    go = True
    steps = 25
    global findf
    global findw
    global findg
    global findp
    turtle.shape("back.gif")
    while (go == True) and (steps > 0):
        x = turtle.xcor()
        y = turtle.ycor()
        x = round(x,0)
        y = round(y,0)

        if 13 < steps <= 25 :
            turtle.shape("back go left.gif")
        if 1 < steps <= 13 :
            turtle.shape("back go right.gif")
        elif steps == 1 :
            turtle.shape("back.gif")
            
        if (-264 <= y <= -236) and (-350 <= x <= -300):
            go = False
        elif (-264 <= y <= -236) and (-275 <= x <= 350):
            go = False
        elif (-164 <= y <= -136) and (-300 <= x <= -250):
            go = False
        elif (-164 <= y <= -136) and (100 <= x <= 300):
            go = False
        elif (-114 <= y <= -86) and (-250 <= x <= -100):
            go = False
        elif (-214 <= y <= -186) and (-200 <= x <= -100):
            go = False
        elif (-64 <= y <= -36) and (-250 <= x <= -100):
            go = False
        elif (-64 <= y <= -36) and (50 <= x <= 100):
            go = False
        elif (36 <= y <= 64) and (-250 <= x <= -150):
            go = False
        elif (36 <= y <= 64) and (100 <= x <= 150):
            go = False
        elif (86 <= y <= 114) and (-300 <= x <= -250):
            go = False
        elif (86 <= y <= 114) and (0 <= x <= 50):
            go = False
        elif (86 <= y <= 114) and (100 <= x <= 150):
            go = False
        elif (116 <= y <= 134) and (-200 <= x <= -50):
            go = False
        elif (136 <= y <= 164) and (-350 <= x <= -250):
            go = False
        elif (141 <= y <= 159) and (-150 <= x <= 50):
            go = False
        elif (136 <= y <= 164) and (100 <= x <= 150):
            go = False
        elif (161 <= y <= 189) and (-200 <= x <= -100):
            go = False
        elif (161 <= y <= 189) and (50 <= x <= 150):
            go = False
        elif (186 <= y <= 214) and (200 <= x <= 250):
            go = False
        elif (216 <= y <= 234) and (-250 <= x <= 300):
            go = False
        elif (241 <= y <= 259) and (-350 <= x <= 300):
            go = False
        elif (241 <= y <= 259) and (325 <= x <= 350):
            go = False
        elif (-250 <= y <= 250) and (-359 <= x <= -341):
            go = False
        elif (100 <= y <= 225) and (-259 <= x <= -241):
            go = False
        elif (-50 <= y <= 0) and (-259 <= x <= -241):
            go = False
        elif (-250 <= y <= -100) and (-259 <= x <= -241):
            go = False
        elif (125 <= y <= 175) and (-209 <= x <= -191):
            go = False
        elif (-200 <= y <= -150) and (-209 <= x <= -191):
            go = False
        elif (50 <= y <= 100) and (-159 <= x <= -141):
            go = False
        elif (150 <= y <= 175) and (-109 <= x <= -91):
            go = False
        elif (-50 <= y <= 125) and (-109 <= x <= -91):
            go = False
        elif (-200 <= y <= -100) and (-109 <= x <= -91):
            go = False
        elif (150 <= y <= 225) and (-59 <= x <= -41):
            go = False
        elif (-200 <= y <= 125) and (-59 <= x <= -41):
            go = False
        elif (-250 <= y <= 50) and (-9 <= x <= 9):
            go = False
        elif (100 <= y <= 175) and (41 <= x <= 59):
            go = False
        elif (-50 <= y <= 50) and (41 <= x <= 59):
            go = False
        elif (150 <= y <= 175) and (91 <= x <= 109):
            go = False
        elif (50 <= y <= 100) and (91 <= x <= 109):
            go = False
        elif (-50 <= y <= 225) and (241 <= x <= 259):
            go = False
        elif (-150 <= y <= 225) and (291 <= x <= 309):
            go = False
        elif (-250 <= y <= 250) and (341 <= x <= 359):
            go = False
        if (-87.5 <= x <= -62.5) and (150 <= y <= 175):
            findf = findf + 1
            if findf == 1:
                go = False
                t_wf.fillcolor("#ffffff")
                t_wf.ht()
                t_wf_dis.ht()
                t_wf.up()
                t_wf_dis.up()
                t_wf.goto(-500,500)
                t_wf_dis.goto(0,-250)
                t_wf.begin_fill()
                for _ in range(4):
                    t_wf.forward(1000)
                    t_wf.right(90)
                t_wf.end_fill()
                t_wf.goto(0,0)
                t_wf.st()
                t_wf_dis.st()
                t_wf.shape("findf.gif")
                t_wf_dis.shape("findf n.gif")
                time.sleep(3)
                t_wf_dis.shape("findf d.gif")
                time.sleep(9)
                t_wf.ht()
                t_wf_dis.ht()
                t_wf.clear()
                go = True
                break
        if (-137.5 <= x <= -112.5) and (150 <= y <= 175):
            findp = findp + 1
            if findp == 1:
                go = False
                t_wp.fillcolor("#ffffff")
                t_wp.ht()
                t_wp_dis.ht()
                t_wp.up()
                t_wp_dis.up()
                t_wp.goto(-500,500)
                t_wp_dis.goto(0,-250)
                t_wp.begin_fill()
                for _ in range(4):
                    t_wp.forward(1000)
                    t_wp.right(90)
                t_wp.end_fill()
                t_wp.goto(0,0)
                t_wp.st()
                t_wp_dis.st()
                t_wp.shape("findp.gif")
                t_wp_dis.shape("findp n.gif")
                time.sleep(3)
                t_wp_dis.shape("findp d.gif")
                time.sleep(9)
                t_wp.ht()
                t_wp_dis.ht()
                t_wp.clear()
                go = True
                break
        if (-312.5 <= x <= -287.5) and (162.5 <= y <= 187.5):
            findg = findg + 1
            if findg == 1:
                go = False
                t_wg.fillcolor("#ffffff")
                t_wg.ht()
                t_wg_dis.ht()
                t_wg.up()
                t_wg_dis.up()
                t_wg.goto(-500,500)
                t_wg_dis.goto(0,-250)
                t_wg.begin_fill()
                for _ in range(4):
                    t_wg.forward(1000)
                    t_wg.right(90)
                t_wg.end_fill()
                t_wg.goto(0,0)
                t_wg.st()
                t_wg_dis.st()
                t_wg.shape("findg.gif")
                t_wg_dis.shape("findg n.gif")
                time.sleep(3)
                t_wg_dis.shape("findg d.gif")
                time.sleep(9)
                t_wg.ht()
                t_wg_dis.ht()
                t_wg.clear()
                go = True
                break
        if (262.5 <= x <= 287.5) and (187.5 <= y <= 212.5):
            findw = findw + 1
            if findw == 1:
                go = False
                t_ww.fillcolor("#ffffff")
                t_ww.ht()
                t_ww_dis.ht()
                t_ww.up()
                t_ww_dis.up()
                t_ww.goto(-500,500)
                t_ww_dis.goto(0,-250)
                t_ww.begin_fill()
                for _ in range(4):
                    t_ww.forward(1000)
                    t_ww.right(90)
                t_ww.end_fill()
                t_ww.goto(0,0)
                t_ww.st()
                t_ww_dis.st()
                t_ww.shape("findw.gif")
                t_ww_dis.shape("findw n.gif")
                time.sleep(3)
                t_ww_dis.shape("findw d.gif")
                time.sleep(9)
                t_ww.ht()
                t_ww_dis.ht()
                t_ww.clear()
                go = True
                break
        if go == False:
            turtle.backward(1)
            go = True
            break
        turtle.forward(1)
        steps = steps - 1
        if (findf >= 1) and (findg >= 1) and (findw >= 1) and(findp >= 1):
            info = True
        else:
            info = False
        if (info == True) and (y >= 250):
            print("congratulation")
            t.ht()
            turtle.ht()
            t.clear()
            turtle_w.write("Congratulation, young trainer",move = False,font = ("Arial",15,"normal"))
            time.sleep(2)
            clear_turtle_w()
            turtle_w.write("you successfully complete the mission")
            time.sleep(2)
            clear_turtle_w()
            turtle.done()
        elif (info == False) and (y >= 250):
            print("congratulation")
            t.ht()
            turtle.ht()
            t.clear()
            turtle_w.write("Congratulation, young trainer",move = False,font = ("Arial",15,"normal"))
            time.sleep(2)
            clear_turtle_w()
            turtle_w.write("You go out of the maze",move = False,font = ("Arial",15,"normal"))
            time.sleep(2)
            clear_turtle_w()
            turtle_w.write("But you did not collect all the information",move = False,font = ("Arial",15,"normal"))
            time.sleep(2)
            clear_turtle_w()
            turtle_w.write("So in this game, you lose",move = False,font = ("Arial",15,"normal"))
            turtle.done()
        #turtle.onkey(stop_down,"Up")
    



#frame 1
turtle_w.ht()
turtle.bgpic("images.png")
turtle_w.penup()
turtle_w.goto(100,100)
turtle_w.write("hi young trainer, what is your name",move = False,font = ("Arial",15,"normal"))
name = input("")
x = len(name)
clear_turtle_w()
turtle_w.write(name,move = False,font = ("Arial",15,"normal"))
turtle_w.forward(11*x)
turtle_w.write(",I am doing a research",move = False,font = ("Arial",15,"normal"))
time.sleep(2)
clear_turtle_w()
turtle_w.write("would you like to help me?",move = False,font = ("Arial",15,"normal"))
time.sleep(2)
clear_turtle_w()
turtle_w.write("Your task is to collect 4 kinds",move = False,font = ("Arial",15,"normal"))
time.sleep(2)
clear_turtle_w()
turtle_w.write("of pokemons' information.",move = False,font = ("Arial",15,"normal"))
time.sleep(2)
clear_turtle_w()
turtle_w.write("They all live in a maze. Go to ",move = False,font = ("Arial",15,"normal"))
time.sleep(2)
clear_turtle_w()
turtle_w.write("stand on the point to observe them,",move = False,font = ("Arial",15,"normal"))
time.sleep(2)
clear_turtle_w()
turtle_w.write("then you can get thier information.",move = False,font = ("Arial",15,"normal"))
time.sleep(2)
clear_turtle_w()
time.sleep(2)
print('''Task:
         collect 4 kinds of pokemons' information
         go out of the maze
         ''')
print('''use up, down, left, right key to control the character. ''')

print('''Mzae CAUTION: You may be dragged into the wall !!!  Be careful
                Some walls will be invisable when you walk by !!! Be careful''')


#maze part
t = turtle.Turtle()
t.speed(0)
t.ht()
t.penup()
t.goto(-350,350)
t.fillcolor("#ffffff")
t.begin_fill()
for _ in range(4):
    t.forward(700)
    t.right(90)
t.end_fill()

        #draw
        #outside
t.pencolor("#000000")
t.goto(-350,-250)
t.pendown()
t.left(90)
t.forward(500)
t.goto(300,250)
t.penup()
t.goto(325,250)
t.pendown()
t.goto(350,250)
t.goto(350,-250)
t.goto(-275,-250)
t.penup()
t.goto(-300,-250)
t.pendown()
t.goto(-350,-250)
        #inside

        #-250 - -200
t.penup()
t.goto(-300,-150)
t.pendown()
t.right(90)
t.forward(50)
t.goto(-250,-250)
t.left(90)
t.forward(150)
t.right(90)
t.forward(150)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(50)
t.penup()
t.goto(-250,0)
t.pendown()
t.goto(-250,-50)
t.right(90)
t.forward(150)
t.left(90)
t.forward(175)
t.goto(-50,125)
t.goto(-50,-200)
t.penup()
t.goto(-100,125)
t.left(90)
t.pendown()
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(100)
t.right(90)
t.forward(25)
t.right(90)
t.forward(50)
t.right(90)
t.goto(-50,150)
t.forward(75)
t.left(90)
t.forward(200)
t.left(90)
t.forward(75)
t.right(90)
t.forward(100)
t.goto(-250,150)
t.right(90)
t.goto(-250,100)
t.goto(-300,100)
t.penup()
t.goto(-250,50)
t.pendown()
t.goto(-150,50)
t.goto(-150,100)

      # 0 - 350
t.penup()
t.goto(-50,150)
t.pendown()
t.right(90)
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.penup()
t.goto(50,150)
t.pendown()
t.forward(25)
t.right(90)
t.forward(100)
t.backward(50)
t.right(90)
t.forward(25)
t.left(90)
t.forward(50)
t.penup()
t.goto(100,100)
t.pendown()
t.forward(50)
t.backward(50)
t.right(90)
t.forward(50)
t.left(90)
t.forward(50)
t.penup()
t.goto(0,-250)
t.pendown()
t.left(90)
t.forward(300)
t.penup()
t.goto(50,50)
t.pendown()
t.backward(100)
t.right(90)
t.forward(50)
t.penup()
t.goto(100,-150)
t.pendown()
t.forward(200)
t.left(90)
t.forward(375)
t.left(90)
t.forward(350)
t.backward(300)
t.left(90)
t.forward(25)
t.goto(200,200)
t.goto(250,200)
t.forward(250)
t.up()
t.shape("circle")
t.pencolor("blue")
t.goto(-125,162.5)
t.stamp()
t.goto(-75,162.5)
t.stamp()
t.goto(-300,175)
t.stamp()
t.goto(275,200)
t.stamp()



turtle.up()
turtle.goto(-285,-250)
turtle.listen()
turtle.st()

turtle.shape("front.gif")


turtle.onkey(up,"Up")
turtle.onkey(left,"Left")
turtle.onkey(right,"Right")
turtle.onkey(down,"Down")


turtle.mainloop()
turtle.done()









