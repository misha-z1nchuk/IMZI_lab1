from tkinter import *
from PIL import ImageTk, Image
import os


def get_dict(adict):
    return '\n'.join('%s %s' % t for t in adict.items())


def adjust_string(str):
    tmp = str.split(' ')
    res = "".join(tmp[0].split('_'))
    return res + tmp[2]


switch_case = dict([
    (5, u'Result: Barack Obama'),
    (4, u'Result: Elon Musk'),
    (3, u'Result: Jeff Bezos'),
    (2, u'Result: Mark Zuckerberg'),
    (1, u'Result: Steve Jobs'),
    (0, u'Result: Volodymyr Zelensky')
])


class View:
    def __init__(self, yh, path):
        self.Yh = yh
        self.path = path
        self._window = self._set_window()
        self._textboxresults = self._set_results()
        self._textbox_mainresult = self._set_mainresult()
        self.button = self.set_button()
        self.lst_click = os.listdir("../Base/training/")
        self.clicks = -1
        self.num_ph = 1
        self.click_button()
        self._window.mainloop()

    def set_yh(self, yh):
        self.yh = yh

    def click_button(self):
        if self.clicks == len(self.path) - 1:
            self.clicks = 0
        else:
            self.clicks += 1
        self.show_results(dict([
            (' ', 'Match percentage'),
            (u'Barack Obama: ', '{:.2f}'.format(self.Yh[5][self.clicks]) + "%"),
            (u'Elon Musk: ', '{:.2f}'.format(self.Yh[4][self.clicks]) + "%"),
            (u'Jeff Bezos: ', '{:.2f}'.format(self.Yh[3][self.clicks]) + "%"),
            (u'Mark Zuckerberg: ', '{:.2f}'.format(self.Yh[2][self.clicks]) + "%"),
            (u'Steve Jobs: ', '{:.2f}'.format(self.Yh[1][self.clicks]) + "%"),
            (u'Volodymyr Zelensky: ', '{:.2f}'.format(self.Yh[0][self.clicks]) + "%")
        ]))
        temp = self.Yh[0][self.clicks]
        pers = 0
        for j in range(0, 5):
            if temp < self.Yh[j + 1][self.clicks]:
                temp = self.Yh[j + 1][self.clicks]
                pers = j + 1

        self.show_main_result(str(switch_case.get(pers)))
        self.show_picture(self.path[self.clicks])
        self._window.mainloop()

    def _set_window(self):
        window = Tk()
        window.title("Lab1_IMZI")
        window.geometry("745x450")
        window.resizable(width=False, height=False)
        window.configure(bg='#3f8c4b')
        return window

    def _set_results(self):
        textbox = Label(font="Arial 16", pady="20", justify=LEFT)
        textbox.config(bg="#3f8c4b")
        textbox.place(x=410, y=0)
        return textbox

    def _set_mainresult(self):
        textbox = Label(font="Arial 22", pady="5", width="23")
        textbox.config(bg="#3f8c4b")
        textbox.place(x=1, y=300)
        return textbox

    def set_button(self):
        btn1 = Button(text="Next Picture", background="#ad8e8e", foreground="#fff",
                      padx="15", font="Arial 20", width=24, height=2, command=self.click_button)
        btn1.place(x=200, y=360)
        return btn1

    def show_picture(self, path):
        img = Image.open(path)
        img = img.resize((350, 300), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(self._window, image=img)
        panel.image = img
        panel.place(x=0, y=0)

    def show_results(self, adict):
        self._textboxresults.config(text=str(get_dict(adict)))

    def show_main_result(self, mainresult):
        self._textbox_mainresult.config(text=mainresult)
