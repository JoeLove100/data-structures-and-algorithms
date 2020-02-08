from collections import namedtuple
from typing import Any

Bracket = namedtuple("Bracket", ["char", "position"])


class Stack:

    def __init__(self):
        self._items = []

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def add(self,
            element: Any) -> None:
        self._items.append(element)

    def pop(self) -> Any:
        return self._items.pop()


def _are_matching(left: str,
                  right: str) -> bool:
    """
    check if the left and right input form a
    correctly ordered pair of brackets
    """

    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text: str,
                  success_message: str) -> str:
    """
    iterate through the input text and search for brackets
    which are not paired up - return the index of the first
    incorrect closing bracket if one exists, or the last
    unclosed open if that exists
    """
    opening_brackets_stack = Stack()
    for i, character in enumerate(text):
        if character in "([{":
            opening_brackets_stack.add(Bracket(character, i + 1))  # add 1 for the 1-based index
        if character in ")]}":
            if opening_brackets_stack.is_empty():
                # no possible corresponding open bracket
                return str(i + 1)
            else:
                prev_bracket = opening_brackets_stack.pop()
                matches = _are_matching(prev_bracket.char, character)

                if not matches:
                    # closes the wrong type of bracket
                    return str(i + 1)

    if opening_brackets_stack.is_empty():
        return success_message
    else:
        # left over open bracket - return index of right-most instance
        remaining_open_bracket = opening_brackets_stack.pop()
        return str(remaining_open_bracket.position)


def main():
    text = input()
    mismatch = find_mismatch(text, "Success")
    print(mismatch)


if __name__ == "__main__":
    main()
