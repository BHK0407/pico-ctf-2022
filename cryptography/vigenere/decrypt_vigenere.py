
'''
# Import sys for system operations and colorama for colored text
import sys
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

# Function to encrypt or decrypt using the Vigenere Cipher
def vigenere_cipher(text, key, mode='encrypt'):
    # Initialize the resulting text
    result_text = ''
    # Repeat the key to match the length of the text
    key_repeated = (key * (len(text) // len(key))) + key[:len(text) % len(key)]
    
    # Iterate through each character in the text
    for i in range(len(text)):
        # Check if the character is an alphabet letter
        if text[i].isalpha():
            # Calculate the shift based on the corresponding key letter
            shift = ord(key_repeated[i].upper()) - ord('A')
            # If decrypting, negate the shift
            if mode == 'decrypt':
                shift = -shift
            
            # Encrypt or decrypt uppercase and lowercase letters separately
            if text[i].isupper():
                result_text += chr((ord(text[i]) + shift - ord('A')) % 26 + ord('A'))
            else:
                result_text += chr((ord(text[i]) + shift - ord('a')) % 26 + ord('a'))
        else:
            # If the character is not an alphabet letter, keep it unchanged
            result_text += text[i]
    
    return result_text

# Specify the key
key = "CYLAB"

# Ask the user if they want to encrypt or decrypt
choice = input(f"{Fore.YELLOW}Would you like to encrypt or decrypt a message? (e/d): ").strip().lower()

if choice == 'e':
    # Get user input message to encrypt
    plaintext = input('Enter your message to encrypt: ')
    # Encrypt the plaintext using the Vigenere cipher
    cipher_text = vigenere_cipher(plaintext, key, mode='encrypt')
    # Print the results
    print(f"{Fore.GREEN}Cipher Text: {cipher_text}")
elif choice == 'd':
    # Get user input cipher text to decrypt
    cipher_text = input('Enter the cipher text to decrypt: ')
    # Decrypt the cipher text using the Vigenere cipher
    decrypted_text = vigenere_cipher(cipher_text, key, mode='decrypt')
    # Print the results
    print(f"{Fore.GREEN}Decrypted Text: {decrypted_text}")

else:
    print(f"{Fore.RED}Invalid input.")
    sys.exit()


'''

import string

def decrypt_text(instr, key):
    """
    Decrypts an input string using a key-based cipher.

    Parameters:
    instr (str): The encrypted input string to be decrypted.
    key (str): The key used for decryption.

    Returns:
    str: The decrypted output string.
    """
    # Define ASCII offsets for lowercase and uppercase letters
    offset_lower = ord('a')
    offset_upper = ord('A')
    
    # Define lowercase and uppercase alphabets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    
    # Create dictionaries for lowercase and uppercase letters using the key
    dicts_l = {}
    dicts_u = {}
    
    # Create mapping for lowercase letters based on the key
    for k in key:
        key_loc = ord(k) - offset_upper  # Calculate position in alphabet
        dicts_l[k] = {chr((ord(l) - offset_lower + key_loc) % 26 + offset_lower): l for l in lower}
    
    # Create mapping for uppercase letters based on the key
    for k in key:
        key_loc = ord(k) - offset_upper
        dicts_u[k] = {chr((ord(u) - offset_upper + key_loc) % 26 + offset_upper): u for u in upper}
    
    # Initialize the decrypted output string
    outstr = ""
    count = 0  # Counter for key position
    
    # Decrypt the input string using the dictionaries
    for c in instr:
        if c.isalpha():
            # Get the current key character based on the counter
            key_char = key[count % len(key)]
            
            # Decrypt lowercase letter using dicts_l
            if c.islower():
                outstr += dicts_l[key_char][c]
            
            # Decrypt uppercase letter using dicts_u
            elif c.isupper():
                outstr += dicts_u[key_char][c]
            
            # Increment the counter for key position
            count += 1
        else:
            # Non-alphabetic characters are added to the output as is
            outstr += c
    
    # Return the decrypted output string
    return outstr

# Example usage:
# You can use any input string and key for decryption by calling the function
instr = "rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_f85729e7}"
key = "CYLAB"
decrypted_text = decrypt_text(instr, key)
print(decrypted_text)

