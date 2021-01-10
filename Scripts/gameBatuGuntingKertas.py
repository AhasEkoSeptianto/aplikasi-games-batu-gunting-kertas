from tkinter import *
import random

# inisiasi root window
root = Tk()
root.title('game batu gunting kertas')
root.geometry('450x550')

scoreuser = '0'
scorecomp = '0'

def user(dapat):
    user = int(dapat)
    comp = random.randint(0,2)
    game = ['batu','gunting','kertas']
    
    hasilgame = ''

    # logika hasil game
    if game[user] > game[comp] :
        if game[user] == 'kertas' and game[comp] == 'batu' :
            hasilgame = 'Win'
        else :
            hasilgame = 'Lost'
    if game[user] < game[comp]:
        if game[user] == 'batu' and game[comp] == 'kertas' :
            hasilgame = 'Lost'
        else :
            hasilgame = 'Win'
    
    if game[user] == game[comp]:
        hasilgame = 'Draw'

    # ubah gambar
    if game[user] == 'kertas':
        canvas1.itemconfig(canvasuser,image=imagekertas)
    elif game[user] == 'gunting':
        canvas1.itemconfig(canvasuser,image=imagegunting)
    elif game[user] == 'batu':
        canvas1.itemconfig(canvasuser,image=imagebatu)
    
    if game[comp] == 'kertas':
        canvas2.itemconfig(canvascomp,image=imagekertas)
    elif game[comp] == 'gunting':
        canvas2.itemconfig(canvascomp,image=imagegunting)
    elif game[comp] == 'batu':
        canvas2.itemconfig(canvascomp,image=imagebatu)
    
    # score set
    global scoreuser
    global scorecomp
    
    scoreuser = int(scoreuser)
    scorecomp = int(scorecomp)
    
    if hasilgame == 'Win':
        scoreuser = scoreuser + 1
        textscoreuser.configure(text=str(scoreuser))
    elif hasilgame == 'Draw':
        pass
    else :
        scorecomp = scorecomp + 1
        textscorecomp.configure(text=str(scorecomp))
    texttanding.configure(text=hasilgame)

# def text & button
text            = Label(root,text='pilih alat')
btnBatu         = Button(root,text='Batu',width=7, command=lambda : user('0'))
btnGunting      = Button(root,text='Gunting',width=7 ,command=lambda : user('1'))
btnKertas       = Button(root,text='Kertas',width=7, command=lambda : user('2'))

# def text score
textscoreuser   = Label(root,text='user : ' + scoreuser)
textscorecomp   = Label(root,text='computer : ' + scorecomp)

texttanding     = Label(root,text='tanding')
textvs          = Label(root,text='VS')
txtuser         = Label(root,text='user')
txtcomputer     = Label(root,text='computer')

# def img
canvas1         = Canvas(root, width=200, height=200)
canvas2         = Canvas(root, width=200, height=200)
imagebatu       = PhotoImage(file="img/batu.png")
imagegunting    = PhotoImage(file="img/gunting.png")
imagekertas     = PhotoImage(file="img/kertas.png")

canvasuser      = canvas1.create_image(20,20,anchor=NW,image=imagebatu)
canvascomp      = canvas2.create_image(20,20,anchor=NW,image=imagebatu)

# place
text.place(relx=0.5,y=40,anchor=CENTER)

# btn place
btnBatu.place(relx=0.3,y=100, anchor=CENTER)
btnGunting.place(relx=0.5,y=100,anchor=CENTER)
btnKertas.place(relx=0.7,y=100,anchor=CENTER)

# text tanding
texttanding.place(relx=0.5,rely=0.4,anchor=CENTER)

# show score
textscoreuser.place(rely=0.4,x=80,anchor=CENTER)
textscorecomp.place(rely=0.4,x=360,anchor=CENTER)

# txt vs
textvs.place(relx=0.5,rely=0.8,anchor=CENTER)

# show img
canvas1.place(x=70,rely=0.8,anchor=CENTER)
txtuser.place(x=70,rely=0.6,anchor=CENTER)


canvas2.place(x=350,rely=0.8,anchor=CENTER)
txtcomputer.place(x=350,rely=0.6,anchor=CENTER)

root.resizable(0,0)
root.mainloop()
