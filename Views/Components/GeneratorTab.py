import customtkinter
import tkinter
from typing import Any


class GeneratorTab:

    def __init__(self,
                 master: Any,
                 name: str = 'Default tab name',
                 core: Any = None,
                 generator_class: Any = None):
        self.core = core
        general_button = customtkinter.CTkButton(master, text=name,
                                                 border_width=2,
                                                 corner_radius=0,
                                                 fg_color=('#282828', '#bebebe'),
                                                 border_color=('#282828', '#bebebe'),
                                                 hover_color=('#616161', '#cacaca'),
                                                 command=lambda: self.show_generator()
                                                 )
        general_button.pack(padx=2, pady=2, fill='x')
        self.generator_class = generator_class
        self.core.generators_list.append(generator_class)
        pass

    def show_generator(self):
        self.core.unpack_all_modules()
        self.generator_class.pack(padx=2, pady=2, fill='both', expand=True)
        pass
