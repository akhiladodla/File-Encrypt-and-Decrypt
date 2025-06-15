import tkinter as tk
from tkinter import filedialog, messagebox
from crypto_engine import CryptoEngine

class EncryptionToolGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("File Encryption/Decryption Tool")
        self.root.geometry("400x300")  # Set window size to 400x300 pixels

        # Create GUI elements
        tk.Label(root, text="Password:").pack(pady=5)  # Label for password field
        self.password_entry = tk.Entry(root, show="*")  # Password field (hidden with *)
        self.password_entry.pack(pady=5)

        tk.Button(root, text="Select File", command=self.select_file).pack(pady=5)  # File selection button
        self.file_label = tk.Label(root, text="No file selected")  # Display selected file name
        self.file_label.pack(pady=5)

        tk.Button(root, text="Encrypt", command=self.encrypt).pack(pady=5)  # Encrypt button
        tk.Button(root, text="Decrypt", command=self.decrypt).pack(pady=5)  # Decrypt button

        self.selected_file = None  # Variable to store the selected file path

    def select_file(self):
        # Open a file picker dialog and store the selected file path
        self.selected_file = filedialog.askopenfilename()
        if self.selected_file:
            # Update the label to show the file name (not the full path)
            self.file_label.config(text=self.selected_file.split("/")[-1])

    def encrypt(self):
        # Check for missing file or password
        if not self.selected_file or not self.password_entry.get():
            messagebox.showerror("Error", "Please select a file and enter a password")
            return
        try:
            # Create a CryptoEngine instance with the user's password
            crypto = CryptoEngine(self.password_entry.get())
            # Output file will have a ".enc" extension
            output_file = self.selected_file + ".enc"
            # Encrypt the file
            crypto.encrypt_file(self.selected_file, output_file)
            # Show success message
            messagebox.showinfo("Success", f"File encrypted as {output_file}")
        except Exception as e:
            # Show error message if encryption fails
            messagebox.showerror("Error", str(e))

    def decrypt(self):
        # Check for missing file or password
        if not self.selected_file or not self.password_entry.get():
            messagebox.showerror("Error", "Please select a file and enter a password")
            return
        try:
            # Create a CryptoEngine instance with the user's password
            crypto = CryptoEngine(self.password_entry.get())
            # Output file will have a ".dec" extension
            output_file = self.selected_file + ".dec"
            # Decrypt the file
            crypto.decrypt_file(self.selected_file, output_file)
            # Show success message
            messagebox.showinfo("Success", f"File decrypted as {output_file}")
        except Exception as e:
            # Show error message if decryption fails (e.g., wrong password)
            messagebox.showerror("Error", "Invalid password or corrupted file")

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = EncryptionToolGUI(root)
    root.mainloop()