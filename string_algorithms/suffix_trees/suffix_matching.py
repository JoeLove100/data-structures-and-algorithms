from guppy import hpy


class Node:

    def __init__(self,
                 start,
                 end):

        self.start = start
        self.end = end
        self.suffix_start = None
        self.successors = []


class SuffixTrie:

    def __init__(self,
                 text,
                 root):

        self._text = text
        self._root = root

    def _build_suffix_trie(self):

        for i in range(len(self._text)):
            suffix = self._text[i:]
            letter_count = 0
            current_node = self._root

            while letter_count < len(suffix):
                next_node = None
                for successor in current_node.successors:
                    if self._text[successor.start] == suffix[letter_count]:
                        next_node = successor
                        letter_count += 1
                        break

                if next_node is None:
                    break
                else:
                    current_node = next_node

            while letter_count < len(suffix):
                next_node = Node(start=i + letter_count, end=i + letter_count)
                current_node.successors.append(next_node)
                current_node = next_node
                letter_count += 1

            current_node.suffix_start = i

    def _collapse_trie(self):

        stack = [self._root]

        while stack:
            current_node = stack.pop()
            next_node = current_node

            while len(next_node.successors) == 1:
                next_node = next_node.successors[0]

            current_node.end = next_node.end
            current_node.suffix_start = next_node.suffix_start
            current_node.successors = next_node.successors

            for successor in current_node.successors:
                stack.append(successor)

    def _get_nodes(self):

        stack = [self._root]
        nodes = []

        while stack:
            current_node = stack.pop()

            if current_node.start is not None and current_node.end is not None:
                nodes.append(self._text[current_node.start: current_node.end + 1])

            for successor in current_node.successors:
                stack.append(successor)

        return nodes

    def create_and_return_tree(self):

        self._build_suffix_trie()
        self._collapse_trie()
        return self._get_nodes()


def get_nodes(text):
    trie = SuffixTrie(text, Node(start=None, end=None))
    tree = trie.create_and_return_tree()
    return tree





