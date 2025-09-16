# -------------------- IMPORTS --------------------
import time
import platform
import tkinter as tk

# -------------------- CONSTANTS --------------------
c = {
    "-": "#ECE2D0",
    "+": "#7FD1B9",
    "++": "#6E5F5D",
    "b": "#000000",
    "w": "#FFFFFF",
    "g": "#4CAF50",
    "r": "#F36B61",
    "y": "#FFEB3B",
    "blu": "#2196F3",
    "m": "#691EE9",
    
}

# -------------------- FUNCTIONS --------------------
def enable_high_dpi():
    """
    Enables high DPI scaling for the application based on the operating system.
    """
    if platform.system() == "Windows":
        try:
            from ctypes import windll
            windll.shcore.SetProcessDpiAwareness(1)
        except:
            pass
    elif platform.system() in ["Darwin", "Linux"]:
        try:
            tk.Tk().call('tk', 'scaling', 2.0)
        except:
            pass

# --------------------------------------------------
def wait(taim=0.5):
    """
    Pauses the execution for a specified amount of time.

    Args:
        taim (float): Time in seconds to wait. Default is 0.5 seconds.
    """
    time.sleep(taim)

# --------------------------------------------------
def make_screen(
    title="Title", winsize="580x450", minsize_x=400, minsize_y=250,
    bg_body=c["++"], bg_int=c["-"], fg_int=c["b"], 
    bg_button=c["+"], fg_button=c["b"],
    label_font=("Arial", 16, "bold"), input_font=("Arial", 14), 
    output_font=("Courier", 12, "bold"), button_font=("Arial", 14, "bold"),
    button_text="PLAY", button_command=None,
    use_title=True, use_input=True, use_button=True, 
    use_loading_bar=True, use_output=True, loading_duration=1500, loading_steps=40
):
    """
    Creates a customizable Tkinter window with various UI components.

    Args:
        title (str): Title of the window.
        winsize (str): Initial size of the window in "widthxheight" format.
        minsize_x (int): Minimum width of the window.
        minsize_y (int): Minimum height of the window.
        bg_body (str): Background color of the window body.
        bg_int (str): Background color of internal components.
        fg_int (str): Foreground color of internal components.
        bg_button (str): Background color of buttons.
        fg_button (str): Foreground color of buttons.
        label_font (tuple): Font for labels.
        input_font (tuple): Font for input fields.
        output_font (tuple): Font for output text.
        button_font (tuple): Font for buttons.
        button_text (str): Text displayed on the button.
        button_command (callable): Function to execute when the button is clicked.
        use_title (bool): Whether to include a title label.
        use_input (bool): Whether to include an input field.
        use_button (bool): Whether to include a button.
        use_loading_bar (bool): Whether to include a loading bar.
        use_output (bool): Whether to include an output area.
        loading_duration (int): Duration of the loading bar animation in milliseconds.

    Returns:
        dict: A dictionary containing references to the UI components.
    """
    window = tk.Tk()
    window.title(title)
    if winsize != "":
        window.geometry(winsize)
        minsize_x, minsize_y = map(int, winsize.split('x'))
    else:
        window.update_idletasks()
        minsize_x = window.winfo_reqwidth()
        minsize_y = window.winfo_reqheight()
    window.minsize(minsize_x, minsize_y)
    window.configure(bg=bg_body)

    next_row = [0]
    ui = {"window": window}

    # -------------------- TITLE --------------------
    if use_title:
        title_label = tk.Label(
            window, text=title, font=label_font,
            bg=bg_int, fg=fg_int, borderwidth=3, relief="solid"
        )
        title_label.grid(row=next_row[0], column=0, padx=10, pady=(10, 5), sticky="ew")
        ui["title_label"] = title_label
        next_row[0] += 1

    # -------------------- INPUT --------------------
    if use_input:
        input_text = tk.Entry(
            window, font=input_font, bg=bg_int, fg=fg_int,
            borderwidth=3, relief="solid", cursor="xterm"
        )
        input_text.grid(row=next_row[0], column=0, padx=10, pady=5, sticky="ew", ipady=5)
        ui["input_text"] = input_text
        next_row[0] += 1

    # -------------------- BUTTON --------------------
    def animate_loading_bar(step=0):
        """
        Animates the loading bar with color transitions and progress updates.

        Args:
            step (int): Current step of the animation.
        """
        total_steps = loading_steps
        interval = loading_duration // total_steps
        percentage = (step / total_steps) * 100

        if percentage <= 30:
            color = c["r"]
        elif percentage <= 60:
            color = c["y"]
        elif percentage <= 90:
            color = c["blu"]
        else:
            color = c["m"]

        bar = "█" * step
        ui["loading_label"].config(text=bar, fg=color)

        if step < total_steps:
            window.after(interval, animate_loading_bar, step + 1)
        else:
            ui["loading_label"].config(text="")
            if "input_text" in ui: ui["input_text"].config(state="normal")
            ui["action_button"].config(state="normal")
            if button_command: button_command()

    def on_click():
        """
        Handles the button click event, triggering the loading bar animation or the button command.
        """
        if use_loading_bar:
            if "input_text" in ui: ui["input_text"].config(state="disabled")
            ui["action_button"].config(state="disabled")
            animate_loading_bar()
        else:
            if button_command: button_command()

    if use_button:
        action_button = tk.Button(
            window, text=button_text, command=on_click,
            font=button_font, bg=bg_button, fg=fg_button,
            borderwidth=3, relief="raised", cursor="hand2",
            activebackground=bg_int, activeforeground=fg_int
        )
        action_button.grid(row=next_row[0], column=0, padx=100, pady=5, sticky="ew")
        ui["action_button"] = action_button
        next_row[0] += 1

    # -------------------- LOADING BAR --------------------
    if use_loading_bar:
        loading_label = tk.Label(window, text="", font=("Arial", 12),
            bg=bg_body, fg=fg_int, anchor="center", justify="center")
        loading_label.grid(row=next_row[0], column=0, padx=20, pady=5, sticky="ew")
        ui["loading_label"] = loading_label
        next_row[0] += 1

    # -------------------- OUTPUT --------------------
    if use_output:
        output_frame = tk.Frame(window, bg=bg_body, borderwidth=3, relief="solid")
        output_frame.grid(row=next_row[0], column=0, padx=10, pady=10, sticky="nsew")
        window.rowconfigure(next_row[0], weight=1)
        output_frame.columnconfigure(0, weight=1)
        output_frame.rowconfigure(0, weight=1)

        output_canvas = tk.Canvas(output_frame, bg=bg_int, highlightthickness=0)
        output_scrollbar = tk.Scrollbar(output_frame, orient="vertical", command=output_canvas.yview)
        output_scrollable_frame = tk.Frame(output_canvas, bg=bg_int)

        output_scrollable_frame.bind(
            "<Configure>",
            lambda e: output_canvas.configure(scrollregion=output_canvas.bbox("all"))
        )

        output_canvas.create_window((0, 0), window=output_scrollable_frame, anchor="n")
        output_canvas.configure(yscrollcommand=output_scrollbar.set)

        output_canvas.grid(row=0, column=0, sticky="nsew")
        output_scrollbar.grid(row=0, column=1, sticky="ns")

        output_label = tk.Label(
            output_scrollable_frame, text="", font=output_font,
            bg=bg_int, fg=fg_int, anchor="center", justify="center",
            wraplength=window.winfo_width() - 20
        )
        output_label.pack(fill="both", expand=True)

        ui["output_label"] = output_label
        next_row[0] += 1

        def write_output(text, clear=True):
            """
            Writes text to the output area.

            Args:
                text (str): Text to display.
                clear (bool): Whether to clear existing text. Default is True.
            """
            if clear:
                output_label.config(text="")
            output_label.config(text=str(text))

        def clear_output():
            """
            Clears the output area.
            """
            output_label.config(text="")

        def update_output_wrap(event=None):
            """
            Updates the wrap length of the output text based on the window width.
            """
            max_width = 800
            current_width = min(window.winfo_width() - 20, max_width)
            output_label.config(wraplength=current_width)

        window.bind("<Configure>", update_output_wrap)
        ui["write_output"] = write_output
        ui["clear_output"] = clear_output

    # -------------------- ADD ELEMENT --------------------
    def add_element(kind="label", text="", font=("Arial", 12), row=None, col=0,
                rowspan=None, colspan=None, padx=10, pady=5, sticky="nsew", weight=0, anchor="w", **kwargs):
        """
        Dynamically adds a UI element to the window.

        Args:
            kind (str): Type of element ("label", "button", "entry").
            text (str): Text to display on the element.
            font (tuple): Font for the element.
            row (int): Row position in the grid.
            col (int): Column position in the grid.
            rowspan (int): Number of rows to span.
            colspan (int): Number of columns to span.
            padx (int): Horizontal padding.
            pady (int): Vertical padding.
            sticky (str): Alignment in the grid.
            weight (int): Weight for column resizing.
            **kwargs: Additional arguments for the element.

        Returns:
            widget: The created widget.
        """
        if row is None:
            row = next_row[0]
            next_row[0] += 1

        if colspan is None:
            colspan = 1
        elif colspan == "all":
            colspan = max(window.grid_size()[0], 1)
            
        if rowspan is None:
            rowspan = 1
        elif rowspan == "all":
            rowspan = max(window.grid_size()[1], 1)

        kind = kind.lower()
        if kind == "label":
            widget = tk.Label(
                window, text=text,
                font=font,
                anchor=anchor,
                bg=kwargs.pop("bg", bg_int),
                fg=kwargs.pop("fg", fg_int),
                borderwidth=3,
                relief="solid",
                **kwargs)
        elif kind == "button":
            widget = tk.Button(
                window,
                text=text,
                font=font,
                bg=kwargs.pop("bg", bg_button),
                fg=kwargs.pop("fg", fg_button),
                activebackground=kwargs.pop("active_bg", bg_int),
                activeforeground=kwargs.pop("active_fg", fg_int),
                borderwidth=3,
                relief="raised",
                cursor="hand2",
                **kwargs)
        elif kind == "entry":
            widget = tk.Entry(
                window,
                font=font,
                bg=kwargs.pop("bg", bg_int),
                fg=kwargs.pop("fg", fg_int),
                borderwidth=3,
                relief="solid",
                **kwargs)
        else:
            raise ValueError(f"Unknown element kind: {kind}")

        widget.grid(row=row, column=col, columnspan=colspan, rowspan=rowspan,
                    padx=padx, pady=pady, sticky=sticky)
        
        window.columnconfigure(col, weight=weight) and window.rowconfigure(row, weight=weight)
        
        return widget
    
    ui["add_element"] = add_element
    
    return ui
