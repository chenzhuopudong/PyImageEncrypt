def read_words(input_words):
    print(type(input_words))
    print(input_words.encode())


def chinese_word_encode_decode(input_words):
    strings = input_words.encode()
    print(strings)
    result = strings.decode('utf-8')
    print(result)


def write_into_file(input_words, output_file):
    strings = input_words.encode()
    print(strings)
    hex_for_file = bytes(strings)
    tmp_file = open(output_file, 'wb')
    tmp_file.write(hex_for_file)
    tmp_file.close()
