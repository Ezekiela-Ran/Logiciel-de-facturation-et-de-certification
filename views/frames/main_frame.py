import customtkinter
from views.frames.head_frame import HeadFrame
from views.frames.body_frame import BodyFrame
from views.frames.foot_frame import FootFrame
from views.foundation.styles import Styles

class MainFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        
        styles = Styles()
        
        super().__init__(master)

        self.pack(fill="both", expand=True, padx=styles.padx, pady=styles.pady)

        # Têtes du cadre principal
        self.head_frame = HeadFrame(self)
        self.head_frame.pack(fill="both", expand=True, pady=styles.pady, side="top")
        
        # Corps du cadre principal
        self.body_frame = BodyFrame(self)
        self.body_frame.pack(fill="both", expand=True, pady=styles.pady, side="top")

        # Pied du cadre principal
        self.foot_frame = FootFrame(self)
        self.foot_frame.pack(fill="both", expand=True, pady=styles.pady, side="bottom")
    