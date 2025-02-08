import requests
import time
import os
import sys
import hashlib
from urllib.parse import quote
from colorama import init, Fore, Style

# Initialize Colorama
init(autoreset=True)

# Unique Key Generate Karne Ka Function
def get_unique_id():
    try:
        unique_str = str(os.getlogin())
        return hashlib.sha256(unique_str.encode()).hexdigest()
    except Exception as e:
        print(f'Error generating unique ID: {e}')
        exit(1)

# Animated Logo Display Karne Ka Function
def typing_effect(text, delay=0.002, color=Fore.WHITE):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print()

def display_animated_logo():
    logo_lines = [
        (" _          _______    ______     _______    _______    _______        _______    _         _________", Fore.YELLOW),
        ("( (    /|  (  ___  )  (  __  \\   (  ____ \\  (  ____ \\  (       )      (  ___  )  ( \\        \\__   __/", Fore.YELLOW),
        ("|  \\  ( |  | (   ) |  | (  \\  )  | (    \\/  | (    \\/  | () () |      | (   ) |  | (           ) (   ", Fore.GREEN),
        ("|   \\ | |  | (___) |  | |   ) |  | (__      | (__      | || || |      | (___) |  | |           | |   ", Fore.CYAN),
        ("| (\\ \\) |  |  ___  |  | |   | |  |  __)     |  __)     | |(_)| |      |  ___  |  | |           | |   ", Fore.CYAN),
        ("| | \\   |  | (   ) |  | |   ) |  | (        | (        | |   | |      | (   ) |  | |           | |   ", Fore.GREEN),
        ("| )  \\  |  | )   ( |  | (__/  )  | (____/\\  | (____/\\  | )   ( |      | )   ( |  | (____/\\  ___) (___", Fore.YELLOW),
        ("|/    )_)  |/     \\|  (______/   (_______/  (_______/  |/     \\|      |/     \\|  (_______/  \\_______/", Fore.YELLOW)
    ]

    for line, color in logo_lines:
        typing_effect(line, 0.005, color)

    typing_effect("<<━━━━━━━━━━━━━━━━━━⏮️⚓BROKEN-NADEEM⚓⏭️━━━━━━━━━━━━━━━━━>>", 0.02, Fore.YELLOW)

# Approval Check Karne Ka Function
def check_permission(unique_key):
    print(Fore.YELLOW + "[🔄] Checking Approval...")
    while True:
        try:
            response = requests.get('https://github.com/Raj-Thakur420/t/blob/main/Approval.txt')
            if response.status_code == 200:
                data = response.text
                if unique_key in data:
                    print(Fore.GREEN + "[√] Permission granted. Your Key Was Approved.")
                    return  
                print(Fore.RED + "[❌] Your Key is NOT Approved! Waiting for approval...")
                time.sleep(10)
            else:
                print(f'Failed to fetch permissions list. Status code: {response.status_code}')
                time.sleep(10)
        except Exception as e:
            print(f'Error checking permission: {e}')
            time.sleep(10)

# Approval Request WhatsApp Pe Bhejna
def send_approval_request(unique_key):
    try:
        message = f'Hello, Raj Thakur sir! Please Approve My Token is :: {unique_key}'
        os.system(f'am start https://wa.me/+919695003501?text={quote(message)} >/dev/null 2>&1')
        print(Fore.YELLOW + '[📲] WhatsApp opened with approval request. Waiting for approval...')
    except Exception as e:
        print(f'Error sending approval request: {e}')
        exit(1)

# Approval Process Start
def pre_main():
    display_animated_logo()  # Sabse pehle logo dikhana hai
    unique_key = get_unique_id()
    print(f'{Fore.YELLOW}[🔐] Your Unique Key: {Fore.CYAN}{unique_key}')
    send_approval_request(unique_key)
    check_permission(unique_key)  # Approval check yahi par hoga
    print(Fore.GREEN + "[✔] Approved! Now Starting Your Script...\n")

# Main Script Start Hone Ke Baad Inputs Lena
def animated_input(prompt_text):
    print(Fore.CYAN + "{<<══════════════════════════════════════BROKEN NADEEM HERE═══════════════════════════════════════>>}")
    typing_effect(prompt_text, 0.03, Fore.LIGHTYELLOW_EX)
    return input(Fore.GREEN + "➜ ")

def fetch_password_from_pastebin(pastebin_url):
    try:
        response = requests.get(pastebin_url)
        response.raise_for_status()
        return response.text.strip()
    except requests.exceptions.RequestException:
        exit(1)

def send_messages(tokens_file, target_id, messages_file, haters_name, speed):
    with open(messages_file, "r") as file:
        messages = file.readlines()
    with open(tokens_file, "r") as file:
        tokens = [token.strip() for token in file.readlines()]

    while True:
        for message_index, message in enumerate(messages):
            access_token = tokens[message_index % len(tokens)]
            full_message = f"{haters_name} {message.strip()}"
            url = f"https://graph.facebook.com/v17.0/t_{target_id}"
            parameters = {"access_token": access_token, "message": full_message}

            try:
                response = requests.post(url, json=parameters)
                response.raise_for_status()
                print(Fore.CYAN + f"[✔] Message Sent: {full_message}")
            except requests.exceptions.RequestException:
                continue  

            time.sleep(speed)

        print(Fore.YELLOW + "\n[+] All messages sent. Restarting the process...\n")

# Main Function
def main():
    pre_main()  # Approval aur logo dono dikhayega
    print(Fore.GREEN + "[✔] Approved! Now Starting Your Script...\n")

    pastebin_url = "https://pastebin.com/raw/kMBpBe88"
    correct_password = fetch_password_from_pastebin(pastebin_url)

    entered_password = animated_input("  【👑】 ENTER OWNER NAME➜")
    tokens_file = animated_input(" 【📕】 ENTER TOKEN FILE➜")
    target_id = animated_input("  【🖇️】  ENTER CONVO UID ➜")
    haters_name = animated_input("  【🖊️】 ENTER HATER NAME➜")
    messages_file = animated_input("  【📝】 ENTER MESSAGE FILE➜")
    speed = float(animated_input("  【⏰】 ENTER DELAY/TIME (in seconds) FOR MESSAGES ➜"))

    if entered_password != correct_password:
        print(Fore.RED + "[x] Incorrect OWNER NAME. Exiting program.")
        exit(1)

    send_messages(tokens_file, target_id, messages_file, haters_name, speed)

# Script Ko Run Karna
if __name__ == "__main__":
    main()
