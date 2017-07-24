"""Trie (digital, radix, prefix tree) -- ordered tree data structure
used to store a dynamic set or associative array
All the descendants of a node have a common prefix
The root = empty string
"""


class TrieNode(object):
    def __init__(self, char):
        self.char = char
        self.children = []    # list of TrieNodes, not characters
        self.words_count = 0  # number matching prefixes

    def get_child(self, letter):
        for child in self.children:
            if child.char == letter:
                return child
        return None


class Trie(object):
    def __init__(self):
        self.root = TrieNode("_")  # any non-alphabet character will do

    def add(self, word):
        current = self.root
        for letter in word:
            next_node = current.get_child(letter)
            if next_node is None:
                next_node = TrieNode(letter)
                current.children.append(next_node)
            next_node.words_count += 1
            current = next_node

    def find(self, prefix):
        current_node = self.root
        for c in prefix:
            next_node = current_node.get_child(c)
            if next_node is None:
                return 0  # reached leaf, prefix not found
            current_node = next_node
        return current_node.words_count


contacts = Trie()
n = int(input())
for _ in range(n):
    op, contact = input().strip().split(' ')
    if op == "add":
        contacts.add(contact)
    elif op == "find":
        print(contacts.find(contact))
