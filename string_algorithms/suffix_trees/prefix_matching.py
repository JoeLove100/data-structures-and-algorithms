class Node:

    def __init__(self,
                 key,
                 letter):

        self.key = key
        self.letter = letter
        self.successors = []


class Trie:

    def __init__(self,
                 root):

        self._root = root
        self._key_count = 1
        self._const = "$"

    def add_to_trie(self,
                    word: str) -> None:

        word = word + self._const
        current_node = self._root
        next_node = None
        letter_count = 0

        while letter_count < len(word):
            for successor in current_node.successors:
                next_node = None
                if successor.letter == word[letter_count]:
                    next_node = successor
                    letter_count += 1
                    break

            if next_node is not None:
                current_node = next_node
            else:
                break

        while letter_count < len(word):
            new_successor = Node(self._key_count, word[letter_count])
            current_node.successors.append(new_successor)
            current_node = new_successor
            self._key_count += 1
            letter_count += 1

    def prefix_match(self,
                     text,
                     position):

        current_node = self._root
        output = []
        count = 0

        while count < len(text):
            next_node = None
            for successor in current_node.successors:
                if successor.letter == self._const:
                    output.append(position)
                elif (count < len(text)) and (successor.letter == text[count]):
                    next_node = successor

            if next_node is None:
                break
            else:
                count += 1
                current_node = next_node

        return output


def prefix_match(text,
                 trie: Trie):

    output = []

    for i in range(len(text)):
        output.extend(trie.prefix_match(text[i:], i))

    return output


def get_match_positions(text,
                        patterns):

    trie = Trie(Node(0, None))
    for p in patterns:
        trie.add_to_trie(p)

    matches = prefix_match(text, trie)
    return matches


def get_match_positions_slow(text,
                             patterns):

    output = []

    for p in patterns:
        for i in range(len(text) - len(p)):
            if text[i: i + len(p)] == p:
                output.append(i)

    return sorted(output)


if __name__ == "__main__":

    txt = input().strip() + "$"
    n_patterns = int(input())
    patterns = [input().strip() for _ in range(n_patterns)]
    matches = get_match_positions(txt, patterns)

    if not matches:
        print("")
    else:
        for m in matches:
            print(m, end=" ")


# if __name__ == "__main__":
#
#     r = get_match_positions('bdabdbaabd', ['ad', 'db', 'bd', 'dc'])
#     print(r)

#
# if __name__ == "__main__":
#
#     import random
#
#     letters = ["a", "b", "c", "d"]
#
#     for _ in range(10000):
#
#         patterns = []
#
#         for _ in range(4):
#             patterns.append("".join([random.choice(letters) for _ in range(2)]))
#
#         patterns = list(set(patterns))
#
#         txt = "".join([random.choice(letters) for _ in range(10)])
#
#         try:
#             my_answer = get_match_positions(txt, patterns)
#             correct_answer = get_match_positions_slow(txt, patterns)
#         except IndexError:
#             print("Index error")
#
#         if my_answer == correct_answer:
#             print("OK")
#         else:
#             print(f"Error for patterns: {patterns} and text: {txt}")
#             print(f"My answer was {my_answer}")
#             print(f"Correct answer was {correct_answer}")
#             break





