import tkinter as tk
from tkinter import messagebox
import turtle
import webbrowser
import random

# Surprise 1: Draw a heart with turtle
def draw_heart():
    turtle.bgcolor("lightpink")
    pen = turtle.Turtle()
    pen.color("red")
    pen.begin_fill()
    pen.speed(1)
    pen.left(140)
    pen.forward(180)
    pen.circle(-90, 200)
    pen.left(120)
    pen.circle(-90, 200)
    pen.forward(180)
    pen.end_fill()

    pen.penup()
    pen.goto(0, -20)
    pen.color("white")
    pen.write("I love you, Baby 💖", align="center", font=("Arial", 18, "bold"))
    pen.hideturtle()
    turtle.done()

# Surprise 2: Open a love song on YouTube
def play_song():
    webbrowser.open("https://youtu.be/FcGy7VGURtM?si=_179eEE1_VEZjxGg")  # Replace with your song

# Surprise 3: Show a cute message
def love_note():
    notes = [
        "You're my today and all of my tomorrows 💌",
        "Life with you is my favorite journey 🚀",
        "You make my heart smile every single day 😊",
        "Rishab, you're my forever person 💑"
    ]
    messagebox.showinfo("For Rishab 💝", random.choice(notes))

# Surprise 4: The final surprise (heart + message)
def final_surprise():
    messagebox.showinfo("Happy Anniversary 🎉", "2 magical years, Rishab 💕\nHere's to forever with you!")
    draw_heart()

# GUI setup
root = tk.Tk()
root.title("Anniversary Surprise for Rishab 🎊")
root.geometry("500x500")
root.config(bg="mistyrose")

label = tk.Label(root, text="Hey Rishab 💖", font=("Comic Sans MS", 20, "bold"),
                 bg="mistyrose", fg="darkred")
label.pack(pady=20)

button1 = tk.Button(root, text="💘 Click for a Love Note", font=("Arial", 14),
                    bg="white", fg="red", command=love_note)
button1.pack(pady=10)

button2 = tk.Button(root, text="🎵 Play Our Song", font=("Arial", 14),
                    bg="white", fg="red", command=play_song)
button2.pack(pady=10)

button3 = tk.Button(root, text="❤️ Final Surprise", font=("Arial", 14, "bold"),
                    bg="red", fg="white", command=final_surprise)
button3.pack(pady=30)

root.mainloop()
