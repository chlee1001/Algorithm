import ast

file = open('vertexInfo.txt', 'r')
contents = file.read()
vertexInfo = ast.literal_eval(contents)
file.close()
print(type(vertexInfo))
print(vertexInfo)

file = open('calInfo.txt', 'r')
contents = file.read()
calInfo = ast.literal_eval(contents)
file.close()
print(type(calInfo))
print(calInfo)

