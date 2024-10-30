"""
    Perform Caesar Cipher encryption or decryption based on the given parameters.

    :param text: The text to encrypt or decrypt.
    :param shift: The number of positions to shift the letters.
    :param encrypt: Whether to encrypt (True) or decrypt (False) the text.
    :return: The encrypted or decrypted text.
    """
def caesar_cipher(text, shift, encrypt=True):
    result = ''
    
  
    for char in text:
        
        if char.isalpha():
           
            base = ord('A') if char.isupper() else ord('a')
            
            if encrypt:
                
                shifted = (ord(char) - base + shift) % 26 + base
            else:
               
                shifted = (ord(char) - base - shift) % 26 + base
                
            result += chr(shifted)
        else:
          
            result += char
    
    return result

def main():
    while True:
        print("Choose an option:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            message = input("Enter the message to encrypt: ")
            print("Shift value is the number of positions you move each letter to encrypt your message.")
            shift = int(input("Enter the shift value: "))
            
            encrypted_message = caesar_cipher(message, shift)
            print(f"Encrypted message: {encrypted_message}")
        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value used while encrypting the message : "))
            decrypted_message = caesar_cipher(message, shift, encrypt=False)
            print(f"Decrypted message: {decrypted_message}")
        elif choice == '3':
            print("Exiting program.")
            print("Coded by Swapnil Sarode!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
