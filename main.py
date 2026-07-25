import customtkinter as ctk


# Setting the default theme
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

# Setting up the app
app = ctk.CTk()
app.title("Notes App")
app.geometry("800x500")

# Creating the layout
app.grid_columnconfigure(0, weight=1)   # Sidebar COL - 1x
app.grid_columnconfigure(1, weight=3)   # Editor COL - 3x times bigger
app.grid_rowconfigure(0, weight=1) # Row

# --------------- Sidebar ---------------
# Creating the Sidebar
sidebar = ctk.CTkFrame(app, width=200)
sidebar.grid(row=0, column=0, sticky="nsew", padx=(10, 5), pady=10)

# Hardcoded titles for development
fake_notes = {
    "Grocery list": "Milk, eggs, bread, coffee",
    "Project ideas": "Build a notes app with CustomTkinter",
    "Meeting notes": "Discussed timeline, next call Friday"
}

# --------------- Editor ---------------
# Creating the Editor
editor_frame = ctk.CTkFrame(app)
editor_frame.grid(row=0, column=1, sticky="nswe", padx=(5, 10), pady=10)

title_entry = ctk.CTkEntry(editor_frame, placeholder_text="Note title")
title_entry.pack(fill="x", padx=10, pady=(10, 5))

content_box = ctk.CTkTextbox(editor_frame)
content_box.pack(fill="both", expand=True, padx=10, pady=(5, 10))



# Load the data
def load_data(title):
    content = fake_notes[title]

    title_entry.delete(0, "end")
    title_entry.insert(0, title)

    content_box.delete('1.0', "end")
    content_box.insert('1.0', content)

# Create Buttons
for title_in_dict in fake_notes:
    btn = ctk.CTkButton(sidebar,
                        text=title_in_dict,
                        command=lambda t=title_in_dict: load_data(t))
    btn.pack(fill="x", padx=10, pady=(10, 5))

app.mainloop()

