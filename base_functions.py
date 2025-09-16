import time
import platform
import tkinter as tk

colors = {
    "-": "#ECE2D0",
    "+": "#7FD1B9",
    "++": "#6E5F5D",
    "b": "#000000",
    "w": "#FFFFFF",
}

def enable_high_dpi():
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

def wait(taim=0.5):
    time.sleep(taim)

def make_screen(
    title="Title", winsize="580x450", minsize_x=400, minsize_y=250,
    bg_body=colors["++"], bg_int=colors["-"], fg_int=colors["b"], 
    bg_button=colors["+"], fg_button=colors["b"],
    label_font=("Arial", 16, "bold"), input_font=("Arial", 14), 
    output_font=("Courier", 12, "bold"), button_font=("Arial", 14, "bold"),
    button_text="PLAY", button_command=None,
    use_title=True, use_input=True, use_button=True, 
    use_loading_bar=True, use_output=True, loading_duration=1500
):
    window = tk.Tk()
    window.title(title)
    if winsize != "":
        window.geometry(winsize)
        minsize_x, minsize_y = map(int, winsize.split('x'))
    else:
        window.update_idletasks()  # Ensure the window is updated to calculate its size
        minsize_x = window.winfo_reqwidth()
        minsize_y = window.winfo_reqheight()
    window.minsize(minsize_x, minsize_y)
    window.configure(bg=bg_body)

    # Track next row to auto-place widgets
    next_row = [0]

    # Diccionario UI
    ui = {"window": window}

    # --- Título ---
    if use_title:
        title_label = tk.Label(
            window, text=title, font=label_font,
            bg=bg_int, fg=fg_int, borderwidth=3, relief="solid"
        )
        title_label.grid(row=next_row[0], column=0, padx=10, pady=(10, 5), sticky="ew")
        ui["title_label"] = title_label
        next_row[0] += 1

    # --- Input ---
    if use_input:
        input_text = tk.Entry(
            window, font=input_font, bg=bg_int, fg=fg_int,
            borderwidth=3, relief="solid", cursor="xterm"
        )
        input_text.grid(row=next_row[0], column=0, padx=10, pady=5, sticky="ew", ipady=5)
        ui["input_text"] = input_text
        next_row[0] += 1

    # --- Botón ---
    def animate_loading_bar(step=0):
        total_steps = 40
        interval = loading_duration // total_steps
        percentage = (step / total_steps) * 100

        if percentage <= 30:
            color = "#FF0000"
        elif percentage <= 60:
            color = "#FFFF00"
        elif percentage <= 90:
            color = "#00FF00"
        else:
            color = "#FF00FF"

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

    # --- Loading bar ---
    if use_loading_bar:
        loading_label = tk.Label(window, text="", font=("Arial", 12),
            bg=bg_body, fg=fg_int, anchor="center", justify="center")
        loading_label.grid(row=next_row[0], column=0, padx=20, pady=5, sticky="ew")
        ui["loading_label"] = loading_label
        next_row[0] += 1

    # --- Output ---
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
            if clear:
                output_label.config(text="")
            output_label.config(text=str(text))

        def clear_output():
            output_label.config(text="")

        def update_output_wrap(event=None):
            max_width = 800
            current_width = min(window.winfo_width() - 20, max_width)
            output_label.config(wraplength=current_width)

        window.bind("<Configure>", update_output_wrap)
        ui["write_output"] = write_output
        ui["clear_output"] = clear_output

    # --- Función para agregar elementos dinámicos ---
    def add_element(kind="label", text="", font=("Arial", 12), row=None, col=0,
                rowspan=None, colspan=None, padx=10, pady=5, sticky="nsew", weight=0, **kwargs):
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
            widget = tk.Label(window, text=text, font=font, borderwidth=3, relief="solid",
                            bg=bg_int, fg=fg_int, anchor="w", **kwargs)
        elif kind == "button":
            widget = tk.Button(window, text=text, font=font, bg=bg_button, borderwidth=3, relief="raised", cursor="hand2",
                            fg=fg_button, activebackground=bg_int, activeforeground=fg_int, **kwargs)
        elif kind == "entry":
            widget = tk.Entry(window, font=font, bg=bg_int, fg=fg_int, borderwidth=3, relief="solid", **kwargs)
        else:
            raise ValueError(f"Unknown element kind: {kind}")

        widget.grid(row=row, column=col, columnspan=colspan, rowspan=rowspan,
                    padx=padx, pady=pady, sticky=sticky)
        
        window.columnconfigure(col, weight=weight)
        
        return widget
    
    ui["add_element"] = add_element

    return ui
