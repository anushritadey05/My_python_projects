from tkinter import *
from tkinter import ttk

def save_info():
    firstname_info = firstname.get()
    lastname_info = lastname.get()
    age_info = age.get()

    with open("user.txt", "w") as file:
        file.write(f"Firstname: {firstname_info}\n")
        file.write(f"Lastname: {lastname_info}\n")
        file.write(f"Age: {age_info}\n")

    print("User", firstname_info, "has been registered successfully")

# GUI Setup
screen = Tk()
screen.geometry("500x500")
screen.title("Python Form")

heading = Label(text="Python Form", bg="grey", fg="black", width="500", height="3")
heading.pack()

firstname_text = Label(text="Firstname *")
lastname_text = Label(text="Lastname *")
age_text = Label(text="Age *")
firstname_text.place(x=15, y=70)
lastname_text.place(x=15, y=140)
age_text.place(x=15, y=210)

firstname = StringVar()
lastname = StringVar()
age = IntVar()

firstname_entry = Entry(textvariable=firstname, width="30")
lastname_entry = Entry(textvariable=lastname, width="30")
age_entry = Entry(textvariable=age, width="30")

firstname_entry.place(x=15, y=100)
lastname_entry.place(x=15, y=180)
age_entry.place(x=15, y=240)

register = Button(screen, text="Register", width="200", height="2", command=save_info, bg="grey")
register.place(x=0, y=300)

screen.mainloop()
