#pip install pandas (in cmd to use dataframes) 
from pydoc_data.topics import topics
import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import time
import pandas as pd
from pandas.core.base import NoNewAttributesMixin 
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
import matplotlib
from os import listdir
import pytest


matplotlib.rcParams['axes.edgecolor'] = 'white'     #globally changes the color of axis to white

#function to add data to an excel file
def add(name,time,lives):
    global file
    lives=abs(lives)
    database=pd.read_excel('Files\\highscore.xlsx','Sheet1')
    scores=round(lives/time*10,2)                                    #score is lives divided by time into 10
    if name == '':                                          #incase the user doesn't enter a name
        name='Player '+str(len(database)+1)
    database.loc[len(database.index)] = [name,time,lives,scores]  
    database.to_excel('Files//highscore.xlsx',index=False)

#function to record the time taken to beat the game
def timing(t1,t2): 
      if t1>t2:
          t1,t2=t2,t1
      return round(t2-t1,2)

valid_game=False

#=================================================================================================

root1=Tk()
root1.title('Hangman')
root1.geometry('800x600')
f1=Frame(root1)
#================================================================================================
#HighScore
def Highscore() :
    database=pd.read_excel('Files\\highscore.xlsx')       
    database['Comparitive Score']=round(database['Score']-database['Score'].mean(),2) #compares with average
    sorted_database=database.sort_values(by=['Score'],ascending=False)

    score=Tk()
    score.title('Highscore')
    l=tk.Label(score,text=sorted_database.to_string(index=False),padx=50,pady=0,bg='#003333', fg='#ff0',bd=10,font=('Helvetica',20,'bold'))
    l.pack()
    score.mainloop()
#==================================================================================================
#Main_Game
def Main_Game():
    global valid_game
    valid_game = True
    root1.destroy()

#==================================================================================================
#topics

#takes a random topic as default if no topic is selected from start screen
topic_count=0
topics_list=listdir('Files\\topics')
topic_file='Files\\topics\\'+random.choice(topics_list)
file = open(topic_file,'r')

#selecting topic using button


def top():
      global topic_count
      global file1
      global topic

      topic_count+=1
      topics_list=listdir('Files\\topics')
      count=len(topics_list)
      topic=topics_list[topic_count]
      
      if topic_count == count:
            topic_count=0
      
      b3.config(text=topic[:-4])
      
      topic_file='Files\\topics\\'+topic
      file1 = open(topic_file,'r')
      return file1





#==================================================================================================
#Statistics

  
def stats():
    def plot():
        database=pd.read_excel('Files\\highscore.xlsx','Sheet1')
        # the figure that will contain the plot
        fig =Figure(figsize = (25,5),facecolor='#003333')

        #data
        x = database.Name.head(4)
        y1= database['Score'].sort_values(ascending=False).head(4)
        y2= database['Time'].sort_values(ascending=True).head(4)
        y3= database['Lives'].sort_values(ascending=False).head(4)
        x4=['Avg','Max','Min','Median']
        y4= [y1.mean(),y1.max(),y1.min(),y1.median()]
        #y4= database['Comparitive Score']
        # adding the subplot
        plot1 = fig.add_subplot(141)
        plot1.set_ylim(y1.min()-1,y1.max()+1)
        plot1.set_title('HIGHSCORE',color='white')
        plot1.set_xlabel('NAMES',color='white')     #x axis label
        plot1.set_ylabel('SCORE',color='white')     #y axis label
        plot1.set_facecolor('#003333')              #change background color
        plot1.tick_params(axis='both', colors='white')  #change value color


        plot2 = fig.add_subplot(142)
        plot2.set_ylim(y2.min()-1,y2.max()+1)
        plot2.set_title('BEST TIME',color='white')
        plot2.set_xlabel('NAMES',color='white')     #x axis label
        plot2.set_ylabel('TINME',color='white')      #y axis label
        plot2.set_facecolor('#003333')              #chagne background color
        plot2.tick_params(axis='both', colors='white')  #change values color

        plot3 = fig.add_subplot(143)
        plot3.set_ylim(y3.min()-1,y3.max()+1)
        plot3.set_title('LIVES',color='white')
        plot3.set_xlabel('NAMES',color='white')     #x axis label
        plot3.set_ylabel('LIVES',color='white')     #y axis label
        plot3.set_facecolor('#003333')              #change background color
        plot3.tick_params(axis='both', colors='white')  #change value color

        plot4 = fig.add_subplot(144)
        plot4.set_title('STATISTICS',color='white')
        plot4.set_xlabel('STATS',color='white')     #x axis label
        plot4.set_ylabel('SCORE',color='white')     #y axis label
        plot4.set_facecolor('#003333')              #change background color
        plot4.tick_params(axis='both', colors='white')  #change value color
        #setting colors of bar graphs
        colors1,colors2,colors3,colors4=[],[],[],[]
        for i in range(len(database.Name.head(4))):
            colors1.append(np.random.rand(3,))
            colors2.append(np.random.rand(3,))
            colors3.append(np.random.rand(3,))
            colors4.append(np.random.rand(3,))

        # plotting the graph
        plot1.bar(x,y1,color=colors1)
        plot2.bar(x,y2,color=colors2)
        plot3.bar(x,y3,color=colors3)
        plot4.bar(x4,y4,color=colors4)

        # creating the Tkinter canvas
        # containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(fig,
                                master = window)  
        canvas.draw()
    
        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().pack()

    # the main Tkinter window
    window = Tk()
    window.config(bg='#003333')  
    # setting the title 
    window.title('Plotting in Tkinter')
    
    # dimensions of the main window
    window.geometry("2000x500")
    
    # button that displays the plot
    plot_button = Button(master = window,command = plot,text = "Plot",padx=50,pady=0,bg='#339966',\
    bd=10,font=('Helvetica',10,'bold'))
    
    # place the button 
    # in main window
    plot_button.pack()
    
    # run the gui
    window.mainloop()
