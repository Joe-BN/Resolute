# Library Imports {Remember}
import customtkinter as ct
from customtkinter import *
import tkinter as tk
from tkinter import * 
from tkinter import ttk
import tkinter.messagebox
from time import strftime
import time


# Intializing Main Window
root = ct.CTk()
root.geometry("600x500")
root.resizable(False, False)
root.title("Resolute")


# Predetermined Theme Settings
ct.set_appearance_mode("System")
ct.set_default_color_theme("blue") 

# Variables
title = "Home   "
common_bg="#444242"
datetoday = strftime('%x')
count = 0

# Arrays
tasks = []

# Functions:   
    # Get date
def get_date_today():
    datetoday = strftime('%x')
    print("Gotten the date: "+str(datetoday))

    # Pages
def home_page():
    home_frame=CTkFrame(root, height=472, width=600,
                        border_color="black", border_width=1)
    home_frame.place(y=27)
    # Show time, day & date
        # Time
    def my_time():
        time_string = strftime('%H:%M:%S %p \n %x')
        l1.configure(text=time_string)
        l1.after(1000,my_time) 
    my_font=('times',100,'bold') 
    l1=CTkLabel(home_frame,font=my_font,height=100, width=300,
                text_color="black")
    l1.place(x=20,y=40)
    my_time()
        # Day
    
        # Date
    
    # Welcome
    welcome = CTkLabel(home_frame, text="Welcome !",
                       font=('New Roman',35))
    welcome.place(x=400,y=340)

    # Button

    
    
        # Tasks Frame
def tasks_page():
    #counts = 0
    #def count_4_today(cause):
        #if cause == "unmark":
        #    counts -= 1
       # elif cause == "mark":
      #      counts += 1
     #   print(counts)
    #count += counts

    tasks_frame=CTkFrame(root, height=472, width=600,
                         border_color="green", border_width=1)
    tasks_frame.place(y=27)
    # Input box
    entry = CTkEntry(tasks_frame, width=250, height=25)
    entry.place(x=25, y=25)

    def add_task():
        task = entry.get()
        if task:
            if task in tasks:
                print("Already added")
            else:
                tasks.append(task)
            print(tasks)
        else:
            tk.messagebox.showwarning(title="Error", message="Must input a task so as to add one",
                                      )
    def add():
        input_text=entry.get()
        if input_text=="":
            tk.messagebox.showwarning(title="Warning!",message="Please Enter some Text")
        else:
            listbox_task.insert(END,input_text)
            #close the root1 window
        entry.delete(0, END)
    # Deletes tasks from the list
    def deletetask():
        selected=listbox_task.curselection()
        if selected:
            listbox_task.delete(selected[0])
        else:
            tk.messagebox.showwarning(title="Error !",message="Item must first be selected !")

    #Executes this to mark completed tasks
    def markcompleted():
        marked=listbox_task.curselection()
        if marked:
            temp=marked[0]
            #store the text of selected item in a string
            temp_marked=listbox_task.get(marked)
            if "|✔|" and "/~/" not in temp_marked:
                # change it
                temp_marked=temp_marked+"  |✔|"
                # delete it then replace it 
                listbox_task.delete(temp)
                listbox_task.insert(temp,temp_marked)
                #count_4_today("mark")
            else:
                tk.messagebox.showwarning(title="Error !",message="Item is already checked !")
        else:
            tk.messagebox.showwarning(title="Error !",message="Task must first be selected")

        #Executes this to mark completed tasks
    def unmarkcompleted():
        marked=listbox_task.curselection()
        if marked:
            temp=marked[0]
            #store the text of selected item in a string
            temp_marked=listbox_task.get(marked)
            if "|✔|" in temp_marked:
                # change it
                temp_marked=temp_marked.replace("  |✔|","")
                # delete it then replace it 
                listbox_task.delete(temp)
                listbox_task.insert(temp,temp_marked)
                #count_4_today("unmark")
            else:
                tk.messagebox.showwarning(title="Error !",message="Item is not checked !")
        else:
            tk.messagebox.showwarning(title="Error !",message="Task must first be selected")
    def partially_done():
        print("Do finish this asap !")
        marked=listbox_task.curselection()
        if marked:
            temp=marked[0]
            #store the text of selected item in a string
            temp_marked=listbox_task.get(marked)
            if "|✔|" not in temp_marked:
                if "|~|" not in temp_marked:
                    # change it
                    temp_delayed=temp_marked+"  |~|"
                    # delete it then replace it 
                    listbox_task.delete(temp)
                    listbox_task.insert(temp,temp_delayed)
                    #count_4_today("mark")
                elif "|~|" in temp_marked:
                    tk.messagebox.showwarning(title="Error !",message="Item is already set to Partially done !")
            elif "|✔|" in temp_marked:
                tk.messagebox.showwarning(title="Error !",message="Item is already checked !")
        else:
            tk.messagebox.showwarning(title="Error !",message="Task must first be selected")


    # Input Button
    taskinput_btn = CTkButton(tasks_frame, text=" Add ",
                             command=lambda:[add_task(), add()],
                             height=20, width=50, corner_radius=5)
    taskinput_btn.place(x=225,y=60)

    # List box
    frame_task=CTkFrame(tasks_frame, height=10,width=64)
    frame_task.place(x=2, y=100)

    listbox_task=Listbox(frame_task,bg="#282727",fg="white",
                        height=10,width=64,font = "Helvetica")  
    listbox_task.pack(side=tk.LEFT)
    scrollbar_task=CTkScrollbar(frame_task)
    scrollbar_task.pack(side=ct.RIGHT,fill=ct.Y)
    listbox_task.configure(yscrollcommand=scrollbar_task.set)
    scrollbar_task.configure(command=listbox_task.yview)

    # Other functional buttons
    delete_button=CTkButton(tasks_frame,text="Delete selected task",width=50,
                            height=20,command=deletetask)
    delete_button.place(x=10, y= 400)
    mark_button=CTkButton(tasks_frame,text="Mark as Complete ",width=50,
                          height=20,command=markcompleted)
    mark_button.place(x=10,y=430)
    unmark_button=CTkButton(tasks_frame,text="Undo Mark",width=50,
                          height=20,command=unmarkcompleted)
    unmark_button.place(x=140,y=430)
    partial_button=CTkButton(tasks_frame, text="Partially Done",
                            command=lambda:[partially_done()])
    partial_button.place(x=250,y=430) 




