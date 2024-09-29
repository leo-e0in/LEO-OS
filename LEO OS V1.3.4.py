
 #----------IMPORTS----------#
import tkinter as tk
import datetime
root = tk.Tk()
from tkinter import messagebox


#---------------------------------------------------FUNCTIONS--------------------------------------------------#
# Function to read users from a text file
def load_users_from_file(filename):
    users = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                username, password = line.strip().split(',')
                users.append([username, password])
    except FileNotFoundError:
        print(f"{filename} not found, starting with an empty user list.")
    return users

# Function to write users to a text file
def save_users_to_file(filename, users):
    with open(filename, 'w') as file:
        for user in users:
            file.write(f"{user[0]},{user[1]}\n")

# Load users from file
USERS = load_users_from_file('users.txt')

# Function to handle login
def login():
    username = USERNAME_ENTRY.get()
    password = PASSWORD_ENTRY.get()
    

    # Check if username and password match any in the USERS list
    for user in USERS:
        if username == user[0] and password == user[1]:
            messagebox.showinfo("Login", "Login Successful!")
            root.quit
            DESKTOP_PROTOCOL()
            return
    messagebox.showerror("Login", "Incorrect username or password!")

# Function to handle user creation
def create_user():
    new_username = new_username_entry.get()
    new_password = new_password_entry.get()

    # Check if the username already exists
    for user in USERS:
        if new_username == user[0]:
            messagebox.showerror("Error", "Username already taken!")
            return

    # Add the new user
    USERS.append([new_username, new_password])
    save_users_to_file('users.txt', USERS)
    messagebox.showinfo("User Created", f"User '{new_username}' created successfully!")

# Function to open the Create User window
def open_create_user_window():
    # Create new window for creating a user
    create_user_window = tk.Toplevel(root, height=1920, width=1080)
    create_user_window.title("Create New User")
    

    tk.Label(create_user_window, text="New Username:").grid(row=0, column=0)
    tk.Label(create_user_window, text="New Password:").grid(row=1, column=0)


    global new_username_entry, new_password_entry
    new_username_entry = tk.Entry(create_user_window)
    new_password_entry = tk.Entry(create_user_window, show="*")

    new_username_entry.grid(row=0, column=1)
    new_password_entry.grid(row=1, column=1)

    create_user_button = tk.Button(create_user_window, text="Create User", command=create_user)
    create_user_button.grid(row=2, column=1)



    
#----------------------------------------------------#LOGIN PAGE#-------------------------------------------------------#
from time import strftime
def my_time():
    time_string = strftime('%H:%M:%S %p \n %A \n %x')
    l1.config(text=time_string)
    l1.after(1000,my_time) # time delay of 1000 milliseconds 
	
l1=tk.Label(root,bg='#dcdcdc',font=('Microsoft YaHei UI Light', 30))
l1.place(x=850, y=150)

my_time()


root.geometry ('1920x1080')
root.title('LEO OS V1.3 - LOG IN / NEW USER')
root.configure(bg='#dcdcdc')


TITLE=tk.Label(root, text='LEO OS |',bg='#dcdcdc', font=('Microsoft YaHei UI Light', 25))
TITLE.place(x=800, y=370)

TITLE2=tk.Label(root, text='WHERE PRIVACY MATTERS' , bg='#dcdcdc', font=('Microsoft YaHei UI Light', 12))
TITLE2.place(x=950, y=385)

USERNAME_ENTRY = tk.Entry(root, font=('Microsoft YaHei UI Light', 20))
USERNAME_ENTRY.place(x=800, y=435, height=50, width=350)

PASSWORD_ENTRY = tk.Entry(root,show="*",font=('Microsoft YaHei UI Light', 20))
PASSWORD_ENTRY.place(x=800, y=500, height=50, width=350)

#--
LOGINFRAME = tk.Frame(root)
LOGINFRAME.columnconfigure(0 , weight=1)
LOGINFRAME.columnconfigure(1 , weight=1)

LOGINBUTTON=tk.Button(LOGINFRAME, text='Login', font=('Microsoft YaHei UI Light', 17),command=login)
LOGINBUTTON.grid(row=0, column=0, sticky=tk.W+tk.E)

