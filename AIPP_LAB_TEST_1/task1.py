from collections import deque

def reverse_list(lst):
    """Return a new list with elements of lst in reverse order."""
    if not isinstance(lst, list):
        raise TypeError("reverse_list expects a list")
    return lst[::-1]


if __name__ == "__main__":
    # Test cases
    tests = [
        ([], []),
        ([1], [1]),
        ([1, 2, 3], [3, 2, 1]),
        (["a", "b", "c"], ["c", "b", "a"]),
        ([1, "a", None], [None, "a", 1]),
    ]

    for inp, expected in tests:
        out = reverse_list(inp)
        assert out == expected, f"Expected {expected}, got {out}"
        assert out is not inp, "Function should return a new list (not modify in-place)"

    print("All tests passed.")


    def reverse_list_for(lst):
        """Return a new list reversed using an index loop."""
        if not isinstance(lst, list):
            raise TypeError("reverse_list expects a list")
        res = []
        for i in range(len(lst) - 1, -1, -1):
            res.append(lst[i])
        return res

    def reverse_list_reversed(lst):
        """Return a new list using the built-in reversed() iterator."""
        if not isinstance(lst, list):
            raise TypeError("reverse_list expects a list")
        return list(reversed(lst))

    def reverse_list_copy_then_reverse(lst):
        """Make a shallow copy and call list.reverse() on it."""
        if not isinstance(lst, list):
            raise TypeError("reverse_list expects a list")
        copy = lst[:]  # shallow copy
        copy.reverse()
        return copy

    def reverse_list_deque(lst):
        """Use collections.deque.extendleft to build the reversed list."""
        if not isinstance(lst, list):
            raise TypeError("reverse_list expects a list")
        d = deque()
        d.extendleft(lst)
        return list(d)

    def reverse_list_recursive(lst):
        """Recursive implementation (not suitable for very large lists)."""
        if not isinstance(lst, list):
            raise TypeError("reverse_list expects a list")
        if not lst:
            return []
        return reverse_list_recursive(lst[1:]) + [lst[0]]
    
