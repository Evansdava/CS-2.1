#!python3

from prefixtreenode import PrefixTreeNode


class PrefixTree:
    """PrefixTree: A multi-way prefix tree that stores strings with efficient
    methods to insert a string into the tree, check if it contains a matching
    string, and retrieve all strings that start with a given prefix string.
    Time complexity of these methods depends only on the number of strings
    retrieved and their maximum length (size and height of subtree searched),
    but is independent of the number of strings stored in the prefix tree, as
    its height depends only on the length of the longest string stored in it.
    This makes a prefix tree effective for spell-checking and autocompletion.
    Each string is stored as a sequence of characters along a path from the
    tree's root node to a terminal node that marks the end of the string.
    """

    # Constant for the start character stored in the prefix tree's root node
    START_CHARACTER = ''

    def __init__(self, strings=None):
        """Initialize this prefix tree and insert the given strings, if any."""
        # Create a new root node with the start character
        self.root = PrefixTreeNode(PrefixTree.START_CHARACTER)
        # Count the number of strings inserted into the tree
        self.size = 0
        # Insert each string, if any were given
        if strings is not None:
            for string in strings:
                self.insert(string)

    def __repr__(self):
        """Return a string representation of this prefix tree."""
        return f'PrefixTree({self.strings()!r})'

    def is_empty(self):
        """Return True if this prefix tree is empty (contains no strings)."""
        return self.size == 0

    def contains(self, string):
        """Return True if this prefix tree contains the given string."""
        data = self._find_node(string)
        return data[0].is_terminal() and data[1] == len(string)

    def insert(self, string):
        """Insert the given string into this prefix tree."""
        # Find the prefix of what's already there
        prefix_data = self._find_node(string)
        node = prefix_data[0]

        # If the full string isn't in the tree:
        if prefix_data[1] != len(string):
            # Add each character as a new node
            for char in string[prefix_data[1]:]:
                new_node = PrefixTreeNode(char)
                node.add_child(char, new_node)
                node = node.get_child(char)
            self.size += 1

        # Set the node to terminal regardless of if a new one was needed
        node.terminal = True

    def _find_node(self, string):
        """Return a pair containing the deepest node in this prefix tree that
        matches the longest prefix of the given string and the node's depth.
        The depth returned is equal to the number of prefix characters matched.
        Search is done iteratively with a loop starting from the root node.
        """
        # Match the empty string
        if len(string) == 0:
            return self.root, 0
        # Start with the root node
        node = self.root
        # Keep track of depth
        i = 0
        for i, char in enumerate(string):
            # Get the next character in the string
            next_node = node.children.get(char, None)
            # Return the current node if the next char isn't found
            if next_node is None:
                return node, i
            else:
                node = next_node
        # Return the last node if the loop completes
        return node, i + 1

    def complete(self, prefix):
        """Return a list of all strings stored in this prefix tree that start
        with the given prefix string.
        """
        # Create a list of completions in prefix tree
        completions = []
        # Skip to after the prefix
        node_depth = self._find_node(prefix)
        # If the prefix isn't found, return an empty list
        if len(prefix) > 0 and node_depth[1] == 0:
            return completions

        # Use a stack to conduct iterative depth-first traversal
        # Tuple of current node and depth
        stack = [(node_depth[0], node_depth[1])]
        # Base of all strings will be prefix
        string = prefix
        while len(stack) > 0:
            # Each iteration, pop the last element of the stack
            node_depth = stack.pop()
            # Separate into two variables for ease of use
            node = node_depth[0]
            depth = node_depth[1]
            # Add children of current node to stack
            if node.num_children() > 0:
                for child in node.children.values():
                    stack.append((child, depth + 1))
            # Set the string to the prefix of the node and add character
            string = string[:depth - 1]
            string += node.character

            # Add to the list of completions if node is terminal
            if node.is_terminal():
                completions.append(string)
        # Return strings in alphabetical order
        return sorted(completions)

    def strings(self):
        """Return a list of all strings stored in this prefix tree."""
        # Find all complete strings in the tree
        return self.complete("")

    def _traverse(self, node, prefix, visit):
        """Traverse this prefix tree with recursive depth-first traversal.
        Start at the given node with the given prefix representing its path in
        this prefix tree and visit each node with the given visit function.
        """
        if node.num_children == 0:
            visit(node)
        else:
            for child in node.children:
                self._traverse(node.get_child(child),
                               prefix + node.character, visit)
            visit(node)


def create_prefix_tree(strings):
    print(f'strings: {strings}')

    tree = PrefixTree()
    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')
    print(f'strings: {tree.strings()}')

    print('\nInserting strings:')
    for string in strings:
        tree.insert(string)
        print(f'insert({string!r}), size: {tree.size}')

    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')

    print('\nSearching for strings in tree:')
    for string in sorted(set(strings)):
        result = tree.contains(string)
        print(f'contains({string!r}): {result}')

    print('\nSearching for strings not in tree:')
    prefixes = sorted(set(string[:len(string) // 2] for string in strings))
    for prefix in prefixes:
        if len(prefix) == 0 or prefix in strings:
            continue
        result = tree.contains(prefix)
        print(f'contains({prefix!r}): {result}')

    print('\nCompleting prefixes in tree:')
    for prefix in prefixes:
        completions = tree.complete(prefix)
        print(f'complete({prefix!r}): {completions}')

    print('\nRetrieving all strings:')
    retrieved_strings = tree.strings()
    print(f'strings: {retrieved_strings}')
    matches = set(retrieved_strings) == set(strings)
    print(f'matches? {matches}')


def main():
    # Simpe test case of string with partial substring overlaps
    strings = ['ABC', 'ABD', 'A', 'XYZ']
    create_prefix_tree(strings)

    # Create a dictionary of tongue-twisters with similar words to test with
    tongue_twisters = {
        'Seashells': 'Shelly sells seashells by the sea shore'.split(),
        'Peppers': 'Peter Piper picked a peck of pickled peppers'.split(),
        'Woodchuck': ('How much wood would a wood chuck chuck'
                      ' if a wood chuck could chuck wood').split()
    }
    # Create a prefix tree with the similar words in each tongue-twister
    for name, strings in tongue_twisters.items():
        print(f'{name} tongue-twister:')
        create_prefix_tree(strings)
        if len(tongue_twisters) > 1:
            print('\n' + '=' * 80 + '\n')


if __name__ == '__main__':
    main()
