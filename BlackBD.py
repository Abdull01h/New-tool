import random
import threading
import time
import tkinter as tk


class AdvancedBlackBDRansomware:

  def __init__(self, master):
    self.master = master
    self.master.attributes("-fullscreen", True)
    self.master.attributes("-topmost", True)
    self.master.configure(bg="black")

    # Block window closing and Alt+F4 completely
    self.master.protocol("WM_DELETE_WINDOW", self.disable_event)

    # Main layout frame
    main_frame = tk.Frame(master, bg="black")
    main_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=40)

    # Header branding
    brand_lbl = tk.Label(
        main_frame,
        text="[ BLACKBD ADVANCED CYBERSECURITY RESEARCH LAB ]",
        font=("Courier", 14, "bold"),
        fg="cyan",
        bg="black",
    )
    brand_lbl.pack(anchor="w", pady=5)

    # Main warning title
    title_lbl = tk.Label(
        main_frame,
        text="YOUR SYSTEM & FILES HAVE BEEN ENCRYPTED!",
        font=("Courier", 22, "bold"),
        fg="red",
        bg="black",
    )
    title_lbl.pack(anchor="w", pady=15)

    # Sub frame for left and right split layout
    content_frame = tk.Frame(main_frame, bg="black")
    content_frame.pack(fill=tk.BOTH, expand=True, pady=10)

    # Left side: Description, countdown, and contact info
    left_frame = tk.Frame(content_frame, bg="black")
    left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    desc_text = (
        "What happened to your files?\n"
        "All your important documents, photos, databases, and other files\n"
        "are encrypted with strong military-grade algorithms.\n\n"
        "This is an educational simulation created by BlackBD.\n"
        "To get your decryption key or for support, contact us at:\n"
        "Email: blackbd2.0@proton.me\n\n"
        "Time left before permanent deletion:"
    )

    desc_lbl = tk.Label(
        left_frame,
        text=desc_text,
        font=("Courier", 11),
        fg="white",
        bg="black",
        justify="left",
    )
    desc_lbl.pack(anchor="w", pady=5)

    # Live countdown clock
    self.time_left = 72 * 3600  # 72 Hours
    self.timer_lbl = tk.Label(
        left_frame, text="72:00:00", font=("Courier", 28, "bold"), fg="red", bg="black"
    )
    self.timer_lbl.pack(anchor="w", pady=5)

    # Password section
    key_frame = tk.Frame(left_frame, bg="black")
    key_frame.pack(anchor="w", pady=10)

    tk.Label(
        key_frame,
        text="Enter Decryption Key:",
        font=("Courier", 12, "bold"),
        fg="cyan",
        bg="black",
    ).pack(anchor="w", pady=2)

    self.entry = tk.Entry(
        key_frame, font=("Courier", 16), width=25, show="*"
    )
    self.entry.pack(anchor="w", pady=2)

    self.btn = tk.Button(
        key_frame,
        text="Decrypt Files",
        font=("Courier", 12, "bold"),
        bg="red",
        fg="white",
        padx=10,
        pady=5,
        command=self.check_key,
    )
    self.btn.pack(anchor="w", pady=5)

    self.status_lbl = tk.Label(
        left_frame, text="", font=("Courier", 11, "bold"), fg="red", bg="black"
    )
    self.status_lbl.pack(anchor="w", pady=2)

    # Right side: Live file encryption progress logs
    right_frame = tk.Frame(
        content_frame, bg="#111111", bd=2, relief=tk.SUNKEN
    )
    right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20)

    tk.Label(
        right_frame,
        text="--- ENCRYPTION LOGS ---",
        font=("Courier", 10, "bold"),
        fg="#00FF00",
        bg="#111111",
    ).pack(pady=5)

    self.log_box = tk.Text(
        right_frame,
        font=("Courier", 9),
        fg="#00FF00",
        bg="#0a0a0a",
        bd=0,
        highlightthickness=0,
    )
    self.log_box.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Initialize threads for timer and logs
    self.running = True
    threading.Thread(target=self.update_timer, daemon=True).start()
    threading.Thread(target=self.simulate_encryption_logs, daemon=True).start()

  def update_timer(self):
    while self.running and self.time_left > 0:
      mins, secs = divmod(self.time_left, 60)
      hours, mins = divmod(mins, 60)
      time_format = f"{hours:02d}:{mins:02d}:{secs:02d}"
      try:
        self.timer_lbl.config(text=time_format)
      except:
        break
      time.sleep(1)
      self.time_left -= 1

  def simulate_encryption_logs(self):
    fake_dirs = [
        "/home/blackbd/Documents/passwords.txt",
        "/home/blackbd/Pictures/family_photo.png",
        "/var/www/html/database.sql",
        "/home/blackbd/Desktop/project_alpha.py",
        "/etc/shadow",
        "/home/blackbd/Downloads/crypto_wallet.dat",
    ]
    while self.running:
      file_path = random.choice(fake_dirs)
      log_msg = f"[+] Encrypted: {file_path} [OK]\n"
      try:
        self.log_box.insert(tk.END, log_msg)
        self.log_box.see(tk.END)
      except:
        break
      time.sleep(0.4)

  def check_key(self):
    # Decryption password is set to 'blackbd123'
    if self.entry.get() == "blackbd123":
      self.running = False
      self.master.destroy()
    else:
      self.status_lbl.config(
          text="[-] Invalid Key! Files remain encrypted."
      )

  def disable_event(self):
    pass


if __name__ == "__main__":
  root = tk.Tk()
  app = AdvancedBlackBDRansomware(root)
  root.mainloop()
