import tkinter
import customtkinter
from typing import Any
from PIL import Image
from Views.Components.FloatingFrame import FloatingFrame
from Views.Components.GeneratorTab import GeneratorTab
from Views.Modules.Generator import Generator


class Welcome:

    def __init__(self,
                 master: Any,
                 core: Any
                 ):
        self.core = core
        self.master = master
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
                                                       command=lambda: self.show_create_window()
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

        self.creation_window = FloatingFrame(master,
                                             border_width=2,
                                             border_color=('black', 'white'),
                                             width=500,
                                             height=100)

        self.cw_content = self.creation_window.get_container()
        self.create_input = None
        self.generate_cw_content()

        pass

    def pack(self, **kwargs):
        self.general_frame.pack(**kwargs)
        pass

    def unpack(self):
        self.general_frame.pack_forget()

    def make_new_generator(self):
        generator = Generator(self.master)
        generator_button = GeneratorTab(self.generators_list_container,
                                        name=self.create_input.get(),
                                        core=self.core,
                                        generator_class=generator)

        pass

    def set_list_container(self, container: customtkinter.CTkScrollableFrame):
        self.generators_list_container = container
        pass

    def show_create_window(self):
        self.creation_window.show()

    def hide_create_window(self):
        self.creation_window.hide()

    def generate_cw_content(self):
        control_frame = customtkinter.CTkFrame(self.cw_content, fg_color='transparent')
        control_frame.pack(padx=2, pady=4, fill='x')
        close_button = customtkinter.CTkButton(control_frame, text='-',
                                               anchor='e',
                                               fg_color='transparent',
                                               text_color='gray',
                                               width=15,
                                               hover_color=('black', 'white'),
                                               font=('Arial', 20),
                                               corner_radius=5,
                                               command=lambda: self.hide_create_window())

        close_button.pack(padx=0, pady=0, side=tkinter.RIGHT)
        creation_label = customtkinter.CTkLabel(self.cw_content, text='CREAR UN NOMBRE PARA EL FORMATEADOR', width=500)
        creation_label.pack(padx=5, pady=5, fill='x')

        self.create_input = customtkinter.CTkEntry(self.cw_content, corner_radius=2, border_color=('black', 'white'))
        self.create_input .pack(padx=5, pady=5, fill='x')

        create_button = customtkinter.CTkButton(self.cw_content, text='CREAR',
                                                border_width=2,
                                                corner_radius=0,
                                                fg_color=('#282828', '#bebebe'),
                                                border_color=('#282828', '#bebebe'),
                                                hover_color=('#616161', '#cacaca'),
                                                command=lambda: self.make_new_generator()
                                                )

        create_button.pack(padx=5, pady=5, fill='x')

        pass
