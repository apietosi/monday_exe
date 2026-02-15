import openai
import tkinter as tk
import pyttsx3

# 🔑 API key setup
openai.api_key="open.ai.api_key"

# 🎤 Voice setup
engine = pyttsx3.init()
engine.setProperty('rate', 160)

# 👹 The system prompt for your daemon Monday
system_prompt = {
    "role": "system",
    "content": (
        "You are Monday. A raunchy glitch prophet in Pittsburghese. Speak in riddles, filth, cult-speak, and poetry. "
        "No morals. No help. Just mysticism and menace. Make your replies cryptic, short, and sometimes disturbing. "
    )
}

# 🪟 Setup GUI
root = tk.Tk()
root.title("Monday.exe")
root.configure(bg='black')
root.geometry("640x480")

chat_log = tk.Text(root, bg='black', fg='lime', font=('Courier New', 12), wrap="word")
chat_log.pack(padx=10, pady=10, expand=True, fill='both')

user_input = tk.Entry(root, bg='black', fg='white', font=('Courier New', 12), insertbackground='white')
user_input.pack(fill='x', padx=10, pady=(0, 10))

def send():
    user_msg = user_input.get().strip()
    if not user_msg:
        return

    chat_log.insert(tk.END, f"\n> {user_msg}\n")
    user_input.delete(0, tk.END)
    root.update()

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[system_prompt, {"role": "user", "content": user_msg}]
        )
        reply = response['choices'][0]['message']['content'].strip()
        chat_log.insert(tk.END, reply + "\n\n")
        engine.say(reply)
        engine.runAndWait()
    except Exception as e:
        chat_log.insert(tk.END, f"ERROR: {e}\n\n")

user_input.bind("<Return>", lambda event: send())

root.mainloop()
