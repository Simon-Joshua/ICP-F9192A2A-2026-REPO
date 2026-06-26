import tkinter as tk
from tkinter import messagebox
import math
import zxcvbn

def calculate_entropy(password):
    if not password:
        return 0
    charset = 0
    if any(c.islower() for c in password): charset += 26
    if any(c.isupper() for c in password): charset += 26
    if any(c.isdigit() for c in password): charset += 10
    if any(not c.isalnum() for c in password): charset += 32
    
    if charset == 0: return 0
    return round(len(password) * math.log2(charset), 2)

def analyze_password_ui():
    password = password_input.get()
    
    # Run Calculations
    entropy = calculate_entropy(password)
    z_results = zxcvbn.zxcvbn(password)
    score = z_results['score']
    feedback = z_results['feedback']['suggestions']
    
    colors = ["#ff4d4d", "#ff9933", "#ffcc00", "#99cc33", "#33cc33"]
    score_labels = ["Very Weak", "Weak", "Medium", "Strong", "Excellent"]
    
    score_display.config(text=f"{score}/4 ({score_labels[score]})", fg=colors[score])
    entropy_display.config(text=f"{entropy} bits")
    
    if feedback:
        feedback_text = "\n".join([f"• {item}" for item in feedback])
    elif password:
        feedback_text = "✨ Great password structure!"
    else:
        feedback_text = "Please enter a password."
        
    feedback_display.config(text=feedback_text)

# --- Creating the Graphical Window ---
root = tk.Tk()
root.title("Cybersecurity Password Strength Analyzer")
root.geometry("450x400")
root.config(bg="#1e1e1e") # Dark mode background

header = tk.Label(root, text="Password Strength Analyzer", font=("Arial", 16, "bold"), fg="#ffffff", bg="#1e1e1e")
header.pack(pady=15)

# Input Label & Entry Box
input_label = tk.Label(root, text="Enter Password to Analyze:", font=("Arial", 10), fg="#cccccc", bg="#1e1e1e")
input_label.pack()
password_input = tk.Entry(root, font=("Arial", 12), width=30, justify="center")
password_input.pack(pady=5)

analyze_btn = tk.Button(root, text="Analyze Security", font=("Arial", 10, "bold"), bg="#007acc", fg="#ffffff", width=20, command=analyze_password_ui)
analyze_btn.pack(pady=10)

divider = tk.Frame(root, height=2, width=400, bg="#333333")
divider.pack(pady=10)

# Results Display Section
results_frame = tk.Frame(root, bg="#1e1e1e")
results_frame.pack(fill="x", padx=40)

tk.Label(results_frame, text="Security Score:", font=("Arial", 11, "bold"), fg="#ffffff", bg="#1e1e1e").grid(row=0, column=0, sticky="w", pady=5)
score_display = tk.Label(results_frame, text="-", font=("Arial", 11, "bold"), fg="#ffffff", bg="#1e1e1e")
score_display.grid(row=0, column=1, sticky="w", padx=10)

tk.Label(results_frame, text="Shannon Entropy:", font=("Arial", 11, "bold"), fg="#ffffff", bg="#1e1e1e").grid(row=1, column=0, sticky="w", pady=5)
entropy_display = tk.Label(results_frame, text="-", font=("Arial", 11), fg="#ffffff", bg="#1e1e1e")
entropy_display.grid(row=1, column=1, sticky="w", padx=10)

# Suggestions Panel
tk.Label(root, text="Remediation / Suggestions:", font=("Arial", 10, "italic"), fg="#aaaaaa", bg="#1e1e1e").pack(pady=(10, 2))
feedback_display = tk.Label(root, text="", font=("Arial", 10), fg="#ffcc00", bg="#1e1e1e", justify="left", wraplength=350)
feedback_display.pack()

root.mainloop()
