import customtkinter as ctk
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from controller.controller import Controller

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# (label, row, col, colspan)
BUTTON_LAYOUT = [
    ("DEL", 1, 0, 3), ("÷",   1, 3, 1),
    ("7",   2, 0, 1), ("8",   2, 1, 1), ("9",   2, 2, 1), ("×",   2, 3, 1),
    ("4",   3, 0, 1), ("5",   3, 1, 1), ("6",   3, 2, 1), ("−",   3, 3, 1),
    ("1",   4, 0, 1), ("2",   4, 1, 1), ("3",   4, 2, 1), ("+",   4, 3, 1),
    (".",   5, 0, 1), ("0",   5, 1, 1), ("=",   5, 2, 2),
]

BTN  = 68
PAD  = 4
COLS = 4

COLORS = {
    "operator": ("#c2410c", "#ea580c"),
    "equals":   ("#3730a3", "#4338ca"), 
    "delete":   ("#0f172a", "#1e293b"), 
    "digit":    ("#0f172a", "#1e293b"), 
}


FRAME_W = (BTN * COLS) + (PAD * (COLS - 1))


class App(ctk.CTk):
    def __init__(self, controller=None):
        super().__init__()
        self.title("Calculator")
        self.resizable(False, False)
        self.configure(fg_color="#080c14")
        self._controller = controller

        container = ctk.CTkFrame(self, fg_color="transparent", width=FRAME_W)
        container.pack(padx=PAD * 2, pady=PAD * 2)
        container.pack_propagate(False)
        container.configure(height=1)  # let children define height
        container.pack_propagate(True)

        self._build_display(container)
        self._build_buttons(container)

    def set_controller(self, controller):
        self._controller = controller

    def set_expression(self, text: str):
        self.expression.configure(text=text)

    def get_expression(self) -> str:
        return self.expression.cget("text")

    def get_display(self) -> str:
        return self.display.cget("text")

    def set_display(self, text: str):
        self.display.configure(
            text=text,
            text_color="#ffffff",
            font=ctk.CTkFont(size=52, weight="normal"),
        )

    def set_error(self, e: Exception):
        self.display.configure(
            text=str(e),
            text_color="#ef4444",
            font=ctk.CTkFont(size=18, weight="normal"),
        )

    def _build_display(self, parent):
        display_frame = ctk.CTkFrame(
            parent, fg_color="#13131a",
            corner_radius=18,
            border_width=1,
            border_color="#23233a",
            width=FRAME_W,
            height=118,
        )
        display_frame.pack(fill="x", pady=(0, PAD))
        display_frame.pack_propagate(False)

        self.expression = ctk.CTkLabel(
            display_frame, text="", anchor="e",
            font=ctk.CTkFont(size=15),
            text_color="#52526e",
            fg_color="transparent",
        )
        self.expression.pack(padx=14, pady=(12, 0), fill="x")

        self.display = ctk.CTkLabel(
            display_frame, text="0", anchor="e",
            font=ctk.CTkFont(size=52, weight="normal"),
            text_color="#ffffff",
            fg_color="transparent",
        )
        self.display.pack(padx=14, pady=(0, 12), fill="x")

    def _build_buttons(self, parent):
        btn_frame = ctk.CTkFrame(parent, fg_color="transparent", width=FRAME_W)
        btn_frame.pack()

        for (label, row, col, colspan) in BUTTON_LAYOUT:
            is_op  = label in {"÷", "×", "−", "+"}
            is_eq  = label == "="
            is_del = label == "DEL"

            key = "operator" if is_op else "equals" if is_eq else "delete" if is_del else "digit"
            fg, hover = COLORS[key]
            txt_color = "#ef4444" if is_del else "#e2e8f0"
            font_size = 18 if is_del else 22

            w = (BTN * colspan) + (PAD * (colspan - 1))

            btn = ctk.CTkButton(
                btn_frame, text=label,
                width=w, height=BTN,
                corner_radius=14,
                font=ctk.CTkFont(size=font_size, weight="bold"),
                fg_color=fg, hover_color=hover,
                text_color=txt_color,
                command=lambda l=label: self._controller and self._controller.on_button(l),
            )
            btn.grid(row=row, column=col, columnspan=colspan,
                     padx=PAD // 2, pady=PAD // 2)

if __name__ == "__main__":
    app = App()
    ctrl = Controller(app)
    app.set_controller(ctrl)
    app.mainloop()
