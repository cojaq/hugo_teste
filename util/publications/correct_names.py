import json
import os
import yaml
import fileinput

def no_accents(s):
    import unicodedata
    return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')) 

def author_files(root):
    author_files=[]
    for r, sub, f in os.walk(root):
        for i in f:
            if i == '_index.md':
                author_files.append(r+'/'+i)

    return author_files

def author_data(root):
    authors_files = author_files(root)

    authors_dict=[]
    for f in authors_files:
        with open(f, 'r') as stream:
            docs = yaml.safe_load_all(stream)
            data = next(docs)
            authors_dict.append({'name': data['name'], 'username': data['authors'][0]})

    return authors_dict

def publication_files(root):
    publication_files=[]
    for r, sub, f in os.walk(root):
        for i in f:
            if i == 'index.md':
                publication_files.append(r+'/'+i)

    return publication_files

def publication_data(root):
    publications_files = publication_files(root)

    authors_publi=[]
    for f in publications_files:
        with open(f, 'r') as stream:
            docs = yaml.safe_load_all(stream)
            data = next(docs)

            for author in data['authors']:
                if author not in [i['publication_name'] for i in authors_publi]:
                    authors_publi.append({'publication_name': author,
                                          'site_username': '',
                                          'link':
                                          ['http://localhost:1313/publication/'+
                                           f.split('/')[-2]]})
                else:
                    for a in authors_publi:
                        if a['publication_name'] == author:
                            a['link'].append('http://localhost:1313/publication/'+ f.split('/')[-2])

    return authors_publi

def generate_json():
    site_authors = author_data('/home/tiago/hugo/imageu/content/en/authors')
    publi_authors = publication_data('/home/tiago/hugo/imageu/content/en/publication')

    list_of_usernames = [i['username'].lower() for i in site_authors]
    publi_authors = [i for i in publi_authors if not
                     no_accents(i['publication_name']).lower() in
                     list_of_usernames ]

    publi_authors = sorted(publi_authors, key=lambda e: (e['publication_name']))

    return publi_authors

def load_json(publication_json):
    if not os.path.exists(publication_json):
        list_publications = generate_json()
        with open(publication_json, 'w', encoding='utf8') as json_file:
            json.dump(publi_authors, json_file, indent=4, ensure_ascii=False)

    with open(publication_json, encoding='utf-8-sig') as json_file:
        json_data = json.loads(json_file.read())

    return json_data

def get_authors_from(md_file):
    with open(md_file, 'r') as stream:
        docs = yaml.safe_load_all(stream)
        data = next(docs)
    return data

def process_all():
    publi_authors = publication_files('/home/tiago/hugo/imageu/content/en/publication')[0:2]

    json_data = load_json('publication_names.json')

    for f in publi_authors:
        print(f)
        data = get_authors_from(f)
        for author in data['authors']:
            for a in json_data:
                if a['publication_name'] == author:
                    if a['site_username']:
                        with fileinput.FileInput(f, inplace=True, backup='.bak') as file:
                            for line in file:
                                print(line.replace('\"'+author+'\"',
                                                   '\"'+a['site_username']+'\"'), end='')


def write_authors(json_data):
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

if __name__ == '__main__':
    process_all()


    #write_authors(json_data)


else:
    pass

