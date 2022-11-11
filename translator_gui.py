# The base code is from https://www.tutorialspoint.com/taking-input-from-the-user-in-tkinter#
#Import the required Libraries
from tkinter import *
from tkinter import ttk
from urllib.request import urlopen
from bs4 import BeautifulSoup

#Create an instance of Tkinter frame
win= Tk()
win.title('Welcome to my Translator')

#Set the geometry of Tkinter frame
#win.geometry("750x250") -- from the original source code
window_width = 750
window_height = 300

#get the screen dimension
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

#find the center point
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

#set the position of the window to the center of the screen
win.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

#set the logo for the program
#win.iconbitmap('./directory_env/pumpkin.ico')
# win.tk.call('wm','iconphoto',win._w,PhotoImage(file='info.gif'))

def display_text():
   global entry
   string= entry.get()
   if (word)==1:
       response = urlopen("http://www.spanishdict.com/translate/" + string + "/")
       soup = BeautifulSoup(response.read(), "html.parser")
       #print(soup)
       results = soup.find("a", class_="YR6epHeU")
       label.configure(text=results.text)
   else:
       return (label.configure(text="Type only 1 word"))
   # elif len(string)>1:
   #    response = urlopen("http://www.spanishdict.com/translate/" + string + "/")
   #    soup = BeautifulSoup(response.read(), "html.parser")
   #    #print(soup)
   #    results = soup.find("a", class_="YR6epHeU")
   #    label.configure(text=results.text)


#Create an Entry widget to accept User Input
entry= Entry(win, width= 40, borderwidth=5)
entry.focus_set()
entry.pack(side=TOP)

#Create a Button to validate Entry Widget
Button_translate = ttk.Button(win, text= "translate",width= 20, command= display_text)
Button_translate.pack(pady=20,side=BOTTOM)
#pack(pady=20)

#Initialize a Label to display the User Input
label=Label(win, text="", font=("Courier 22 bold"))
label.place(relx =1, rely =1, anchor='s')
label.pack(side=BOTTOM)

win.mainloop()
