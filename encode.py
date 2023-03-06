key = int(input("Enter a key:"))
with open('encode2.txt', 'r') as file:
    original_text = file.read().replace('\n', '')
    length = len(original_text)
# original_text = open('encode.txt', 'r')
# cipher_text = original_text
cipher_text = ''

cipher_cycle = key * 2 - 2

for row in range(key):
    index = 0

    # For the first rail
    if row == 0:
        while index < len(original_text):
            cipher_text += original_text[index]
            index += cipher_cycle

    # For the last rail
    elif row == key - 1:
        index = row
        while index < len(original_text):
            cipher_text += original_text[index]
            index += cipher_cycle

    # For the inner rows
    else:
        left_index = row
        right_index = cipher_cycle - row
        while left_index < len(original_text):
            cipher_text += original_text[left_index]

            if right_index < len(original_text):
                cipher_text += original_text[right_index]

            left_index += cipher_cycle
            right_index += cipher_cycle

with open('cipher_text.txt', 'w') as file:
    file.write(cipher_text)



# print(cipher_text)
