
from tkinter import *

root = Tk()

'''
Napisz program, składający się z 7-iu przycisków, kolory których odpowiadają tęczy. Przy kliknięciu na przycisk w polu tekstowym wyświetla się
kod koloru a w Entry nazwa koloru.

#ff0000: czerwony
#ff7d00: pomarańczowy
#ffff00: żółty
#00ff00: zielony
#007dff: niebieski
#0000ff: granatowy
#7d00ff: fioletowy
'''

colors = {
    "#ff0000": "czerwony",
    "#ff7d00": "pomarańczowy",
    "#ffff00": "żółty",
    "#00ff00": "zielony",
    "#007dff": "niebieski",
    "#0000ff": "granatowy",
    "#7d00ff": "fioletowy",
}


class MyButtons:

    def __init__(self, master, text_color, hex_color):
        self.text_color = text_color
        self.hex_color = hex_color
        self.b = Button(root, bg=hex_color, command=self.get_color)
        self.b.pack(fill=X)

    def get_color(self):
        l['text'] = self.text_color
        e.delete(0, END)
        e.insert(0, self.hex_color)


l = Label(root)
e = Entry(root, width=30, justify='center')
l.pack()
e.pack()

for k, v in colors.items():
    MyButtons(root, v, k)


root.mainloop()
