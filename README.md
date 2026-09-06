## 📋 Secure Information & Development Milestone Survey App
An elegant, cross-platform desktop application built with Python 3, CustomTkinter, and Tkinter. This application features a multi-screen workflow that collects a validated user profile, walks them through dynamic multi-line checkboxes and multi-choice decision screens with fluid navigation, and generates a structured summary text file report.
------------------------------
## ✨ Features

* Validated User Profiles: Enforces field completion, strictly validates 10-digit numerical phone inputs, and checks for basic @ and . structure on emails before launching surveys.
* Dynamic UI Layout Generation: Adapts smoothly across multiple view panels. The application dynamically renders native elements and automatically flows long strings into paragraphs to avoid frame clipping.
* Persistent Tracking & Navigation Canvas: Offers smooth horizontal flow with dedicated ◀ BACK and NEXT ▶ buttons, tracking and recording responses over a structural question array.
* Crash-Proof Architecture: Completely decouples internal tracking variable event loops from Tkinter background callback queues to avoid standard memory trace faults.
* Structured Text File Downloader: Uses native system dialog explorers to let users name and drop clean summary .txt results files anywhere on their machines.

------------------------------
## 🛠️ Technology Stack & Dependencies

| Component | Technology | Purpose |
|---|---|---|
| Language | Python 3.8+ | Core development stack. |
| Framework | CustomTkinter | Renders hardware-accelerated dark/light layout themes. |
| Sub-Engine | Tkinter / Tcl | Handles deep system-native file and widget tracking. |

------------------------------
## 🚀 Getting Started## 1. Prerequisites
Ensure you have Python 3.8 or higher installed on your system. You can verify your version by running:

python --version

## 2. Install Required Packages
This project relies on customtkinter. Install it smoothly via pip:

pip install customtkinter

(Note: standard tkinter and filedialog are bundled natively inside Python's standard library).
## 3. Running the Application
Download or copy the python code into a script named app.py and run it via terminal or command prompt:

python app.py

------------------------------
## 🗺️ Application Workflow

[ Screen 1: Registration Form ]
│
▼ (Validates Text Input, Phone & Email Forms)
[ Screen 2: Case A - Checkbox Milestone List ] <───┐
│                                    │  (Allows Users to Step
▼ (Press Next)                       │   Back and Forth at Will)
[ Screen 2: Case B - Yes / Unsure / No System ] ────┘
│
▼ (Survey Sequence Terminates Progress)
[ Screen 3: Complete & Download Action Canvas ]
│
▼ (Triggers OS File System Dialog Drop)
[ Process Complete ]

------------------------------
## 📁 Source File Layout
The script architecture is segmented into cleanly organized structural blocks:

* __init__() Window Setup & Style Mapping: Initializes application grids, anchors overall layout constraints (600x600), and outlines survey dataset values.
* submit_profile() Form Auditor: Validates fields sequentially, striping out whitespace or characters to ensure absolute data fidelity before advancing layout cards.
* load_question() Navigation Router: Dynamically sweeps older dynamic subwidgets away, reads theme profiles to calculate exact hex backgrounds, and draws checkboxes natively.
* record_*() Response Processors: Buffers active response entries safely into local variable arrays without blocking Tkinter's user execution loop thread.
* trigger_file_download() Exporter: Formats files with dividers and tags, opening system file save explorer workflows.

------------------------------
## 📝 Generated Output Example
When a user triggers a download, the exported text document is neatly structured for effortless data parsing:

========================================
SURVEY RESULTS              
========================================

USER PROFILE:
Name:    Yahya Doe
Email:   yahya.doe@example.com
Address: 123 Dev Lane, Tech City
Phone:   1234567890

----------------------------------------
RESPONSES:
1. Check off each of the tasks that your baby is able to do
   Answer: Calm to an adult's voice., Make brief eye contact with an adult when held., Cry when they are uncomfortable

2. Do you prefer working from home over an office?
   Answer: Yes

3. Is Python your favorite programming language?
   Answer: Yes

4. Do you use dark mode on all your apps?
   Answer: Unsure

5. Have you ever broken a production database?
   Answer: No

6. Do you drink coffee while coding?
   Answer: Yes

------------------------------
## 🔧 Troubleshooting## 💡 The window appears too small or elements crowd each other
If you alter text options or inject longer milestone strings, change the canvas boundaries inside the __init__ constructor layer:

self.geometry("600x600") # Increase these constraint integers if adding large arrays

💡 Getting color errors on older Python versions
This script uses self._apply_appearance_mode() to ensure Tkinter components can interpret CustomTkinter's advanced dual light/dark strings. If any OS color faults happen, verify that your theme theme color initialization arrays explicitly map a correct background configuration value.
------------------------------
