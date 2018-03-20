
from tkinter import *

import random

class Game:

    def __init__(self,root):

        self.root= root
        root.configure(background='white')
        root.resizable(width=800, height=600)
        root.rowconfigure(3, {'minsize': 30})
        root.columnconfigure(3, {'minsize': 30})

        menubar = Menu(root)
        root.config(menu=menubar)

        menubar.add_command(label="New Game", command=self.deal)

        menubar.add_command(label="Quit!", command=self.quitATM)

        self.label= Label(root, text="Welcome to the Python Memory Game",font="bold",bg="white")

     ########################################### Memory cards GUI ################################################

        self.card1_a= Button(root, text="1",fg="gray",activebackground="blue",command=self.card1a)
        self.card1_a.config( height = 20, width = 25 )


        self.card1_b=Button(root,text="1b",fg="green")
        self.card1_b.config( height = 20, width = 25)


      ############################################## sets out the cards on the table ##################################
    def RemoveAll(self):

        self.card1_b.grid_remove()
        self.card1_a.grid_remove()

        self.card1a()

    def randomize (self):

        self.label.grid(row=0,column=2)
        root.resizable(width=800, height=600)
    # #column number random generator
        c=(1,2,3)
        global x
        x= random.sample(c,3)
        #print ("x",x)

    #row number random generator
        r=(1,2)
        global y
        y= random.sample(r,2)
        #print ("y",y)
        return x,y


##################################### when card is clicked on ##########################################################
    def card_reveal(self):

        self.randomize()

        global info
        info=self.card1_a.grid_info()

        global y
        y=int(info["row"])

        global x
        x=int(info["column"])

        self.card1_b.grid(row=y,column=x,padx=(10,10),pady=(10,10))

    def deal(self):

        #first deal
        self.RemoveAll()
        self.randomize()

        print (x,y)
        root.resizable(width=800, height=600)

        self.card1_a.grid(row=y[1],column=x[0],padx=(10,10),pady=(10,10))
        self.card1_b.grid(row=y[1],column=x[1],padx=(10,10),pady=(10,10))
        #
        # self.card2_a.grid(row=y[0],column=x[1],padx=(10,10),pady=(10,10))
        # self.card2_b.grid(row=y[0],column=x[2],padx=(10,10),pady=(10,10))
        # #
        # self.card3_a.grid(row=y[1],column=x[2],padx=(10,10),pady=(10,10))
        # self.card3_b.grid(row=y[0],column=x[0],padx=(10,10),pady=(10,10))

    def card1a(self):

        pass
        # info=self.card1_a.grid_info()
        #
        # print(info)
        # #
        # y=int(info["row"])
        # x=int(info["column"])
        # self.card1_a= Button(root, text="1",fg="black",bg="blue",relief=SUNKEN)
        #
        # self.card1_a.grid(row=y,column=x,padx=(10,10),pady=(10,10))
        # self.card1_a.config( height = 20, width = 25 )
        #
        #


        # self.card1_b=Button(root,text="1b",fg="green")
        # self.card1_b.grid(row=y,column=x,padx=(10,10),pady=(10,10))
        # self.card1_b.config( height = 20, width = 25)
        #
        # info=self.card2_a.grid_info()
        # print (x,y)
        # self.card2_a=Button(root,text="1b",fg="green")
        # self.card2_a.grid(row=y,column=x,padx=(10,10),pady=(10,10))
        # self.card2_a.config( height = 20, width = 25)
        #
        # info=self.card2_b.grid_info()
        # self.card2_b=Button(root,text="1b",fg="green")
        # self.card2_b.grid(row=y,column=x,padx=(10,10),pady=(10,10))
        # self.card2_a.config( height = 20, width = 25)
        #
        # info=self.card3_a.grid_info()
        #
        # self.card3_a=Button(root,text="1b",fg="green")
        # self.card3_a.grid(row=y,column=x,padx=(10,10),pady=(10,10))
        # self.card2_a.config( height = 20, width = 25)
        #
        #
        # info=self.card3_b.grid_info()
        # self.card3_b=Button(root,text="1b",fg="green")
        # self.card3_b.grid(row=y,column=x,padx=(10,10),pady=(10,10))
        # self.card2_a.config( height = 20, width = 25)

    def quitATM(self):
        self.root.quit
        sys.exit(0)

#class Shuffle (Game):










root=Tk()
GAME= Game(root)
root.mainloop()
