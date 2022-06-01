''' Exercício referente ao vídeo 16 
 André de Oliveira Águila Favoto - 11811EAU013''' 

import csv, wget

url_csv = 'https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python-Patreon-CSV/patrons.csv'
path_destination = './aux_files/'
wget.download(url_csv, path_destination)

html_output = ''
names = []

with open('./aux_files/patrons.csv', 'r') as data_file:
    csv_data = csv.DictReader(data_file)

    #avoiding first line
    next(csv_data)

    for line in csv_data:
        if line['FirstName'] == 'No Reward':
            break
        names.append(f"{line['FirstName']} {line['LastName']}")

html_output += f'<p> There are currently {len(names)} public contributors. Thank you! </p>'

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\n<li>{name}</li>'

html_output += '\n</ul>'

print(html_output)

"""     #avoiding two first lines
    next(csv_data)
    next(csv_data)

    for line in csv_data:
        if line[0] == 'No Reward':
            break
        names.append(f'{line[0]} {line[1]}')

html_output += f'<p> There are currently {len(names)} public contributors. Thank you! </p>'

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\n<li>{name}</li>'

html_output += '\n</ul>' """