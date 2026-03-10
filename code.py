from tkinter import *

def quit():
    main_window.destroy()

def print_names():
    name_count = 0
    Label(main_window, font='bold', text="Row").grid(column=0,row=6)
    Label(main_window, font='bold', text="Full Name").grid(column=1,row=6)
    Label(main_window, font='bold', text="Item needed").grid(column=2,row=6)
    Label(main_window, font='bold', text="Amount of needed item")
    Label(main_window, font='bold', text="Date of hire").grid(column=3, row=6)
    Label(main_window, fon='bold', text="Date of retrn").grid(column=4,row=6)





def entry_print():
    Label(main_window, text= entry_first_name.get()) .grid(column=0,row=3, sticky=E)
    Label(main_window, text= entry_last_name.get()) .grid(column=1,row=3,sticky=E)

def main():
    Button(main_window, text="Quit",command=quit) .grid(column=0,row=0)
    Button(main_window, text="Print", command = entry_print) .grid(column=1, row=3, sticky=W)
    Label(main_window, text="First Name") .grid(column=0,row=1)

main_window =Tk()
main()