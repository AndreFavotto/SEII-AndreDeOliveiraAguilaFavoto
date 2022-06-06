''' Exercício referente ao vídeo 20 
 André de Oliveira Águila Favoto - 11811EAU013''' 


try:
    f = open('./aux_files/testfile.txt')
    # if f.name == 'unwanted_file.txt':
    #     raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print('Executing finally')

