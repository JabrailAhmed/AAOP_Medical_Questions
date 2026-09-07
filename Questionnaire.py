import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json

class InfantSurveyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Infant Wellness & Family Questionnaire")
        self.root.geometry("700x550")
        self.root.configure(bg="#f8f9fa")
        
        # Comprehensive question dataset structured directly from the PDF pages
        self.survey_data = [
            # --- SECTION 1 ---
            {
                "section": "DEVELOPMENTAL TASKS",
                "type": "checkbox_group",
                "question": "Check off each of the tasks that your baby is able to do:",
                "options": [
                    "Stay awake for a short time to feed.",
                    "Calm to an adult’s voice.",
                    "Move arms and legs at the same time when startled.",
                    "Make brief eye contact with an adult when held.",
                    "Lift and turn their head to the side briefly when he is on his tummy.",
                    "Keep his hands in a fist.",
                    "Cry when she is uncomfortable."
                ]
            },
            {
                "section": "VISION",
                "type": "radio",
                "question": "Do you have concerns about how your baby sees?",
                "options": ["yes", "no", "unsure"]
            },
            # --- SECTION 2 ---
            {
                "section": "YOUR FAMILY’S HEALTH AND WELL-BEING\nLiving Situation and Food Security",
                "type": "radio",
                "question": "Is permanent housing a worry for you?",
                "options": ["yes", "no"]
            },
            {
                "section": "YOUR FAMILY’S HEALTH AND WELL-BEING\nLiving Situation and Food Security",
                "type": "radio",
                "question": "Do you have the things you need to take care of your baby, such as a crib, car safety seat, and diapers?",
                "options": ["yes", "no"]
            },
            {
                "section": "YOUR FAMILY’S HEALTH AND WELL-BEING\nLiving Situation and Food Security",
                "type": "radio",
                "question": "Does your home have enough heat, hot water and electricity?",
                "options": ["yes", "no"]
            },
            {
                "section": "YOUR FAMILY’S HEALTH AND WELL-BEING\nLiving Situation and Food Security",
                "type": "radio",
                "question": "Do you have health insurance for yourself?",
                "options": ["yes", "no"]
            },
            {
                "section": "YOUR FAMILY’S HEALTH AND WELL-BEING\nLiving Situation and Food Security",
                "type": "radio",
                "question": "Within the past 12 months, were you ever worried whether your food would run out before you got money to buy more?",
                "options": ["yes", "no"]
            },
            {
                "section": "YOUR FAMILY’S HEALTH AND WELL-BEING\nLiving Situation and Food Security",
                "type": "radio",
                "question": "Within the past 12 months, did the food you bought not last and you did not have money to get more?",
                "options": ["yes", "no"]
            },
            {
                "section": "YOUR FAMILY’S HEALTH AND WELL-BEING\nLiving Situation and Food Security",
                "type": "radio",
                "question": "Do you need help in finding community support services, such as WIC or food stamps?",
                "options": ["yes", "no"]
            },
            # --- SECTION 3 ---
            {
                "section": "FAMILY SUPPORT",
                "type": "radio",
                "question": "Do you search the internet to learn about how to care for your baby?",
                "options": ["yes", "no"]
            },
            # --- SECTION 4 ---
            {
                "section": "GETTING TO KNOW YOUR BABY\nHow You Are Feeling",
                "type": "radio",
                "question": "Do you sleep when the baby sleeps?",
                "options": ["yes", "no"]
            },
            {
                "section": "GETTING TO KNOW YOUR BABY\nHow You Are Feeling",
                "type": "radio",
                "question": "Does your partner or do other family members help with the baby?",
                "options": ["yes", "no"]
            },
            {
                "section": "GETTING TO KNOW YOUR BABY\nHow You Are Feeling",
                "type": "radio",
                "question": "If you have other children, are you able to spend time with them?",
                "options": ["yes", "no", "NA"]
            },
            # --- SECTION 5 ---
            {
                "section": "CARING FOR YOUR BABY",
                "type": "radio",
                "question": "Do you read to your baby?",
                "options": ["yes", "no"]
            },
            {
                "section": "CARING FOR YOUR BABY",
                "type": "radio",
                "question": "Is a TV, computer, tablet, or smartphone on in the background when your baby is in the room?",
                "options": ["yes", "no"]
            },
            {
                "section": "CARING FOR YOUR BABY",
                "type": "radio",
                "question": "Is your baby able to fully awaken for feedings?",
                "options": ["yes", "no"]
            },
            {
                "section": "CARING FOR YOUR BABY",
                "type": "radio",
                "question": "Do you have questions about how to calm your baby?",
                "options": ["yes", "no"]
            },
            # --- SECTION 6 ---
            {
                "section": "WHEN TO CALL YOUR DOCTOR / EMERGENCY PLANNING",
                "type": "radio",
                "question": "Do you know how to take your baby’s temperature rectally?",
                "options": ["yes", "no"]
            },
            {
                "section": "WHEN TO CALL YOUR DOCTOR / EMERGENCY PLANNING",
                "type": "radio",
                "question": "Do you have a list of emergency phone numbers?",
                "options": ["yes", "no"]
            },
            {
                "section": "WHEN TO CALL YOUR DOCTOR / EMERGENCY PLANNING",
                "type": "radio",
                "question": "Do you have any questions about taking your baby out in public places?",
                "options": ["yes", "no"]
            },
            # --- SECTION 7 ---
            {
                "section": "FEEDING YOUR BABY\nGeneral Information",
                "type": "radio",
                "question": "Does your baby feed well?",
                "options": ["yes", "no"]
            },
            {
                "section": "FEEDING YOUR BABY\nGeneral Information",
                "type": "radio",
                "question": "Do you have any questions about how your baby is growing?",
                "options": ["yes", "no"]
            },
            {
                "section": "FEEDING YOUR BABY\nGeneral Information",
                "type": "radio",
                "question": "Are you having problems burping your baby?",
                "options": ["yes", "no"]
            },
            {
                "section": "FEEDING YOUR BABY\nGeneral Information",
                "type": "radio",
                "question": "Can you tell when your baby is hungry?",
                "options": ["yes", "no"]
            },
            {
                "section": "FEEDING YOUR BABY\nGeneral Information",
                "type": "radio",
                "question": "Can you tell when your baby is full?",
                "options": ["yes", "no"]
            },
            {
                "section": "FEEDING YOUR BABY\nGeneral Information",
                "type": "radio",
                "question": "Does your baby have 5 or 6 wet disposable diapers (or 6-8 cloth diapers) and 3 or 4 stools a day?",
                "options": ["yes", "no"]
            },
            # --- SECTION 8 ---
            {
                "section": "FEEDING YOUR BABY\nBreastfeeding Questions",
                "type": "radio",
                "question": "Is breastfeeding uncomfortable or painful?",
                "options": ["yes", "no"]
            },
            {
                "section": "FEEDING YOUR BABY\nBreastfeeding Questions",
                "type": "radio",
                "question": "Do you eat foods that are high in protein (such as eggs, lean meat, poultry, fish, or beans) every day?",
                "options": ["yes", "no"]
            },
            {
                "section": "FEEDING YOUR BABY\nBreastfeeding Questions",
                "type": "radio",
                "question": "Are you continuing to take prenatal vitamins?",
                "options": ["yes", "no"]
            },
            {
                "section": "FEEDING YOUR BABY\nBreastfeeding Questions",
                "type": "radio",
                "question": "Do you take medications (either over-the-counter or prescription) or herbal supplements?",
                "options": ["yes", "no"]
            },
            {
                "section": "FEEDING YOUR BABY\nBreastfeeding Questions",
                "type": "radio",
                "question": "Are you giving your baby vitamin D drops?",
                "options": ["yes", "no"]
            },
            # --- SECTION 9 ---
            {
                "section": "FEEDING YOUR BABY\nFormula Feeding Questions",
                "type": "radio",
                "question": "Are you using iron-fortified formula?",
                "options": ["yes", "no"]
            },
            {
                "section": "FEEDING YOUR BABY\nFormula Feeding Questions",
                "type": "radio",
                "question": "Do you have any questions about using formula, such as how much it costs or how to prepare it?",
                "options": ["yes", "no"]
            },
            # --- SECTION 10 ---
            {
                "section": "SAFETY\nCar and Home Safety",
                "type": "radio",
                "question": "Is your baby fastened securely in a rear-facing car safety seat in the back seat every time they ride in a vehicle?",
                "options": ["yes", "no"]
            },
            {
                "section": "SAFETY\nCar and Home Safety",
                "type": "radio",
                "question": "Are you having any problems with your car safety seat?",
                "options": ["yes", "no"]
            },
            {
                "section": "SAFETY\nCar and Home Safety",
                "type": "radio",
                "question": "Is your water heater set so the temperature at the faucet is at or below 120℉/49℃?",
                "options": ["yes", "no"]
            },
            # --- SECTION 11 ---
            {
                "section": "SAFETY\nSafe Sleep",
                "type": "radio",
                "question": "Does your baby sleep on their back?",
                "options": ["yes", "no"]
            },
            {
                "section": "SAFETY\nSafe Sleep",
                "type": "radio",
                "question": "Does your baby sleep in a crib?",
                "options": ["yes", "no"]
            },
            {
                "section": "SAFETY\nSafe Sleep",
                "type": "radio",
                "question": "Does your baby sleep in your room?",
                "options": ["yes", "no"]
            }
        ]
        
        self.current_index = 0
        self.responses = {}
        
        self.setup_ui()
        self.load_question()

    def setup_ui(self):
        # Progress Bar Frame
        self.progress_frame = tk.Frame(self.root, bg="#f8f9fa")
        self.progress_frame.pack(fill="x", padx=40, pady=(20, 0))
        
        self.progress_bar = ttk.Progressbar(self.progress_frame, orient="horizontal", mode="determinate")
        self.progress_bar.pack(fill="x", side="left", expand=True, padx=(0, 10))
        
        self.progress_text = tk.Label(self.progress_frame, text="", font=("Arial", 10), bg="#f8f9fa", fg="#6c757d")
        self.progress_text.pack(side="right", padx=(10, 0))
        
        # Primary Container Card
        self.card = tk.Frame(self.root, bg="white", bd=1, relief="solid", highlightthickness=0)
        self.card.pack(pady=20, padx=40, fill="both", expand=True)
        
        # Section Header Area
        self.section_label = tk.Label(self.card, text="", font=("Arial", 11, "bold"), bg="#e9ecef", fg="#495057", anchor="w", padx=15, pady=8)
        self.section_label.pack(fill="x", side="top")
        
        # Inner Frame for Question Content
        self.content_frame = tk.Frame(self.card, bg="white", padx=25, pady=25)
        self.content_frame.pack(fill="both", expand=True)
        
        self.question_label = tk.Label(self.content_frame, text="", font=("Arial", 13), bg="white", fg="#212529", wraplength=580, justify="left", anchor="w")
        self.question_label.pack(anchor="w", pady=(0, 20))
        
        self.options_frame = tk.Frame(self.content_frame, bg="white")
        self.options_frame.pack(fill="both", expand=True)
        
        # Navigation Button Frame
        self.nav_frame = tk.Frame(self.content_frame, bg="white")
        self.nav_frame.pack(side="bottom", fill="x", pady=(15, 0))
        
        self.btn_back = tk.Button(self.nav_frame, text="Back", font=("Arial", 11), bg="#6c757d", fg="white", bd=0, padx=18, pady=6, command=self.prev_question)
        self.btn_back.pack(side="left")
        
        self.btn_next = tk.Button(self.nav_frame, text="Next", font=("Arial", 11), bg="#007fff", fg="white", bd=0, padx=18, pady=6, command=self.next_question)
        self.btn_next.pack(side="right")

    def load_question(self):
        # Clean out old components from options area
        for widget in self.options_frame.winfo_children():
            widget.destroy()
            
        q_data = self.survey_data[self.current_index]
        
        # Update progress and headers
        total_q = len(self.survey_data)
        self.progress_bar["value"] = ((self.current_index) / total_q) * 100
        self.progress_text.config(text=f"{self.current_index + 1} of {total_q}")
        self.section_label.config(text=q_data["section"].upper())
        self.question_label.config(text=q_data["question"])
        
        # Manage back button state
        if self.current_index == 0:
            self.btn_back.pack_forget()
        else:
            self.btn_back.pack(side="left")
            
        # Manage terminal button behavior
        if self.current_index == total_q - 1:
            self.btn_next.config(text="Submit Survey", bg="#2ecc71")
        else:
            self.btn_next.config(text="Next", bg="#007fff")
            
        # Draw UI based on specific question formats
        if q_data["type"] == "radio":
            self.radio_var = tk.StringVar()
            # Retrieve answer if backtracking
            saved_ans = self.responses.get(f"Q_{self.current_index}")
            if saved_ans:
                self.radio_var.set(saved_ans.get("answer", ""))
                
            for opt in q_data["options"]:
                rb = tk.Radiobutton(self.options_frame, text=opt.capitalize(), variable=self.radio_var, value=opt, font=("Arial", 11), bg="white", activebackground="white", anchor="w", padx=10)
                rb.pack(fill="x", pady=6)
                
        elif q_data["type"] == "checkbox_group":
            self.check_vars = {}
            saved_data = self.responses.get(f"Q_{self.current_index}", {})
            saved_answers = saved_data.get("completed_tasks", [])
            
            for opt in q_data["options"]:
                var = tk.BooleanVar()
                if opt in saved_answers:
                    var.set(True)
                self.check_vars[opt] = var
                cb = tk.Checkbutton(self.options_frame, text=opt, variable=var, font=("Arial", 11), bg="white", activebackground="white", anchor="w", justify="left", wraplength=550)
                cb.pack(fill="x", pady=5)

    def next_question(self):
        q_data = self.survey_data[self.current_index]
        
        # Capture current inputs
        if q_data["type"] == "radio":
            val = self.radio_var.get()
            if not val:
                messagebox.showwarning("Selection Required", "Please select an answer option before moving forward.")
                return
            self.responses[f"Q_{self.current_index}"] = {
                "question": q_data["question"],
                "section": q_data["section"].replace("\n", " - "),
                "answer": val
            }
        elif q_data["type"] == "checkbox_group":
            selected = [opt for opt, var in self.check_vars.items() if var.get()]
            self.responses[f"Q_{self.current_index}"] = {
                "question": q_data["question"],
                "section": q_data["section"],
                "completed_tasks": selected
            }
            
        # Direct navigation or write out finalized data
        if self.current_index < len(self.survey_data) - 1:
            self.current_index += 1
            self.load_question()
        else:
            self.save_and_exit()

    def prev_question(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.load_question()

    def save_and_exit(self):
        # Save structured results payload directly to local disk JSON
        output_filename = "infant_screening_results.json"
        with open(output_filename, "w", encoding="utf-8") as f:
            json.dump(self.responses, f, indent=4, ensure_ascii=False)
            
        messagebox.showinfo("Survey Completed", f"All responses captured and recorded locally to '{output_filename}'.")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = InfantSurveyApp(root)
    root.mainloop()