#==================================================================================================
#Functions

def quit() :
    global valid_game
    valid_game = False
    root1.destroy()

#==================================================================================================

#Starting Screen Label

Title_img= PhotoImage(file='Media\\Hangman.png')
#---------------------------------------------------------------------------------------------------

Label=Label(root1,                          #add image here later
            bg='#003333',image=Title_img,
            bd=10,
            font=('Arial',10,'bold'))


Label.place(relx=0.5,rely=0.2, anchor=CENTER)

#==================================================================================================

#starting screen buttons

b1=Button(root1,text='Start Game',padx=50,pady=0,bg='#339966',bd=10,font=('Helvetica',10,'bold'),command=Main_Game)
b1.place(relx=0.5, rely=0.5, anchor=CENTER)

b2=Button(root1,text='HighScore',padx=50,pady=0,bg='#339966',bd=10,font=('Helvetica',10,'bold'),command=Highscore)
b2.place(relx=0.5, rely=0.6, anchor=CENTER)

b3=Button(root1,text='Topics',padx=50,pady=0,bg='#339966',bd=10,font=('Helvetica',10,'bold'),command=top)
b3.place(relx=0.5, rely=0.7, anchor=CENTER)

b4=Button(root1,text='QUIT',padx=50,pady=0,bg='Red',bd=10,font=('Helvetica',10,'bold'),command=quit)
b4.place(relx=0.5, rely=0.9, anchor=CENTER)

b5=Button(root1,text='Statistics',padx=50,pady=0,bg='#339966',bd=10,font=('Helvetica',10,'bold'),command=stats)
b5.place(relx=0.5, rely=0.8, anchor=CENTER)

root1.config(bg='#003333')

root1.mainloop()
#======================================================================================================================

