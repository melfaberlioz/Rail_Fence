def encoding_text(text, key):
    # create matrix to hold the encoded text
    # means create an empty list for each rail
    matrix = [[] for _ in range(key)]
    # loop through the plaintext, adding each letter to the appropriate rail
    row = 0
    direction = 1
    # Iterate over the text and add each character to the matrix
    for char in text:
        matrix[row].append(char)
        row += direction

        # if we reach the top or bottom of the matrix, change direction
        if row == key - 1 or row == 0:
            direction *= -1

    # join the letters in each row to create the ciphertext/encoded text
    ciphertext = ''
    for row in matrix:
        ciphertext += ''.join(row)
    return ciphertext
    # return ''.join([''.join(row) for row in matrix])


def decoding_text(text, key):
    # Create matrix to hold the decoded text
    matrix = [['' for _ in range(len(text))] for _ in range(key)]
    row = 0
    direction = 1

    # Create a matrix with placeholder characters
    for i in range(len(text)):
        matrix[row][i] = '-'
        row += direction
        if row == key - 1 or row == 0:
            direction *= -1

    # replace the placeholder characters with the actual characters
    index = 0
    for i in range(key):
        for j in range(len(text)):
            if matrix[i][j] == '-' and index < len(text):
                matrix[i][j] = text[index]
                index += 1

    # Read the decoded string from the matrix
    row = 0
    decoded_text = ''
    direction = 1
    for i in range(len(text)):
        decoded_text += matrix[row][i]
        row += direction
        if row == key - 1 or row == 0:
            direction *= -1
    return decoded_text


def encode_file(input_file, output_file, key):
    block_size = 1024

    with open(input_file, 'r') as input_file, \
            open(output_file, 'w') as output_file:
        while True:
            block_of_text = input_file.read(block_size)
            if not block_of_text:
                break

            # encode the block using the rail fence cipher
            encoded_block = encoding_text(block_of_text, key)

            # write the encoded block to the output file
            output_file.write(encoded_block)


def decode_file(input_file, output_file, key):
    block_size = 1024
    with open(input_file, 'r') as input_file, \
            open(output_file, 'w') as output_file:
        while True:
            block_of_text = input_file.read(block_size)
            if not block_of_text:
                break  # end of file

            # decode the block using the Rail Fence Cipher
            decoded_block = decoding_text(block_of_text, key)

            # write the decoded block to the output file
            output_file.write(decoded_block)


key_1 = int(input("Enter the key: "))
encoded_file = encoding_text('encode2.txt', key_1)
encode_file('encode2.txt', 'cipher_text.txt', key_1)

key_2 = int(input("Enter the key: "))
decoded_file = decoding_text('decrypted_text.txt', key_2)
decode_file('cipher_text.txt', 'decrypted_text.txt', key_2)
