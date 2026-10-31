# f=open("demo.txt","a")

# f.write("this is python class")

# # print(f.readline())

# f.close()
# import os
# os.remove("sample.txt")

with open("demo.txt","r") as f:
    data=f.read()

with open("demo.txt","w") as f:

    newdata=data.replace("c++","python")
    f.write(newdata)

with open("t.text", "w") as f:
    f.write("rahman")