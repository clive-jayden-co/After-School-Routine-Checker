import tkinter as tk
from tkinter import messagebox

class AfterSchoolRoutineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("After-School Routine Checker")
        self.root.geometry("450x400")
        self.root.configure(bg="#f0f4f8")

        self.routine = [
            "Have a healthy snack",
            "Complete homework assignments",
            "Pack backpack for tomorrow",
            "Read for 20 minutes",
            "Enjoy free time or play outside"
        ]
        self.current_index = 0

        self.title_label = tk.Label(
            root, 
            text="After-School Routine Checker", 
            font=("Helvetica", 16, "bold"), 
            bg="#f0f4f8", 
            fg="#2c3e50"
        )
        self.title_label.pack(pady=15)

        self.input_frame = tk.Frame(root, bg="#f0f4f8")
        self.input_frame.pack(pady=10)

        tk.Label(self.input_frame, text="Type Task:", font=("Helvetica", 11), bg="#f0f4f8").grid(row=0, column=0, padx=5)
        self.task_entry = tk.Entry(self.input_frame, font=("Helvetica", 11), width=25)
        self.task_entry.grid(row=0, column=1, padx=5)
        self.task_entry.bind("<KeyRelease>", self.on_key_release)

        self.last_char_label = tk.Label(root, text="Last character typed: None", font=("Helvetica", 10, "italic"), bg="#f0f4f8", fg="#7f8c8d")
        self.last_char_label.pack()

        self.btn_check = tk.Button(
            root, 
            text="Check Entry", 
            command=self.check_entry, 
            font=("Helvetica", 11, "bold"), 
            bg="#3498db", 
            fg="white", 
            padx=10, 
            pady=5
        )
        self.btn_check.pack(pady=15)

        self.routine_zone = tk.Label(
            root, 
            text=f"Current Routine Objective:\n{self.routine[self.current_index]}\n\n(Click here to progress routine)", 
            font=("Helvetica", 12), 
            bg="#ffffff", 
            fg="#34495e", 
            bd=2, 
            relief="groove", 
            width=35, 
            height=6
        )
        self.routine_zone.pack(pady=10)
        self.routine_zone.bind("<Button-1>", self.on_zone_click)

    def on_key_release(self, event):
        if event.char:
            self.last_char_label.config(text=f"Last character typed: '{event.char}'")

    def check_entry(self):
        text = self.task_entry.get().strip()
        if not text:
            messagebox.showwarning("Warning", "No task entered! Please type something.")
        else:
            messagebox.showinfo("Success", f"Task registered: {text}")

    def on_zone_click(self, event):
        self.current_index = (self.current_index + 1) % len(self.routine)
        next_task = self.routine[self.current_index]
        self.routine_zone.config(text=f"Current Routine Objective:\n{next_task}\n\n(Click here to progress routine)")

if __name__ == "__main__":
    root = tk.Tk()
    app = AfterSchoolRoutineApp(root)
    root.mainloop()
