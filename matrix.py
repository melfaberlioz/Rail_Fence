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


def rail_fence_encode_file(input_filename, output_filename, key):
    block_size = 1024

    with open(input_filename, 'r') as input_file, \
            open(output_filename, 'w') as output_file:
        while True:
            block = input_file.read(block_size)
            if not block:
                break

            # encode the block using the rail fence cipher
            encoded_block = encoding_text(block, key)

            # write the encoded block to the output file
            output_file.write(encoded_block)


def rail_fence_decode_file(input_filename, output_filename, key):
    block_size = 1024
    with open(input_filename, 'r') as input_file, \
            open(output_filename, 'w') as output_file:
        while True:
            block = input_file.read(block_size)
            if not block:
                break  # end of file

            # decode the block using the Rail Fence Cipher
            decoded_block = decoding_text(block, key)

            # write the decoded block to the output file
            output_file.write(decoded_block)


key_1 = int(input("Enter the key: "))
# Read text from file
encoded_file = encoding_text('encode2.txt', key_1)
rail_fence_encode_file('encode2.txt', 'cipher_text.txt', key_1)

key_2 = int(input("Enter the key: "))
decoded_file = decoding_text('decrypted_text.txt', key_2)
rail_fence_decode_file('cipher_text.txt', 'decrypted_text.txt', key_2)
# encode_rail_fence('encode2.txt', key_1)
# (rail_fence_encode_file(, 'cipher_text.txt', key)
