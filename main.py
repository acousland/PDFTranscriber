import tkinter as tk
from tkinter import filedialog
import subprocess
import os

def open_file():
    global file_path
    file_path = filedialog.askopenfilename()

def run_ocrmypdf():
    output_text_path = os.path.splitext(file_path)[0] + '.txt'
    output_pdf_path = os.path.splitext(file_path)[0] + '_ocr.pdf'
    subprocess.run(['ocrmypdf', '--redo-ocr', '--sidecar', output_text_path, file_path, output_pdf_path])
    display_output_text(output_text_path)

def display_output_text(output_text_path):
    with open(output_text_path, 'r') as file:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, file.read())

root = tk.Tk()

file_path = ''

open_file_button = tk.Button(root, text='Open File', command=open_file)
open_file_button.pack()

output_text = tk.Text(root)
output_text.pack()

run_button = tk.Button(root, text='Run ocrmypdf', command=run_ocrmypdf)
run_button.pack()

root.mainloop()