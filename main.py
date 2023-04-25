from tkinter import *
import random

MAX_LEN = 16
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']
DICT =[0,1,2,3]
DICTSET = ['DIGITS','LOCASE_CHARACTERS','UPCASE_CHARACTERS','SYMBOLS']


def saveData():
    replace = False
    with open("hello.txt", 'r') as fp:
        lines = fp.readlines()
        i = 0
        for line in lines:
            x = line.split(' | ')
            if x[0].lower() == website_entry.get().lower():
                with open("hello.txt", 'w') as my_file:
                    lines[i] = f"{website_entry.get()} | {password_entry.get()} | {email_entry.get()}"
                    my_file.writelines(lines)
                replace = True
                break
            i += i

    if replace == False:
        with open("hello.txt", 'a') as my_file:
            my_file.write(f"{website_entry.get()} | {password_entry.get()} | {email_entry.get()}\n")




def generatepassword():
    password = ""
    for x in range(MAX_LEN):
        set = DICTSET[random.choice(DICT)]
        if set == "DIGITS":
            passcode = random.choice(DIGITS)
        elif set == "LOCASE_CHARACTERS":
            passcode = random.choice(LOCASE_CHARACTERS)
        elif set == "UPCASE_CHARACTERS":
            passcode = random.choice(UPCASE_CHARACTERS)
        else:
            passcode = random.choice(SYMBOLS)

        password += passcode
    password_entry.delete(0, END)
    password_entry.insert(0, password)


def searchpassword():
    searchString = search_entry.get()

    password_entry.delete(0, END)
    website_entry.delete(0, END)
    email_entry.delete(0, END)
    with open("hello.txt", 'r') as fp:
        lines = fp.readlines()
        for line in lines:
            # check if string present on a current line
            x = line.split(' | ')
            if x[0].lower().find(searchString.lower()) != -1:
                password_entry.insert(0, x[1])
                website_entry.insert(0, x[0])
                email_entry.insert(0, x[2])
                break


window = Tk()
window.title("Password Generator")
window.geometry('400x200')
website_label = Label(text="Website")
website_label.grid(row=0,column=0,sticky = W, pady = 3, padx = 3)
email_label = Label(text="Email/Username")
email_label.grid(row=1,column=0,sticky = W, pady = 3, padx = 3)
password_label = Label(text="Password")
password_label.grid(row=2,column=0,sticky = W, pady = 3, padx = 3)

search_label = Label(text="Search Password")
search_label.grid(row=4,column=0,columnspan=3, pady = 3, padx = 3)
# Text Widget

website_entry = Entry(width=48)
website_entry.grid(row=0,column=1,columnspan=2,sticky = W, pady = 3, padx = 3)
email_entry = Entry(width=48)
email_entry.grid(row=1,column=1,columnspan=2,sticky = W, pady = 3, padx = 3)
email_entry.insert(0,"jtnjmb@gmail.com")
password_entry = Entry(width=28, show="*")
password_entry.grid(row=2,column=1)
generateBUtton = Button(text="Generate Password", width=15,command=generatepassword)
generateBUtton.grid(row=2,column=2)
generateBUtton = Button(text="Add", width=40, command=saveData)
generateBUtton.grid(row=3,column=1,columnspan=2,pady = 4)

search_entry = Entry(width=40)
search_entry.grid(row=5,column=0,columnspan=2)
searchBUtton = Button(text="Search Website", width=15,command=searchpassword)
searchBUtton.grid(row=5,column=2)

window.mainloop()