from PIL import Image

def encrypt_decrypt_image(image_path, shift, encrypt=True):
 
    with Image.open(image_path) as img:
       
        width, height = img.size
        
       
        new_img = Image.new('RGB', (width, height))
        
       
        for x in range(width):
            for y in range(height):
               
                r, g, b = img.getpixel((x, y))
                
                if encrypt:
               
                    r = (r + shift) % 256
                    g = (g + shift) % 256
                    b = (b + shift) % 256
                else:
                   
                    r = (r - shift) % 256
                    g = (g - shift) % 256
                    b = (b - shift) % 256
                
                new_img.putpixel((x, y), (r, g, b))
        
        if encrypt:
            new_img.save('encrypted_image.png')
            print("Image encrypted and saved as 'encrypted_image.png'")
        else:
            new_img.save('decrypted_image.png')
            print("Image decrypted and saved as 'decrypted_image.png'")

def main():
    while True:
        print("Choose an option:")
        print("1. Encrypt Image")
        print("2. Decrypt Image")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            image_path = input("Enter the path to the image file to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypt_decrypt_image(image_path, shift)
        elif choice == '2':
            image_path = input("Enter the path to the image file to decrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypt_decrypt_image(image_path, shift, encrypt=False)
        elif choice == '3':
            print("Exiting program.")
            print("Coded by SWAPNIL SARODE!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
