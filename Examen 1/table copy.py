from tkinter import *
from  tkinter import ttk
import pandas as pd

ws  = Tk()
ws.title('PythonGuides')
ws.geometry('500x500')
ws['bg'] = '#AC99F2'

game_frame = Frame(ws)
game_frame.place(x=0, y=0)
game_frame.config(height=500, width=500)

#scrollbar
 


my_game = ttk.Treeview(game_frame, selectmode ='browse')
my_game.pack(side='right')

# Constructing vertical scrollbar
# with treeview
horscrlbar = ttk.Scrollbar(game_frame,
                           orient ="horizontal",
                           command = my_game.yview)
 
# Calling pack method w.r.to vertical
# scrollbar
horscrlbar.pack(side ='bottom', fill ='x')
 
# Configuring treeview
my_game.configure(yscrollcommand = horscrlbar.set)

# Constructing vertical scrollbar
# with treeview
verscrlbar = ttk.Scrollbar(game_frame,
                           orient ="vertical",
                           command = my_game.yview)
 
# Calling pack method w.r.to vertical
# scrollbar
verscrlbar.pack(side ='right', fill ='x')
 
# Configuring treeview
my_game.configure(xscrollcommand = verscrlbar.set)





#game_scroll.config(command=my_game.yview)
#game_scroll.config(command=my_game.xview)

#define our column
df = pd.read_csv('airlines_final.csv')

my_game["columns"] = df.columns.values.tolist()
for x in range(len(df.columns.values)):
    my_game.column(df.columns.values[x], width=100)
    my_game.heading(df.columns.values[x], text=df.columns.values[x])


for index, row in (df.loc[::-1]).iterrows():
    my_game.insert("",0,text=index,values=list(row))



my_game.pack()


ws.mainloop()