NEWUSERBUTTON= tk.Button(LOGINFRAME, text='New User', font=('Microsoft YaHei UI Light',17),command=open_create_user_window)
NEWUSERBUTTON.grid(row=0, column=1, sticky=tk.W+tk.E)

LOGINFRAME.place(x=800, y=570)




#------------------------------DESKTOP------------------------------------------------
def DESKTOP_PROTOCOL():
    global DESKTOP_WINDOW
    DESKTOP_WINDOW = tk.Toplevel(root,bg='#dcdcdc', height=1920, width=1080)
    DESKTOP_WINDOW.title("LEO OS 1.3.3 - DESKTOP")
    DESKTOP_WINDOW.geometry ('1920x1080')
    
    TASKBAR=tk.Label(DESKTOP_WINDOW,text='',  bg='grey', height=1920, width=10)
    TASKBAR.place(x=0, y=0)
    
    CALCULATOR_BUTTON=tk.Button(DESKTOP_WINDOW,text='Calculator', font=('Microsoft YaHei UI Light',10),command=CALCULATOR_APP)
    CALCULATOR_BUTTON.place(x=100,y=20)

    FILEMANAGER_BUTTON=tk.Button(DESKTOP_WINDOW,text='File Manager', font=('Microsoft YaHei UI Light',10),command=FILE_MANAGER)
    FILEMANAGER_BUTTON.place(x=200,y=20)

    NOTEPAD_BUTTON=tk.Button(DESKTOP_WINDOW,text='Notepadf', font=('Microsoft YaHei UI Light',10),command=NOTEPAD)
    NOTEPAD_BUTTON.place(x=300,y=20)
                    
#-------------------------------------------------------------------------------------------------------APPS------------------------------------------------------------------------------------------------------------------------------




#-------------------------CALCULATOR APP---------------------------------------
global CALCULATION
CALCULATION=('')

