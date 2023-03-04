from tkinter import *
from main import HashPath


def save_hash():
    h = str(txt.get())
    obj = HashPath()

    obj.add_hash(h)


def delete_hash():
    h = str(txt.get())
    obj = HashPath()

    obj.remove_hash(f'hash/{h}')


def change_index():
    New_window = Toplevel(window)
    New_window.geometry('450x350')
    lbl = Label(New_window, text="Сhange index")
    lbl.grid(column=0, row=0)

    def change():
        index = str(txt_new_1.get())
        index_new = str(txt_new_2.get())

        obj = HashPath()
        obj.change_index(index, index_new)

    txt_new_1 = Entry(New_window, width=70)
    txt_new_1.grid(column=0, row=1)

    txt_new_2 = Entry(New_window, width=70)
    txt_new_2.grid(column=0, row=2)

    btn_new = Button(New_window, text="Сhange index", command=change)
    btn_new.grid(column=0, row=5)



window = Tk()
window.geometry('650x550')
window.title("Hash_path")

lbl = Label(window, text="Hash_path")
lbl.grid(column=0, row=0)

txt = Entry(window, width=70)
txt.grid(column=0, row=2)

btn = Button(window, text="Hash and save", command=save_hash)
btn.grid(column=0, row=3)

btn_1 = Button(window, text="Delete hash_file", command=delete_hash)
btn_1.grid(column=0, row=4)

btn_2 = Button(window, text="Сhange index", command=change_index)
btn_2.grid(column=0, row=5)

txt_edit = Text(window, width=81)
txt_edit.grid(column=0, row=6)


window.mainloop()