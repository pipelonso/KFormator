import customtkinter
from typing import Union, Tuple, List, Optional, Any


class FloatingFrame:

    def __init__(self,
                 master: Any,
                 width: int = 300,
                 height: int = 200,
                 direction: str = 'center',  # up, down, center, left, right, up_left, up_right, down_left, down_right
                 x_padding: int = 2,
                 y_padding: int = 2,
                 corner_radius: Optional[Union[int, str]] = None,
                 border_width: Optional[Union[int, str]] = None,

                 bg_color: Union[str, Tuple[str, str]] = "transparent",
                 fg_color: Optional[Union[str, Tuple[str, str]]] = None,
                 border_color: Optional[Union[str, Tuple[str, str]]] = None,

                 background_corner_colors: Union[Tuple[Union[str, Tuple[str, str]]], None] = None,
                 overwrite_preferred_drawing_method: Union[str, None] = None
                 ):

        self.width = width
        self.height = height
        self.direction = direction
        if self.direction not in ['up', 'down', 'center', 'left', 'right',
                                  'up_left', 'up_right', 'down_left', 'down_right']:
            raise Exception('"' + self.direction + '" is not a compatible direction')

        self.master = master
        self.x_padding = x_padding
        self.y_padding = y_padding
        self.general_frame = customtkinter.CTkFrame(master,
                                                    width=width,
                                                    height=height,
                                                    corner_radius=corner_radius,
                                                    border_width=border_width,
                                                    bg_color=bg_color,
                                                    fg_color=fg_color,
                                                    border_color=border_color,
                                                    background_corner_colors=background_corner_colors,
                                                    overwrite_preferred_drawing_method=
                                                    overwrite_preferred_drawing_method
                                                    )
        self.showFrame = False
        self.register_bind()
        pass

    def register_bind(self):
        self.master.bind('<Configure>', self.on_bind)

    def on_bind(self, event):
        if self.showFrame:
            if self.direction == 'center':
                w_width = self.master.winfo_width()
                w_height = self.master.winfo_height()
                center_x_corner = (w_width / 2) - (self.width / 2)
                center_y_corner = (w_height / 2) - (self.height / 2)
                self.general_frame.place(x=center_x_corner, y=center_y_corner)
            elif self.direction == 'left':
                w_height = self.master.winfo_height()
                center_y_corner = (w_height / 2) - (self.height / 2)
                self.general_frame.place(x=self.x_padding, y=center_y_corner)
            elif self.direction == 'right':
                w_width = self.master.winfo_width()
                w_height = self.master.winfo_height()
                center_y_corner = (w_height / 2) - (self.height / 2)
                center_x_corner = w_width - self.width - self.x_padding
                self.general_frame.place(x=center_x_corner, y=center_y_corner)
            elif self.direction == 'down':
                w_width = self.master.winfo_width()
                w_height = self.master.winfo_height()
                center_x_corner = (w_width / 2) - (self.width / 2)
                center_y_corner = w_height - self.height - self.y_padding
                self.general_frame.place(x=center_x_corner, y=center_y_corner)
            elif self.direction == 'up':
                w_width = self.master.winfo_width()
                center_x_corner = (w_width / 2) - (self.width / 2)
                self.general_frame.place(x=center_x_corner, y=self.y_padding)
            elif self.direction == 'up_left':
                self.general_frame.place(x=self.x_padding, y=self.y_padding)
            elif self.direction == 'up_right':
                w_width = self.master.winfo_width()
                center_x_corner = w_width - self.width - self.x_padding
                self.general_frame.place(x=center_x_corner, y=self.y_padding)
            elif self.direction == 'down_left':
                w_height = self.master.winfo_height()
                center_y_corner = w_height - self.height - self.y_padding
                self.general_frame.place(x=self.x_padding, y=center_y_corner)
            elif self.direction == 'down_right':
                w_width = self.master.winfo_width()
                w_height = self.master.winfo_height()
                center_x_corner = w_width - self.width - self.x_padding
                center_y_corner = w_height - self.height - self.x_padding
                self.general_frame.place(x=center_x_corner, y=center_y_corner)
            pass
        pass

    def show(self):
        self.showFrame = True
        if self.direction == 'center':
            w_width = self.master.winfo_width()
            w_height = self.master.winfo_height()
            center_x_corner = (w_width / 2) - (self.width / 2)
            center_y_corner = (w_height / 2) - (self.height / 2)
            self.general_frame.place(x=center_x_corner, y=center_y_corner)
        elif self.direction == 'left':
            w_height = self.master.winfo_height()
            center_y_corner = (w_height / 2) - (self.height / 2)
            self.general_frame.place(x=self.x_padding, y=center_y_corner)
        elif self.direction == 'right':
            w_width = self.master.winfo_width()
            w_height = self.master.winfo_height()
            center_y_corner = (w_height / 2) - (self.height / 2)
            center_x_corner = w_width - self.width - self.x_padding
            self.general_frame.place(x=center_x_corner, y=center_y_corner)
        elif self.direction == 'down':
            w_width = self.master.winfo_width()
            w_height = self.master.winfo_height()
            center_x_corner = (w_width / 2) - (self.width / 2)
            center_y_corner = w_height - self.height - self.y_padding
            self.general_frame.place(x=center_x_corner, y=center_y_corner)
        elif self.direction == 'up':
            w_width = self.master.winfo_width()
            center_x_corner = (w_width / 2) - (self.width / 2)
            self.general_frame.place(x=center_x_corner, y=self.y_padding)
        elif self.direction == 'up_left':
            self.general_frame.place(x=self.x_padding, y=self.y_padding)
        elif self.direction == 'up_right':
            w_width = self.master.winfo_width()
            center_x_corner = w_width - self.width - self.x_padding
            self.general_frame.place(x=center_x_corner, y=self.y_padding)
        elif self.direction == 'down_left':
            w_height = self.master.winfo_height()
            center_y_corner = w_height - self.height - self.y_padding
            self.general_frame.place(x=self.x_padding, y=center_y_corner)
        elif self.direction == 'down_right':
            w_width = self.master.winfo_width()
            w_height = self.master.winfo_height()
            center_x_corner = w_width - self.width - self.x_padding
            center_y_corner = w_height - self.height - self.x_padding
            self.general_frame.place(x=center_x_corner, y=center_y_corner)

    def hide(self):
        self.showFrame = False
        self.general_frame.place_forget()

    def get_container(self):
        return self.general_frame
