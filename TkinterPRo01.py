import os.path
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


class MainUI(tk.Tk) :

    def __init__(self) :
        super().__init__()
        self.title('App')

    @classmethod
    def PressedLogin(cls) :
        root = Tk()
        root.title('Data Extraction App')
        root.geometry('1000x750')

        Label(root,text='Data Extraction GUI',font="Raleway",bg="#FFFFFF",fg="Black",height=2,width=68).place(
            x=50,y=50)

        variable = StringVar(root)
        variable.set("one")  # default value

        w = OptionMenu(root,variable,"one","two","three")
        w.place(x=50,y=70)

        instructions = Text(root,font="Raleway",borderwidth=6,relief="groove",bg="#FFFFFF",fg="black",height=2,width=50)
        instructions.place(x=250,y=150)
        instructions02 = Text(root,font="Raleway",borderwidth=6,relief="groove",bg="#FFFFFF",fg="black",height=2,
                              width=50)
        instructions02.place(x=250,y=300)
        instructions03 = Text(root,font="Raleway",borderwidth=6,relief="groove",bg="#FFFFFF",fg="black",height=2,
                              width=50)
        instructions03.place(x=250,y=450)

        def XlsxButton() :
            brwoseText.set('Loading...')
            file = filedialog.askopenfilename(parent=root,title="Choose a file",
                                              filetypes=[('All files','*.*'),("Xlsx files","*.xlsx")])
            if file :
                if os.path.splitext(file) != '.xlsx' :
                    messagebox.showinfo('Alert','Selected file has no xlsx format')
                else :
                    instructions.insert(END,file)
                brwoseText.set('Load Xlsx')

        def DocxButton() :
            brwoseText02.set('Loading...')
            file = filedialog.askopenfilename(parent=root,title="Choose a file",
                                              filetypes=[('All files','*.*'),("Docx files","*.docx")])
            if file :
                if os.path.splitext(file) != '.docx' :
                    messagebox.showinfo('Alert','Selected file has no docx format')
                else :
                    instructions02.insert(END,file)
                brwoseText02.set('Load Docx')

        def FolderButton() :
            brwoseText03.set('Loading...')
            file = filedialog.askdirectory()
            if file :
                instructions03.insert(END,file)
                brwoseText03.set('Destination')

        brwoseText = StringVar()
        brwoseText_btn = Button(root,textvariable=brwoseText,borderwidth=2,relief="groove",
                                command=lambda : XlsxButton(),font="Raleway",bg="#20bebe",fg="black",height=2,width=15)

        brwoseText02 = StringVar()
        brwoseText_btn02 = Button(root,textvariable=brwoseText02,borderwidth=2,relief="groove",
                                  command=lambda : DocxButton(),font="Raleway",bg="#FFFFFF",fg="Black",height=2,
                                  width=15)

        brwoseText03 = StringVar()
        brwoseText_btn03 = Button(root,textvariable=brwoseText03,borderwidth=2,relief="groove",
                                  command=lambda : FolderButton(),font="Raleway",bg="#20bebe",fg="black",height=2,
                                  width=15)

        SubmitButton_Text = StringVar()
        SubmitButton = Button(root,textvariable=SubmitButton_Text,borderwidth=2,relief="groove",
                              command=lambda : FolderButton(),font="Raleway",bg="#20bebe",fg="black",height=2,width=15)
        #
        brwoseText.set('Load Xlsx')
        brwoseText_btn.place(x=50,y=150)

        brwoseText02.set('Load Docx')
        brwoseText_btn02.place(x=50,y=300)

        brwoseText03.set('Destination')
        brwoseText_btn03.place(x=50,y=450)

        SubmitButton_Text.set('Submit')
        SubmitButton.place(x=640,y=550)

        root.mainloop()


if __name__ == '__main__' :
    MainUI.PressedLogin()
