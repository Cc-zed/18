from tkinter import *

bomb = 100
score = 0
bestscore = 0
press_return = True

def start(event):
    global press_return
    global bomb
    global score
    global bestscore

    if not press_return:
        pass
    else:
        bomb = 100
        score = 0
        bestscore = 0
        label.config(text="")
        update_display()
        update_point()
        update_bomb()
        press_return = False

def update_display():
    global score
    global bomb
    if bomb >50:
        bomb_label.config(image=normal_photo)
    elif 0<bomb<50:
        bomb_label.config(image=no_photo)
    else:
        bomb_label.config(image=bang_photo)
    fuse_label.config(text="Fuse = "+str(bomb))
    score_label.config(text="Score = "+str(score))
    fuse_label.after(100, update_display)

def update_bomb():
    global bomb
    bomb -= 5
    if is_alive():
        fuse_label.after(400, update_bomb)

def update_point():
    global score
    score += 1
    if is_alive():
        score_label.after(3000, update_point)

def click():
    global bomb
    if is_alive():
        bomb += 1

def is_alive():
    global bomb
    global press_return
    if bomb <= 0:
        label.config(text="Bang!")
        press_return = True
        best_score()
        return False
    else:
        return True


def best_score():
    global bestscore
    global score
    file_path = "Your_file_path" #<-------------------------------------------------FOR BEST SCORE, ENTER YOUR FILE PATH
    if bestscore < score:
        bestscore = score
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("Best score: " + str(bestscore))

         



root = Tk()
root.title("Game")
root.geometry("500x550")

label = Label(root, text="Press [Enter] to start the game", font=("Comic Sans Ms", 16))
label.pack()

fuse_label = Label(root, text="Fuse: " + str(bomb), font=("Comic Sans Ms", 16))
fuse_label.pack()

score_label = Label(root, text="Score: " + str(score), font=("Comic Sans Ms", 16))
score_label.pack()

no_photo = PhotoImage(file="C:/Users/Sad_ist/Desktop/Python projects/Py projects/Homework/images/bomb_no.gif")
normal_photo = PhotoImage(file="C:/Users/Sad_ist/Desktop/Python projects/Py projects/Homework/images/bomb_normal.gif")
bang_photo = PhotoImage(file="C:/Users/Sad_ist/Desktop/Python projects/Py projects/Homework/images/pow.gif")

bomb_label = Label(root, image=normal_photo)
bomb_label.pack()

click_button = Button(root, text="Click me", font=("Comic Sans Ms", 14), command=click)
click_button.pack()

root.bind('<Return>', start)

root.mainloop()
