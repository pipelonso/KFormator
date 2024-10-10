import tkinter
import customtkinter
from typing import Any
from Views.Components.FloatingFrame import FloatingFrame


class Generator:

    def __init__(self,
                 master: Any):

        self.is_show_asset_menu = False

        self.general_frame = customtkinter.CTkFrame(master)

        sup_bar = customtkinter.CTkFrame(self.general_frame, fg_color=('black', 'white'))
        sup_bar.pack(padx=5, pady=5, fill='x')

        add_button = customtkinter.CTkButton(sup_bar, text='+',
                                             fg_color=('white', 'black'),
                                             width=30,
                                             height=30,
                                             text_color=('black', 'white'),
                                             command=lambda: self.show_asset_menu())
        add_button.pack(padx=2, pady=2, side=tkinter.LEFT)

        self.asset_menu = FloatingFrame(self.general_frame, y_padding=45,
                                        x_padding=5,
                                        direction='up_left',
                                        border_width=2,
                                        border_color=('black', 'white')
                                        )

        asset_buttons_frame = customtkinter.CTkFrame(self.asset_menu.get_container(),
                                                     border_width=2,
                                                     border_color=('black', 'white'))
        asset_buttons_frame.pack(padx=5, pady=5, fill='y', side=tkinter.LEFT, expand=True)

        asset_example_frame = customtkinter.CTkFrame(self.asset_menu.get_container())
        asset_example_frame.pack(padx=5, pady=5, fill='both', side=tkinter.RIGHT, expand=True)

        code_list_button = customtkinter.CTkButton(asset_buttons_frame, text='[ ]',
                                                   text_color=('black', 'white'),
                                                   border_width=2,
                                                   border_color=('black', 'white'),
                                                   width=30, height=30,
                                                   fg_color=('white', 'black'),
                                                   hover_color='gray'
                                                   )
        code_list_button.pack(padx=5, pady=5)

        code_line_button = customtkinter.CTkButton(asset_buttons_frame, text='>_',
                                                   text_color=('black', 'white'),
                                                   border_width=2,
                                                   border_color=('black', 'white'),
                                                   width=30, height=30,
                                                   fg_color=('white', 'black'),
                                                   hover_color='gray'
                                                   )
        code_line_button.pack(padx=5, pady=5)

        code_list_loop_button = customtkinter.CTkButton(asset_buttons_frame, text='⟲',
                                                        text_color=('black', 'white'),
                                                        border_width=2,
                                                        border_color=('black', 'white'),
                                                        width=30, height=30,
                                                        fg_color=('white', 'black'),
                                                        hover_color='gray'
                                                        )
        code_list_loop_button.pack(padx=5, pady=5)

        self.default_info_frame = customtkinter.CTkFrame(asset_example_frame)
        self.default_info_frame.pack(padx=2, pady=2, fill='both', expand=True)

        info_frame_welcome_emote = customtkinter.CTkLabel(self.default_info_frame, text='૮･ﻌ･ა', font=('Arial', 40))
        info_frame_welcome_emote.pack(padx=5, pady=5, fill='x')

        asset_wb_message_info_frame = customtkinter.CTkLabel(self.default_info_frame, text='La información de cada '
                                                                                           'componente aparecera aqui')
        asset_wb_message_info_frame.pack(padx=5, pady=5, fill='x')
        pass

    def pack(self, **kwargs):
        self.general_frame.pack(**kwargs)
        pass

    def unpack(self):
        self.general_frame.pack_forget()

    def show_asset_menu(self):
        if not self.is_show_asset_menu:
            self.asset_menu.show()
            self.is_show_asset_menu = True
        else:
            self.asset_menu.hide()
            self.is_show_asset_menu = False
