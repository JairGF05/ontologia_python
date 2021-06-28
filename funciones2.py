from clases import *

g = rdflib.Graph()
# ... add some triples to g somehow ...
g.parse("fcc_instancias.owl")


def run():
    # alumno2 = alumno()
    # alumno2.Semestre_alumno = [5]
    # alumno2.Correo = ['jairgf05@gmail.com']
    # alumno2.Telefono = ['555878745']
    # alumno2.Nombre = ['Jair GF']
    # alumno2.Edad = [58]
    # alumno2.Fecha_ingreso = ['2020-05-30T00:00:00']
    # onto.save(file = "fcc_instancias.owl", format = "rdfxml")
  
    
    # materia2 = materia_basica()
    # materia2.Horario_materia = ['Lunes-Viernes']
    # materia2.Periodo_materia = [3]
    # materia2.Creditos_materia = [5]
    # materia2.Horas_trabajo_materia = [4]
    # materia2.Horas_laboratorio_materia = [4]
    # materia2.Nombre_materia = ['Algebra']
    # materia2.Horas_teoria_materia = [5]
    # materia2.area = ['Basica']
    # materia2.Es_enseñada_por =[onto.P0000000]
    # materia2.Es_cursada_por =[onto.alumno1]
    # onto.save(file = "fcc_instancias.owl", format = "rdfxml")
    #print(onto.alumno1)

    #print(onto.profesor.direct_instances())
    #print('instancia agregada')
    #agrega_profesor()
    try:
        qres = g.query(
        '''
        prefix ns0: <http://www.semanticweb.org/user/ontologies/2021/4/untitled-ontology-42#>
        SELECT DISTINCT ?Profesor ?Enseña
        WHERE {
       
        ?x ns0:Nombre ?Profesor.
        ?x ns0:Enseña  ?Enseña.
        {
                SELECT ?tipo
                where{
                    ?x a ns0:Optativa.
                    ?x ns0:Tipo_optativa ?tipo.
                    VALUES ?tipo {"Disciplinaria"}
                }
            }
        }
        ''')
        for row in qres:
            print(row)
        print('tamaño',len(qres))
    except Exception as e:
        print(e)
    

if __name__ == '__main__':
    run()