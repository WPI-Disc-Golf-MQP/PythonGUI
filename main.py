# import customtkinter as ctk
# import tkinter as tk
# from tkinter import ttk
# import pandas as pd
import json 

# my imports 
from serial_connection import serialInst
from helper_functions import send_message_and_wait_for_response, send_msg
from button_functions import *
from GUI import main_GUI

# command line interface for GUI testing 
def main_CLI():
    while True:
        # get  
        # print('checked for responses:')
        # if serialInst.inWaiting() > 0: 
        #     line = serialInst.readline()
        #     print("Received data:", line.decode('utf-8').strip())
        # print()

        # send 
        action = input("what do you want to do? (SEND, SEND START, SEND STOP, MODULES)")
        if action == "SEND":
            msg = json.dumps({"msgType":"CAN","msgID":1,"msg":12345}) 
            send_message_and_wait_for_response(serialInst, msg)

        elif action == "SEND START": 
            msg = json.dumps({"msgType":"CAN","msgID":1,"msg":0}) # tells Conveyor Module to run routine 0
            send_message_and_wait_for_response(serialInst, msg)

        elif action == "SEND STOP": 
            msg = json.dumps({"msgType":"CAN","msgID":1,"msg":1}) # tells Conveyor Module to run routine 1
            send_message_and_wait_for_response(serialInst, msg)

        elif action == "MODULES": 
            msg = json.dumps({"msgType":"MODULES","msgID":None,"msg":None})
            send_message_and_wait_for_response(serialInst, msg)
        
        else:
            print('not recognized')


while True: 
    GUICLI = input('Boot GUI or CLI Interface? (GUI / CLI)')
    if GUICLI == "GUI":
        app = main_GUI()
        app.mainloop()
    elif GUICLI == "CLI": 
        main_CLI()
    else: 
        print('please input a valid input...')