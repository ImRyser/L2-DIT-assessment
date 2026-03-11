from tkinter import*

def quit():
    main_window.destroy()

def entry_print():
    Label(main_window, text= entry_first_name.get()).grid(column=0,row=3,sticky=E)
    Label(main_window, text= entry_last_name.get()).grid(column=0,row=3,sticky=W)

def main():
    Button(main_window, text="Quit", command=quit).grid(column=0,row=0)
    Button(main_window, text="Print",command=entry_print).grid(column=1,row=0)
    Label(main_window, text="First name").grid(column=0,row=1)
    Label(main_window, text="Last Name").grid(column=0,row=2)
    main_window.mainloop()

main_window =Tk()
entry_first_name = Entry(main_window)
entry_first_name.grid(column=1,row=1,padx=10,pady=5)
entry_last_name = Entry(main_window)
entry_last_name.grid(column=1,row=2,padx=10,pady=5)
main()