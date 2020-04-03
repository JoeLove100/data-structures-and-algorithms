class Node:

    def __init__(self,
                 start,
                 end,
                 key,
                 successors=None):

        self.start = start
        self.end = end
        self.key = key
        self.suffix_start = None

        if successors is not None:
            self.successors = successors
        else:
            self.successors = []


class SuffixTrie:

    def __init__(self,
                 text):

        self._text = text
        self._nodes = {0: Node(start=0, end=0, key=0)}

    def _split_node(self,
                    current_node,
                    suffix_start,
                    suffix_end):

        count = 0
        split = False
        max_length = min(suffix_end - suffix_start, current_node.end - current_node.start)

        while count < max_length:
            if self._text[suffix_start + count] == self._text[current_node.start + count]:
                count += 1
            else:
                split = True
                break

        if split:
            self._nodes[len(self._nodes)] = Node(start=current_node.start + count,
                                                 end=current_node.end, key=len(self._nodes),
                                                 successors=current_node.successors)
            self._nodes[len(self._nodes)] = Node(start=suffix_start + count,
                                                 end=suffix_end, key=len(self._nodes))

            current_node.end = current_node.start + count
            current_node.successors = [len(self._nodes) - 2, len(self._nodes) - 1]

        return split

    def _build_suffix_tree(self):

        for i in range(len(self._text)):
            # print(i)
            # self.display_all_nodes()
            node_stack = [0]
            letter_count = 0

            while node_stack:
                node_added = False
                current_node_key = node_stack.pop()
                for successor_key in self._nodes[current_node_key].successors:
                    successor_node = self._nodes[successor_key]
                    if self._text[successor_node.start] == self._text[i + letter_count]:
                        node_was_split = self._split_node(successor_node, i + letter_count, len(self._text))
                        if node_was_split:
                            node_added = True
                        else:
                            node_stack.append(successor_key)
                            letter_count += (successor_node.end - successor_node.start)
                            node_added = True
                        break

                if not node_added:
                    self._nodes[len(self._nodes)] = Node(start=i + letter_count,
                                                         end=len(self._text),
                                                         key=len(self._nodes))
                    self._nodes[current_node_key].successors.append(len(self._nodes) - 1)

    def display_all_nodes(self):

        for n in self._nodes.values():
            if n.key == 0:
                continue
            else:
                print(self._text[n.start: n.end])

    def return_nodes(self):

        nodes = []
        for n in self._nodes.values():
            nodes.append(self._text[n.start: n.end])

        return nodes


def get_nodes_2(text):

    trie = SuffixTrie(text)
    trie._build_suffix_tree()
    nodes = trie.return_nodes()
    return nodes


if __name__ == "__main__":

    word = input().strip()
    trie = SuffixTrie(word)
    trie._build_suffix_tree()
    trie.display_all_nodes()

#
# if __name__ == "__main__":
#
#     import random
#     letters = ["A", "G", "T", "C"]
#
#     for _ in range(10000):
#         word = "".join([random.choice(letters) for _ in range(10)]) + "$"
#         nodes_1 = sorted(get_nodes(word))
#         nodes_2 = sorted(get_nodes_2(word))
#         nodes_2.remove("")  # remove root node
#
#         if nodes_1 == nodes_2:
#             print("Ok")
#         else:
#             print(f"Error for {word}")
#             print(f"Old method gives: {nodes_1}")
#             print(f"New method gives {nodes_2}")
#             break






