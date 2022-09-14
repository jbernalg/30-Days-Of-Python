# ----------------------File Handling-------------------------

#-------------Open() built-in function----------------
# to handle data
# syntax
# open('filename', mode)  mode(r, a, w, x, t, b)

# r: Read. Opens a file for reading, it returns an error if the file does not exist.
# a: Append. Opens a file for appending, creates the file if it does not exist.
# w: Write. Opens a file for writing, creates the file if it does not exist.
# x: Create. Creates the specified file, return an error if the file exist.
# t: Text. Default value. Text mode
# b: Binary. Binary mode. (images)

#----------------Opening files for reading ----------------------
# the deafult mode of open is reading
# To open file I have created and saved a file named reading_file.txt in the current directory
f = open('./reading_file.txt')
print(f) 

#----------------Reading Methods--------------------
# read(): read the whole text as string
# If we want to limit the number of character we want to read, we can limit it by passing int value
# to the read(number) method.
txt = f.read()
print(type(txt))
print(txt)
f.close()

# let us print the first 10 characters of the text file.
f = open('./reading_file.txt')
txt = f.read(10)
print(txt)
f.close()

# readlines(): read all text line by line and returns a list of lines
f = open('./reading_file.txt')
lines = f.readlines()
print(lines)
f.close()
