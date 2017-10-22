

import csv

from .models import Book
"""
f = open('data/books.csv')

reader = csv.reader(f)

data = [*reader]
keys = data[0]

d = [dict(zip(keys, point)) for point in data[1:]]


def sub(point):
    return {
        'original_title'            : point['original_title'], 
        'isbn'                      : point['isbn'], 
        'authors'                   : point['authors'], 
        'original_publication_year' : point['original_publication_year'],
        'image_url'                 : point['image_url'],
    }

a = [*map(sub, d)]

print(a[0].keys())


def make(point):
    Book.objects.create(*{
        'title'     : point['original_title'], 
        'isbn'      : point['isbn'], 
        'author'    : point['authors'], 
        'published' : point['original_publication_year'],
        'imageurl'  : point['image_url'],
    })

"""