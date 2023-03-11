key = int(input("Enter a key:"))
with open('cipher_text.txt', 'r') as file:
    ciphertext = file.read()

length = len(ciphertext)

plaintext = '.' * length

cycle = 2 * key - 2
units = length // cycle

rail_lengths = [0] * key

# top rail length
rail_lengths[0] = units
# inner rail length
for i in range(1, key - 1):
    rail_lengths[i] = 2 * units
# bottom rail length
rail_lengths[key-1] = units

for i in range(length % cycle):
    # print(i)
    if i < key:
        rail_lengths[i] += 1
    else:
        rail_lengths[cycle-i] += 1

# print(rail_lengths)

# replace characters in the top rail fence

# print(plaintext)
index = 0
rail_offset = 0
for c in ciphertext[:rail_lengths[0]]:
    plaintext = plaintext[:index] + c + plaintext[index+1:]
    index += cycle

rail_offset += rail_lengths[0]
# print(plaintext)

# replace char in the inner rails
for row in range(1, key - 1):
    left_index = row
    right_index = cycle - row
    left_char = True
    for c in ciphertext[rail_offset:rail_offset+rail_lengths[row]]:
        if left_char:
            plaintext = plaintext[:left_index] + c + plaintext[left_index+1:]
            left_index += cycle
            left_char = not left_char
        else:
            plaintext = plaintext[:right_index] + c + plaintext[right_index+1:]
            right_index += cycle
            left_char = not left_char
    rail_offset += rail_lengths[row]
    # print(plaintext)

# bottom rail fence
index = key - 1
rail_offset = 0
for c in ciphertext[:rail_lengths[0]]:
    plaintext = plaintext[:index] + c + plaintext[index+1:]
    index += cycle
rail_offset += rail_lengths[0]
print(plaintext)
