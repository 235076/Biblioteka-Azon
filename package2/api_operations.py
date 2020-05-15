import time
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


def get_data_type(data, api_key):
    data_in_type = []
    for d in data:
        time.sleep(1)
        data_id = d.pk
        data_type = d.entry_type_id
        print(str(data_type))
        try:
            response = requests.get("https://api.e-science.pl/api/azon/entry/" + str(data_id) + "/",
                                    headers={'X-Api-Key': api_key})
            response.raise_for_status()
            json_data = response.json()
            if data_type is '1':
                print("elo")
                book = get_book(json_data)
                data_in_type.append(book)
            if data_type is '4':
                print("elo?")
                phd = get_phd(json_data)
                data_in_type.append(phd)
            print("lecimy tutaj")
        except requests.HTTPError as http_err:
            print("http error")
    return data_in_type


def get_book(json_data):
    item = json_data['item']
    data = {'pk': json_data['pk'], 'authors': json_data['authors'], 'title': json_data['title'],
            'year': item['publish_time'], 'publisher': item['publisher'], 'isbn': item['isbn'],
            'note': json_data['comments'], 'address': item['publish_place'], 'edition': item['numeration'],
            'series': item['series_name']}
    book = bibTextClasses.Book(**data)
    return book


def get_phd(json_data):
    item = json_data['item']
    data = {'pk': json_data['pk'], 'authors': json_data['authors'], 'title': json_data['title'],
            'school': json_data['partner'], 'year': item['creation_time'], 'address': item['creation_place'],
            'note': json_data['comments']}
    phd = bibTextClasses.Phdthesis(**data)
    return phd


class Data:
    def __init__(self, pk, title, entry_type, entry_type_id, partner,
                 scientific_domain, authors, co_creators, attachments_number):
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
