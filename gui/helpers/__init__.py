import tkinter as ttk
from tkinter.constants import *
def create_form_entry(mst,label,variable):
    form_field_container = ttk.Frame(master=mst)
    form_field_container.pack(fill=X,expand=YES,pady=5)
    
    form_field_label = ttk.Label(master=form_field_container,text=label,width=15)
    form_field_label.pack(side=LEFT,padx=12)
    
    form_input = ttk.Entry(master=form_field_container,textvariable=variable)
    form_input.setvar(value=variable.get())
    form_input.pack(side=LEFT,padx=5,fill=X,expand=YES)
    return form_input

def create_submit_button(frame,buttonValue,action=None):
    submitButton = ttk.Button(frame,text=buttonValue,command=action)
    submitButton.pack(pady=5)
    return submitButton