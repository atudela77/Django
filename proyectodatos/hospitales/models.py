from django.db import models
import oracledb


# Create your models here.
class Departamento:
    numero = 0
    nombre = ""
    localidad = ""


class ServiceDepartamentos:
    def __init__(self):
        self.conn = oracledb.connect(
            user="system",
            password="oracle",
            dsn="localhost:1521/xe"
        )

    def getDepartamentos(self):
        sql = '''
            select dept_no, dnombre, loc
            from dept
            order by dept_no
        '''
        cursor = self.conn.cursor()
        cursor.execute(sql)
        lista = []
        for dep, nom, loc in cursor:
            dept = Departamento()
            dept.numero = dep
            dept.nombre = nom.title()
            dept.localidad = loc.title()
            lista.append(dept)
        cursor.close()
        return lista

    def insertDepartamento(self, numero, nombre, localidad):
        sql = '''
            insert into dept 
                (dept_no, dnombre, loc)
            values
                (:p1, :p2, :p3)
        '''
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql, (numero, nombre, localidad))
            registros = cursor.rowcount
            self.conn.commit()
            cursor.close()
        except oracledb.IntegrityError:
            registros = 0
        return registros

    def eliminarDepartamento(self, numero):
        sql = '''
            delete from dept
            where dept_no = :p1
        '''
        cursor = self.conn.cursor()
        cursor.execute(sql, (numero,))
        eliminado = cursor.rowcount
        self.conn.commit()
        cursor.close()
        return eliminado

    def modificarDepartamento(self, numero, nombre, localizacion):
        sql = '''
            update dept
               set dnombre = :p1,
                   loc = :p2
            where dept_no = :p3
        '''
        cursor = self.conn.cursor()
        cursor.execute(sql, (nombre, localizacion, numero))
        actualizado = cursor.rowcount
        self.conn.commit()
        cursor.close()
        return actualizado

    def detallesDepartamento(self, numero):
        sql = '''
            select dept_no, dnombre, loc
            from dept
            where dept_no = :p1
        '''
        cursor = self.conn.cursor()
        cursor.execute(sql, (numero,))
        num, nom, loc = cursor.fetchone()
        dept = Departamento()
        dept.numero = num
        dept.nombre = nom
        dept.localidad = loc
        cursor.close()
        return dept


class Hospital:
    codigo = 0
    nombre = ""
    direccion = ""
    telefono = ""
    numero_camas = ""


class ServiceHospital:
    def __init__(self):
        self.conn = oracledb.connect(
            user="system",
            password="oracle",
            dsn="localhost:1521/xe"
        )

    def getHospitales(self):
        sql = '''
            select hospital_cod, nombre, direccion, telefono, num_cama
            from hospital
            order by hospital_cod
        '''
        cursor = self.conn.cursor()
        cursor.execute(sql)
        lista = []
        for cod, nom, dir, tel, cam in cursor:
            hosp = Hospital()
            hosp.codigo = cod
            hosp.nombre = nom.title()
            hosp.direccion = dir.title()
            hosp.telefono = tel
            hosp.numero_camas = cam
            lista.append(hosp)
        cursor.close()
        return lista


class Empleado:
    apellido = ""
    oficio = ""
    salario = ""
    depto = 0


class serviceEmpleados():
    def __init__(self):
        self.conn = oracledb.connect(
            user="system",
            password="oracle",
            dsn="localhost:1521/xe"
        )

    def empleadosDepartamento(self, numdept):
        sql = '''
            select apellido, oficio, salario, dept_no
            from emp
            where dept_no = :p1
        '''
        cursor = self.conn.cursor()
        cursor.execute(sql, (numdept,))
        lista = []
        for ape, ofi, sal, dep in cursor:
            empleado = Empleado()
            empleado.apellido = ape.title()
            empleado.oficio = ofi.title()
            empleado.salario = f"{sal:,.2f}€"
            empleado.depto = dep
            lista.append(empleado)
        cursor.close()
        return lista