def CALCULATOR_APP():
    global CALCULATION
    CALCULATION=('')


    def add_to_calculation(symbol):
        global CALCULATION
        CALCULATION += str(symbol)
        TEXT_RESULT.delete(1.0, 'end')
        TEXT_RESULT.insert(1.0, CALCULATION)

    def evaluate_caclulation():
         global CALCULATION
         try:
           RESULT=str(eval(CALCULATION))
           CALCULATION = ''
           TEXT_RESULT.delete(1.0, 'end')
           TEXT_RESULT.insert(1.0, RESULT)
         except:
                  pass

    def clear_field():
        global CALCULATION
        CALCULATION=''
        TEXT_RESULT.delete(1.0, 'end')


    global CALCULATOR_WINDOW
    CALCULATOR_WINDOW = tk.Toplevel(DESKTOP_WINDOW, height=500, width=300)
    CALCULATOR_WINDOW.title("CALCULATOR")
    
    global TEXT_RESULT
    TEXT_RESULT= tk.Text(CALCULATOR_WINDOW, height=2, width=16, font=('Ariel', 24))
    TEXT_RESULT.grid(columnspan=5)

    #NUMBERS
    NUM1 =tk.Button(CALCULATOR_WINDOW, text='1', width=5, font=('Microsoft YaHei UI Light',10),command=lambda: add_to_calculation(1))
    NUM1.grid(row=2, column=1)
    
    NUM2=tk.Button(CALCULATOR_WINDOW, text='2', width=5, font=('Microsoft YaHei UI Light',10),command=lambda: add_to_calculation(2))
    NUM2.grid(row=2, column=2)

    NUM3=tk.Button(CALCULATOR_WINDOW, text='3', width=5, font=('Microsoft YaHei UI Light',10),command=lambda: add_to_calculation(3))
    NUM3.grid(row=2, column=3)

    NUM4=tk.Button(CALCULATOR_WINDOW, text='4', width=5, font=('Microsoft YaHei UI Light',10),command=lambda: add_to_calculation(4))
    NUM4.grid(row=3, column=1)

    NUM5 =tk.Button(CALCULATOR_WINDOW, text='5', width=5, font=('Microsoft YaHei UI Light',10),command=lambda: add_to_calculation(5))
    NUM5.grid(row=3, column=2)
    
    NUM6=tk.Button(CALCULATOR_WINDOW, text='6', width=5, font=('Microsoft YaHei UI Light',10),command=lambda: add_to_calculation(6))
    NUM6.grid(row=3, column=3)

    NUM7=tk.Button(CALCULATOR_WINDOW, text='7', width=5, font=('Microsoft YaHei UI Light',10),command=lambda: add_to_calculation(7))
    NUM7.grid(row=4, column=1)

    NUM8=tk.Button(CALCULATOR_WINDOW, text='8', width=5, font=('Microsoft YaHei UI Light',10),command=lambda: add_to_calculation(8))
    NUM8.grid(row=4, column=2)

    NUM9=tk.Button(CALCULATOR_WINDOW, text='9', width=5, font=('Microsoft YaHei UI Light',10),command=lambda: add_to_calculation(9))
    NUM9.grid(row=4, column=3)

    NUM0=tk.Button(CALCULATOR_WINDOW, text='0', width=5, font=('Microsoft YaHei UI Light',10),command=lambda: add_to_calculation(0))
    NUM0.grid(row=5, column=2)
    
    #SYMBOLS AND CLEAR
    SYMBOL_PLUS=tk.Button(CALCULATOR_WINDOW, text='+', width=5, font=('Microsoft YaHei UI Light',10),command=lambda: add_to_calculation('+'))
    SYMBOL_PLUS.grid(row=2, column=4)

    SYMBOL_MINUS=tk.Button(CALCULATOR_WINDOW, text='-', width=5, font=('Microsoft YaHei UI Light',10),command=lambda: add_to_calculation('-'))
    SYMBOL_MINUS.grid(row=3, column=4)

    SYMBOL_MULTIPLY=tk.Button(CALCULATOR_WINDOW, text='*', width=5, font=('Microsoft YaHei UI Light',10),command=lambda: add_to_calculation('*'))
    SYMBOL_MULTIPLY.grid(row=4, column=4)
    
    SYMBOL_DIVIDE=tk.Button(CALCULATOR_WINDOW, text='/', width=5, font=('Microsoft YaHei UI Light',10),command=lambda: add_to_calculation('/'))
    SYMBOL_DIVIDE.grid(row=5, column=4)

    SYMBOL_OPENBRACKET=tk.Button(CALCULATOR_WINDOW, text='(', width=5, font=('Microsoft YaHei UI Light',10),command=lambda: add_to_calculation('('))
    SYMBOL_OPENBRACKET.grid(row=5, column=1)

    SYMBOL_CLOSEDBRACKET=tk.Button(CALCULATOR_WINDOW, text=')', width=5, font=('Microsoft YaHei UI Light',10),command=lambda: add_to_calculation(')'))
    SYMBOL_CLOSEDBRACKET.grid(row=5, column=3)

    SYMBOL_CLOSEDBRACKET=tk.Button(CALCULATOR_WINDOW, text=')', width=5, font=('Microsoft YaHei UI Light',10),command=lambda: add_to_calculation(')'))
    SYMBOL_CLOSEDBRACKET.grid(row=5, column=3)

    CLEAR_CALCULATION=tk.Button(CALCULATOR_WINDOW, text='C', width=11, font=('Microsoft YaHei UI Light',10),command= clear_field)
    CLEAR_CALCULATION.grid(row=6, column=1, columnspan=2)


    SYMBOL_EQUALS=tk.Button(CALCULATOR_WINDOW, text='=', width=11, font=('Microsoft YaHei UI Light',10),command= evaluate_caclulation)
    SYMBOL_EQUALS.grid(row=6, column=3, columnspan=2)



    

#-------------------------------------------FILE MANAGER-------------------------------------------

def FILE_MANAGER():
    global FILEMANAGER_WINDOW
    FILEMANAGER_WINDOW= tk.Toplevel(DESKTOP_WINDOW, height=600, width=1000,bg='#dcdcdc')
    FILEMANAGER_WINDOW.title("File Manager")


#------------------------------------------------------------WORDPAD------------------------------------------------

def NOTEPAD():
    global WORD_WINDOW
    NOTEPAD_WINDOW= tk.Toplevel(DESKTOP_WINDOW, height=800, width=600,bg='#dcdcdc')
    NOTEPAD_WINDOW.title("WordPad")




#-------------------------)
root.mainloop()






