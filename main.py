import tkinter
import customtkinter
from pytube import YouTube

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Videos Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10,pady=10)

#Lnk Input
link = customtkinter.CTkEntry(app, width=350, height=40)
link.pack()

# Run App
app.mainloop()

