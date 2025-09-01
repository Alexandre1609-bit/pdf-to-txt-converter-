import os
import PyPDF2
import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title("pdf en txt")
root.minsize(400, 200)

def convertir():
    if not os.path.isdir("temp"):
        os.mkdir("temp")

    # Demande des fichiers
    pdf_path = filedialog.askopenfilename(
        title="Choisir un fichier PDF",
        filetypes=[("Fichiers PDF", "*.pdf")]
    )
    if not pdf_path:
        return  # l'utilisateur annule

    txt_path = filedialog.asksaveasfilename(
        title="Enregistrer sous",
        defaultextension=".txt",
        filetypes=[("Fichiers texte", "*.txt")]
    )
    if not txt_path:
        return  # l'utilisateur annule

    # Dossier temporaire
    BASEDIR = os.path.realpath("temp")

    # Si pas de chemin TXT fourni → crée un nom automatique
    if len(txt_path) == 0:
        txt_path = os.path.join(
            BASEDIR,
            os.path.basename(os.path.normpath(pdf_path)).replace(".pdf", "") + ".txt"
        )

    # Lecture du PDF
    with open(pdf_path, "rb") as pdf_obj:
        pdf_read = PyPDF2.PdfReader(pdf_obj)

        # Parcours des pages
        for i, page in enumerate(pdf_read.pages):
            text = page.extract_text() or ""  # parfois None
            with open(txt_path, "a+", encoding="utf-8") as f:
                f.write(text + "\n")

            print(f"--- Page {i+1} ---")
            print(text)

    messagebox.showinfo("Succès", f"Conversion terminée !\nEnregistré dans :\n{txt_path}")

# --- bouton convertir ---
btn = tk.Button(root, text="Convertir un PDF en TXT", command=convertir)
btn.pack(pady=20)

root.mainloop()
