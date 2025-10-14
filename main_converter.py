# JOHANNA OKAS / KTA-25 / ARVUSYSTEEMID 

from lookup_table import octal_to_binary
import time

# ANSI color codes text
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def slow_print(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def is_valid_octal(octal_str):
    return all(char in octal_to_binary for char in octal_str)

def convert_octal_to_binary(octal_str):
    result = ""

    for digit in octal_str:
        input(f"{GREEN}> Press {RESET}ENTER{GREEN} to convert [{RESET}{digit}{GREEN}] to Binary...{RESET}")
        binary = octal_to_binary[digit]
        result += binary
        print(f"{GREEN}> OCT {RESET}{digit}{GREEN} ==> BIN {RESET}{binary}")
    
    # Only show full binary once, after all digits are converted
    print(f"\n{GREEN}>> FINAL BINARY:{RESET} {result}")
    return result

def main():
    print((f'{GREEN} ========{RESET} OCTAL > BINARY CONVERTER {GREEN}======={RESET}\n'
           f'{GREEN}##{RESET} Johanna Okas / KTA-25 / Arvusysteemid {GREEN}##{RESET}\n'
           '-------------------------------------------\n'))

    while True:
        slow_print(f"{GREEN}>> ENTER OCTAL NUMBER {RESET}")
        octal = input(f"{GREEN}> {RESET}").strip()

        if not octal:
            print((f'{RED}!! EMPTY INPUT. Please enter a valid octal number.\n'
            f'Octal numbers only use digits 0-7. Example: 57, 123, 640\n{RESET}'))
            continue

        if not is_valid_octal(octal):
            print((f'{RED}!! INVALID INPUT. Please enter a valid octal number.\n'
            f'Octal numbers only use digits 0-7. Example: 57, 123, 640\n{RESET}'))
            continue

        convert_octal_to_binary(octal)

        again = input(f"{GREEN}> CONVERT ANOTHER OCTAL? ({RESET}Y/N{GREEN}):{RESET} ").strip().lower()
        if again != 'y':
            print("> HEAD AEGA. /|\\ ^._.^ /|\\")
            break
        print(f"\n-------------------------------------------\n")

if __name__ == "__main__":
    main()