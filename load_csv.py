# -*- coding: ISO-8859-1 -*-
# Kommentaren over gjør slik at vi kan skrive æ, ø og å i python

import csv # modul for lesing av csv data

# <open>(filnavn, parametere) returnerer et <file> objekt i samme mappe som python dokumentet
# <with> passer på at <file> objektet fjernes fra minne etter with blokken
# "rb", hvor "r" står for "read" og "b" står for "binary", må ikke være med. Les mer om <open> parametere her:
# https://www.programiz.com/python-programming/methods/built-in/open
with open('corona.csv', 'rb') as csvfile:
    # <reader> returnerer et objekt av verdier, lest fra filen i minnet
    # "delimeter" forteller hva som splitter dataen. I en CSV (Comma Separated Values), er det som oftest ','
    reader = csv.reader(csvfile, delimiter=',')

    # printer hver rekke fra csv filen
    for row in reader:
        # printer en rekke ved å "join"e en array/liste
        # hvert array element blir lagt sammen som en string, og mellom hver av
        # dem kommer ' -- ' stringen. Prøv å bytte det ut med noe annet
        print(' -- '.join(row))
