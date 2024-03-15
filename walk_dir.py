# Walk through a directory-like structure, outputting the names of folders and files.
# Each folder/file should be indented to the left according to its level from the root,
# and also should have the number of files it contains overall beneath it

"""
Need to walk through the current directory. Outputting the names of folders
and files.

We need to print the files and their indentation. Plus the number of
files in each directory

We want to take the rootdir as input.
Then we will walk through the directory
assembling some form of tree structure.
We will add it to a Tree class and finally
print it out.
"""

from genericpath import isdir
import os
from queue import Queue

class Node:
    """
    Holds the working directory along with the children.
    """
    def __init__(self, path = None) -> None:
        self.path = path
        self.children = []
        self.file_count = 0
        self.indentation = 0

def bfs(path) -> Node:
    """
    Navigate file structure and built a root node
    """
    root = Node(path)
    queue = [(root,0)]
    while queue:
        curr_dir, depth = queue.pop()
        curr_dir.indentation = depth
        files = os.listdir(curr_dir.path)
        
        for file in files:
            full_path = os.path.join(curr_dir.path, file)
            if os.path.isdir(full_path):
                child_node = Node(full_path)
                curr_dir.children.append(child_node)
                queue.append((child_node, depth+1))
            else:
                curr_dir.file_count += 1
    return root

def print_tree(node):
    print(" " * node.indentation + os.path.basename(node.path) + " " + str(node.file_count))
    for child in node.children:
        print_tree(child)

def main():
    root = bfs(os.getcwd())
    print_tree(root)
    return root

if __name__ == "__main__":
    root = main()
