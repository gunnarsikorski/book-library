from tkinter import *

window = Tk()

label1 = Label(window, text = 'Title')
label1.grid(row=0, column=0)

label2 = Label(window, text = 'Author')
label2.grid(row=0, column=2)

label3 = Label(window, text = 'Year')
label3.grid(row=1, column=0)

label4 = Label(window, text = 'ISBN')
label4.grid(row=1, column=2)


title_input = StringVar()
entry1 = Entry(window, textvariable = title_input)
entry1.grid(row=0, column=1)

author_input = StringVar()
entry2 = Entry(window, textvariable = author_input)
entry2.grid(row=0, column=3)

year_input = StringVar()
entry3 = Entry(window, textvariable = year_input)
entry3.grid(row=1, column=1)

isbn_input = StringVar()
entry4 = Entry(window, textvariable = isbn_input)
entry4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb = Scrollbar(window)
sb.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb.set)
sb.configure(command=list1.yview)

window.mainloop()
