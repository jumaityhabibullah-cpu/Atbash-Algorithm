def atbash_cipher(text):
    result = ""

    for char in text:
        if char.isalpha():
            # Uppercase letters
            if char.isupper():
                result += chr(65 + (25 - (ord(char) - 65)))
            # Lowercase letters
            else:
                result += chr(97 + (25 - (ord(char) - 97)))
        else:
            # Non-alphabet characters remain unchanged
            result += char

    return result

def main():
    print("Atbash Cipher")
    plaintext = input("Enter plaintext: ")

    # Encrypt using Atbash
    encrypted = atbash_cipher(plaintext)
    print("\nEncrypted (Atbash):", encrypted)

    # Decrypt (same process as encryption)
    decrypted = atbash_cipher(encrypted)
    print("Decrypted (Original):", decrypted)
    
if __name__ == "Main":
    main()
