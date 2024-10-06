import tkinter
import customtkinter
from typing import Any
from PIL import Image


class Welcome:

    def __init__(self,
                 master: Any
                 ):
        self.general_frame = customtkinter.CTkFrame(master)
        self.generators_list_container = None

        image_path = "Resources/Images/KFORMATOR LOGO.png"
        image = customtkinter.CTkImage(light_image=Image.open(image_path), size=(571, 181))

        up_frame = customtkinter.CTkFrame(self.general_frame, fg_color='transparent')
        up_frame.pack(padx=0, pady=0, fill='both', expand=True)

        centered_frame = customtkinter.CTkFrame(self.general_frame, fg_color='transparent')
        centered_frame.pack(padx=0, pady=0, fill='both', expand=True)

        down_frame = customtkinter.CTkFrame(self.general_frame, fg_color='transparent')
        down_frame.pack(padx=0, pady=0, fill='both', expand=True)

        label = customtkinter.CTkLabel(centered_frame, image=image, text="")
        label.pack(pady=20)

        general_description_label = customtkinter.CTkLabel(centered_frame,
                                                           text='Kformator es una aplicación sideñada para formatear'
                                                                'listas en forma de codigo.')
        general_description_label.pack(padx=2, pady=2, fill='both')

        buttons_frame = customtkinter.CTkFrame(centered_frame, fg_color='transparent')
        buttons_frame.pack(padx=2, pady=2)

        new_generator_button = customtkinter.CTkButton(buttons_frame, text='+ Nuevo formateador',
                                                       border_width=2,
                                                       corner_radius=0,
                                                       fg_color=('#282828', '#bebebe'),
                                                       border_color=('#282828', '#bebebe'),
                                                       hover_color=('#616161', '#cacaca'),
                                                       command=lambda: self.make_new_generator()
                                                       )
        new_generator_button.pack(padx=2, pady=2, side=tkinter.LEFT)

        load_generator_button = customtkinter.CTkButton(buttons_frame,  text='Cargar desde un archivo',
                                                        border_width=2,
                                                        corner_radius=0,
                                                        fg_color=('#282828', '#bebebe'),
                                                        border_color=('#282828', '#bebebe'),
                                                        hover_color=('#616161', '#cacaca')
                                                        )

        load_generator_button.pack(padx=2, pady=2, side=tkinter.RIGHT)

        pass

    def pack(self, **kwargs):
        self.general_frame.pack(**kwargs)
        pass

    def unpack(self):
        self.general_frame.pack_forget()

    def make_new_generator(self):

        generator_button = customtkinter.CTkButton(self.generators_list_container, text='text')
        generator_button.pack(padx=2, pady=2, fill='x')

        pass

    def set_list_container(self, container: customtkinter.CTkScrollableFrame):
        self.generators_list_container = container
        pass

