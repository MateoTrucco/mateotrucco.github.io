"""
=========================
    FUNCIONES BASICAS
=========================

Functions:

wait(taim) - espera taim segundos

! write(text, speed)     |   imprime el texto
! wInput(texto, speed)   |   imprime el texto y pide una respuesta
! playAgain()            |   pide una respuesta y devuelve True o False
! encuadrar(texto)       |   encuadra el texto
! alarm(s=0, loop=1)     |   reproduce un sonido

"""

import time
import platform
import tkinter as tk

colors = {
    "-": "#ECE2D0",
    "+": "#7FD1B9",
    "++":"#6E5F5D",
    
    "b": "#000000",
    "w": "#FFFFFF",
}

def enable_high_dpi():
    """
    Enables high DPI scaling for Tkinter applications.

    Configures the application for high-resolution displays on Windows, macOS, or Linux.
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

def wait(taim=0.5):
    """Waits for the specified number of seconds."""
    time.sleep(taim)

def write(text="", char_speed=0.03):
    """Prints the text with a simulated typing speed."""
    for char in text:
        print(char, end='', flush=True)
        wait(char_speed)

def write_input(prompt_text="", char_speed=0.03):
    """Prints the prompt text with a simulated typing speed and waits for user input."""
    write(prompt_text, char_speed)
    response = input('\n--- ')
    return response

def frame_text(text):
    """
    Frames the given text with a box.
    """
    lines = text.split('\n')
    max_length = max(len(line) for line in lines)
    frame_width = max_length + 2

    framed_text = ''

    framed_text += '┌' + '─' * frame_width + '┐\n'
    for line in lines:
        framed_text += '│ ' + line.ljust(max_length) + ' │\n'
    framed_text += '└' + '─' * frame_width + '┘'

    return framed_text

def make_screen(
    bg_body=colors["++"], bg_int=colors["-"], fg_int=colors["b"],
    bg_button=colors["+"], fg_button=colors["b"],
    title="Title", winsize="580x450", minsize_x=400, minsize_y=250,
    label_font=("Arial", 16, "bold"), input_font=("Arial", 14),
    button_text="PLAY", button_font=("Arial", 14, "bold"), button_command=None,
):
    """
    Makes a basic screen with:
        - title
        - input
        - button
        - output with scrollbar

    Returns a dictionary with:
        - window, input_text, output_label, action_button
        - helpers: write_output, clear_output
    """
    window = tk.Tk()
    window.title(title)
    window.geometry(winsize)
    window.minsize(minsize_x, minsize_y)
    window.configure(bg=bg_body)

    window.columnconfigure(0, weight=1)
    window.rowconfigure(3, weight=1)

    label = tk.Label(
        window, text=title, font=label_font,
        bg=bg_int, fg=fg_int, borderwidth=3, relief="solid"
    )
    label.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="ew")

    input_text = tk.Entry(
        window, font=input_font, bg=bg_int, fg=fg_int,
        borderwidth=3, relief="solid", cursor="xterm"
    )
    input_text.grid(row=1, column=0, padx=10, pady=5, sticky="ew", ipady=5)

    if button_command is None:
        button_command = lambda: None
    action_button = tk.Button(
        window, text=button_text, command=button_command,
        font=button_font, bg=bg_button, fg=fg_button,
        borderwidth=3, relief="raised", cursor="hand2",
        activebackground=bg_int, activeforeground=fg_int
    )
    action_button.grid(row=2, column=0, padx=100, pady=5, sticky="ew")

    output_frame = tk.Frame(window, bg=bg_body, borderwidth=3, relief="solid")
    output_frame.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
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
        output_scrollable_frame, text="", font=("Courier", 12, "bold"),
        bg=bg_int, fg=fg_int, anchor="center", justify="center",
        wraplength=window.winfo_width() - 20
    )
    output_label.pack(fill="both", expand=True)

    def write_output(text, clear=True):
        """Writes text to the output label. If clear is True, clears previous text."""
        if clear:
            output_label.config(text="")
        output_label.config(text=str(text))

    def clear_output():
        """Clears the output label."""
        output_label.config(text="")

    def update_output_wrap(event=None):
        """Updates the wraplength of the output label based on window width."""
        max_width = 800
        current_width = min(window.winfo_width() - 20, max_width)
        output_label.config(wraplength=current_width)

    window.bind("<Configure>", update_output_wrap)

    return {
        "window": window,
        "input_text": input_text,
        "output_label": output_label,
        "action_button": action_button,
        "write_output": write_output,
        "clear_output": clear_output,
    }