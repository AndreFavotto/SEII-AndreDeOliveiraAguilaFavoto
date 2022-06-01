''' Exercício referente ao vídeo 15 
 André de Oliveira Águila Favoto - 11811EAU013''' 

#Manipulating csv file in format first_name,last_name,email

import csv

""" with open('csvfile.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')

        for line in csv_reader:
            csv_writer.writerow(line)
 """

with open('csvfile.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file) #associates column title as key and each line as a value of the respective key
    
    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name', 'email']
        
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        
        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)
        
