import requests

from package2 import bibTextClasses


def author_data_by_id(api_key, id):
    try:
        response = requests.get("https://api.e-science.pl/api/azon/authors/entries/" + str(id) + "/",
                                headers={'X-Api-Key': api_key})
        response.raise_for_status()
        json_data = response.json()
        results = json_data['results']
        data = []
        for item in results:
            data.append(Data(**item))
        return data

    except requests.HTTPError as http_err:
        print('http error')

def get_data_type(data,api_key):

    data_in_type =[]
    for d in data:
        data_id = d.pk
        data_type = data.entry_type_id
        try:
            response = requests.get("https://api.e-science.pl/api/azon\
                /entry/"+str(data_id)+"/", headers={'X-Api-Key': api_key})
            response.raise_for_status()
            json_data = response.json()
            if data_type == 1:
                book = get_book(json_data)
                data_in_type.append(book)
        except requests.HTTPError as http_err:
            print("http error")


    return data_in_type


def get_book(json_data):
    data = {}
    item = json_data['item']
    data['authors'] = json_data['authors']
    data['title'] = json_data['title']
    data['year'] = item['publish_time']
    data['publisher'] = item['publisher']
    data['isbn'] = item['isbn']
    data['note'] = json_data['comments']
    data['address'] = item['publish_place']
    data['edition'] = item['numeration']
    data['series'] = item['series_name']
    book = bibTextClasses.Book(**data)
    return book

class Data:
    def __init__(self, pk, title, entry_type, entry_type_id, partner,
                 scientific_domain, authors, co_creators, attachments_number,
                 highlight, file_result):
        self.pk = pk
        self.title = title
        self.entry_type = entry_type
        self.entry_type_id = entry_type_id
        self.partner = partner
        self.scientific_domain = scientific_domain
        self.authors = []
        for i in range(len(authors)):
            author = [authors[i]['pk'], authors[i]['first_name'],
                      authors[i]['last_name']]
            self.authors.append(author)

        self.co_creators = []
        for i in range(len(co_creators)):
            co_creator = [co_creators[i]['pk'], co_creators[i]['full_name']]
            self.authors.append(co_creator)

        self.attachments_number = attachments_number
        self.highlight = highlight
        self.file_result = file_result
