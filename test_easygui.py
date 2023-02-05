#import tkinter as tk
import easygui

easygui.msgbox("Witaj w easyGUI.")

flavor = easygui.buttonbox("Twój ulubiony smak?",
              choices = ['Waniljowe', 'Czekoladowe', 'Truskawkowe'] )
easygui.msgbox("Wybrałes: " + flavor)

flavor = easygui.choicebox("Twój ulubiony smak?",
              choices = ['Waniljowe', 'Czekoladowe', 'Truskawkowe'] )
easygui.msgbox("Wybrałes: " + flavor)

flavor = easygui.enterbox("Twój ulubiony smak?", default="Waniljowe")
easygui.msgbox("Wybrałes: " + flavor)