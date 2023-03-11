import time

key = int(input("Enter a key:"))
# block_size = 1024
with open('encode2.txt', 'r') as file:
    # while True:
    block_of_plain_text = file.read().replace('\n', '')
        # if not block_of_plain_text:
        #     break
    length = len(block_of_plain_text)
cipher_text = ''

cipher_cycle = key * 2 - 2

for row in range(key):
    index = 0

    # For the first rail
    if row == 0:
        while index < len(block_of_plain_text):
            cipher_text += block_of_plain_text[index]
            index += cipher_cycle

    # For the last rail
    elif row == key - 1:
        index = row
        while index < len(block_of_plain_text):
            cipher_text += block_of_plain_text[index]
            index += cipher_cycle

    # For the inner rows
    else:
        left_index = row
        right_index = cipher_cycle - row
        while left_index < len(block_of_plain_text):
            cipher_text += block_of_plain_text[left_index]

            if right_index < len(block_of_plain_text):
                cipher_text += block_of_plain_text[right_index]

            left_index += cipher_cycle
            right_index += cipher_cycle

with open('cipher_text.txt', 'w') as file:
    file.write(cipher_text)


start_time = time.time()
end_time = time.time()
interpretation_time = end_time - start_time

print(f"Time of interpretation: {interpretation_time:.10f} seconds")











# original_text = open('encode.txt', 'r')
# cipher_text = original_text