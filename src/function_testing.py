from hypothesis import given
from hypothesis import strategies as st
import random
from splay_tree import insert, splay


# Property-based testing with Hypothesis
@given(st.lists(st.integers(), min_size=0, max_size=1000))
def test_splay_function(keys):
    if len(keys) > 0:
        search_key = random.choice(keys)
    else:
        search_key = 1
    #print(keys, search_key)

    # Create the initial binary search tree
    root = None
    for key in keys:
        root = insert(root, key)

    # Perform the search operation
    result = splay(root, search_key)

    # Validate the splay tree structure and splay function
    assert validate_splay_tree(result)
    if len(keys) > 0:
        assert result.key == search_key


# Helper function to validate the splay tree structure
def validate_splay_tree(root):
    if root is None:
        return True
    if root.left and root.left.key > root.key:
        return False
    if root.right and root.right.key < root.key:
        return False
    return validate_splay_tree(root.left) and validate_splay_tree(root.right)


# Run the tests
if __name__ == "__main__":
    test_splay_function()
