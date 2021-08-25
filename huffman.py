
import heapq
from collections import Counter, namedtuple


class Node(namedtuple("Node", ['left', 'right'])):
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')


class Leaf(namedtuple("Leaf", ['char'])):
    def walk(self, code, acc):
        code[self.char] = acc or '0'


def huffman_encode(s):

    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))

    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, count1, left = heapq.heappop(h)
        freq2, count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1

    code = {}
    if h:
        [(freq, count, root)] = h
        root.walk(code, '')

    return code


def huffman_decode(s, code_dict):

    decoded = ""

    i = 0
    while i < len(s):

        for code in code_dict:
            if s[i:].startswith(code):
                decoded += code_dict[code]
                i += len(code)
                break

    return decoded


def read_and_encode():
    s = input()
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s)
    print(len(code), len(encoded))
    for ch in sorted(code):
        print("{}: {}".format(ch, code[ch]))
    print(encoded)


def read_and_decode():

    n_letters, length = [int(x) for x in input().split()]
    code_dict = {}
    for i in range(n_letters):
        letter, code = input().split(': ')
        code_dict[code] = letter
    encoded = input()

    decoded = huffman_decode(encoded, code_dict)
    print(decoded)


if __name__ == "__main__":

    read_and_decode()

