import pytest
from splay_tree import newNode, splay

# Valid test cases
def test_valid_balanced_tree():
    root = newNode(100)
    root.left = newNode(50)
    root.right = newNode(200)
    root.left.left = newNode(40)
    root.left.left.left = newNode(30)
    root.left.left.left.left = newNode(20)

    splayed_root = splay(root, 20)
    assert splayed_root.key == 20

def test_valid_unbalanced_tree():
    root = newNode(100)
    root.right = newNode(200)
    root.right.right = newNode(300)
    root.right.right.right = newNode(400)

    splayed_root = splay(root, 400)
    assert splayed_root.key == 400

def test_valid_single_node_tree():
    root = newNode(100)

    splayed_root = splay(root, 100)
    assert splayed_root.key == 100

def test_valid_smallest_and_largest_keys():
    root = newNode(100)
    root.left = newNode(50)
    root.left.left = newNode(20)
    root.right = newNode(200)
    root.right.right = newNode(300)

    splayed_smallest = splay(root, 20)
    assert splayed_smallest.key == 20

    splayed_largest = splay(root, 300)
    assert splayed_largest.key == 300

def test_valid_multiple_repeated_keys():
    root = newNode(100)
    root.left = newNode(50)
    root.left.left = newNode(50)
    root.right = newNode(200)
    root.right.right = newNode(200)

    splayed_root = splay(root, 50)
    assert splayed_root.key == 50

# Invalid test cases
def test_invalid_empty_tree():
    root = None

    splayed_root = splay(root, 100)
    assert splayed_root is None

def test_invalid_key():
    root = newNode(100)
    root.left = newNode(50)
    root.right = newNode(200)

    splayed_root = splay(root, 300)
    assert splayed_root.key == 200

def test_invalid_tree_structure():
    root = newNode(100)
    root.left = newNode(50)
    root.left.right = newNode(120)
    root.right = newNode(200)

    splayed_root = splay(root, 120)
    assert splayed_root.key != 120

def test_invalid_unexpected_data_types():
    root = newNode(100)

    with pytest.raises(TypeError):
        splayed_root = splay(root, "invalid_key")


# Boundary test cases
def test_boundary_single_node_tree_lowest_and_highest_keys():
    root = newNode(float('-inf'))
    root.right = newNode(float('inf'))

    splayed_lowest = splay(root, float('-inf'))
    assert splayed_lowest.key == float('-inf')

    splayed_highest = splay(root, float('inf'))
    assert splayed_highest.key == float('inf')

def test_boundary_tree_all_keys_same():
    root = newNode(100)
    root.left = newNode(100)
    root.right = newNode(100)

    splayed_root = splay(root, 100)
    assert splayed_root.key == 100

def test_boundary_tree_two_nodes_specific_key_orders():
    root = newNode(100)
    root.left = newNode(50)
    root.right = newNode(200)

    # Ascending key order
    splayed_asc = splay(root, 200)
    assert splayed_asc.key == 200

    # Descending key order
    splayed_desc = splay(root, 50)
    assert splayed_desc.key == 50

    # Same key values
    splayed_same = splay(root, 100)
    assert splayed_same.key == 100

def test_boundary_tree_extreme_unbalanced_structure():
    root = newNode(100)
    root.right = newNode(200)
    root.right.right = newNode(300)
    root.right.right.right = newNode(400)
    root.right.right.right.right = newNode(500)

    splayed_root = splay(root, 500)
    assert splayed_root.key == 500

# Run the tests
if __name__ == "__main__":
    pytest.main(['-v', 'black_box_testing.py'])
