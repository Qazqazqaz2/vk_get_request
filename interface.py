from tkinter import *
import webbrowser

import main


def callback(event):
    print(111)
    webbrowser.open_new(r"https://oauth.vk.com/authorize?client_id=2685278&scope=1073737727&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&revoke=1")
 
def str_to_sort_list(event):
    token = ent.get()
    token = token.split('access_token=')[-1]
    token = token.split('&')[0]
    try:
        text = ent_1.get(1.0,END)
        print(text)
    except Exception as e:
        print(e)
        text = 'Hi'
    main.main(token, text)



root = Tk()
root.geometry("500x500")

ent = Entry(width=100)
but = Button(text="Запуск бота")
lab = Label(width=100, fg='black', text='Введите ссылку полученную после разрешения')
lab_1 = Label(width=100, fg='black', text='Введите текст сообщения')

ent_1 = Text(width=100, height=10)

label = Label(root, text="Предоставить разрешение", fg="blue", cursor="hand2")

but.bind('<Button-1>', str_to_sort_list)
label.bind("<Button-1>", callback)

lab.pack()
label.pack()
ent.pack()
lab_1.pack()
ent_1.pack()
but.pack()

root.mainloop()
