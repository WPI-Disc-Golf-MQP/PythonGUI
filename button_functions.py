from helper_functions import send_msg
import customtkinter as ctk

def start_machine():
    # global machine_started
    # machine_started = True
    # start_button.configure(state=ctk.DISABLED)
    # stop_button.configure(state=ctk.NORMAL)

    # add_button.configure(state=ctk.DISABLED)
    # remove_button.configure(state=ctk.DISABLED)
    # export_button.configure(state=ctk.DISABLED)

    send_msg()


def stop_machine():
    global machine_started
    machine_started = False
    start_button.configure(state=ctk.NORMAL)
    stop_button.configure(state=ctk.DISABLED)
    
    add_button.configure(state=ctk.NORMAL)
    remove_button.configure(state=ctk.NORMAL)
    export_button.configure(state=ctk.NORMAL)

def setConveyorSpeed(speed):
    if speed == 0: 
        stop_machine()
    elif speed > 0: 
        start_machine() 

def add_entry():
    # data = enter_qty.get()
    # if data:
    #     machine_data.loc[len(machine_data)] = [data]
    
    # simply just add entries to df here 

    update_output_table()
    update_input_table()

def remove_entry():
    # selected_index = table.selection()
    # if selected_index:
    #     index_to_remove = int(selected_index[0])
    #     machine_data.drop(index_to_remove, inplace=True)

    # simple just remove item from df here 

    # update_table()
    pass


def update_output_table():
    # remove all entries in the table 
    for item in out_table.get_children():
        out_table.delete(item)

    # add back all entries from pandas    
    for index, row in output_data_df.iterrows():
        out_table.insert("", "end", values=tuple(output_data_df.iloc[index]))

def update_input_table():
    # remove all entries in the table 
    for item in table.get_children():
        table.delete(item)

    # add back all entries from pandas    
    for index, row in input_data_df.iterrows():
        print(tuple(input_data_df.iloc[index]))

        table.insert("", "end", values=tuple(input_data_df.iloc[index]))
