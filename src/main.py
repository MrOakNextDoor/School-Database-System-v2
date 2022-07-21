
#   Libraries
import tkinter as tk

#   Code
class Main(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.overrideredirect(True)

        self.testlbl = tk.Label(self, text='HELLO WORLD', 
            font=('Bahnschrift', 12))

        self.mainloop()

if __name__ == '__main__':
    app = Main()