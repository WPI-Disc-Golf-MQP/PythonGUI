# import tkinter as tk
# import asyncio

# async def change_button_color(button, new_color, delay_seconds):
#     await asyncio.sleep(delay_seconds)
#     button.config(bg=new_color)
#     print('farts')

# def on_button_click():
#     # Asynchronously await the function to change color after 1 second
#     asyncio.run(change_button_color(button, "red", 1))

# # Create the Tkinter window
# root = tk.Tk()
# root.title("Async Tkinter Example")

# # Create a button
# button = tk.Button(root, text="Change Color", command=on_button_click)
# button.pack(pady=20)

# # Start the Tkinter event loop
# asyncio.set_event_loop(asyncio.new_event_loop())
# root.mainloop()
import tkinter as tk
import asyncio

async def change_button_color(button, new_color, delay_seconds):
    await asyncio.sleep(delay_seconds)
    button.config(bg=new_color)

def on_button_click():
    # Asynchronously await the function to change color after 1 second
    asyncio.create_task(change_button_color(button, "red", 1))

# Create the Tkinter window
root = tk.Tk()
root.title("Async Tkinter Example")

# Create a button
button = tk.Button(root, text="Change Color", command=on_button_click)
button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
