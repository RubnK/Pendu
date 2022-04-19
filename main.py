## Copyright RubnK for RCorp™
from tkinter import *
from random import randrange

## Update of the word displayed on the screen
def maj_mot_en_cours(mot_en_cours, lettre, secret):
    n = len(secret)
    for i in range(n):
        if secret[i] == lettre: ## Verification that the letter pressed corresponds to a letter of the secret word
            mot_en_cours[2 * i] = lettre

## Hangman update
def score(lettre):
    global nro, end, img
    if lettre not in secret:
        cnv.delete(images[nro])
        nro -= 1
        cnv.create_image((width_img / 2, height_img / 2),
                         image=images[nro])
        if nro == 0:
            cnv.create_image((width_img / 2, height_img / 2),
                             image=fail)
            lbl["text"] = " ".join(secret)

            end = True
    elif mot_en_cours == list(" ".join(secret)):
        cnv.create_image((width_img / 2, height_img / 2), image=win)
        end = True

## Choose a letter to try
def choisir_lettre(event):
    if end:
        return
    btn = event.widget
    lettre = btn["text"]
    btn["state"] = DISABLED
    maj_mot_en_cours(mot_en_cours, lettre, secret)
    lbl["text"] = "".join(mot_en_cours)
    score(lettre)

## Game init
def init():
    global end, mot_en_cours, secret, nro, img
    secret = arbres[randrange(len(arbres))]
    mot_en_cours = list(' '.join("●" * len(secret))) ## Create text place with "●"
    lbl["text"] = ''.join(mot_en_cours)
    cnv.delete(ALL)
    cnv.create_image((width_img / 2, height_img / 2), image=images[-1])

    for btn in btns:
        btn["state"] = NORMAL

    nro = limite
    end = False


root = Tk()
root.title("Le jeu du pendu") ## Set game name
root.iconbitmap('data/graphics/logo.ico') ## Set game icon

limite = 7 ## Fail limit

images = [PhotoImage(file="data/graphics/pendu_"+str(nb_echecs)+".png") for nb_echecs in range(limite + 1)] ## Hangman pictures

fail = PhotoImage(file="data/graphics/wasted.png") ## Image "Wasted" if the game is lost
win = PhotoImage(file="data/graphics/win.png") ## Image "Mission Passed" if the game is won

## Definition of the images area

width_img = win.width()
height_img = win.height()

cnv = Canvas(
    root, width=width_img, height=height_img, highlightthickness=0)
cnv.grid(row=0, column=0, padx=20, pady=20)

## Text

lbl = Label(
    root, font=('Deja Vu Sans Mono', 45, 'bold'), width=23, fg="black")
lbl.grid(row=0, column=1)

## Replay button

reset = Button(root, text="Nouveau", font="Times 15 bold", command=init)
reset.grid(row=1, column=0)

## Letters buttons

lettres = Frame(root)
lettres.grid(row=1, column=1)

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
btns = []

for i in range(2):
    for j in range(10):
        btn = Button(
            lettres,
            text=ALPHA[10 * i + j],
            relief=FLAT,
            font='times 30')
        btn.grid(row=i, column=j)
        btn.bind("<Button-1>", choisir_lettre)
        btns.append(btn)

for j in range(6):
    btn = Button(
        lettres, text=ALPHA[20 + j], relief=FLAT, font='times 30')
    btn.grid(row=2, column=j + 2)
    btn.bind("<Button-1>", choisir_lettre)
    btns.append(btn)

## Words file
with open("data/liste_mots.txt") as f:
    arbres = f.read().split("\n")

init()

root.mainloop()
