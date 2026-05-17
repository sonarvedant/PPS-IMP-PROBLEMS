"""
File handling and Dictionaries

FILE
- A file is a named location on disk used to store information.
- Files provide persistent storage in secondary memory.
- Each file is identified by its path. The backslash (\) is the path delimiter on Windows.

Paths
- Absolute path: the complete path from the root directory to the file.
- Relative path: the path from the current working directory to the file.

Types of Files
1) Text file
- Data is stored as readable characters.
- A text/ASCII file contains characters that are easy to read and edit.
- Common file operations: open, read, write, append.
- Text files can be opened with a text editor like Notepad.
- Text files are less likely to become corrupted from small changes.
- Each line may contain characters and ends with a newline marker.
- When writing, newline characters are translated to carriage return/line feed (CR/LF) on Windows.
- When reading, CR/LF sequences are converted back to newline characters.

2) Binary file
- Data is stored in encoded (binary) form.
- Images, audio, and other non-text data use binary files.
- If a single bit is corrupted, the file may become unreadable.
- Binary files cannot be reliably opened with a plain text editor.

Opening Files in Python
- Use the built-in function open() to open a file.
- Syntax: file_object = open(file_name, mode)
- Recommended syntax: with open(file_name, mode) as f:
- File modes:
  - r: open for reading
  - w: open for writing (truncate existing file)
  - x: open for exclusive creation, fails if file exists
  - a: open for appending
  - t: open in text mode
  - b: open in binary mode
  - +: open for both reading and writing

File Object Attributes
- Opening a file returns a file object.
- The file object provides methods and attributes for file operations.
- Always close files when done: file_object.close()

Reading Files
- f.read(): reads the entire file contents.
- print(f.read()): prints the text with newline formatting applied.
- f.readline(): reads a single line from the file.
  - Returns an empty string when the end of file is reached.
- f.readlines(): reads all lines into a list.
- list(f): returns the file contents as a list of lines.

Writing Files
- Open the file in write mode using 'w', 'a', or 'x'.
- Syntax: file.write(contents)
- f.writelines(lines): writes a list of strings to the file.

Appending Files
- Use append mode: 'a' or 'ab'.
- This preserves existing file contents and adds new data at the end.

Dictionaries
Operations
1) Adding items to dictionaries
2) Removing items from dictionaries
3) Updating dictionary values
4) Checking dictionary length
"""
