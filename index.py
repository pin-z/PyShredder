import PySimpleGUI as sg
import shred
import os

# Set the theme and window size
sg.theme('DarkBlue')
window_size = (500, 300)
button_color = "Teal"

# Define the layout of the main menu
menu_layout = [
    [sg.Column([
        [sg.Button("Shred File", button_color=("white", button_color), size=(10, 3), font=("Helvetica", 16))],
        [sg.Button("Shred Folder", button_color=("white", button_color), size=(10, 3), font=("Helvetica", 16))]
    ], element_justification="center", expand_x=True, expand_y=True)]
]

# Define the layout of the shredding method menu
method_layout = [
    [sg.Column([
        [sg.Button("3-pass DoD", button_color=("white", button_color), size=(10, 2), font=("Helvetica", 16))],
        [sg.Button("Gutmann Method", button_color=("white", button_color), size=(10, 2), font=("Helvetica", 16))],
        [sg.Button("Random Overwrite", button_color=("white", button_color), size=(10, 2), font=("Helvetica", 16))],
        [sg.Button("Hex Overwrite", button_color=("white", button_color), size=(10, 2), font=("Helvetica", 16))],
        [sg.Button("Hybrid Shred", button_color=("white", button_color), size=(10, 2), font=("Helvetica", 16))]
    ], element_justification="center", expand_x=True, expand_y=True)]
]

method_layout_2 = [
    [sg.Column([
        [sg.Button("3-pass DoD", button_color=("white", button_color), size=(10, 2), font=("Helvetica", 16))],
        [sg.Button("Gutmann Method", button_color=("white", button_color), size=(10, 2), font=("Helvetica", 16))],
        [sg.Button("Random Overwrite", button_color=("white", button_color), size=(10, 2), font=("Helvetica", 16))],
        [sg.Button("Hybrid Shred", button_color=("white", button_color), size=(10, 2), font=("Helvetica", 16))]
    ], element_justification="center", expand_x=True, expand_y=True)]
]

# Create the main menu window
menu_window = sg.Window("Shredder", menu_layout, size=window_size)

# Event loop for the main menu window
while True:
    event, values = menu_window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Shred File":
        # Get the file path from the user
        file_path = sg.popup_get_file("Select a file to shred")
        if file_path:
            # Create the shredding method menu window
            method_window = sg.Window("Shredder - Shred File", method_layout, size=(500, 400))

            # Event loop for the shredding method menu window
            while True:
                event, values = method_window.read()
                if event == sg.WINDOW_CLOSED:
                    break
                elif event == "3-pass DoD":
                    # Shred the file with the 3-pass DoD 5220.22-M method
                    shred.shred_file_dod(file_path)
                    os.remove(file_path)
                    sg.popup("File shredded securely!")
                    break
                elif event == "Gutmann Method":
                    # Shred the file with the Gutmann method
                    shred.shred_file_gutmann(file_path)
                    os.remove(file_path)
                    sg.popup("File shredded securely!")
                    break
                elif event == "Random Overwrite":
                    # Overwrite the file with random data
                    shred.random_shred_file(file_path, passes=10)
                    os.remove(file_path)
                    sg.popup("File shredded securely!")
                    break
                elif event == "Hex Overwrite":
                    # Overwrite the file with random hexadecimal values
                    shred.overwrite_hex_values(file_path, passes=3)
                    os.remove(file_path)
                    sg.popup("File shredded securely!")
                    break
                elif event == "Hybrid Shred":
                    # Overwrite the file with random hexadecimal values
                    shred.Hybrid_shredFile(file_path)
                    os.remove(file_path)
                    sg.popup("File shredded securely!")
                    break

            method_window.close()
    elif event == "Shred Folder":
        # Get the folder path from the user
        folder_path = sg.popup_get_folder("Select a folder to shred")
        if folder_path:
            # Create the shredding method menu window
            method_window = sg.Window("Shredder - Shred Folder", method_layout_2, size=window_size)

# Event loop for the main menu window
while True:
    event, values = menu_window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event in ("Shred File", "Shred Folder"):
        # Get the file or folder path from the user
        path = sg.popup_get_file("Select a file to shred") if event == "Shred File" else sg.popup_get_folder("Select a folder to shred")
        if path:
            # Create the shredding method menu window
            method_window = sg.Window("Shredder - Method Selection", method_layout, size=Wsize)

            # Event loop for the shredding method menu window
            while True:
                event, values = method_window.read()
                if event == sg.WINDOW_CLOSED:
                    break
                elif event in ("3-pass DoD", "Gutmann Method", "Random Overwrite", "Hex Overwrite", "Hybrid Shred"):
                    # Perform the shredding operation based on the selected method
                    # ... (shredding operations here)
                    sg.popup("File/Folder shredded securely!", title="Success")
                    break

            method_window.close()

menu_window.close()
