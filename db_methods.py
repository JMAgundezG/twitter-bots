import sqlite3 as lite
import sys,codecs

def parseoInsultos(txt):
    db = lite.connect('twitterbot.db')  # obtengo la base de datos

    with db:
        cursor = db.cursor()
        file = open('insultos.txt', 'r')
        text = file.read()
        for line in text.split():
            print(line)
            cursor.execute('INSERT INTO insultos (insulto) VALUES (?)', (line,))  # este debe ser el formato

    db.commit()  # guardo los cambios

def parseoPalabrasMal(txt):

    db = lite.connect('twitterbot.db')

    with db:
        cursor = db.cursor()
        file = open(txt,'r')
        text = file.read()
        for line in text.split():
            print(line)
            cursor.execute('INSERT INTO palabrasMal (palabra) VALUES (?)', (line,))

    db.commit()

def listaPalabrasMal() :
    db = lite.connect('twitterbot.db')

    with db:
        cursor = db.cursor()
        cursor.execute("SELECT palabra FROM palabrasMal")
        palabras = cursor.fetchall()#me devuelve en tupla lo último que halla consultado
        return ([p[0] for p in palabras])

def listaInsultos():
    db = lite.connect('twitterbot.db')

    with db:
        cursor = db.cursor()
        cursor.execute("SELECT insulto FROM insultos")
        palabras = cursor.fetchall()  # me devuelve en tupla lo último que halla consultado
        return ([p[0] for p in palabras])








