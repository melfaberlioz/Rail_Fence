key = 3
plain_text = "butimokaytoneverknow"
cipher_text = ''

cipher_cycle = key * 2 - 2

for row in range(key):
    index = 0

    # For the first rail
    if row == 0:
        while index < len(plain_text):
            cipher_text += plain_text[index]
            index += cipher_cycle

    # For the last rail
    elif row == key - 1:
        index = row
        while index < len(plain_text):
            cipher_text += plain_text[index]
            index += cipher_cycle

    # For the inner rows
    else:
        left_index = row
        right_index = cipher_cycle - row
        while left_index < len(plain_text):
            cipher_text += plain_text[left_index]

            if right_index < len(plain_text):
                cipher_text += plain_text[right_index]

            left_index += cipher_cycle
            right_index += cipher_cycle

print(cipher_text)
