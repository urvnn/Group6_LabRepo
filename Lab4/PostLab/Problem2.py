#tested on desktop via VSCode

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select a Text File",
    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
)

if file_path:
    print(f"Selected file: {file_path}")
else:
    print("No file selected.")
