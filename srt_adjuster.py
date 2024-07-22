from tkinter import Tk, Label, Button, Entry, filedialog, StringVar, messagebox, Menu
from datetime import timedelta
import re
import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
    result = chardet.detect(raw_data)
    return result['encoding']

def add_delay_to_timestamp(timestamp, delay_seconds):
    time_obj = timedelta(hours=int(timestamp[0:2]),
                         minutes=int(timestamp[3:5]),
                         seconds=int(timestamp[6:8]),
                         milliseconds=int(timestamp[9:12]))
    new_time_obj = time_obj + timedelta(seconds=delay_seconds)
    total_seconds = int(new_time_obj.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    milliseconds = new_time_obj.microseconds // 1000
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"

def adjust_srt_timing(file_path, delay_seconds, save_path):
    encoding = detect_encoding(file_path)
    with open(file_path, 'r', encoding=encoding) as file:
        lines = file.readlines()

    time_pattern = re.compile(r'(\d{2}:\d{2}:\d{2},\d{3})')

    adjusted_lines = []
    for line in lines:
        match = time_pattern.findall(line)
        if match:
            start_time, end_time = match
            new_start_time = add_delay_to_timestamp(start_time, delay_seconds)
            new_end_time = add_delay_to_timestamp(end_time, delay_seconds)
            line = line.replace(start_time, new_start_time).replace(end_time, new_end_time)
        adjusted_lines.append(line)

    with open(save_path, 'w', encoding=encoding) as file:
        file.writelines(adjusted_lines)
    return save_path

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("SRT files", "*.srt")])
    file_path_var.set(file_path)

def save_file():
    save_path = filedialog.asksaveasfilename(defaultextension=".srt", filetypes=[("SRT files", "*.srt")])
    save_path_var.set(save_path)
    save_path_label.config(text=f"Save Path: {save_path}")

def adjust_file():
    try:
        file_path = file_path_var.get()
        save_path = save_path_var.get()
        delay_seconds = int(delay_var.get())
        if file_path and delay_seconds and save_path:
            new_file_path = adjust_srt_timing(file_path, delay_seconds, save_path)
            result_label.config(text=f"Adjusted file saved as: {new_file_path}")
        else:
            raise ValueError("Please select a file, enter delay time, and specify save path.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def show_info():
    info_text = "Developed by: Mohamad Alyafi\nContact: mohamad.n.alyafi@gmail.com"
    messagebox.showinfo("Info", info_text)

def check_update():
    info_text = "No available updates"
    messagebox.showinfo("Check for updates", info_text)

# GUI setup
root = Tk()
root.title("SRT Time Adjuster")
root.geometry("1110x620")
root.minsize(1110, 620)

file_path_var = StringVar()
save_path_var = StringVar()
delay_var = StringVar()

# Widget definitions
file_label = Label(root, text="Select SRT File:")
browse_button = Button(root, text="Browse", command=select_file)
delay_label = Label(root, text="Enter delay time (seconds):")
delay_entry = Entry(root, textvariable=delay_var)
save_label = Label(root, text="Save Adjusted File As:")
save_button = Button(root, text="Choose the new srt file path and name", command=save_file)
save_path_label = Label(root, text="", wraplength=500)
adjust_button = Button(root, text="Adjust", command=adjust_file)
result_label = Label(root, text="")

# Placing widgets with enough spacing
file_label.place(relx=0.5, rely=0.3, anchor='center')
browse_button.place(relx=0.5, rely=0.35, anchor='center')
delay_label.place(relx=0.5, rely=0.4, anchor='center')
delay_entry.place(relx=0.5, rely=0.45, anchor='center')
save_label.place(relx=0.5, rely=0.5, anchor='center')
save_button.place(relx=0.5, rely=0.55, anchor='center')
save_path_label.place(relx=0.5, rely=0.6, anchor='center')
adjust_button.place(relx=0.5, rely=0.65, anchor='center')
result_label.place(relx=0.5, rely=0.7, anchor='center')

# Create the menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Add the Info menu
info_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Options", menu=info_menu)
info_menu.add_command(label="Check for updates", command=check_update)
info_menu.add_command(label="About", command=show_info)

root.mainloop()
