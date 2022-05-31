''' Exercício referente ao vídeo 11 
 André de Oliveira Águila Favoto - 11811EAU013''' 

""" f = open('./aux_files/test.txt', 'r')

print(f.name)
print(f.mode)
f.close() """

with open('./aux_files/test.txt','r') as f:
    #this mode excuses the need for closing the file.
    """ for line in f:
        print(line)  """

    #reading "little by little - 100 by 100 characters"
    """ size_to_read = 100
    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end='')
        f_contents = f.read(size_to_read) #reads only the 100 non-readen characters
         """
    #f.seek(number) moves the reading cursor to the number° character
    pass

with open('./aux_files/test.txt','r') as rf:
    with open('./aux_files/test2.txt','w') as wf:
        for lin in rf:
            wf.write(lin)

#to read/write in binary mode, we need to add a b next to the options r or w