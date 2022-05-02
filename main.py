from mimetypes import add_type
import tkinter as tk
from tkinter import ttk
import os.path


class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)

        # Make the app responsive
        for index in [0, 1, 2]:
            self.columnconfigure(index=index, weight=1)
            self.rowconfigure(index=index, weight=1)

            # create controll variables
            self.playerName = 'player'
            self.playerScore = 0
            self.sharkScore = 0
            self.sharkNameScore = 'Shark: ' + str(self.sharkScore)
            self.playerNameScore = self.playerName + \
                ': ' + str(self.playerScore)
            self.level_val = tk.IntVar(value=2)

            self.buttonRowVal = 0
            self.buttonRow = 0
            self.var = 0
            self.buttons = []
            self.teiler = []
            self.button_int = 0
            self.button_int2 = 0

        # Create widgets :)
        self.setup_widgets()

    def setup_widgets(self):
        # create a Frame for the Levelbuttons
        self.levelbtn_Frame = ttk.LabelFrame(
            self, text='choose a Level', padding=(20, 10))
        self.levelbtn_Frame.grid(
            row=2, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew"
        )

        # create the Levelbuttons

        self.firstbtn = ttk.Radiobutton(self.levelbtn_Frame, text='Level 1',
                                        value=1, variable=self.level_val, command=self.destroyPlayground)
        self.firstbtn.grid(row=0, column=0, padx=(
            20, 10), pady=10, sticky="nsew")
        self.secondbtn = ttk.Radiobutton(
            self.levelbtn_Frame, text='Level 2', value=2, variable=self.level_val, command=self.destroyPlayground)
        self.secondbtn.grid(row=1, column=0, padx=(
            20, 10), pady=10, sticky="nsew")
        self.thirdbtn = ttk.Radiobutton(self.levelbtn_Frame, text='Level 3',
                                        value=3, variable=self.level_val, command=self.destroyPlayground)
        self.thirdbtn.grid(row=2, column=0, padx=(
            20, 10), pady=10, sticky="nsew")

        # create a Frame for the Score
        self.Score_frame = ttk.LabelFrame(self, text='Score', padding=(20, 10))
        self.Score_frame.grid(
            row=2, column=1, padx=(20, 10), pady=(20, 10), sticky='nsew'
        )

        # create Playerscore Entry
        self.Player_entry = ttk.Entry(self.Score_frame)
        self.Player_entry.insert(0, self.playerNameScore)
        self.Player_entry.grid(
            row=0, column=0, padx=5, pady=(0, 10), sticky="e"
        )
        self.Player_entry.configure(state='readonly')

        # create Sharkscore Entry
        self.Shark_entry = ttk.Entry(self.Score_frame,)
        self.Shark_entry.insert(0, self.sharkNameScore)
        self.Shark_entry.grid(
            row=1, column=0, padx=5, pady=(0, 10), sticky="nsew"
        )
        self.Shark_entry.configure(state='readonly')

        # create Frame for playground
        self.playground_frame = ttk.LabelFrame(
            self, text='Playground', padding=(20, 10))
        self.playground_frame.grid(
            row=0, column=0, columnspan=3, padx=(20, 10), pady=(20, 10), sticky='nsew'
        )

        # create playground
        self.createPlayground()

        # Separator
        self.separator2 = ttk.Separator(self)
        self.separator2.grid(row=1, column=0, columnspan=3,
                             padx=(20, 10), pady=10, sticky="ew")

        # create a Frame for the config
        self.config_frame = ttk.LabelFrame(
            self, text='Preferences', padding=(20, 10))
        self.config_frame.grid(
            row=2, column=2, padx=(20, 10), pady=(20, 10), sticky='nsew'
        )

        # Label
        self.namelabel = ttk.Label(
            self.config_frame,
            text="Your nickname",
            justify="center",
            font=("-size", 12, "-weight", "bold"),
        )
        self.namelabel.grid(row=0, column=0, pady=10, columnspan=2)

        # create playername entry
        self.pName_entry = ttk.Entry(self.config_frame,)
        self.pName_entry.insert(0, self.playerName)
        self.pName_entry.grid(
            row=1, column=0, padx=5, pady=(0, 10), sticky="ew"
        )
        self.pName_entry.bind('<Return>', self.updateName)

        # crate switch for theme mode
        self.apperanceSwitch = ttk.Checkbutton(
            self.config_frame, text='Lightmode', style='Switch.TCheckbutton', command=self.apperance
        )
        self.apperanceSwitch.grid(
            row=2, column=0, padx=5, pady=10, sticky="nsew")

        # create Quit-Button
        self.quit_button = ttk.Button(
            self.config_frame, text='EXIT', style='Accent.TButton', command=self.quit
        )
        self.quit_button.grid(row=3, column=0, padx=5, pady=5, sticky='nsew')

        # create Label win/lose screen
        self.label_ = ttk.Label(
            self,
            text='test',
            justify='center',
            font=("-size", 15, "-weight", "bold"),
        )

        




        # Sizegrip
        self.sizegrip = ttk.Sizegrip(self)
        self.sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))






    def apperance(self):
        if root.tk.call("ttk::style", "theme", "use") == "azure-dark":
            root.tk.call('set_theme', 'light')
        else:
            root.tk.call('set_theme', 'dark')

    def updateName(self, e):
        self.Player_entry.configure(state='normal')
        self.playerName = self.pName_entry.get()
        self.playerNameScore = self.playerName + ': ' + str(self.playerScore)
        self.Player_entry.delete(0, tk.END)
        self.Player_entry.insert(0, self.playerNameScore)
        self.Player_entry.configure(state='readonly')

    def updateScore(self, j):
        self.playerNameScore = self.playerName + ': ' + str(self.playerScore)
        self.Player_entry.config(state='normal')
        self.Player_entry.delete(0, tk.END)
        self.Player_entry.insert(0, self.playerNameScore)
        self.updateShark(j)

    def updateShark(self, j):
        #self.button_int = 0
        j = j+1
        self.i = 1
        while self.i <= j:
            if j % self.i == 0:
                Teiler = j//self.i
                if Teiler != j:
                    self.teiler.append(Teiler)
                    self.i = self.i+1
                    self.teiler = list(dict.fromkeys(self.teiler))

                else:
                    self.i = self.i+1
            else:
                self.i = self.i+1

        self.sharkScore = 0
        for item in range(len(self.buttons)):
            itemn = item+1

            for itm in self.teiler:

                itmn = itm+1
                if itmn == itemn and self.buttons[item-1]['text'] != '✘' and self.buttons[item-1]['text'] != '✔':

                    self.buttons[item-1].config(text='✘')
                    self.buttons[item-1].config(state='disabled')
                    self.sharkScore = self.sharkScore + item
                    self.sharkNameScore = f'Shark: {self.sharkScore}'
                    self.Shark_entry.config(state='normal')
                    self.Shark_entry.delete(0, tk.END)
                    self.Shark_entry.insert(0, self.sharkNameScore)
                    self.Shark_entry.config(state='readonly')
                    self.button_int += 1
        pass

    def destroyPlayground(self):
        for widget in self.playground_frame.winfo_children():
            widget.destroy()
        self.createPlayground()

    def disableButtons(self, j, var):

        for i in range(len(self.buttons)):
            if i == var:
                self.buttons[i].config(state='disabled')
                self.buttons[i].config(text='✔')
                self.playerScore = self.playerScore + int(j) + 1
                pass

    def createPlayground(self):
        self.var = 0
        self.buttons.clear()
        self.playgroundVal = self.level_val.get() * 10

        for j in range(self.playgroundVal):

            if self.buttonRowVal == 5:
                self.buttonRowVal = 0
                self.buttonRow = self.buttonRow + 1

            self.e = ttk.Button(self.playground_frame, text=j+1,
                                command=lambda var=self.var, j=j, : self.buttonClick(j, var))
            self.e.grid(row=self.buttonRow, column=self.buttonRowVal,
                        padx=(10), pady=(10), sticky='nsew')
            self.var += 1
            self.buttons.append(self.e)
            self.buttonRowVal = self.buttonRowVal + 1

    def end(self):
        self.top = tk.Toplevel()
        self.top.update()
        self.top.minsize(self.top.winfo_width(), self.top.winfo_height())
        x_cordinate = int((self.top.winfo_screenwidth() / 2) - (self.top.winfo_width() / 2))
        y_cordinate = int((self.top.winfo_screenheight() / 2) - (self.top.winfo_height() / 2))
        self.top.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))
        self.top.title('YOU WIN')
        # create Label win/lose screen
        self.label_ = ttk.Label(
            self.top,
            text='test',
            justify='center',
            font=("-size", 32, "-weight", "bold"),
        )
        if self.playerScore > self.sharkScore:
            self.win_screen()
        else:
            self.lose_screen()

    def buttonClick(self, j, var):
        self.button_int2 += 1

        self.firstbtn.config(state='disabled')
        self.secondbtn.config(state='disabled')
        self.thirdbtn.config(state='disabled')

        self.disableButtons(j, var)
        if (self.button_int + self.button_int2) == len(self.buttons):

            self.updateScore(j)
            self.end()
        else:
            self.updateScore(j)

    def quit(self):
        root.quit()

    def win_screen(self):
        # 'YOU WIN'
       
    
        
        self.label_['text'] = 'YOU WIN'
        self.label_.grid(row=1, column=0, padx=50, pady=70, columnspan=3)

    def lose_screen(self):
        # 'YOU LOSE'
        self.label_['text'] = 'YOU LOSE'
        self.label_.grid(row=1, column=0, padx=50, pady=70, columnspan=3)



if __name__ == '__main__':
    root = tk.Tk()
    root.title('Numb-Shark')

    # Simply set the theme
    dir_path = os.path.dirname(os.path.realpath(__file__))
    root.tk.call('source', os.path.join(dir_path, 'azure.tcl'))
    root.tk.call("set_theme", "dark")

    app = App(root)
    app.pack(fill="both", expand=True)

    # Set a minsize for the window, and place it in the middle
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) -
                      (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) -
                      (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))

    root.mainloop()
