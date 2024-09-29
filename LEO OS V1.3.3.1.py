
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
            root.quit()
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



#----------------------------------------------------------------GUI-----------------------------------------------------------------------------
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


root.mainloop()
DESKTOP_WINDOW = tk.Toplevel(root,bg='#dcdcdc', height=1920, width=1080)
DESKTOP_WINDOW.title("LEO OS 1.3.3 - DESKTOP")
DESKTOP_WINDOW.geometry ('1920x1080')
TASKBAR=tk.Label(DESKTOP_WINDOW,text='',  bg='grey', height=1920, width=10)
TASKBAR.place(x=0, y=0)


#-------------------------------------------------------------------------------------------------------APPS------------------------------------------------------------------------------------------------------------------------------
#CALCULATOR APP

CACLULATION=''

def open_create_calculator_window():
    # Create new window for creating a user
    global CALCULATOR_WINDOW
    CALCULATOR_WINDOW = tk.Toplevel(DESKTOP_WINDOW, height=300, width=300)
    CALCULATOR_WINDOW.title("CALCULATOR")


def add_to_caclulation(symbol):
    global CALCULATION
    CACLULATION += str(symbol)
    RESULT.delete(1.0, 'end')
    RESULT.insert(1.0, CALCULATION)

def evaluate_caclulation():
    global calculation
    try:
        CALCULATION=str(eval(CALCULATION))
        RESULT.delete(1.0, 'end')
        RESULT.insert(1.0, CALCULATION)
    except:
        pass
                  
def clear_field():
    global CALCULATION
    CALCULATION=''
    RESULT.delete(1.0, 'end')
    
        
CALCULATOR_BUTTON=tk.Button(DESKTOP_WINDOW,text='Calculator', font=('Microsoft YaHei UI Light',10),command=open_create_calculator_window)
CALCULATOR_BUTTON.place(x=100,y=20)

RESULT= tk.Text(CALCULATOR_WINDOW, height=2, width=16, font=('Ariel', 24))
RESULT.grid(columnspan=5)


NUM1 =tk.Button(CALCULATOR_WINDOW, text='1', width=5, font=('Microsoft YaHei UI Light'),command=lambda: add_to_calculation)
NUM1.grid(row=2, column=1)

NUM2=tk.Button(CALCULATOR_WINDOW, text='2', width=5, font=('Microsoft YaHei UI Light'),command=lambda: add_to_calculation)
NUM2.grid(row=2, column=1)

NUM3=tk.Button(CALCULATOR_WINDOW, text='3', width=5, font=('Microsoft YaHei UI Light'),command=lambda: add_to_calculation)
NUM3.grid(row=2, column=2)

NUM3=tk.Button(CALCULATOR_WINDOW, text='3', width=5, font=('Microsoft YaHei UI Light'),command=lambda: add_to_calculation)
NUM3.grid(row=2, column=3)
#-------------------------
root.mainloop()






