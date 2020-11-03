# this method is much easier and quicker, but since pyautogui is not a built-in module, the classic tkinter approach was also attempted.

from pyautogui import prompt, alert
h = prompt(text="Enter your height: ", title="Height calculator", default='')
alert(text=f"Your height is {h}!", title="Height calculator", button="OK")
