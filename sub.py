# def readFile(fileName):
#     with open("./story.txt","r") as openFile:
#         readFile =  openFile.read()
#         return readFile 

# def  countWords():
#     text  = readFile("./story.txt").split()
#     # print(text)
#     count = {}
#     for i in text:
#         if i in count:
#             count[i] += 1
#         else:
#             count[i] =  1
#     return count

# print(countWords())


# newFile  =  open("zuri.txt","w")
# writeFile = "open"
# finalFile = newFile.write(writeFile)
# newFile.close()

# readFile= newFile.read()
# print(readFile)
# write =  w, read = r, append =a

# openFile = open("zuri.txt","r")
# print(openFile.read())


# # Open the file in append & read mode ('a+')
# with open("sample2.txt", "a+") as file_object:
#     # Move read cursor to the start of file.
#     file_object.seek(0)
#     # If file is not empty then append '\n'
#     data = file_object.read(100)
#     if len(data) > 0 :
#         file_object.write("\n")
#     # Append text at the end of file
#     file_object.write("hello hi")


# fileName = input('Enter .txt file: ')
# msg = input("Enter message you  want to append: ")
# # new_file = open("hello.txt","w")
# openFile = open(fileName, "a")
# openFile.write("\n")
# openFile.write(msg)
# openFile.close()

# readFile=open(fileName,"r")
# readFile.read()

# x=['be','me','to']
# count = 0
# for ae in x:
#     count +=1
#     print(ae)

def readFile(filename):
    openFile = open(filename, "r")
    readFile = openFile.read()
    print(readFile)

readFile("./hello.txt")