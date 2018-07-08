from Tkinter import *#we use lot of Tkinter objects
window= Tk()# creates a blank window widgets go next
def lbs_conversion():
  #print(entry1_var.get())  #get method of the string var object to get string out of entry
  kilos= float(entry1_var.get())*0.4535
  ounces= float(entry1_var.get())*16.0
  grams= float(entry1_var.get())*453.5
  text1.insert(END,kilos)
  text2.insert(END,ounces)
  text3.insert(END,grams)
button1= Button(window,text= 'Run', command=lbs_conversion)
button1.pack()
#button1.Grid(row=0,column=0)
#button2=Button(window, text='Exit')
#button2.Pack(row=0, column=1)
entry1_var= StringVar()# stringvar object declaration is equal to variable entry1_var
#this variable will get the value from the entry widget
entry1= Entry(window, textvariable= entry1_var )#get value from here when user makes an entry
entry1.pack()
#entry1.Grid(row=0, column=1)
text1= Text(window,height=1, width=10)
text1.pack()
text2= Text(window, height=1, width=10)
text2.pack()
text3= Text(window, height=1, width=10)
text3.pack()
#text1.Grid(row=0,column=2)





window.mainloop()# enables the close button as user's wish, otherwise closes in split of a second
