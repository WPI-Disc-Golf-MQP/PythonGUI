import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import pandas as pd

def main_GUI():

    ctk.set_appearance_mode("Light")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("Machine Control App")

    def styler():
        style = ttk.Style()
        
        style.theme_use("clam")

        style.configure("Treeview",
        #                 background="solver",
        #                 foreground="black",
                        rowheight=50,
        #                 fieldbackground="silver",
        #                 # bordercolor="#343638",
        #                 # borderwidth=0
                        )
        # # change selected color 
        style.map('Treeview', background=[('selected', 'green')])

        style.configure("Treeview.Heading",
                        background="grey",
                        foreground="white",
                        relief="flat")
        # style.map("Treeview.Heading",
        #             background=[('active', '#3484F0')])
    styler() 

    input_starting_data = {
        'SKU': ['SKU001', 'SKU002', 'SKU003', 'SKU004', 'SKU005'],
        'Qty': [10, 20, 15, 30, 25],
        'Manufacturer': ['Manufacturer A', 'Manufacturer B', 'Manufacturer A', 'Manufacturer C', 'Manufacturer B']
    }

    output_starting_data = {
        'ID': ['SKU001-10132023-0001','SKU001-10132023-0002','SKU001-10132023-0003','SKU001-10132023-0004','SKU001-10132023-0005'],
        'Diameter': ['10 in','10 in','10 in','10 in','10 in'],
        'Wing Width': ['0.15 in','0.15 in','0.15 in','0.15 in','0.15 in'],

        'Wing Depth':['0.15 in','0.15 in','0.15 in','0.15 in','0.15 in'],
        'Height':['1.5 in','1.5 in','1.5 in','1.5 in','1.5 in'],

        'Weight':['124 g','124 g','124 g','124 g','124 g'],
        'Flex':['0.1 in','0.1 in','0.1 in','0.1 in','0.1 in'],
        'Profile':['graph','graph','graph','graph','graph'],
        'Images':['n/a','n/a','n/a','n/a','n/a'],
    }


    machine_started = False
    input_data_df = pd.DataFrame(input_starting_data)
    output_data_df = pd.DataFrame(output_starting_data)


    # main (top) frame
    main_frame  = ctk.CTkFrame(app)
    main_frame.grid(row=0,  column=0, columnspan=2, padx=5,pady=5)
    stop_button = ctk.CTkLabel(main_frame, text="Flying Disc Measurement Machine",font=ctk.CTkFont(size=50, weight="bold"))
    stop_button.grid(row=0, column=1)
    start_button = ctk.CTkButton(main_frame, text="Start Machine", command= lambda:setConveyorSpeed(50) )
    start_button.grid(row=1,  column=0)
    stop_button = ctk.CTkButton(main_frame, text="Stop Machine", command=lambda:setConveyorSpeed(50), state=ctk.DISABLED)
    stop_button.grid(row=1, column=2)
    Operations = ctk.CTkLabel(main_frame, text="This is where the Operations of the machine are displayed. Where each ID disc is in what module.")
    Operations.grid(row=1, column=1)

    # debugging button (bottom) frame
    button_frame  = ctk.CTkFrame(app)
    button_frame.grid(row=2,  column=0, columnspan=2, padx=5,pady=5)

    msg_button = ctk.CTkButton(button_frame, text=r'Send Ping {"msgType":"CAN","msgID":512,"msg":12345}',command=send_msg)
    msg_button.grid(row=0, column=0)

    # input (left) frame
    input_frame  =  ctk.CTkFrame(app)
    input_frame.grid(row=1,  column=0, padx=5,pady=5)
    ctk.CTkLabel(input_frame, text="Input", font=ctk.CTkFont(size=20, weight="bold")).grid(row=0,  column=0,)

    table = ttk.Treeview(input_frame, columns=("c1", "c2", "c3"), show='headings', height=8)
    table.column("# 1", anchor=tk.CENTER)
    table.heading("# 1", text="SKU")
    table.column("# 2", anchor=tk.CENTER)
    table.heading("# 2", text="Qty")
    table.column("# 3", anchor=tk.CENTER)
    table.heading("# 3", text="Manufacturer")
    table.grid(row=2,column=0)

    # add remove frame (part of input frame) 
    add_remove_frame = ctk.CTkFrame(input_frame)
    add_remove_frame.grid(row=1,  column=0)
    enter_qty = ctk.StringVar() # variable that is a string
    enter_SKU = ctk.StringVar() # variable that is a string
    ctk.CTkEntry(add_remove_frame, textvariable=enter_SKU,placeholder_text="SKU").grid(row=0,column=0)
    ctk.CTkEntry(add_remove_frame, textvariable=enter_qty,placeholder_text="Qty").grid(row=0,column=1)
    add_button = ctk.CTkButton(add_remove_frame, text="Add Entry", command=add_entry)
    add_button.grid(row=0,column=2)
    remove_button = ctk.CTkButton(add_remove_frame, text="Remove Entry", command=remove_entry)
    remove_button.grid(row=0,column=3)

    # output (right) frame
    output_frame = ctk.CTkFrame(app)
    output_frame.grid(row=1,  column=1,padx=5,pady=5)
    ctk.CTkLabel(output_frame, text="Output", font=ctk.CTkFont(size=20, weight="bold")).grid(row=0,  column=0,  padx=5,  pady=5)
    export_button = ctk.CTkButton(output_frame, text="Export", command=add_entry)
    export_button.grid(row=1,column=0)

    out_table = ttk.Treeview(output_frame, columns=("c1", "c2", "c3",'c4','c5','c6','c7','c8','c9'), show='headings', height=8)
    out_table.column("# 1", anchor=tk.CENTER,width=150)
    out_table.heading("# 1", text="ID (SKU-Date-Index)")
    out_table.column("# 2", anchor=tk.CENTER,width=125)
    out_table.heading("# 2", text="Diameter (in)")
    out_table.column("# 3", anchor=tk.CENTER,width=125)
    out_table.heading("# 3", text="Wing Width (in)")

    out_table.column("# 4", anchor=tk.CENTER,width=125)
    out_table.heading("# 4", text="Wing Depth (in)")
    out_table.column("# 5", anchor=tk.CENTER,width=125)
    out_table.heading("# 5", text="Profile Height (in)")

    out_table.column("# 6", anchor=tk.CENTER,width=125)
    out_table.heading("# 6", text="Weight (g)")

    out_table.column("# 7", anchor=tk.CENTER,width=125)
    out_table.heading("# 7", text="Flex (Deflection)")
    out_table.column("# 8", anchor=tk.CENTER,width=125)
    out_table.heading("# 8", text="Profile (graph)")
    out_table.column("# 9", anchor=tk.CENTER,width=125)
    out_table.heading("# 9", text="Images (image)")
    out_table.grid(row=2,column=0)

    return app
    app.mainloop()
