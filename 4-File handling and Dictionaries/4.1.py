#program to print details of file object
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "4.0.notes.py")

A = open(file_path, "r+")
print(A)