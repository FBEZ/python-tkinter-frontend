import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from script import my_script

opened_filename = ""
selected_option = ""

def run_script():
    my_script(file_label["text"], selected.get())
    
# Main window creation
root = tk.Tk()
root.title('Open File Dialog')
root.resizable(False, False)
root.iconbitmap("myIcon.ico")
root.geometry('300x150')
selected = tk.StringVar()

# label showing the filename
file_label = tk.Label(text="<Select a file>")


# run button, disable before finding file
run_button = ttk.Button(
    root,
    text='Run Script',
    command=run_script,
    state="disabled"
)

def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Choose file',
        initialdir='/',
        filetypes=filetypes)
    
    if(filename!=''): # valid filename selected
        file_label["text"] = filename
        run_button["state"]="normal"
        opened_filename=filename
        selected_option=selected.get()


# open button
open_button = ttk.Button(
    root,
    text='Open a File',
    command=select_file
)




file_label.pack(expand=True)
open_button.pack(expand=True)
# Radio button for choice. "text" is what is shown on the gui, "value" is the value passed to the variable
r1 = ttk.Radiobutton(root, text='Option 1', value='Value 1', variable=selected)
selected.set("Value 1")
r2 = ttk.Radiobutton(root, text='Option 2', value='Value 2', variable=selected)
r3 = ttk.Radiobutton(root, text='Option 3', value='value 3', variable=selected)
r1.pack()
r2.pack()
r3.pack()
#run button
run_button.pack(expand=True)

# run the application
root.mainloop()

