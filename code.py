from tkinter import *

def quit():
    main_window.destroy()

def entry_print():
    print(entry_first_name.get())
    print(entry_last_name.get())

def main():
    Button(main_window, text="Quit", command=quit) .grid()
    Button(main_window, text="Print", command=entry_print) .grid

main_window = Tk()
entry_first_name = Entry(main_window)
entry_first_name.grid()

entry_last_name = Entry(main_window)
entry_last_name.grid()

main()