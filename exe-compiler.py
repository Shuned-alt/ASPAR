#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import subprocess
import customtkinter
import tkinter as tk
import threading
import shutil
from tkinter import filedialog
from tkinter import messagebox
from ASPARSYS import ASPAR

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("400x400")
app.title("ASPAR SYSTEM")

def run_script():
    def run_script_thread():
        try:
            # create a new window
            popup = tk.Toplevel()
            popup.title("Script is running")
            popup.geometry("450x100")
            popup_label = tk.Label(popup, text="The code is running. Don't close this window", font=("Roboto", 12), wraplength=450)
            popup_label.pack(pady=10)

            # run the script
            ASPAR()

            # update the popup window to show the success message
            popup_label.config(text="Script has finished running.")
            popup.title("Success")

            # get the path of the current directory
            dir_path = os.path.dirname(os.path.realpath(__file__))

            # get the path of the parent directory
            parent_dir = os.path.abspath(os.path.join(dir_path, os.pardir))

            # open the file explorer to the parent directory
            subprocess.Popen(f'explorer "{parent_dir}"')

        except subprocess.CalledProcessError as e:
            # show error message if script fails
            messagebox.showerror("Error", f"Script failed with error code {e.returncode}: {e.stderr.decode()}")
        except Exception as e:
            # show error message for any other exception
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        

    # start the script in a separate thread
    script_thread = threading.Thread(target=run_script_thread)
    script_thread.start()

def upload_file(file_num):
    file_path = filedialog.askopenfilename()
    os.makedirs('data', exist_ok=True)  # create folder if it doesn't exist
    if file_num == 1:
        new_file_path = os.path.join('data', 'course_raw_data.xlsx')
    elif file_num == 2:
        new_file_path = os.path.join('data', 'room_raw_data.xlsx')
    else:
        new_file_path = os.path.join('data', 'faculty_raw_data.xlsx')

    shutil.copy2(file_path, new_file_path)
    #print(f"Copied {file_path} to {new_file_path}")
    message = f"Copied and renamed {file_path} to {new_file_path}"
    # create a new window
    popup = tk.Toplevel()
    popup.title("Upload successful")
    popup.geometry("450x100")
    popup_label = tk.Label(popup, text=message, font=("Roboto", 12), wraplength=450)
    popup_label.pack(pady=10)
    #app.text_widget.insert("end", message + "\n")



frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, text="ASPAR", font=("Roboto", 20))
label_1.pack(pady=10, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, text="Upload Courses", font=("Roboto", 12), command=lambda:upload_file(1))
button_1.pack(pady=10, padx=10)

button_2 = customtkinter.CTkButton(master=frame_1, text="Upload Rooms", font=("Roboto", 12), command=lambda:upload_file(2))
button_2.pack(pady=10, padx=10)

button_3 = customtkinter.CTkButton(master=frame_1, text="Upload Faculty", font=("Roboto", 12), command=lambda:upload_file(3))
button_3.pack(pady=10, padx=10)

submit_button = customtkinter.CTkButton(master=frame_1, text="Run Program", font=("Roboto", 12), command=lambda:run_script())
submit_button.pack(pady=10, padx=10)

app.mainloop()
# In[ ]:




