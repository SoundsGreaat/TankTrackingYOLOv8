import tkinter as tk
from tkinter import filedialog, ttk
from ttkthemes import ThemedTk
from track_objects import track_objects


def select_file():
    filename = filedialog.askopenfilename(filetypes=[('Video files', '*.mp4;*.avi;*.mov')])
    if filename:
        root.destroy()
        track_objects(filename)


root = ThemedTk(theme='breeze')
root.title('Tank Tracking App')
root.geometry('250x75')

select_file_button = ttk.Button(root, text='Select Video File', command=select_file)
select_file_button.pack(side=tk.TOP, pady=20)

root.mainloop()
