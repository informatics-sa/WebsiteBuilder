from lib import *
from lib.utils import *



def update_participations():
    members = load_json('people')
    with open('./root/data/participations.old.json', encoding='utf-8') as f:
        parts_str = f.read()
    for mem in members:
        oid = mem['id']
        iid = mem['iid']
        parts_str = parts_str.replace(f'"{oid}"', f'"{iid}"')
    write_text('./root/data/participations.json', parts_str)

def update_exams():
    members = load_json('people')
    with open('./root/data/exams.old.json', encoding='utf-8') as f:
        parts_str = f.read()
    for v in members:
        oid = v['id']
        iid = v['iid']
        parts_str = parts_str.replace(f'"{oid}"', f'"{iid}"')
    write_text('./root/data/exams.json', parts_str)


def check_distinct_ids():
    participations = load_json('participations.old')
    unique_names = set()
    for par in participations:
        for user in par['participants']:
            unique_names.add(user.lower().replace(' ', '_'))
    names = sorted(list(unique_names))
    for i in names:
        print(i)

def generate_members():
    previous_members = load_json('people')
    preunique_set = set()
    for mem in previous_members:
        preunique_set.add(mem['id'])
        if mem['enname'] == mem['id']:
            mem['enname'] = mem['id'].replace('_', ' ').title()
    
    participations = load_json('participations.old')
    unique_names = set()
    for par in participations:
        for user in par['participants']:
            user = str(user).lower()
            if user not in preunique_set:
                unique_names.add(user.lower())
    
    names = sorted(list(unique_names))
    data = previous_members
    idx = len(preunique_set)+1
    for n in names:
        data.append({
            'iid': idx,
            'id': n,
            'arname': n,
            'enname': n.replace('_', ' ').title()
        })
        idx += 1
    write_text('./root/data/people.json', json.dumps(data, ensure_ascii=False))



def generate_members_names():
    members = load_json('people')
    for p in members:
        p['enname'] = p['id'].replace('_', ' ').title()
        if p['arname'] == '':
            p['arname'] = p['id']
    write_text('./root/data/people.json', json.dumps(members))

def sort_by_date(date_format="%Y/%m/%d"):
    # Read JSON file
    from datetime import datetime
    with open('./root/data/participations.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Sort objects by start date
    sorted_data = sorted(data, key=lambda x: datetime.strptime(x['start'], date_format), reverse=True)
    
    # Write sorted data to output file
    with open('./root/data/participations.json', 'w', encoding='utf-8') as f:
        json.dump(sorted_data, f, indent=4)

#generate_members_names()
# check_distinct_ids()
# exit(1)
#update_exams()
generate_members()
print("Generated members")
update_participations()
print("Updated participations")
sort_by_date()
print("Sorted by date")