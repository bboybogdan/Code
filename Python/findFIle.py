import os
fileType = '.py'

anyFile = os.listdir('Python')
for file in anyFile:
	if file.endswith(fileType):
		print(file)

