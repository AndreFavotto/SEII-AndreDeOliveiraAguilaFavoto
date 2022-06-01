''' Exercício referente ao vídeo 14 
 André de Oliveira Águila Favoto - 11811EAU013''' 

#Automatically rename files from "Title - Course - #num .ext" to "num-Title.ext"

import os

os.chdir('desired_files_path')

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f) #separating file from extension
    f_title, f_course, f_num = f_name.split('-') #Splitting filename into parts
    #Removing spaces
    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2) #Remove spaces, get digits in front of "#" and fill with zeroes on the left

    new_name = f'{f_num}-{f_title}{f_ext}'
    os.rename(f, new_name)