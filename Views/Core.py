import tkinter
import customtkinter
from Views.Modules.welcome import Welcome
from Views.Modules.Generator import Generator
from Views.Components.FloatingFrame import FloatingFrame


class Core:

    def __init__(self):
        app = customtkinter.CTk()
        app.geometry('1000x600')

        self.generators_list = []

        general_frame = customtkinter.CTkFrame(app)
        general_frame.pack(padx=2, pady=2, fill='both', expand=True)

        sidebar = customtkinter.CTkFrame(general_frame)
        sidebar.pack(side=tkinter.LEFT, padx=2, pady=2, fill='y')

        general_content_frame = customtkinter.CTkFrame(general_frame)
        general_content_frame.pack(padx=2, pady=2, fill='both', expand=True)

        tittle_label = customtkinter.CTkLabel(sidebar, text='KFORMATOR')
        tittle_label.pack(padx=2, pady=2, fill='x')

        self.main_button = customtkinter.CTkButton(sidebar, text='INICIO',
                                                   command=lambda: self.show_welcome(),
                                                   border_width=2,
                                                   corner_radius=0,
                                                   fg_color=('#282828', '#bebebe'),
                                                   border_color=('#282828', '#bebebe'),
                                                   hover_color=('#616161', '#cacaca')
                                                   )
        self.main_button.pack(padx=5, pady=2, fill='x')

        open_generators_list_frame = customtkinter.CTkScrollableFrame(sidebar, corner_radius=0)
        open_generators_list_frame.pack(padx=5, pady=5, fill='both', expand=True)

        self.welcome = Welcome(general_content_frame, core=self)
        self.welcome.set_list_container(open_generators_list_frame)

        self.generator = Generator(general_content_frame)

        self.show_welcome()

        app.mainloop()
        pass

    def show_welcome(self):
        self.unpack_all_modules()
        self.welcome.pack(padx=2, pady=2, fill='both', expand=True)
        pass

    def show_generator(self):
        self.unpack_all_modules()
        self.generator.pack(padx=2, pady=2, fill='both', expand=True)
        pass

    def unpack_all_modules(self):
        for generator in self.generators_list:
            generator.unpack()
        self.welcome.unpack()
        pass
