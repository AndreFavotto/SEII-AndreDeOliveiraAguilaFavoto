#For practice: copying and renaming files from Thread modules since the 
#examples are the same, with a few changes

import os, shutil

for file in os.listdir('../Thread/'):
    if file == 'photos_thread06':
        continue
    shutil.copy(f'../Thread/{file}', '.')
    name, number_n_ext = file.split('thread')
    new_name = f'Multiprocessing{number_n_ext}'
    os.rename(f'./{file}', new_name)
