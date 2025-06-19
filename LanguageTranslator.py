from tkinter import Tk, Label, Text, Button, ttk, StringVar
from googletrans import Translator, LANGUAGES

# Create the Translator object
translator = Translator()

# Function to perform translation
def translate_text():
    try:
        input_text = text_input.get("1.0", "end-1c")  # Get input text
        source_lang = src_lang.get()
        target_lang = tgt_lang.get()

        # Perform translation
        translated = translator.translate(input_text, src=source_lang, dest=target_lang)

        # Display the translated text
        text_output.delete("1.0", "end")
        text_output.insert("1.0", translated.text)
    except Exception as e:
        text_output.delete("1.0", "end")
        text_output.insert("1.0", f"Error: {e}")

# Function to clear text fields
def clear_text():
    text_input.delete("1.0", "end")
    text_output.delete("1.0", "end")

# Initialize the main window
root = Tk()
root.title("Google Translator App")
root.geometry("600x400")
root.resizable(False, False)

# Source Language Dropdown
Label(root, text="Source Language:", font=("Arial", 12)).place(x=30, y=20)
src_lang = StringVar()
src_dropdown = ttk.Combobox(root, textvariable=src_lang, values=list(LANGUAGES.values()), state="readonly", width=30)
src_dropdown.place(x=150, y=20)
src_dropdown.set("english")  # Default value

# Target Language Dropdown
Label(root, text="Target Language:", font=("Arial", 12)).place(x=30, y=60)
tgt_lang = StringVar()
tgt_dropdown = ttk.Combobox(root, textvariable=tgt_lang, values=list(LANGUAGES.values()), state="readonly", width=30)
tgt_dropdown.place(x=150, y=60)
tgt_dropdown.set("hindi")  # Default value

# Input Text Box
Label(root, text="Text to Translate:", font=("Arial", 12)).place(x=30, y=100)
text_input = Text(root, height=6, width=70, wrap="word", font=("Arial", 10))
text_input.place(x=30, y=130)

# Output Text Box
Label(root, text="Translated Text:", font=("Arial", 12)).place(x=30, y=250)
text_output = Text(root, height=6, width=70, wrap="word", font=("Arial", 10), bg="#f0f0f0")
text_output.place(x=30, y=280)

# Translate Button
translate_button = Button(root, text="Translate", font=("Arial", 12), bg="blue", fg="white", command=translate_text)
translate_button.place(x=470, y=20)

# Clear Button
clear_button = Button(root, text="Clear", font=("Arial", 12), bg="red", fg="white", command=clear_text)
clear_button.place(x=470, y=60)

# Run the GUI application
root.mainloop()