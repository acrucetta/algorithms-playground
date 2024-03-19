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
from dataclasses import dataclass, field

@dataclass
class Node:
    path : str
    children : list = field(default_factory=list)
    file_count : int = 0
    indentation : int = 0

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
        curr_dir.file_count = len(files)

        for file in files:
            full_path = os.path.join(curr_dir.path, file)
            child_node = Node(full_path, [], 0, depth)
            curr_dir.children.append(child_node)

            if os.path.isdir(full_path):
                queue.append((child_node, depth+1))
            else:
                curr_dir.file_count += 1
    return root

def dfs(node : Node, visited : list = [], depth : int = 0):
    visited.append(node)
    paths = os.listdir(node.path)
    for path in paths:
        full_path = os.path.join(node.path, path)
        child_node = Node(full_path, [], 0, depth + 1)
        node.children.append(child_node)
        if os.path.isdir(full_path) and child_node not in visited:
            dfs(child_node, visited, depth+1)
        else:
            node.file_count+=1

def print_tree(node):
    print(" " * node.indentation + os.path.basename(node.path) + " " + str(node.file_count))
    for child in node.children:
        print_tree(child)

def main():
    path = os.path.join(os.getcwd(), "test")
    # root = bfs(path)
    root_node = Node(path)
    dfs(root_node)
    print_tree(root_node)
    return "yay"

if __name__ == "__main__":
    root = main()
