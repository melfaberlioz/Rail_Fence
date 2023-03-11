key = int(input("Enter a key:"))
with open('cipher_text.txt', 'r') as file:
    cipher_text = file.read()

length = len(cipher_text)
original_text = ''
# original_text = "." * length

cycle = 2 * key - 2
units = length // cycle

rail_lengths = [0] * key

# top rail length
rail_lengths[0] = units

# inner rail fence
for i in range(1, key - 1):
    rail_lengths[i] = 2 * units

# bottom rail fence
rail_lengths[key-1] = units


for i in range(length % cycle):
    if i < key:
        rail_lengths[i] += 1

    else:
        rail_lengths[cycle-i] += 1

# print(rail_lengths)
# print(original_text)

# replace characters in the top rail fence
index = 0
rail_offset = 0
for c in cipher_text[:rail_lengths[0]]:
    original_text = original_text[:index] + c + original_text[index+1:]
    index += cycle

rail_offset += rail_lengths[0]
# print(original_text)

# replace characters in the inner rails
for row in range(1, key - 1):
    left_index = row
    right_index = cycle - row
    left_char = True
    for c in cipher_text[rail_offset:rail_offset+rail_lengths[row]]:
        if left_char:
            plain_text = original_text[:left_index] + c + original_text[left_index + 1:]
            left_index += cycle
            left_char = not left_char
        else:
            plain_text = original_text[:right_index] + c + original_text[right_index+1:]
            right_index += cycle
            left_char = not left_char

rail_offset += rail_lengths[row]

# replace characters in the bottom rail fence
index = key - 1
for c in cipher_text[rail_offset:]:
    plain_text = original_text[:index] + c + original_text[index+1:]
    index += cycle

# with open('decrypted_text.txt', 'w') as file:
#     file.write(cipher_text)
rail_offset += rail_lengths[0]
print(original_text)
