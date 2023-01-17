import sys

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            char_code = ord(char)
            char_code -= shift
            if char.isupper():
                if char_code < ord('A'):
                    char_code += 26
            elif char.islower():
                if char_code < ord('a'):
                    char_code += 26
            decrypted_text += chr(char_code)
        else:
            decrypted_text += char
    return decrypted_text

def shift_check(text):
    common_words = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I', 'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at']
    text = text.lower()
    count = 0
    for word in common_words:
        if word in text:
            count += 1
    if count > len(common_words) / 2:
        return True
    else:
        return False


def main():
    if len(sys.argv) != 2:
        print("Error: Missing command-line argument.")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            text = file.read()
    except:
        print(f"Error:Cannot open {filename}. Sorry about that.")
        sys.exit(1)

    for shift in range(1, 26):
        decrypted_text = decrypt(text, shift)
        if shift_check(decrypted_text):
            print(decrypted_text)
            break
    else:
        print("Could not decrypt the message.")

if __name__ == "__main__":
    main()
