def rail_fence_encrypt(plain_text, num_rails):
    fence = [[] for _ in range(num_rails)]  # create an empty fence
    rail = 0
    direction = 1  # direction of the rails
    for char in plain_text:
        fence[rail].append(char)
        rail += direction
        if rail == num_rails - 1 or rail == 0:
            direction = -direction  # switch direction at the ends
    # join the fence rails to form the cipher text
    cipher_text = ""
    for rail in fence:
        cipher_text += "".join(rail)
    return cipher_text

def rail_fence_decrypt(cipher_text, num_rails):
    fence = [[] for _ in range(num_rails)]  # create an empty fence
    rail = 0
    direction = 1  # direction of the rails
    for i in range(len(cipher_text)):
        fence[rail].append(None)  # placeholder for letters to be added
        rail += direction
        if rail == num_rails - 1 or rail == 0:
            direction = -direction  # switch direction at the ends
    # fill in the fence rails with the cipher text
    index = 0
    for rail in fence:
        for i in range(len(rail)):
            rail[i] = cipher_text[index]
            index += 1
    # read the fence rails in a zigzag to form the plain text
    plain_text = ""
    rail = 0
    direction = 1  # direction of the rails
    for i in range(len(cipher_text)):
        plain_text += fence[rail][0]  # take the first letter of the rail
        fence[rail] = fence[rail][1:]  # remove the first letter
        rail += direction
        if rail == num_rails - 1 or rail == 0:
            direction = -direction  # switch direction at the ends
    return plain_text

# read plain text from file
with open('encode.txt', 'r') as file:
    plain_text = file.read().replace('\n', '')

num_rails = 3

# encrypt
cipher_text = rail_fence_encrypt(plain_text, num_rails)
print(cipher_text)

# write cipher text to file
with open('cipher_text.txt', 'w') as file:
    file.write(cipher_text)

# read cipher text from file
with open('cipher_text.txt', 'r') as file:
    cipher_text = file.read().replace('\n', '')

# decrypt
decrypted_text = rail_fence_decrypt(cipher_text, num_rails)
print(decrypted_text)

# write decrypted text to file
with open('decrypted_text.txt', 'w') as file:
    file.write(decrypted_text)
