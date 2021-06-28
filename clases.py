from owlready2 import *
import rdflib

#cargando la ontologia
onto = get_ontology('fcc_instancias.owl').load()

#clase persona y sus respectivas subclases
class persona(Thing):
    namespace = onto

class alumno(Thing):
    namespace = onto

#propiedades de alumno
class Correo(DataProperty):
    ontology = onto
    range    = [str]

class Semestre_alumno(DataProperty):
    ontology = onto
    range    = [int]

class Telefono(DataProperty):
    ontology = onto
    range    = [str]

class Nombre(DataProperty):
    ontology = onto
    range    = [str]


class Edad(DataProperty):
    ontology = onto
    range    = [int]

class Fecha_ingreso(DataProperty):
    ontology = onto
    range    = [datetime.datetime]



#################################
class profesor(Thing):
    namespace = onto
#propiedades de la clase profesor
class Cargo_administrativo_profesor(DataProperty):
    ontology = onto
    range    = [str]

class Telefono(DataProperty):
    ontology = onto
    range    = [str]

class Edad(DataProperty):
    ontology = onto
    range    = [int]

class Primer_contrato(DataProperty):
    ontology = onto
    range    = [datetime.datetime]

class Nombre(DataProperty):
    ontology = onto
    range    = [str]

class Correo(DataProperty):
    ontology = onto
    range    = [str]


#################################
#clase materia y sus respectivas subclases
class materia(Thing):
    namespace = onto

class materia_basica(Thing):
    namespace = onto
#propiedades materia_basica
class Horario_materia(DataProperty):
    ontology = onto
    range    = [str]

class Horas_teoria_materia(DataProperty):
    ontology = onto
    range    = [int]

class Periodo_materia(DataProperty):
    ontology = onto
    range    = [int]

class Creditos_materia(DataProperty):
    ontology = onto
    range    = [int]

class Horas_trabajo_materia(DataProperty):
    ontology = onto
    range    = [int]


class Horas_laboratorio_materia(DataProperty):
    ontology = onto
    range    = [int]


class Nombre_materia(DataProperty):
    ontology = onto
    range    = [str]

class area(DataProperty):
    ontology = onto
    range    = [str]



class Es_enseñada_por(ObjectProperty):
    domain = [onto.materia]
    #ontology = onto
    range    = [onto.profesor]

class Es_cursada_por(ObjectProperty):
    domain = [onto.materia]
    #ontology = onto
    range    = [onto.alumno]


class Requiere(ObjectProperty):
    domain = [onto.materia]
    #ontology = onto
    range    =[ onto.materia]



##############################################

class materia_formativa(Thing):
    namespace = onto

class Optativa(Thing):
    namespace = onto
#propiedades de materia formativa
class Horas_laboratorio(DataProperty):
    ontology = onto
    range    = [int]

class Horas_teoria_materia(DataProperty):
    ontology = onto
    range    = [int]

class Periodo_materia(DataProperty):
    ontology = onto
    range    = [int]

class Creditos_materia(DataProperty):
    ontology = onto
    range    = [int]

class Horas_trabajo_materia(DataProperty):
    ontology = onto
    range    = [int]

class Horario_materia(DataProperty):
    ontology = onto
    range    = [str]

class Nombre_materia(DataProperty):
    ontology = onto
    range    = [str]






def run():
    pass

if __name__ == '__main__':
    run()