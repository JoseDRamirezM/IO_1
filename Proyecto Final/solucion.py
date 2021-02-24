import sys
import tkinter as tk

class StdOutRedirect:
    def __init__(self,  text: tk.Text) -> None:
        self._text = text

    def write(self,  out: str) -> None:
        self._text.insert(tk.END,  out)


class VentanaResultados(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent,  *args, **kwargs)
        self.stdout_text = tk.Text(
            self,  bg="black",  fg="#38B179",  font=("Helvetica", 15))
        self.stdout_text.pack(expand=True, fill=tk.BOTH)
        sys.stdout = StdOutRedirect(self.stdout_text)