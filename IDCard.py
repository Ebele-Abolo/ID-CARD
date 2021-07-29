# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 08:08:09 2021

@author: joyab
"""

from tkinter import*

root = Tk()
root.title("Identity Card")
root.geometry("300x400")

label_id = ()
label_name = ()
label_dob= ()
label_pin= ()
label_address= ()
label_vehicle= ()
def function():
    label_id = ("1973725837, Drivers licence: yes")
    print(label_id)
    label_name = ("Hank J. Wimbleton, license holder: wallet. ")
    print(label_name)
    label_dob = ("September 22, 1996, DOB holder: wallet. ")
    print(label_dob)
    label_pin = ("092296, pin holder wallet.")
    print(label_pin)
    label_address = ("92296, Nevada.")
    print(label_address)
    label_vehicle = ("four wheeler, car holder: garage.")
    print(label_vehicle)
    
btn1 = Button(root)
btn1 = Button(root, text="Who are you? ", command = random_number)
btn1.place(relx= 0.5, rely=0.5, anchor=CENTER ) 
root.mainloop()
