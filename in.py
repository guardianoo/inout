import os

cwd = os.getcwd()
path = os.path.abspath(cwd)

file = __file__

os.listdir('D:\AGENCIA BIT3D\#25 ARCIELO FITNESS\# BOLETOS')

os.chdir('D:\AGENCIA BIT3D\#25 ARCIELO FITNESS\# BOLETOS')

os.getcwd()

full_list = os.listdir(path)
files_list = [i.lower() for i in full_list if os.path.isfile(i) and '.py' not in i]

# types = list(set([i.split('.')[-1] for i in files_list]))
# for file_type in types:
#     os.mkdir(file_type)

# for file in files_list:
#     path_from = cwd + '/' + file
#     path_to = cwd + '/' + file.split('.')[-1] + '/' + file
#     os.replace(path_from, path_to)