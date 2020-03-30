from collections import deque


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

    def add_to_trie(self,
                    word: str) -> None:

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

    def get_adjacency_list(self):

        adj_list = {}
        queue = deque([self._root])

        while queue:
            current = queue.popleft()
            adj_list.update({current.key: []})

            for successor in current.successors:
                adj_list[current.key].append(successor)
                queue.append(successor)

        return adj_list


if __name__ == "__main__":

    n = int(input())
    trie = Trie(Node(0, []))
    c = 1
    words = [input().strip() for _ in range(n)]
    for w in words:
        trie.add_to_trie(w)

    adj = trie.get_adjacency_list()
    for key, successors in adj.items():
        for s in successors:
            print("%d->%s:%s" % (key, s.key, s.letter))


