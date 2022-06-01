''' Exercício referente ao vídeo 15 
 André de Oliveira Águila Favoto - 11811EAU013''' 

#Manipulating csv file in format first_name,last_name,email

import csv, wget

""" with open('csvfile.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')

        for line in csv_reader:
            csv_writer.writerow(line)
 """

url_csv = 'https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python-CSV/names.csv'
path_destination = './aux_files/'
wget.download(url_csv, path_destination)

with open('./aux_files/names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file) #associates column title as key and each line as a value of the respective key
    
    with open('./aux_files/new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name', 'email']
        
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        
        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)