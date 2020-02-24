"""This will handle the hashing of files. It's probably gonna go away eventually, cause rn I don't know what I'm doing"""

import md5
import os

hashPath = "C:/Users/zwebb/Documents/Practice"
mf = open("testfile.json", "w")

#traverses whole filepath of the specified project folder, hashing each file and writing the hash and accompanying filename to a temp file
for root, dirs, files in os.walk(hashPath):
    for file in files:
        mf.write(os.path.join(os.path.relpath(root, hashPath), file) + ' ' + md5.md5(os.path.join(root,file)) + '\n')

mf.close()