import ctypes
import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()

ROOT.withdraw()
h = simpledialog.askstring(title="Height Calculator Tool", prompt="Enter your height with units: ")

ctypes.windll.user32.MessageBoxW(0, f"Your height is {h}!", "Height Calculator Tool", 0)