def schedule_page():
    schedule_frame=CTkFrame(root, height=472, width=600,
                         border_color="blue", border_width=1)
    schedule_frame.place(y=27)

    welcome = CTkLabel(schedule_frame, text="Welcome to the schedule page !",
                       font=('New Roman',20))
    welcome.place(x=15,y=15)

def data_page():
    data_frame=CTkFrame(root, height=472, width=600,
                         border_color="yellow", border_width=1)
    data_frame.place(y=27)

    welcome = CTkLabel(data_frame, text="Welcome to the Analysis page !",
                       font=('New Roman',20))
    welcome.place(x=15,y=15)

def settings_page():
    settings_frame=CTkFrame(root, height=472, width=600,
                         border_color="purple", border_width=1)
    settings_frame.place(y=27)

    welcome = CTkLabel(settings_frame, text="Welcome to the settings page !",
                       font=('New Roman',20))
    welcome.place(x=15,y=15)


    # Actual settings:
        # Theme
        # Fonts
        # Background Image

   
    # Menu function
def toggle_menu():
    def identifier(num):
        print("Page number: "+str(num))
        if num == 1:
            title = "Home   "
        elif num == 2:
            title = "Tasks   "
        elif num == 3:
            title = "Schedule   "
        elif num == 4:
            title = "Data   "
        elif num == 5:
            title = "Settings   "
        Header.configure(text=title)
    def collapse_menu():
        menu_frame.destroy()
        toggle_btn.configure(text="☰", command=toggle_menu, border_width=0) 
    root_height = root.winfo_height()
    menu_frame = CTkFrame(root, height=root_height, width=150,
                        corner_radius= 5, border_color="black",
                        border_width=1)
    menu_frame.place(x=0, y=29)

    # Menu content {Buttons}
        # Home Button (1)
    home_btn = CTkButton(menu_frame, text="Home",
                         font=('Bold', 14), width=140,
                        height=25, corner_radius=5,
                        command=lambda:[identifier(1), collapse_menu(),
                                        home_page()])
    home_btn.place(x=5, y=10)
        # Tasks Button (2)
    task_btn = CTkButton(menu_frame, text="Tasks",
                         font=('Bold', 14), width=140,
                        height=25, corner_radius=5,
                        command=lambda:[identifier(2), collapse_menu(),
                                        tasks_page()])
    task_btn.place(x=5, y=45)
        # Notification/Alarm Button (3)
    schedule_btn = CTkButton(menu_frame, text="Schedule",
                         font=('Bold', 14), width=140,
                        height=25, corner_radius=5,
                        command=lambda:[identifier(3), collapse_menu(),
                                        schedule_page()])
    schedule_btn.place(x=5, y=80)
        # Data Button (4)
    data_btn = CTkButton(menu_frame, text="Data",
                         font=('Bold', 14), width=140,
                        height=25, corner_radius=5,
                        command=lambda:[identifier(4), collapse_menu(),
                                        data_page()])
    data_btn.place(x=5, y=115)
        # Settings Button (5)
    settings_btn = CTkButton(menu_frame, text="Settings",
                         font=('Bold', 14), width=140,
                        height=25, corner_radius=5,
                        command=lambda:[identifier(5), collapse_menu(),
                                        settings_page()])
    settings_btn.place(x=5, y=150)

    toggle_btn.configure(text=" << ", command=collapse_menu, border_width=1)


# Header    
head_frame = CTkFrame(root, border_color="black", border_width=0.6)
head_frame.pack(side=ct.TOP, fill=ct.X)
head_frame.configure(height=28) 
Header = ct.CTkLabel(head_frame, text=title, font=('Bold', 14))
Header.pack(side=ct.RIGHT) # Fix me latter
toggle_btn = CTkButton(head_frame, text='☰',width=40,
                        corner_radius=3.5, border_color="white",
                        border_width=0, command=lambda:[toggle_menu()])
toggle_btn.pack(side=ct.TOP, anchor=ct.W)


home_page()

# Window Running { Infinite loop }
root.mainloop()