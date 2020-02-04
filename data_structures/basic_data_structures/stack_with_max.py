import sys


class StackWithMax:
    """
    implementation of a stack class which can
    retrieve the max element in O(1) time
    """

    def __init__(self):
        self.__stack = []
        self.__max_stack = []

    def push(self,
             a: int) -> None:
        self.__stack.append(a)
        if len(self.__max_stack) == 0 or self.__max_stack[-1] <= a:
            self.__max_stack.append(a)

    def pop(self) -> int:
        assert(len(self.__stack))
        p = self.__stack.pop()
        if p == self.__max_stack[-1]:
            self.__max_stack.pop()
        return p

    def max(self) -> int:
        return self.__max_stack[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.push(int(query[1]))
        elif query[0] == "pop":
            stack.pop()
        elif query[0] == "max":
            print(stack.max())
        else:
            assert 0
