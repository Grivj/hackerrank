"""Solution for: https://www.hackerrank.com/challenges/one-week-preparation-kit-queue-using-two-stacks/problem"""


class Queue:
    """
    A queue is an abstract data type that maintains the order in which elements were added to it,
    allowing the oldest elements to be removed from the front and new elements to be added to the rear.
    """

    def __init__(self, stack_1: list = [], stack_2: list = []):
        self.stack_1 = stack_1  # used for enqueue operations
        self.stack_2 = stack_2  # used for dequeue operations

    def enqueue(self, x: int) -> None:
        """Add a new element x to the end of the queue."""
        self.stack_1.append(x)

    def dequeue(self) -> int:
        """Remove the element from the front of the queue and return it."""
        if not self.stack_2:
            self._transpose_stack_1()

        return self.stack_2.pop()

    def _transpose_stack_1(self) -> None:
        """
        Transpose the totality of stack_1 into stack_2.
        Results in stack_1 being reversed into stack_2.
        """
        while len(self.stack_1) > 0:
            self.stack_2.append(self.stack_1.pop())

    def print_head(self) -> None:
        """Print the element at the front of the queue."""
        if not self.stack_2:
            self._transpose_stack_1()

        print(self.stack_2[-1])


if __name__ == '__main__':
    n_queries = int(input())  # Input: Number of queries to perform.
    q = Queue()

    for _ in range(1, n_queries + 1):
        query = list(
            # Input: Query to perform. (Type:int, x:Optional[int])
            map(int, input().rstrip().split())
        )
        query_type = query[0]

        if query_type == 1:
            """Enqueue element x into the end of the queue."""
            x = query[1]
            q.enqueue(x)

        elif query_type == 2:
            """Dequeue the element at the front of the queue."""
            q.dequeue()

        elif query_type == 3:
            """Print the element at the front of the queue."""
            q.print_head()