if valid_game is True: #if quit is clicked on the main game valid game is made false and the rest of the game wont start
    #Getting Names

    namewindow=Tk()
    namewindow.config(bg='#003333')
    namewindow.title('ENTER NAME')
    namewindow.geometry('600x300')

    e1=Entry(namewindow,bg='#004d4d',fg='white',bd=8,font=('Helvetica',20,'bold'))
    e1.place(relx=0.5,rely=0.4,anchor=CENTER)

    def get_name():
        global name
        name=e1.get()


    button1=Button(namewindow,text='Enter Name',padx=50,pady=0,bg='#339966',bd=10,font=('Helvetica',10,'bold'),command=lambda : [get_name(),namewindow.destroy()])
    button1.place(relx=0.5,rely=0.6,anchor=CENTER)



    namewindow.mainloop()
    #======================================================================================================================

    #MAIN GAME
    score = 0
    run = True
    lives=6
    Chosen_Topic = file1.readlines()
    # main loop
    while run:
        t1=time.time()
        root = Tk()
        root.geometry('905x700')
        root.title('HANG MAN')
        root.config(bg = '#003333')
        count = 0
        win_count = 0

        # choosing word

        selected_word = random.choice(Chosen_Topic).strip('\n').lower()
        topic_label=tk.Label(root,text='Topic: '+topic[:-4],bg='#004d4d',fg='white',bd=8,font=('Helvetica',20,'bold'))
        topic_label.place(x=0,y=150)
      
        # creation of word dashes variables
        x = 250
        for i in range(0,len(selected_word)):
            x += 60
            exec('d{}=tk.Label(root,text="_",bg="#E7FFFF",font=("arial",40))'.format(i))
            exec('d{}.place(x={},y={})'.format(i,x,450))
            
        #letters icon
        al = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for let in al:
            exec('{}=PhotoImage(file="Media//{}.png")'.format(let,let))
            
        # hangman images
        h123 = ['h1','h2','h3','h4','h5','h6','h7']
        for hangman in h123:
            exec('{}=PhotoImage(file="Media\\{}.png")'.format(hangman,hangman))
            
        #letters placement
        button = [['b1','a',0,595],['b2','b',70,595],['b3','c',140,595],['b4','d',210,595],['b5','e',280,595],['b6','f',350,595],['b7','g',420,595],['b8','h',490,595],['b9','i',560,595],['b10','j',630,595],['b11','k',700,595],['b12','l',770,595],['b13','m',840,595],['b14','n',0,645],['b15','o',70,645],['b16','p',140,645],['b17','q',210,645],['b18','r',280,645],['b19','s',350,645],['b20','t',420,645],['b21','u',490,645],['b22','v',560,645],['b23','w',630,645],['b24','x',700,645],['b25','y',770,645],['b26','z',840,645]]

        for q1 in button:
            
            exec('{}=Button(root,bd=0,command=lambda:check("{}","{}"),bg="#E7FFFF"\
            ,activebackground="#E7FFFF",font=10,image={})'.format(q1[0],q1[1],q1[0],q1[1]))

            exec('{}.place(x={},y={})'.format(q1[0],q1[2],q1[3]))
            
        #hangman placement
        han = [['c1','h1'],['c2','h2'],['c3','h3'],['c4','h4'],['c5','h5'],['c6','h6'],['c7','h7']]
        for p1 in han:
            exec('{}=tk.Label(root,bg="#E7FFFF",image={})'.format(p1[0],p1[1])) 

        # placement of first hangman image ``
        c1.place(x = 200,y = 0)       #not sure why its -50 but removing it messes with the image placement
        
        # exit buton
        def close():
            global run
            global valid_game
            answer = messagebox.askyesno('ALERT','YOU WANT TO CLOSE WINDOW')
            if answer == True:
                run = False
                valid_game=False
                root.destroy()
                
        e1 = PhotoImage(file = 'Media\\exit.png')
        ex = Button(root,bd = 0,command = close,bg="#E7FFFF",activebackground = "#E7FFFF",font = 10,image = e1)
        ex.place(x=770,y=10)

        # button press check function
        def check(letter,button):
            global count,win_count,run,score,lives,t2
            exec('{}.destroy()'.format(button))
            if letter in selected_word:
                for i in range(0,len(selected_word)):
                    if selected_word[i] == letter:
                        win_count += 1
                        exec('d{}.config(text="{}")'.format(i,letter.upper()))
                if win_count == len(selected_word):
                    t2=time.time() 
                    score += 1
                    answer = messagebox.askyesno('GAME OVER','YOU WON!\nWANT TO PLAY AGAIN?')
                    if answer == True:
                        run = True
                        root.destroy()   
                    else:
                        run = False
                        root.destroy()
            else:
                count += 1
                lives -=1
                exec('c{}.destroy()'.format(count))
                exec('c{}.place(x={},y={})'.format(count+1,200, 0))    # why is it -50 and why do the dashes disappear on making it positive
                if count == 6: 
                    valid_game=False
                    answer = messagebox.askyesno('GAME OVER','YOU LOST!\nTHE WORD IS {}\nWANT TO PLAY AGAIN?'.format(selected_word.upper()))
                    if answer == True:
                        run = True
                        score = 0
                        root.destroy()
                    else:
                        run = False
                        root.destroy()
                    
                
        root.mainloop()
    

if valid_game is True:
      add(name,timing(t1,t2),lives)#add a way to calculate lives and replace the 2 with the variable for that


