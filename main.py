import customtkinter as ctk
from database.database import get_all_notes, update_note, add_note, delete_note

# Appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# App details
app = ctk.CTk()
app.title("MindJOT")
app.geometry("800x500")
app.iconbitmap("assets/MindJot-ICON.ico")

# Row and Column config
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=5)
app.grid_rowconfigure(0, weight=1)

# ------------ Sidebar ----------
sidebar_container = ctk.CTkFrame(app, width=200)
sidebar_container.grid(row=0, column=0, sticky="nswe", padx=(10, 5), pady=10)

# Add new note button
new_note_btn = ctk.CTkButton(sidebar_container, text="New Note")
new_note_btn.pack(fill="x", padx=10, pady=(10, 20))

# Main Side bar
sidebar = ctk.CTkScrollableFrame(sidebar_container)
sidebar.pack(fill="both", expand=True, padx=10, pady=(0, 10))

# ---------- Editor -----------
editor_frame = ctk.CTkFrame(app)
editor_frame.grid(row=0, column=1, sticky="nswe", padx=(5, 10), pady=10)

# Title
title_entry = ctk.CTkEntry(editor_frame, placeholder_text="Note title")
title_entry.pack(fill="x", padx=10, pady=(10, 5))

content_box = ctk.CTkTextbox(editor_frame)
content_box.pack(fill="both", expand=True, padx=10, pady=(5, 10))

current_note_id = None

def clear_editor():
    global current_note_id
    current_note_id = None
    title_entry.delete(0, "end")
    content_box.delete("1.0", "end")

def load_note(note_id, title, content):
    global current_note_id
    current_note_id = note_id
    title_entry.delete(0, "end")
    title_entry.insert(0, title)
    content_box.delete("1.0", "end")
    content_box.insert("1.0", content)

# Refresh SideBar
def refresh_sidebar():
    for widget in sidebar.winfo_children():
        widget.destroy()

    notes = get_all_notes()

    for note in notes:
        note_id, title, content, created_at, updated_at = note
        btn = ctk.CTkButton(
            sidebar,
            text=title,
            command=lambda i=note_id, t=title, c=content: load_note(i, t, c)
        )
        btn.pack(fill="x", padx=0, pady=5)

# Save Note
def save_current_note():
    if current_note_id is None:
        return
    new_title = title_entry.get()
    new_content = content_box.get("1.0", "end").strip()
    update_note(current_note_id, new_title, new_content)
    refresh_sidebar()

# Create a new note
def create_new_note():
    add_note("Untitled note", "")
    refresh_sidebar()
    # Load notes in DESC order
    notes = get_all_notes()
    newest = notes[0]
    load_note(newest[0], newest[1], newest[2])

# Delete note
def delete_current_note(event=None):
    if current_note_id is None:
        return
    delete_note(current_note_id)
    clear_editor()
    refresh_sidebar()


new_note_btn.configure(command=create_new_note)

save_btn = ctk.CTkButton(editor_frame, text="Save", command=save_current_note)
save_btn.pack(fill="x", padx=10, pady=(0, 5))

delete_btn = ctk.CTkButton(editor_frame, text="Delete", fg_color="darkred", hover_color="#8b0000", command=delete_current_note)
delete_btn.pack(fill="x", padx=10, pady=(0, 10))

refresh_sidebar()

app.mainloop()