import os

def read_dir(folder):
    for root, dirs, files in os.walk(folder):
        # print(root, dirs, files)
        level = root.count(os.sep)
        indent = ' ' * 4 * level
        print(f'{indent} [{os.path.basename(root)}]')
        sub_indent = ' ' * 4 * (level + 1)
        # print(root, files, level, indent, sub_indent)
        for file in files:
            print(f'{sub_indent} {file}')

read_dir('folder')
"""
 [folder]
     1.txt
     [subfolder1]
         2.txt
         3.txt
     [subfolder2]
         5.txt
         [subfolder2-1]
             4.txt

"""





# tree = os.walk('folder')
# # print(tree)  # <generator object walk at 0x01DE34C0>
# for files in tree:
#     print(files)
#
# """
# Вывод print(files):
#
# ('folder', ['subfolder1', 'subfolder2'], ['1.txt'])
# ('folder\\subfolder1', [], ['2.txt', '3.txt'])
# ('folder\\subfolder2', ['subfolder2-1'], ['5.txt'])
# ('folder\\subfolder2\\subfolder2-1', [], ['4.txt'])
# """
