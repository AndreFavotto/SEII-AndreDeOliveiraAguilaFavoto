''' Exercício referente ao vídeo 10 
 André de Oliveira Águila Favoto - 11811EAU013''' 

import os

""" print(os.getcwd()) 

# os.chdir('DesidedFolder/Subfolder/')

print(os.listdir()) #files and folders in current directory

#manipulating files and directories
os.makedirs('Folder_os/Subfolder_os')
os.rmdir('Folder_os/Subfolder_os')
os.rename('filetorename.extension', 'newname.extension')
 """

#os.stat 
""" from datetime import datetime

modtime = os.stat('py09.py').st_mtime
print(f'modified at: {datetime.fromtimestamp(modtime)}')
 """
#os.walk('path') goes through the path tracking every folder and files, returning dirpath, dirname and filename (tuple) 

print(os.environ.get('HOME'))

#os.path.join(path, otherpath) - avoids double slashes, spaces or other errors while joining paths

""" os.path.basename('tmp/text.txt')
os.path.dirname('tmp/text.txt')
os.path.split('tmp/text.txt')
os.path.exists('tmp/text.txt')
os.path.isfile('tmp/text.txt')
os.path.isdir('tmp/text.txt')
os.path.splitext('tmp/text.txt') #separates filename and extension
print(dir(os.path)) """