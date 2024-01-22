def xor_cipher(input_path, output_path, key):
    try:
        with open(input_path, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{input_path}' was not found.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    result = ""
    for i in range(len(text)):
        current_char = text[i]
        current_key_char = key[i % len(key)]
        result += chr(ord(current_char) ^ ord(current_key_char))

    try:
        with open(output_path, 'w') as file:
            file.write(result)
        print(f"File successfully written to {output_path}")
    except Exception as e:
        print(f"An error occurred while writing to file: {e}")

    print("Output:")
    print(result)

# Example usage
key = "YourSecretKey"  # Replace with your secret key
input_file = "path/to/your/input.txt"  # Path to the input file
output_file = "path/to/your/encrypted.txt"  # Path to save the encrypted file
xor_cipher(input_file, output_file, key)
