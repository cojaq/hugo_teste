from bs4 import BeautifulSoup
import json
import os.path
from template_students import get_template
import os
from collections import Counter

def no_accents(s):
    import unicodedata
    return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')) 

def extractor(s):
    if s.find('\n') == -1:
        return  s[:s.find("(")], s[s.find("(")+1:s.find(")")], ""
    return  s[:s.find("(")], s[s.find("(")+1:s.find(")")], s[s.find('\n')+1:]

def process(s, category):
    import unicodedata
    import re

    name, role, work = extractor(s)
    username = no_accents(name.split()[0]).lower()
    display_order = 10

    try:
        year = int(re.findall(r'\d{4}', role)[-1]) 
    except:
        year = 2000

    if 'alumni' in category:
        group = 'Alumni'
    else:
        group = 'Researchers'

    if category == 'alumni_pos':
        role = f'Post-Doctoral Alumni ({year})| ' + role
        display_order = 10

    elif category == 'alumni_phd':
        role = f'PhD Alumni ({year})| ' + role
        display_order = 20

    elif category == 'alumni_master':
        role = f'MSc Alumni ({year})| ' + role
        display_order = 30

    elif category == 'alumni_undergrad':
        role = f'IC/TF Alumni ({year})| ' + role
        display_order = 40

    else:
        role = ' Student| ' + role
        display_order = 50

    dd = {'username' : username, 'name':name, 'role': role, 'work':work,
            'category':category, 'group': group, 'display_order': display_order,
            'year': year}

    return dd

def process_all(uls):
    list_of_students = []

    current_students = uls[0]
    for s in current_students.findAll('li'):
        d = process(s.text, "current")
        list_of_students.append(d)

    pos_docs_alumini= uls[1]
    for s in pos_docs_alumini.findAll('li'):
        d = process(s.text, "alumni_pos")
        list_of_students.append(d)

    phd_alumini = uls[2]
    for s in phd_alumini.findAll('li'):
        d = process(s.text, "alumni_phd")
        list_of_students.append(d)

    master_aluminis = uls[3:15]
    for master_alumini in master_aluminis:
        for s in master_alumini.findAll('li'):
            d = process(s.text, "alumni_master")
            list_of_students.append(d)

    undergrad_aluminis = uls[15:]
    for undergrad_alumini in undergrad_aluminis:
        for s in undergrad_alumini.findAll('li'):
            d = process(s.text, "alumni_undergrad")
            list_of_students.append(d)

    return list_of_students

def generate_json(html):
    with open("supervision.html") as fp:
        soup = BeautifulSoup(fp, "html.parser")

    uls = soup.findAll('ul')

    list_of_students = process_all(uls)

    my_own_order = ['current', 'alumni_pos', 'alumni_phd', 'alumni_master','alumni_undergrad']
    order = {key: i for i, key in enumerate(my_own_order)}

    list_of_students = sorted(list_of_students, key=lambda e: (order[e['category']], e['username'], e['role']))

    return list_of_students


if __name__ == '__main__':

    if not os.path.exists('students.json'):
        list_of_students = generate_json("supervision.html")
        with open('students.json', 'w', encoding='utf8') as json_file:
            json.dump(list_of_students, json_file, indent=4, ensure_ascii=False)

    with open('students.json', encoding='utf-8-sig') as json_file:
        json_data = json.loads(json_file.read())

    c = Counter([i['username'] for i in json_data])

    conflicts = [p for p in c.most_common() if p[1] > 1]

    for username, cnt in conflicts:
        conflicts = [i for i in json_data if i['username'] == username]
        print('Conflito com username: '+username)
        for i in conflicts:
            print('username: '+i['username']+' name: '+i['name']+ ' role: '+i['role'])
        print('=================')

    if conflicts:
        print('Resolva os conflitos no arquivos students.json antes de continuar')
        exit()


    for student in json_data:
        name = student['name']
        username = student['username']
        role = student['role']
        user_directory = 'authors/' + username
        filename = 'authors/' + username + '/_index.md'

        if os.path.exists(user_directory):
            continue

        os.makedirs(user_directory)
        template = get_template(student)
        user_file = open(filename,'w')
        user_file.write(template)
        user_file.close()

else:
    pass

