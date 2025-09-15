import tkinter as tk
import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Function to speak text
def speak_text():
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        engine.say(text)
        engine.runAndWait()

# Function to update volume
def update_volume(value):
    engine.setProperty("volume", float(value))

# Create the main window
root = tk.Tk()
root.title("Text to Speech (TTS) App")
root.geometry("400x350")

# Label
label = tk.Label(root, text="Enter text to speak:", font=("Arial", 12))
label.pack(pady=10)

# Textbox
text_entry = tk.Text(root, height=6, width=40, font=("Arial", 11))
text_entry.pack(pady=5)

# Speak button
speak_button = tk.Button(root, text="Speak", command=speak_text,
                         font=("Arial", 12), bg="lightblue")
speak_button.pack(pady=10)

# Volume label
volume_label = tk.Label(root, text="Volume:", font=("Arial", 12))
volume_label.pack(pady=5)

# Volume slider (0.0 to 1.0)
volume_slider = tk.Scale(root, from_=0.0, to=1.0, resolution=0.1,
                         orient="horizontal", command=update_volume, length=200)
volume_slider.set(1.0)  # default full volume
volume_slider.pack(pady=5)

# Run the application
root.mainloop()
