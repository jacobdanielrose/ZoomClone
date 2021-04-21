##############################
#       Zoom Clone v0.1      #
##############################

from vidstream import *
import tkinter as tk
import socket
import threading
import requests

local_ip_address = socket.gethostbyname(socket.gethostname())
public_ip_address = requests.get('https://api.ipify.org').text



if __name__ == '__main__':

    # GUI
    window = tk.Tk()
    window.title("My Zoom Clone v0.0.1 Alpha")
    window.geometry('300x200')

    label_target_ip = tk.Label(window, text="Target IP:")
    label_target_ip.pack()

    text_target_ip = tk.Text(window, height=1)
    text_target_ip.pack()

    btn_listen  = tk.Button(window, text="Start Listening", width=50)
    btn_listen.pack(anchor=tk.CENTER, expand=True)