for i in range (2,21):
    if i==12 or i==13:
        continue
    f = open(f"py{str(i).rjust(2,'0')}.py", 'w')
    f.write(f"''' Exercício referente ao vídeo {str(i).rjust(2,'0')} \n André de Oliveira Águila Favoto - 11811EAU013''' ")
    f.close()