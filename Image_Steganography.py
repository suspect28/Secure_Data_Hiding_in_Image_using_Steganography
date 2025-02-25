from PIL import Image
import itertools

def encode_image(image_path, message, output_path):
    image = Image.open(image_path)
    encoded_image = image.copy()
    width, height = image.size
    message += chr(0)  # Add a null character to mark the end of the message
    message_bits = ''.join(format(ord(char), '08b') for char in message)
    message_bits_iter = iter(message_bits)

    for x, y in itertools.product(range(width), range(height)):
        pixel = list(image.getpixel((x, y)))
        for n in range(3):  # Iterate over RGB channels
            try:
                pixel[n] = pixel[n] & ~1 | int(next(message_bits_iter))
            except StopIteration:
                encoded_image.putpixel((x, y), tuple(pixel))
                encoded_image.save(output_path)
                return
        encoded_image.putpixel((x, y), tuple(pixel))

def decode_image(image_path):
    image = Image.open(image_path)
    width, height = image.size
    message_bits = []

    for x, y in itertools.product(range(width), range(height)):
        pixel = list(image.getpixel((x, y)))
        for n in range(3):
            message_bits.append(pixel[n] & 1)

    message_bits = ''.join(map(str, message_bits))
    message_chars = [chr(int(message_bits[i:i+8], 2)) for i in range(0, len(message_bits), 8)]
    return ''.join(message_chars).split(chr(0))[0]  # Split at the null character and return the message

def main():
    while True:
        choice = input("Menu:\n  1. Encrypt\n  2. Decrypt\n  3. Exit\nEnter your choice: ")

        if choice == '1':
            image_path = input("Enter the path of the image to encode: ")
            message = input("Enter the message to encode: ")
            output_path = input("Enter the output path for the encoded image: ")
            encode_image(image_path, message, output_path)
            print("Message encoded and saved to", output_path)
        elif choice == '2':
            image_path = input("Enter the path of the image to decode: ")
            message = decode_image(image_path)
            print("Decoded message:", message)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
