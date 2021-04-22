from tkinter import *
import backend

window = Tk()
window.title('Book Library')

## INPUT LABELS ##

label1 = Label(window, text='Title')
label1.grid(row=0, column=0)

label2 = Label(window, text='Author')
label2.grid(row=0, column=2)

label3 = Label(window, text='Year')
label3.grid(row=1, column=0)

label4 = Label(window, text='ISBN')
label4.grid(row=1, column=2)


## INPUT FIELDS ##

title_input = StringVar()
entry1 = Entry(window, textvariable=title_input)
entry1.grid(row=0, column=1)

author_input = StringVar()
entry2 = Entry(window, textvariable=author_input)
entry2.grid(row=0, column=3)

year_input = StringVar()
entry3 = Entry(window, textvariable=year_input)
entry3.grid(row=1, column=1)

isbn_input = StringVar()
entry4 = Entry(window, textvariable=isbn_input)
entry4.grid(row=1, column=3)


## OUTPUT FIELD ##

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)


## SCROLLBAR ##

sb = Scrollbar(window)
sb.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb.set)
sb.configure(command=list1.yview)


## BUTTONS ##

b1 = Button(window, text='View All', width=12)
b1.grid(row=2, column=3)

b2 = Button(window, text='Search', width=12)
b2.grid(row=3, column=3)

b3 = Button(window, text='Add Entry', width=12)
b3.grid(row=4, column=3)

b4 = Button(window, text='Update', width=12)
b4.grid(row=5, column=3)

b5 = Button(window, text='Delete', width=12)
b5.grid(row=6, column=3)

b6 = Button(window, text='Close', width=12)
b6.grid(row=7, column=3)

window.mainloop()
