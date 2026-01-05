import os
import tkinter as tk
import ctypes

from utils.image import Image
from utils.position import Position
from utils.text import Text
from utils.input import Input
from utils.extra import Extra


class App:
    def __init__(self):

        # App Info
        self.title = "oClip"
        self.version = "1.0.0"
        self.author = "Nabir14"
        self.icon_path = os.path.join(os.path.dirname(__file__), "assets", "icon.png")

        # DPI Awareness for Windows
        if os.name == 'nt':
            user32 = ctypes.windll.user32
            user32.SetProcessDPIAware()
        
        # Global Variables
        self.overlay = None
        self.canvas = None
        
        # UI Code
        self.r = tk.Tk()
        self.r.title(self.title + " v" + self.version  + " by " + self.author)
        self.r.iconphoto(True, tk.PhotoImage(file=self.icon_path))
        self.r.geometry("480x320")
        self.r.resizable(False, False)

        # Top Control Code
        self.controlFrame = tk.Frame(self.r)
        self.controlFrame.pack(side='top', fill='x')
        
        self.newButton = tk.Button(self.controlFrame, text="New", command=self.new_clip)
        self.newButton.pack(side='left',fill='x', expand=True)
        self.copyButton = tk.Button(self.controlFrame, text="Copy", command=self.copy_text)
        self.copyButton.pack(side='right', fill='x', expand=True)

        self.previewButton = tk.Button(self.r, text="Preview", command=Image.preview_screenshot)
        self.previewButton.pack(fill='x', expand=True)

        # Others
        self.textBox = tk.Text(self.r, height=25, width=80)
        self.textBox.pack()
        self.r.mainloop()

    def new_clip(self):
        self.r.iconify()

        self.overlay = tk.Toplevel()
        self.overlay.attributes('-fullscreen', True)
        self.overlay.attributes('-alpha', 0.1)

        self.overlay.update()

        self.canvas = tk.Canvas(self.overlay, width=self.overlay.winfo_width(), height=self.overlay.winfo_height())
        self.canvas.pack(fill='both', expand=True)
        self.canvas.bind("<ButtonPress-1>", Input.on_click)
        self.canvas.bind("<B1-Motion>", self.update_rect)
        self.canvas.bind("<ButtonRelease-1>", self.process_clip)
    
    def process_clip(self, event):
        Input.on_release(event)

        self.r.deiconify()

        image = Image.take_screenshot(Input.start_pos, Input.end_pos)
        text = Text.extract(image.convert('L'))
        self.textBox.delete('1.0', tk.END)
        self.textBox.insert(tk.END, text)

        self.overlay.destroy()
        
    def copy_text(self):
        self.textBox.clipboard_clear()
        self.textBox.clipboard_append(self.textBox.get('1.0', tk.END))
        self.r.update()
    
    def update_rect(self, event):
        if self.canvas:
            self.canvas.delete("all")
            self.canvas.create_rectangle(Extra.to_bbox_coords(Input.start_pos, Position(event.x, event.y)), outline="blue", width=3)
 

App()