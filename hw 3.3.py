# Your friend works for an antique book shop that sells books between 1800 and 1950
# They want to quickly categorise books by the century and decade that they were written.
# Write a program that takes a year (e.g. 1872)
# outputs the century and decade (e.g. "Eighteenth Century, Seventies")
import math

book_year = int(input('What year was the book written? '))


def century(book_year):
#could use same method as decade to isolate century e.g. math.floor((book_year%1000)/100)
    if 1799 < book_year < 1900:
        century = 'Nineteenth century'
    elif 1899 < book_year < 2000:
        century = 'Twentieth century'
    else:
        century = 'Century not recognised'

    return century


def decade(book_year):
    book_decade = math.floor((book_year % 100) / 10)
    if book_decade == 0:
        book_decade = 'Noughties'
    elif book_decade == 1:
        book_decade = 'Tens'
    elif book_decade == 2:
        book_decade = 'Twenties'
    elif book_decade == 3:
        book_decade = 'Thirties'
    elif book_decade == 4:
        book_decade = 'Fourties'
    elif book_decade == 5:
        book_decade = 'Fifties'
    elif book_decade == 6:
        book_decade = 'Sixties'
    elif book_decade == 7:
        book_decade = 'Seventies'
    elif book_decade == 8:
        book_decade = 'Eighties'
    elif book_decade == 9:
        book_decade = 'Nineties'
    else:
        book_decade = 'Decade not recognised'

    return book_decade


print('{}, {}'.format(century(book_year), decade(book_year)))

#code would be improved by using dictonary e.g.:

century_name = {
    8 : 'Nineteenth',
    9 : 'Twentieth'
}

decade_name = {
    0 : 'Noughties',
    1 : 'Tens',
    2 : 'Twenties',
    3 : 'Thirties',
    4 : 'Fourties',
    5 : 'Fifties',
    6 : 'Sixties',
    7 : 'Seventies',
    8 : 'Eighties',
    9 : 'Nineties'
}

century_number = math.floor((book_year % 1000)/100)
decade_number = math.floor((book_year % 100) / 10)

if decade_number in decade_name and century_number in century_name:
    print('{} century, {}'.format(century_name[century_number],decade_name[decade_number]))
else:
    print('Year not recognised')