def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt a message? (E/D): ").upper()
        if choice not in ['E', 'D']:
            print("Invalid choice. Please select 'E' for encryption or 'D' for decryption.")
            continue
        
        message = input("Enter the message: ")
        shift = int(input("Enter the shift value: "))
        
        if choice == 'E':
            result = encrypt(message, shift)
            print(f"Encrypted message: {result}")
        else:
            result = decrypt(message, shift)
            print(f"Decrypted message: {result}")
        
        continue_choice = input("Do you want to perform another operation? (yes/no): ").lower()
        if continue_choice != 'yes':
            break

if __name__ == "__main__":
    main()
