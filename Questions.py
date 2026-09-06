import tkinter as tk
import tkinter.filedialog as fd
import customtkinter as ctk

# Set the overall look and feel
ctk.set_appearance_mode("System")  # Options: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"

class SurveyApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        # --- Window Setup ---
        self.title("Secure Information Survey")
        self.geometry("600x600")
        self.resizable(False, False)

        # --- Survey Questions ---
        self.questions = [
            ("Check off each of the tasks that your baby is able to do:",
             ["Stay awake for a short time to feed.",
              "Calm to an adult's voice.",
              "Move her arms and legs at the same time when startled.",
              "Make brief eye contact with an adult when held.",
              "Lift and turn their head to the side briefly when on their tummy.",
              "Keep hands in a fist.",
              "Cry when they are uncomfortable."]),
            "Do you prefer working from home over an office?",
            "Is Python your favorite programming language?",
            "Do you use dark mode on all your apps?",
            "Have you ever broken a production database?",
            "Do you drink coffee while coding?",
        ]

        self.current_index = 0
        self.recorded_answers = [""] * len(self.questions)
        self.user_profile = {}

        self.checkbox_vars = []
        self.checkbox_objects = []

        # --- Form Screen UI Elements (Screen 1) ---
        self.form_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.form_frame.pack(pady=20, padx=40, fill="both", expand=True)

        self.form_title = ctk.CTkLabel(
            self.form_frame, text="Please Enter Your Details", font=ctk.CTkFont(size=20, weight="bold")
        )
        self.form_title.pack(pady=(0, 15))

        self.fields = [
            ("First Name:", "first_name"),
            ("Last Name:", "last_name"),
            ("Email Address:", "email"),
            ("Address:", "address"),
            ("Phone Number (10 digits):", "phone"),
        ]
        self.entries = {}

        for label_text, key in self.fields:
            lbl = ctk.CTkLabel(self.form_frame, text=label_text, font=ctk.CTkFont(size=13))
            lbl.pack(anchor="w", padx=140, pady=(3, 1))

            clean_placeholder = label_text.replace(":", "").replace(" (10 digits)", "").lower()
            entry = ctk.CTkEntry(self.form_frame, width=320, placeholder_text=f"Enter {clean_placeholder}")
            entry.pack(padx=20, pady=(0, 8))
            self.entries[key] = entry

        self.submit_btn = ctk.CTkButton(
            self.form_frame, text="Start Survey", font=ctk.CTkFont(size=15, weight="bold"), height=40, command=self.submit_profile
        )
        self.submit_btn.pack(pady=(15, 0))

        # --- Survey Screen UI Elements (Screen 2) ---
        self.survey_frame = ctk.CTkFrame(self, fg_color="transparent")

        self.progress_bar = ctk.CTkProgressBar(self.survey_frame, width=480)
        self.progress_bar.pack(pady=(15, 5), padx=40)
        self.progress_bar.set(0)

        self.counter_label = ctk.CTkLabel(
            self.survey_frame, text="", font=ctk.CTkFont(size=14, weight="bold")
        )
        self.counter_label.pack(pady=2, padx=40)

        # Container for the question label
        self.question_frame = ctk.CTkFrame(self.survey_frame, fg_color="transparent", height=60)
        self.question_frame.pack(fill="x", padx=40, pady=5)
        self.question_frame.pack_propagate(False)

        self.question_label = ctk.CTkLabel(
            self.question_frame, text="", font=ctk.CTkFont(size=16, weight="bold"), wraplength=480, justify="center"
        )
        self.question_label.pack(fill="both", expand=True)

        # Center middle horizontal row for navigation controls
        self.middle_navigation_frame = ctk.CTkFrame(self.survey_frame, fg_color="transparent")
        self.middle_navigation_frame.pack(fill="x", padx=15, pady=10)

        # Left Backwards Button
        self.back_nav_button = ctk.CTkButton(
            self.middle_navigation_frame, text="◀ BACK", width=100, height=40,
            font=ctk.CTkFont(size=13, weight="bold"), fg_color="#7f8c8d", hover_color="#95a5a6",
            command=self.step_backward
        )
        self.back_nav_button.pack(side="left")

        # Right Forwards Button
        self.forward_nav_button = ctk.CTkButton(
            self.middle_navigation_frame, text="NEXT ▶", width=100, height=40,
            font=ctk.CTkFont(size=13, weight="bold"), fg_color="#3498db", hover_color="#2980b9",
            command=self.step_forward
        )
        self.forward_nav_button.pack(side="right")

        # Centered Checkbox display frame inside main survey container area
        self.checkbox_frame = ctk.CTkScrollableFrame(self.survey_frame, width=340, height=220, fg_color="transparent")

        # --- Bottom Control Frame Row ---
        self.control_frame = ctk.CTkFrame(self.survey_frame, fg_color="transparent")
        self.control_frame.pack(fill="x", pady=(10, 20), padx=40)

        self.yes_button = ctk.CTkButton(
            self.control_frame, text="YES", width=110, height=45, font=ctk.CTkFont(size=15, weight="bold"),
            fg_color="#2ecc71", hover_color="#27ae60", command=lambda: self.record_bottom_response("Yes")
        )
        self.unsure_button = ctk.CTkButton(
            self.control_frame, text="UNSURE", width=110, height=45, font=ctk.CTkFont(size=15, weight="bold"),
            fg_color="#f39c12", hover_color="#d35400", command=lambda: self.record_bottom_response("Unsure")
        )
        self.no_button = ctk.CTkButton(
            self.control_frame, text="NO", width=110, height=45, font=ctk.CTkFont(size=15, weight="bold"),
            fg_color="#e74c3c", hover_color="#c0392b", command=lambda: self.record_bottom_response("No")
        )

        self.download_button = ctk.CTkButton(
            self.control_frame, text="📥 Download .txt", width=250, height=45, font=ctk.CTkFont(size=16, weight="bold"),
            fg_color="#3498db", hover_color="#2980b9", command=self.trigger_file_download
        )

    def submit_profile(self):
        """Validates input field values, enforces numericality, and restricts length to exactly 10 digits."""
        self.form_title.configure(text="Please Enter Your Details", text_color=ctk.ThemeManager.theme["CTkLabel"]["text_color"])
        self.entries["phone"].configure(border_color=ctk.ThemeManager.theme["CTkEntry"]["border_color"])
        self.entries["email"].configure(border_color=ctk.ThemeManager.theme["CTkEntry"]["border_color"])

        for _, key in self.fields:
            val = self.entries[key].get().strip()
            if not val:
                self.form_title.configure(text="All fields are required!", text_color="#e74c3c")
                return
            self.user_profile[key] = val

        if "@" not in self.user_profile["email"] or "." not in self.user_profile["email"]:
            self.form_title.configure(text="Please enter a valid email address!", text_color="#e74c3c")
            self.entries["email"].configure(border_color="#e74c3c")
            return

        phone_digits_only = self.user_profile["phone"].replace(" ", "").replace("-", "").replace("(", "").replace(")", "")

        if not phone_digits_only.isdigit():
            self.form_title.configure(text="Phone number must contain only numbers!", text_color="#e74c3c")
            self.entries["phone"].configure(border_color="#e74c3c")
            return

        if len(phone_digits_only) != 10:
            self.form_title.configure(text="Phone number must be exactly 10 digits!", text_color="#e74c3c")
            self.entries["phone"].configure(border_color="#e74c3c")
            return

        self.form_frame.pack_forget()
        self.survey_frame.pack(pady=20, fill="both", expand=True)
        self.load_question()

    def update_scrollbar_visibility(self):
        """Dynamically calculates element height to safely hide or reveal the scrollbar handle."""
        self.update_idletasks()
        bbox = self.checkbox_frame._canvas.bbox("all")
        if bbox:
            content_height = bbox[3] - bbox[1]
            frame_height = self.checkbox_frame._canvas.winfo_height()

            if content_height <= frame_height:
                self.checkbox_frame._scrollbar.grid_forget()
                self.checkbox_frame._canvas.configure(width=340)

    def load_question(self):
        """Monitors overall response index loop values to step text layout panels."""
        for cb in self.checkbox_objects:
            try:
                cb.pack_forget()
                cb.destroy()
            except Exception:
                pass

        try:
            self.checkbox_frame._scrollbar.grid_forget()
        except Exception:
            pass

        self.checkbox_frame.pack_forget()
        self.checkbox_vars = []
        self.checkbox_objects = []

        if self.current_index < len(self.questions):
            self.counter_label.configure(text=f"Question {self.current_index + 1} of {len(self.questions)}")
            self.progress_bar.set(self.current_index / len(self.questions))

            if self.current_index == 0:
                self.back_nav_button.configure(state="disabled", fg_color="#bdc3c7")
            else:
                self.back_nav_button.configure(state="normal", fg_color="#7f8c8d")

            # --- CASE 1: The First Question (Scrollable Checklist View Layer Centered) ---
            if self.current_index == 0:
                question_text, options = self.questions[self.current_index]
                self.question_label.configure(text=question_text)

                self.forward_nav_button.pack(side="right")
                self.yes_button.pack_forget()
                self.unsure_button.pack_forget()
                self.no_button.pack_forget()

                self.checkbox_frame.pack(pady=10, expand=True)

                for option in options:
                    var = tk.IntVar(value=0)
                    cb = ctk.CTkCheckBox(
                        self.checkbox_frame, text=option, variable=var,
                        onvalue=1, offvalue=0, font=ctk.CTkFont(size=12)
                    )
                    cb.pack(anchor="w", pady=6, padx=10, fill="x")
                    self.checkbox_vars.append((var, option))
                    self.checkbox_objects.append(cb)

                self.after(50, self.update_scrollbar_visibility)

            # --- CASE 2: Text Response Option Framework ---
            else:
                self.forward_nav_button.pack_forget()
                self.yes_button.pack_forget()
                self.unsure_button.pack_forget()
                self.no_button.pack_forget()

                self.yes_button.pack(side="left", expand=True, padx=5)
                self.unsure_button.pack(side="left", expand=True, padx=5)
                self.no_button.pack(side="left", expand=True, padx=5)

                self.question_label.configure(text=self.questions[self.current_index])

            self.update()
        else:
            self.transition_to_download()

    def step_forward(self):
        """Processes checklist logic for question 1 using side button link selection tracking."""
        if self.current_index == 0:
            selected_choices = []
            for var, text in self.checkbox_vars:
                if var.get() == 1:
                    selected_choices.append(text)
            self.recorded_answers[0] = ", ".join(selected_choices) if selected_choices else "None selected"

        self.current_index += 1
        self.load_question()

    def step_backward(self):
        """Steps backwards to preceding timeline tracking locations cleanly."""
        if self.current_index > 0:
            self.current_index -= 1
            self.load_question()

    def record_bottom_response(self, user_choice):
        """Stores text responses collected from bottom buttons row configurations."""
        self.recorded_answers[self.current_index] = user_choice
        self.current_index += 1
        self.load_question()

    def transition_to_download(self):
        """Hides design components completely and swaps view window blocks layout layers."""
        self.progress_bar.set(1.0)
        self.counter_label.configure(text="Survey Complete!")

        self.back_nav_button.pack_forget()
        self.forward_nav_button.pack_forget()

        self.yes_button.pack_forget()
        self.unsure_button.pack_forget()
        self.no_button.pack_forget()

        self.download_button.pack(pady=20)

        self.question_label.configure(
            text=f"Thank you, {self.user_profile['first_name']}!\n\nClick the button below to download your summary text report asset file contents.",
            font=ctk.CTkFont(size=15),
            justify="center"
        )
        self.update()

    def trigger_file_download(self):
        """Launches native system file explorer panel framework to structure output asset drops."""
        default_name = f"survey_{self.user_profile['first_name'].lower()}_{self.user_profile['last_name'].lower()}.txt"

        save_path = fd.asksaveasfilename(
            initialfile=default_name,
            defaultextension=".txt",
            filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")]
        )

        if not save_path:
            return

        file_content = "========================================\n"
        file_content += "            SURVEY RESULTS              \n"
        file_content += "========================================\n\n"
        file_content += "USER PROFILE:\n"
        file_content += f"Name:    {self.user_profile['first_name']} {self.user_profile['last_name']}\n"
        file_content += f"Email:   {self.user_profile['email']}\n"
        file_content += f"Address: {self.user_profile['address']}\n"
        file_content += f"Phone:   {self.user_profile['phone']}\n\n"
        file_content += "----------------------------------------\n"
        file_content += "RESPONSES:\n"

        for i, q in enumerate(self.questions):
            q_text = q[0] if isinstance(q, tuple) else q
            file_content += f"{i+1}. {q_text}\n"
            file_content += f"   Answer: {self.recorded_answers[i]}\n\n"

        with open(save_path, "w", encoding="utf-8") as file:
            file.write(file_content)


if __name__ == "__main__":
    app = SurveyApp()
    app.mainloop()
