
class Book:
    def __init__(self, authors, title, publisher, year, volume='',
                 series='', address='', edition='', month='', note='', isbn=''):
        self.authors = []
        for i in range(len(authors)):
            author = authors[i]['author']
            self.authors.append(author)
        self.authors_string = ''
        for i in range(len(self.authors)):
            self.authors_string += self.authors[i]
            if(i != len(self.authors) - 1):
                self.authors_string += ', '
        self.title = title
        self.publisher = publisher
        self.year = year
        self.volume = volume
        self.series = series
        self.address = address
        self.edition = edition
        self.month = month
        self.note = note
        self.isbn = isbn


    def to_bibtext(self):
        #niezbedne
        bib = f'@book{{{self.pk},\n  author =\t"{self.authors_string}", \
            \n  title =\t"{self.title}",\n  publisher =\t"{self.publisher}", \
            \n  year =\t{self.year},'
        #opcjonalne
        if(self.volume != '' and self.volume is not None):
            bib += f'\n  volume =\t"{self.volume}",'
        if(self.series != '' and self.series is not None):
            bib += f'\n  series =\t"{self.series}",'
        if(self.address != '' and self.address is not None):
            bib += f'\n  address =\t"{self.address}",'
        if(self.edition != '' and self.edition is not None):
            bib += f'\n  edition =\t"{self.edition}",'
        if(self.month != '' and self.month is not None):
            bib += f'\n  month =\t{self.month},'
        if(self.note != '' and self.note is not None):
            bib += f'\n  note =\t"{self.note}",'
        if(self.isbn != '' and self.isbn is not None):
            bib += f'\n  isbn =\t"{self.isbn}",'
        bib = bib+'\n}\n'
        return bib