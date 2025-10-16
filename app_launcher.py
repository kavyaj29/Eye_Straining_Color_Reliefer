import tkinter as tk
from tkinter import ttk
import pygetwindow as gw
from threading import Thread

# Import from the new, correct files
from capture_screen import capture_full_screen
from capture_window import capture_window_seamlessly

def start_window_capture():
    """Starts capturing the window selected in the listbox."""
    selected_item = window_listbox.curselection()
    if not selected_item:
        print("No window selected!")
        return
        
    window_title = window_listbox.get(selected_item)
    
    root.destroy() 
    
    capture_thread = Thread(target=capture_window_seamlessly, args=(window_title,))
    capture_thread.start()

def start_screen_capture():
    """Starts capturing the entire screen."""
    root.destroy()
    capture_thread = Thread(target=capture_full_screen)
    capture_thread.start()

# --- UI Setup ---
root = tk.Tk()
root.title("Choose What to Share")
root.geometry("400x350")

screen_frame = ttk.Frame(root, padding="10")
screen_frame.pack(fill='x')
screen_label = ttk.Label(screen_frame, text="Share your entire screen:")
screen_label.pack(side='left', padx=5)
screen_button = ttk.Button(screen_frame, text="Share Screen", command=start_screen_capture)
screen_button.pack(side='right', padx=5)

separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x', pady=5)

window_frame = ttk.Frame(root, padding="10")
window_frame.pack(fill='both', expand=True)
window_label = ttk.Label(window_frame, text="Or, choose a specific window to share:")
window_label.pack(anchor='w')

window_listbox = tk.Listbox(window_frame)
window_listbox.pack(fill='both', expand=True, pady=5)

all_windows = gw.getAllTitles()
for title in all_windows:
    if title:
        window_listbox.insert(tk.END, title)

share_window_button = ttk.Button(window_frame, text="Share Selected Window", command=start_window_capture)
share_window_button.pack(pady=5)

root.mainloop()

