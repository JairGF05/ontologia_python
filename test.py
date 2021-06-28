from owlready2 import *

query=list(default_world.sparql("""
prefix ns0: <http://www.semanticweb.org/user/ontologies/2021/4/untitled-ontology-42#>
SELECT ?Nombre_materia ?Creditos ?Area 
WHERE {
  ?x ns0:Nombre_materia  ?Nombre_materia.
  ?x ns0:Creditos_materia   ?Creditos.
  ?x ns0:area  ?Area.
  VALUES ?Area {'Tecnologia'}
}
"""))
for i in query:
    for x in i:
        print(x)