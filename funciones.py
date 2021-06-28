from owlready2 import *
import rdflib

#cargando ontologia
onto = get_ontology('fcc_instancias.owl').load()
g = rdflib.Graph()
g.parse("fcc_instancias.rdf")
go = get_ontology("fcc.owl").load()

def mostrar_clases():
    '''
    Devuelve todas las clases de la ontologia
    '''
    clases = []
    for c in onto.classes():
        clases.append(c.name)
    return clases

def muostrar_alumnos():
    datos_alumno = {}
    alumnos = onto.alumno.direct_instances()
    for alumno in alumnos:
        #alumno.Correo
        print(
            f'''
            Nombre: {alumno.Nombre}
            Id: {alumno}
            correo: {alumno.Correo}
            semestre: {alumno.Semestre_alumno}
            teléfono: {alumno.Edad}
            edad: {alumno.Edad}
            fecha de ingreso: {alumno.Fecha_ingreso}

         ''')

def muestra_tripletas():
    res =[]
    qres = g.query(
    """
    SELECT ?subject ?predicate ?object
    WHERE {
    ?subject ?predicate ?object
    }
    LIMIT 25

    """)

    for row in qres:
        row = str(row).replace('rdflib.term.URIRef', '').replace('(', '').replace(')', '')
        #print(row)
        res.append(row)
        print(res)
   # return res

def numero_clases():
    '''
    Este método utiliza la libreria owlready2 en lugar de rdflib
    '''
    resultado = list(default_world.sparql('''SELECT (COUNT(?x) AS ?nb)
                { ?x a owl:Class . } '''))
    print(resultado)

def consulta_prueba():
    resultado = list(default_world.sparql('''
                SELECT ?y
                { ?y rdfs:label "alumno" .
                 }'''))
    print(resultado)

def run():
    clases = mostrar_clases()
    #print(clases)
    alumnos = muostrar_alumnos()
    #tripletas =muestra_tripletas()
    #numero_clases()

    
        

if __name__ == '__main__':
    run()