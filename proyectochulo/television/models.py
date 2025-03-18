from django.db import models
import oracledb


# Create your models here.
class Serie:
    idserie = 0
    titulo = ""
    imagen = ""
    annio = 0


class Personaje:
    idpersonaje = 0
    nombre = ""
    imagen = ""
    idserie = 0


class serviceSeries:
    def __init__(self):
        self.conn = oracledb.connect(
            user="system",
            password="oracle",
            dsn="localhost:1521/xe"
        )

    def getSeries(self):
        sql = '''
            select idserie, serie, imagen, anyo
            from series
            '''
        cursor = self.conn.cursor()
        cursor.execute(sql)
        lista = []
        for id, tit, img, anio in cursor:
            serie = Serie()
            serie.idserie = id
            serie.titulo = tit
            serie.imagen = img
            serie.annio = anio
            lista.append(serie)
        cursor.close()
        return lista

    def getPersonajes(self):
        sql = '''
            select idpersonaje, personaje, imagen, idserie 
            from personajes
        '''
        cursor = self.conn.cursor()
        cursor.execute(sql)
        lista = []
        for idp, nom, img, ids in cursor:
            personaje = Personaje()
            personaje.idpersonaje = idp
            personaje.nombre = nom
            personaje.imagen = img
            personaje.idserie = ids
            lista.append(personaje)
        cursor.close()
        return lista
