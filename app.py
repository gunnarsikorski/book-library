from tkinter import *
import backend


def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    entry1.delete(0, END)
    entry1.insert(END, selected_tuple[1])
    entry2.delete(0, END)
    entry2.insert(END, selected_tuple[2])
    entry3.delete(0, END)
    entry3.insert(END, selected_tuple[3])
    entry4.delete(0, END)
    entry4.insert(END, selected_tuple[4])


def view_command():
    list1.delete(0, END)  # First makes sure it clears the output field of data
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    for row in backend.view():
        # END is where it will add the next row of data and so on
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    for row in backend.search(title_input.get(), author_input.get(), year_input.get(), isbn_input.get()):
        list1.insert(END, row)


def add_command():
    backend.insert(title_input.get(), author_input.get(),
                   year_input.get(), isbn_input.get())
    view_command()


def update_command():
    backend.update(selected_tuple[0], title_input.get(), author_input.get(), year_input.get(), isbn_input.get())


def delete_command():
    backend.delete(selected_tuple[0])


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

list1.bind('<<ListboxSelect>>', get_selected_row)

## BUTTONS ##

b1 = Button(window, text='View All', width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text='Search', width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text='Add Entry', width=12, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text='Update', width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text='Delete', width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text='Close', width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
