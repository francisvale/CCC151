from tkinter import *
from tkinter import ttk
import csv

root = Tk()
root.geometry("720x440")
root.title("Student Information System")

# create style
style = ttk.Style()
style.theme_use("clam")

# Frame for TreeView and scroll
tree_frame = Frame(root)
tree_frame.pack(pady=10)

# scroll
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)


# Functions
def display_data():
    with open('student.csv', 'r') as displayFile:
        display = csv.reader(displayFile)

        next(display)
        delete_all()

        for line in display:
            my_tree.insert(parent='', index='end', iid=line[0], text='',
                           values=(line[0], line[1], line[2], line[3], line[4]))


def delete_all():
    for record in my_tree.get_children():
        my_tree.delete(record)


def add():
    flag = 0
    with open('student.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            if id_number.get() == row[0]:
                flag += 1
                error_messages.config(text='ID number already existed.')
    if flag < 1 and id_number.get() != "":
        with open('student.csv', 'a', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow([id_number.get(), name_entry.get(),
                             course_entry.get(), year_entry.get(), gender_entry.get()])
            error_messages.config(text='')
    if id_number.get() == '':
        error_messages.config(text='Please put an ID number.')

    display_data()

    id_number.delete(0, END)
    name_entry.delete(0, END)
    course_entry.delete(0, END)
    year_entry.delete(0, END)
    gender_entry.delete(0, END)


def remove_one():
    selection = my_tree.selection()
    lines = list()
    with open("Student.csv", "r") as file:
        reader = csv.reader(file)
        for line in reader:
            lines.append(line)
            if line[0] in selection:
                lines.remove(line)
    with open("Student.csv", "w", newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
    display_data()
    error_messages.config(text='')


def edit():
    flag = 0
    selected = my_tree.focus()
    lines_test = list()
    with open('student.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines_test.append(row)
            if row[0] == selected:
                lines_test.remove(row)
    for data in lines_test:
        if data[0] == id_number.get():
            flag += 1
            error_messages.config(text='ID number already existed.')

    lines = list()
    members = my_tree.focus()
    count = 0
    with open('student.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            if row[0] == members and id_number.get() != '':
                if flag < 1:
                    lines.remove(row)
                    lines.insert(count, [id_number.get(), name_entry.get(),
                                         course_entry.get(), year_entry.get(), gender_entry.get()])
                    error_messages.config(text='')
            count += 1
    with open('student.csv', 'w', newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
    if id_number.get() == '':
        error_messages.config(text='Please put an ID number.')

    display_data()

    id_number.delete(0, END)
    name_entry.delete(0, END)
    course_entry.delete(0, END)
    year_entry.delete(0, END)
    gender_entry.delete(0, END)


def select():
    id_number.delete(0, END)
    name_entry.delete(0, END)
    course_entry.delete(0, END)
    year_entry.delete(0, END)
    gender_entry.delete(0, END)

    selected = my_tree.focus()
    values = my_tree.item(selected, 'values')

    # output selected values
    id_number.insert(0, values[0])
    name_entry.insert(0, values[1])
    course_entry.insert(0, values[2])
    year_entry.insert(0, values[3])
    gender_entry.insert(0, values[4])

    error_messages.config(text='')


def back(event):
    display_data()
    error_messages.config(text='')


def search(event):
    for record in my_tree.get_children():
        my_tree.delete(record)

    x = search_entry.get()

    with open('student.csv', "r") as f:
        reader_file = csv.reader(f)

        for items in reader_file:
            for element in items:
                if x in element:
                    my_tree.insert(parent='', index='end', iid=items[0], values=items)
                    break
    error_messages.config(text='')


def search2():
    for record in my_tree.get_children():
        my_tree.delete(record)

    x = search_entry.get()

    with open('student.csv', "r") as f:
        reader_file = csv.reader(f)

        for items in reader_file:
            for element in items:
                if x in element:
                    my_tree.insert(parent='', index='end', iid=items[0], values=items)
                    break
    error_messages.config(text='')


def update(data):
    my_tree.delete(0, END)

    for item in data:
        my_tree.insert(END, item)


def deselect():
    id_number.delete(0, END)
    name_entry.delete(0, END)
    course_entry.delete(0, END)
    year_entry.delete(0, END)
    gender_entry.delete(0, END)


def sort_name():
    lines = list()
    with open('student.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        next(reader)
        for row in reader:
            lines.append(row)

    for i in range(1, len(lines)):
        count = 0
        for j in range(0, len(lines) - 1):
            if lines[j][1] > lines[j + 1][1]:
                lines[count], lines[count + 1] = lines[count + 1], lines[count]
            count += 1
    lines.insert(0, ["ID Number", "Name", "Course", "Year Level", "Gender"])
    with open('student.csv', 'w', newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
    display_data()


def sort_id():
    lines = list()
    with open('student.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        next(reader)
        for row in reader:
            lines.append(row)

    for i in range(1, len(lines)):
        count = 0
        for j in range(0, len(lines) - 1):
            if lines[j][0] > lines[j + 1][0]:
                lines[count], lines[count + 1] = lines[count + 1], lines[count]
            count += 1
    lines.insert(0, ["ID Number", "Name", "Course", "Year Level", "Gender"])
    with open('student.csv', 'w', newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
    display_data()


def sort_course():
    lines = list()
    with open('student.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        next(reader)
        for row in reader:
            lines.append(row)

    for i in range(1, len(lines)):
        count = 0
        for j in range(0, len(lines) - 1):
            if lines[j][2] > lines[j + 1][2]:
                lines[count], lines[count + 1] = lines[count + 1], lines[count]
            count += 1
    lines.insert(0, ["ID Number", "Name", "Course", "Year Level", "Gender"])
    with open('student.csv', 'w', newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
    display_data()


def sort_gender():
    lines = list()
    with open('student.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        next(reader)
        for row in reader:
            lines.append(row)

    for i in range(1, len(lines)):
        count = 0
        for j in range(0, len(lines) - 1):
            if lines[j][4] > lines[j + 1][4]:
                lines[count], lines[count + 1] = lines[count + 1], lines[count]
            count += 1
    lines.insert(0, ["ID Number", "Name", "Course", "Year Level", "Gender"])
    with open('student.csv', 'w', newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
    display_data()


# Add TreeView
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)

# Defining Columns
my_tree['columns'] = ('ID number', 'Name', 'Course', 'Year Level', 'Gender')

# Formatting Column
my_tree.column("#0", stretch=NO, width=0)
my_tree.column("ID number", width=120, anchor=W)
my_tree.column("Name", width=170, anchor=W)
my_tree.column("Course", width=100, anchor=W)
my_tree.column("Year Level", width=110, anchor=W)
my_tree.column("Gender", width=120, anchor=W)

# Create Headings
my_tree.heading("ID number", text='ID Number', command=sort_id, anchor=W)
my_tree.heading("Name", text='Name', command=sort_name, anchor=W)
my_tree.heading("Course", text='Course', command=sort_course, anchor=W)
my_tree.heading("Year Level", text='Year Level', command=sort_id, anchor=W)
my_tree.heading("Gender", text='Gender', command=sort_gender, anchor=W)

# Add Data CSV
display_data()

# Display TreeView
my_tree.pack()

# configure scrollbar
tree_scroll.config(command=my_tree.yview)

# Frame for record entries
add_container = LabelFrame(root, text="Record", padx=4, pady=5)
add_container.pack(pady=10)
# Frame for actions
add_container2 = LabelFrame(root, text="Actions", padx=56, pady=5)
add_container2.pack()

# Labels
index = Label(root, text='')
index.pack()

error_messages = Label(root, text='', fg="red")
error_messages.pack()

il = Label(add_container, text="ID Number")
il.grid(row=0, column=0)

nl = Label(add_container, text="Name")
nl.grid(row=0, column=1)

cl = Label(add_container, text="Course")
cl.grid(row=0, column=2)

yl = Label(add_container, text="Year Level")
yl.grid(row=0, column=3)

gl = Label(add_container, text="Gender")
gl.grid(row=0, column=4)

search_btn = Button(add_container2, text='Search', command=search2)
search_btn.grid(row=0, column=6)

# Inputs
id_number = Entry(add_container, borderwidth=2)
id_number.grid(row=1, column=0)

name_entry = Entry(add_container, borderwidth=2)
name_entry.grid(row=1, column=1)

course_entry = Entry(add_container, borderwidth=2)
course_entry.grid(row=1, column=2)

year_entry = Entry(add_container, borderwidth=2)
year_entry.grid(row=1, column=3)

gender_entry = Entry(add_container, borderwidth=2)
gender_entry.grid(row=1, column=4)

search_entry = Entry(add_container2, borderwidth=2)
search_entry.grid(row=0, column=5, padx=10)

# Buttons
add_entry = Button(add_container2, text="Add", command=add)
add_entry.grid(row=0, column=0, padx=10)

modify_entry = Button(add_container2, text="Modify", command=edit)
modify_entry.grid(row=0, column=1, padx=10)

remove_one = Button(add_container2, text='Remove', command=remove_one)
remove_one.grid(row=0, column=2, padx=10)

select_record = Button(add_container2, text='Select', command=select)
select_record.grid(row=0, column=3, padx=10)

deselect_record = Button(add_container2, text='Deselect', command=deselect)
deselect_record.grid(row=0, column=4, padx=10)

# Create a binding for the search box
search_entry.bind("<KeyPress>", back)
search_entry.bind("<Return>", search)

root.mainloop()
