'''
data=f.read()-reads entire file
data=f.read(5)- read first five charachters
data=f.readline() - reads one line at a time
'''

File=open('file.txt','r')
# data=File.read()
# print(data)
# print(type(data))

line1=File.readline()
print(line1)

line2=File.readline()
print(line2)
File.close()