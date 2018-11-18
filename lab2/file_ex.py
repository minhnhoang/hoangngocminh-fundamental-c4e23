content = '''
Tiêu đề:
Nội dung
'''
# Option 1:
# #1. Open file
# # f = open("content.txt","w") # w:write, to edit file
# #2. Write file
# f.write(content)
# #3. Close file
# f.close()

# Option 2:
with open("content.txt","r") as f:
    c = f.read()
    print(c)
    # f.write(content)