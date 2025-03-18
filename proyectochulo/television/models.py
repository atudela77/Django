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
    nomserie = ""


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
            select p.idpersonaje, p.personaje, p.imagen, p.idserie, s.serie 
            from personajes p, series s
            where p.idserie = s.idserie
        '''
        cursor = self.conn.cursor()
        cursor.execute(sql)
        lista = []
        for idp, nom, img, ids, nms in cursor:
            personaje = Personaje()
            personaje.idpersonaje = idp
            personaje.nombre = nom
            personaje.imagen = img
            personaje.idserie = ids
            personaje.nomserie = nms
            lista.append(personaje)
        cursor.close()
        return lista

    def getPersonajesSerie(self, numserie):
        sql = '''
            select p.idpersonaje, p.personaje, p.imagen, p.idserie, s.serie 
            from personajes p, series s
            where p.idserie = s.idserie and p.idserie = :p1
        '''
        cursor = self.conn.cursor()
        cursor.execute(sql, (numserie,))
        lista = []
        for idp, nom, img, ids, nms in cursor:
            personaje = Personaje()
            personaje.idpersonaje = idp
            personaje.nombre = nom
            personaje.imagen = img
            personaje.idserie = ids
            personaje.nomserie = nms
            lista.append(personaje)
        cursor.close()
        return lista
    
    def updatePersonaje(self, idPersonaje, nombre, imagen, idSerie):
        sql = '''
            update personajes
               set
                    personaje = :p1,
                    imagen = :p2,
                    idserie = :p3
            where idpersonaje = :p4
        '''
        cursor = self.conn.cursor()
        cursor.execute(sql, (nombre, imagen, idSerie, idPersonaje))
        self.conn.commit()
        cursor.close()

    def findPersonaje(self, idpersonaje):
        sql = '''
            select idpersonaje, personaje, imagen, idserie 
            from personajes
            where idpersonaje = :p1
        '''
        cursor = self.conn.cursor()
        cursor.execute(sql, (idpersonaje,))
        idp, nom, img, ids = cursor.fetchone()
        person = Personaje()
        person.idpersonaje = idp
        person.nombre = nom
        person.imagen = img
        person.idserie = ids
        cursor.close()
        return person

    def findSerie(self, idserie):
        sql = '''
            select idserie, serie, imagen, anyo
            from series
            where idserie = :p1
            '''
        cursor = self.conn.cursor()
        cursor.execute(sql, (idserie,))
        ids, ser, img, yr = cursor.fetchone()
        serie = Serie()
        serie.idserie = ids
        serie.serie = ser
        serie.imagen = img
        serie.annio = yr
        cursor.close()
        return serie
