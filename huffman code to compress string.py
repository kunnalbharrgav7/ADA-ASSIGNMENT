#  Implement the Huffman coding algorithm to compress a given string in  Python.

import heapq
from collections import defaultdict


def huffman_encoding(data):
    freq_dict = defaultdict(int)
    for char in data:
        freq_dict[char] += 1

    if len(freq_dict) == 1:
        char = list(freq_dict.keys())[0]
        return '0' * freq_dict[char], {'0': char}

    heap = [[freq, [char, '']] for char, freq in freq_dict.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        low = heapq.heappop(heap)
        high = heapq.heappop(heap)
        for pair in low[1:]:
            pair[1] = '0' + pair[1]
        for pair in high[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [low[0] + high[0]] + low[1:] + high[1:])

    encoding = dict(heap[0][1:])
    encoded_data = ''.join([encoding[char] for char in data])

    return encoded_data, encoding


def huffman_decoding(encoded_data, encoding):
    decoding = {code: char for char, code in encoding.items()}
    current_code = ''
    decoded_data = ''
    for bit in encoded_data:
        current_code += bit
        if current_code in decoding:
            decoded_data += decoding[current_code]
            current_code = ''
    return decoded_data


if __name__ == '__main__':
    data = "this is a test string for huffman encoding"
    encoded_data, encoding = huffman_encoding(data)
    print('Encoded data:', encoded_data)
    decoded_data = huffman_decoding(encoded_data, encoding)
    print('Decoded data:', decoded_data)

