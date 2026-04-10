import customtkinter as ctk

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
PAD  = 6
COLS = 4

COLORS = {
    "operator": ("#c2410c", "#ea580c"),
    "equals":   ("#3730a3", "#4338ca"), 
    "delete":   ("#0f172a", "#1e293b"), 
    "digit":    ("#0f172a", "#1e293b"), 
}


class CalculatorView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.resizable(False, False)
        self.configure(fg_color="#080c14") 
        self._build_display()
        self._build_buttons()

    def _build_display(self):
        self.display = ctk.CTkLabel(
            self, text="0", anchor="e",
            font=ctk.CTkFont(size=52, weight="normal"),
            text_color="#ffffff",
            fg_color="transparent",
            width=(BTN * COLS) + (PAD * (COLS - 1)),
            height=100,
        )
        self.display.grid(row=0, column=0, columnspan=COLS,
                          padx=PAD, pady=(20, 10), sticky="ew")

    def _build_buttons(self):
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
                self, text=label,
                width=w, height=BTN,
                corner_radius=16,
                font=ctk.CTkFont(size=font_size, weight="bold"),
                fg_color=fg, hover_color=hover,
                text_color=txt_color,
            )
            btn.grid(row=row, column=col, columnspan=colspan,
                     padx=PAD // 2, pady=PAD // 2)

        self.grid_columnconfigure(list(range(COLS)), weight=1)


if __name__ == "__main__":
    app = CalculatorView()
    app.mainloop()
