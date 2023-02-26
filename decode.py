key = 3
cipher_text = "bmyekuioatnvrnwtkoeo"

length = len(cipher_text)

plain_text = "." * length

cycle = 2 * key - 2
units = length // cycle

rail_lengths = [0] * key

# top rail fence
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

# print(plain_text)
# replace characters in the top rail fence
index = 0
rail_offset = 0
for c in cipher_text[:rail_lengths[0]]:
    plain_text = plain_text[:index] + c + plain_text[index+1:]
    index += cycle

rail_offset += rail_lengths[0]
# print(plain_text)

# replace characters in the inner rails
for row in range(1, key - 1):
    left_index = row
    right_index = cycle - row
    left_char = True
    for c in cipher_text[rail_offset:rail_offset+rail_lengths[row]]:
        if left_char:
            plain_text = plain_text[:left_index] + c + plain_text[left_index + 1:]
            left_index += cycle
            left_char = not left_char
        else:
            plain_text = plain_text[:right_index] + c + plain_text[right_index+1:]
            right_index += cycle
            left_char = not left_char

rail_offset += rail_lengths[row]
# print(plain_text)

# replace characters in the bottom rail fence
index = key - 1
for c in cipher_text[rail_offset:]:
    plain_text = plain_text[:index] + c + plain_text[index+1:]
    index += cycle

# rail_offset += rail_lengths[0]
print(plain_text)
