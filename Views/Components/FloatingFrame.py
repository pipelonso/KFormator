import customtkinter
from typing import Any


class FloatingFrame:

    def __init__(self,
                 master: Any):
        self.master = master
        self.general_frame = customtkinter.CTkFrame(master)
        self.showFrame = False
        self.register_bind()
        pass

    def register_bind(self):
        self.master.bind('<Configure>', self.on_bind)

    def on_bind(self, event):
        if self.showFrame:

            pass
        pass

    def show(self):
        self.showFrame = True
