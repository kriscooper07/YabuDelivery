import tkinter as tk
from tkinter import font

# Create the main window
root = tk.Tk()
root.title("YABU - The House of Katsu")
root.geometry("300x600")
root.configure(bg='#FFD700')

# Create a custom font
title_font = font.Font(family="Helvetica", size=24, weight="bold")
subtitle_font = font.Font(family="Helvetica", size=12, weight="bold")

# Add the logo
logo_canvas = tk.Canvas(root, width=100, height=100, bg='#FFD700', highlightthickness=0)
logo_canvas.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
logo_canvas.create_oval(10, 10, 90, 90, fill="#8B4513", outline="#8B4513")
logo_canvas.create_line(30, 30, 70, 30, fill="#FFD700", width=10)
logo_canvas.create_line(30, 50, 70, 50, fill="#FFD700", width=10)
logo_canvas.create_line(30, 70, 70, 70, fill="#FFD700", width=10)

# Add the title label
title_label = tk.Label(root, text="YABU", bg='#FFD700', fg="white", font=title_font)
title_label.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

# Add the subtitle label
subtitle_label = tk.Label(root, text="The House of Katsu", bg='#FFD700', fg="white", font=subtitle_font)
subtitle_label.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

# Add the Get Started button
button = tk.Button(root, text="Get Started", bg='#FFD700', fg="black", font=subtitle_font, command=root.quit)
button.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

# Run the application
root.mainloop()
