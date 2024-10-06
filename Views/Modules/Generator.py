import tkinter
import customtkinter
from typing import Any


class Generator:

    def __init__(self,
                 master: Any):

        self.general_frame = customtkinter.CTkFrame(master)
        pass

    def pack(self, **kwargs):
        self.general_frame.pack(**kwargs)
        pass

    def unpack(self):
        self.general_frame.pack_forget()
