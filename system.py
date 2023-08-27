import tkinter as tk
from tkinter import scrolledtext

# Detailed information about different types of computer viruses
virus_info = """
1. Worms:
Worms are self-replicating malware that spread without human intervention. They exploit vulnerabilities in operating systems and network protocols to propagate. Worms can consume network bandwidth and slow down systems.

2. Trojans:
Trojans disguise themselves as legitimate software but carry malicious intent. They can create backdoors, steal sensitive information, or harm the system. Trojans are often spread through email attachments or malicious downloads.

3. Ransomware:
Ransomware encrypts files on a victim's system and demands a ransom payment for decryption. It can cause significant data loss and financial damage. Prevention includes regular backups and cautious online behavior.

4. Spyware:
Spyware secretly collects user information without consent. It can monitor browsing habits, capture keystrokes, and steal sensitive data. Anti-malware tools are essential for detecting and removing spyware.

5. Adware:
Adware displays unwanted advertisements to generate revenue for attackers. While not always malicious, adware can be annoying and slow down system performance. Ad-blockers and regular scans help mitigate adware.

6. Rootkits:
Rootkits provide unauthorized access to a computer system, often by exploiting system vulnerabilities. They can hide malicious processes and allow attackers to maintain control over the system. Regular system updates help prevent rootkit attacks.

7. Keyloggers:
Keyloggers record keystrokes on an infected system. Attackers use them to capture sensitive information like passwords and credit card details. Using secure password practices and updated antivirus software can prevent keylogger attacks.
"""

def show_virus_info():
    virus_window = tk.Toplevel(root)
    virus_window.title("Computer Virus Information")

    info_text = scrolledtext.ScrolledText(virus_window, wrap=tk.WORD, width=80, height=30)
    info_text.pack(padx=20, pady=10)
    info_text.insert(tk.END, virus_info)

# Create a GUI window
root = tk.Tk()
root.title("Main Window")

# Create a button to show virus information
virus_button = tk.Button(root, text="Show Virus Info", command=show_virus_info)
virus_button.pack(padx=20, pady=10)

# Start the GUI event loop
root.mainloop()
