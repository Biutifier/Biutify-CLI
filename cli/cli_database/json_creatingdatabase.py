import json

json_data = '[\
    {"filename": "hello_world.txt",\
     "hash": "564trsturkos"\
    },\
    {"filename": "hi.txt",\
     "hash": "1332"\
    }\
]'

class FileEntry:
    def __init__(self, filename: str, hashnum: str, idnum: int = None):
        self.idnum = idnum
        self.filename = filename
        self.hashnum = hashnum 
    def __str__(self):
        return " FileEntry Instance \n--------------------\n  ID: %s\n  Filename: %s\n  Hash: %s" % (self.idnum, self.filename, str(self.hashnum) if self.hashnum is not None else "N/A")

#converting json file into a list
def convert_to_list():
    with open('data.json') as data_file:
        data = json.load(data_file)
        return data

def create_entry(file):
    data = convert_to_list()    
    json_data = {
        "filename": file.filename,
        "hash": file.hashnum,
        "id": file.idnum
    }
    data.append(json_data)
    save_to_file()
#add to list, save to file

#comparing two hash strings
def search_hash(hash: str):
    data = convert_to_list() 
    for element in data:
        if hash == element['hash']:
            return FileEntry(element['filename'], element['hashnum'], element['idnum'] )
            #compare to other hash something

#calling file name
#same as search_hash function
def search_name(name: str):
    data = convert_to_list()
    for element in data:
        if name == element['filename']:
            return FileEntry(element['filename'], element['hashnum'], element['idnum'] )

#changes filename
def update_entry(file: FileEntry):
    data = convert_to_list()
    for index in range(len(data)):
        if data[index]['id'] == file.idnum:
            data[index]['filename'] = file.filename
            data[index]['hash'] = file.hashnum

#removes id from list
def delete_from_id(id: int):
    data = convert_to_list() 
    for element in data:
        if 'id' in element:
            del element['id']

#removes hash from list
def delete_from_hash(hash: str):
    data = convert_to_list() 
    for element in data:
        if 'hash' in element:
            del element['hash']

#removes name from list
def delete_from_name(name: str):
    data = convert_to_list() 
    for element in data:
        if 'name' in element:
            del element['name']

#converting list back into a json file
#list name data_file
def save_to_file(data):
    json_data = json.dumps(data)
    with open('data.json') as data_file:
        data_file.pop
        data_file.write
