import customtkinter
from pytube import YouTube


#system settings

customtkinter.set_appearance_mode("System") #will get the dark or light mode being used.
customtkinter.set_default_color_theme("blue")

#application frmae

prac_app = customtkinter.CTk()
prac_app.geometry("720x480")
prac_app.title("YouTube Downloader")

prac_app.mainloop()