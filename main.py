import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from clases import *
import rdflib
import re
from PyQt5.QtGui import QIcon, QPixmap

g = rdflib.Graph()
#g.parse("fcc_instancias.ttl", format='ttl')
g.parse("fcc_instancias.owl")
#Declaración de interfaces secundarias
class WindowProfesor(QMainWindow):
    def __init__(self):
        super().__init__()
        #aqui va nombre de interfaz creada en designer
        uic.loadUi('interfaces\\profesor.ui', self)
        #botonos de la ventana profesor
        self.boton_agregar_profesor.clicked.connect(self.agrega_profesor)
        self.boton_eliminar_profesor.clicked.connect(self.elimina_profesor)

    def agrega_profesor(self):
        nombre =self.edit_nombre.text()
        telefono = self.edit_telefono.text()
        cargo = self.edit_cargo.text()
        edad = int(self.edit_edad.text())
        primer_contrato = self.edit_contrato.text()
        correo = self.edit_correo.text()
        enseña = self.edit_ensena.text()

        #almacenando datos
        profesor1 = profesor()
        profesor1.Telefono = [telefono]
        profesor1.Cargo_administrativo_profesor = [cargo]
        profesor1.Edad = [edad]
        profesor1.Primer_contrato = [primer_contrato]
        profesor1.Nombre =[nombre]
        profesor1.correo = [correo]

        lista_materias = onto.search(type=onto.materia)
        for indiv in lista_materias:
            if enseña == indiv.Nombre_materia[0]:
                profesor1.Enseña =[indiv]

        onto.save(file = "fcc_instancias.owl", format = "rdfxml")
        self.label_mensaje_profesor.setText("Datos registrados")
    
    def elimina_profesor(self):
        nombre =self.edit_nombre.text()
        lista_profesores = onto.search(type=onto.profesor)
        for indiv in lista_profesores:
            #print(str(indiv.Nombre[0]))
            #print(nombre)
            if str(indiv.Nombre[0]) == nombre:
                destroy_entity(indiv)
                self.label_mensaje_profesor.setText("Registro eliminado")
                onto.save(file = "fcc_instancias.owl", format = "rdfxml")
            
                
    


class WindowAlumno(QMainWindow):
    def __init__(self):
        super().__init__()
        #aqui va nombre de interfaz creada en designer
        uic.loadUi('interfaces\\alumno.ui', self)
        #Botones de la ventana alumno
        self.boton_agregar_alumno.clicked.connect(self.agrega_alumno)
        self.boton_eliminar_alumno.clicked.connect(self.elimina_alumno)

    def agrega_alumno(self):
        nombre =self.edit_nombre_alumnos.text()
        correo = self.edit_correo_alumnos.text()
        semestre = self.edit_semestre_alumnos.text()
        telefono = self.edit_telefono_alumnos.text()
        edad = int(self.edit_edad_alumnos.text())
        fecha_ingreso = self.edit_fecha_alumnos.text()
        cursa = self.edit_cursa_alumnos.text()

        
        #agregar cursa
        #almacenando datos
        alumno1 = alumno()
        alumno1.Nombre = [nombre]
        alumno1.correo =[correo]
        alumno1.semestre = [semestre]
        alumno1.Telefono = [telefono]
        alumno1.Edad = [edad]
        alumno1.Fecha_ingreso = [fecha_ingreso]


        lista_materias = onto.search(type=onto.materia)
        for indiv in lista_materias:
            if cursa == indiv.Nombre_materia[0]:
                alumno1.Cursa =[indiv]

        # res =[]
        # lista_materias = onto.search(type=onto.materia)
        # cursa = str(cursa).split(',')
        # for indiv in lista_materias:
        #     for alumno in cursa:
        #         if alumno == indiv.Nombre[0]:
        #             #print(alumno)
        #             res.append(indiv)
       
        # alumno1.Es_cursada_por =res



                
        onto.save(file = "fcc_instancias.owl", format = "rdfxml")
        self.label_mensaje_alumno.setText("Datos registrados")

    def elimina_alumno(self):
        nombre =self.edit_nombre_alumnos.text()
        lista_alumnos = onto.search(type=onto.alumno)
        for indiv in lista_alumnos:
            if str(indiv.Nombre[0]) == nombre:
                destroy_entity(indiv)
                onto.save(file = "fcc_instancias.owl", format = "rdfxml")
                self.label_mensaje_alumno.setText("Registro eliminado")
            

    
class WindowBasica(QMainWindow):
    def __init__(self):
        super().__init__()
        #aqui va nombre de interfaz creada en designer
        uic.loadUi('interfaces\\materia_basica.ui', self)
        #botones ventana materia básica
        self.boton_agregar_basica.clicked.connect(self.agrega_materia_basica)
        self.boton_eliminar_basica.clicked.connect(self.elimina_materia_basica)

    def agrega_materia_basica(self):
        nombre =self.edit_nombre_basica.text()
        periodo = self.edit_periodo_basica.text()
        creditos = self.edit_creditos_basica.text()
        horas_trabajo = self.edit_htrabajo_basica.text()
        horas_laboratorio = self.edit_hlaboratorio_basica.text()
        horario = self.edit_horario_basica.text()
        area = self.edit_area_basica.text()
        horas_teoria = self.edit_hteoria_basica.text()
        cursada_por = self.edit_cursada_basica.text()
        enseñada_por = self.edit_ensenada_basica.text()
        requiere = self.edit_requiere_basica.text()

        materia_basica1 = materia_basica()
        materia_basica1.Horario_materia = [horario]
        materia_basica1.Periodo_materia = [periodo]
        materia_basica1.Creditos_materia = [creditos]
        materia_basica1.Horas_trabajo_materia = [horas_trabajo]
        materia_basica1.Horas_laboratorio_materia = [horas_laboratorio]
        materia_basica1.Nombre_materia = [nombre]
        materia_basica1.area = [area]
        materia_basica1.Horas_teoria_materia = [horas_teoria]


        #falta agregar las 3 ultimas
        lista_alumnos = onto.search(type=onto.alumno)
        lista_profesores = onto.search(type=onto.profesor)
        lista_materias = onto.search(type=onto.materia)

        for indiv in lista_alumnos:
            if cursada_por == indiv.Nombre[0]:
                materia_basica1.Es_cursada_por =[indiv]


        # res =[]
        # cursada_por = str(cursada_por).split(',')
        # for indiv in lista_alumnos:
        #     for alumno in cursada_por:
        #         if alumno == indiv.Nombre[0]:
        #             #print(alumno)
        #             res.append(indiv)
       
        # materia_basica1.Es_cursada_por =res


        # for indiv in lista_alumnos:
        #     for alumno in cursada_por:
        #         if indiv.Nombre[0] == alumno :
        #             materia_basica1.Es_cursada_por =[indiv]
        #         else:
        #             continue

        for indiv in lista_profesores:
            if enseñada_por == indiv.Nombre[0]:
                materia_basica1.Es_enseñada_por =[indiv]
        
        for indiv in lista_materias:
            if requiere == indiv.Nombre_materia[0]:
                materia_basica1.Requiere =[indiv]
        onto.save(file = "fcc_instancias.owl", format = "rdfxml")
        self.label_mensaje_basica.setText("Datos registrados")
    
    def elimina_materia_basica(self):
        nombre =self.edit_nombre_basica.text()
        lista_materias_basicas = onto.search(type=onto.materia_basica)
        for indiv in lista_materias_basicas:
            if str(indiv.Nombre_materia[0]) == nombre:
                destroy_entity(indiv)
                onto.save(file = "fcc_instancias.owl", format = "rdfxml")
                self.label_mensaje_basica.setText("Registro eliminado")
            

class WindowFormativa(QMainWindow):
    def __init__(self):
        super().__init__()
        #aqui va nombre de interfaz creada en designer
        uic.loadUi('interfaces\\materia_formativa.ui', self)
        #botones ventana materia básica
        self.boton_agregar_formativa.clicked.connect(self.agrega_materia_formativa)
        self.boton_eliminar_formativa.clicked.connect(self.elimina_materia_formativa)

    def agrega_materia_formativa(self):
        nombre =self.edit_nombre_formativa.text()
        periodo = self.edit_periodo_formativa.text()
        creditos = self.edit_creditos_formativa.text()
        horas_trabajo = self.edit_htrabajo_formativa.text()
        horas_laboratorio = self.edit_hlaboratorio_formativa.text()
        horario = self.edit_horario_formativa.text()
        area = self.edit_area_formativa.text()
        horas_teoria = self.edit_hteoria_formativa.text()
        cursada_por = self.edit_cursada_formativa.text()
        enseñada_por = self.edit_ensenada_formativa.text()
        requiere = self.edit_requiere_formativa.text()
        

        if self.checkBox_optativa.isChecked():
            materia_formativa1 = Optativa()
            materia_formativa1.Horario_materia = [horario]
            materia_formativa1.Periodo_materia = [periodo]
            materia_formativa1.Creditos_materia = [creditos]
            materia_formativa1.Horas_trabajo_materia = [horas_trabajo]
            materia_formativa1.Horas_laboratorio_materia = [horas_laboratorio]
            materia_formativa1.Nombre_materia = [nombre]
            materia_formativa1.area = [area]
            materia_formativa1.Horas_teoria_materia = [horas_teoria]
            #falta agregar las 3 ultimas
            lista_alumnos = onto.search(type=onto.alumno)
            lista_profesores = onto.search(type=onto.profesor)
            lista_materias = onto.search(type=onto.materia)
            res = []
            for indiv in lista_alumnos:
                if cursada_por == indiv.Nombre[0]:
                    materia_formativa1.Es_cursada_por =[indiv]

            for indiv in lista_profesores:
                if enseñada_por == indiv.Nombre[0]:
                    materia_formativa1.Es_enseñada_por =[indiv]
            
            for indiv in lista_materias:
                if requiere == indiv.Nombre_materia[0]:
                    materia_formativa1.Requiere =[indiv]
            
            onto.save(file = "fcc_instancias.owl", format = "rdfxml")
            self.label_mensaje_formativa.setText("Datos registrados")


           
        else:
            materia_formativa1 = materia_formativa()
            materia_formativa1.Horario_materia = [horario]
            materia_formativa1.Periodo_materia = [periodo]
            materia_formativa1.Creditos_materia = [creditos]
            materia_formativa1.Horas_trabajo_materia = [horas_trabajo]
            materia_formativa1.Horas_laboratorio_materia = [horas_laboratorio]
            materia_formativa1.Nombre_materia = [nombre]
            materia_formativa1.area = [area]
            materia_formativa1.Horas_teoria_materia = [horas_teoria]
            #falta agregar las 3 ultimas
            lista_alumnos = onto.search(type=onto.alumno)
            lista_profesores = onto.search(type=onto.profesor)
            lista_materias = onto.search(type=onto.materia)
            res = []
            for indiv in lista_alumnos:
                if cursada_por == indiv.Nombre[0]:
                    materia_formativa1.Es_cursada_por =[indiv]

            for indiv in lista_profesores:
                if enseñada_por == indiv.Nombre[0]:
                    materia_formativa1.Es_enseñada_por =[indiv]
            
            for indiv in lista_materias:
                if requiere == indiv.Nombre_materia[0]:
                    materia_formativa1.Requiere =[indiv]

            onto.save(file = "fcc_instancias.owl", format = "rdfxml")
            self.label_mensaje_formativa.setText("Datos registrados")
    
    def elimina_materia_formativa(self):
        if self.checkBox_optativa.isChecked():
            nombre =self.edit_nombre_formativa.text()
            lista_materias_optativas = onto.search(type=onto.Optativa)
            for indiv in lista_materias_optativas:
                if str(indiv.Nombre_materia[0]) == nombre:
                    destroy_entity(indiv)
                    onto.save(file = "fcc_instancias.owl", format = "rdfxml")
                    self.label_mensaje_formativa.setText("Registro eliminado")
        else:
            nombre =self.edit_nombre_formativa.text()
            lista_materias_formativas = onto.search(type=onto.materia_formativa)
            for indiv in lista_materias_formativas:
                if str(indiv.Nombre_materia[0]) == nombre:
                    destroy_entity(indiv)
                    onto.save(file = "fcc_instancias.owl", format = "rdfxml")
                    self.label_mensaje_formativa.setText("Registro eliminado")
            



#terminan interfaces secundarias
class WindowGrafo(QMainWindow):
    def __init__(self):
        super().__init__()
        #aqui va nombre de interfaz creada en designer
        uic.loadUi('interfaces\\ventana_grafo.ui', self)
        #opcion pixmap en las propiedades de label en qt designer


#interfaz principal
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        #aqui va nombre de interfaz creada en designer
        uic.loadUi('interfaces\\interfaz.ui', self)
        #botones ventana principal
        self.boton_acciones_profesor.clicked.connect(self.ventana_profesor) #sin los parentesis
        self.boton_acciones_alumno.clicked.connect(self.ventana_alumno) #sin los parentesis
        self.boton_acciones_materia_basica.clicked.connect(self.ventana_materia_basica)
        self.boton_acciones_materia_formativa.clicked.connect(self.ventana_materia_formativa)
        self.boton_grafo.clicked.connect(self.ventana_grafo)

        self.boton_iniciar.clicked.connect(self.leer_consulta)
        self.boton_limpiar.clicked.connect(self.limpiar)

    

    def leer_consulta(self):
        self.label_principal.clear()
        self.resultado.clear()
        # try:
        #     query =self.consulta.toPlainText()
        #     query=list(default_world.sparql(query))
        #     for i in query:
        #         #self.resultado.append(str(i).replace('[', '').replace(']', '').replace('fcc_instancias.', ''))
        #         self.resultado.append(str(i))
        # except:
        #     self.resultado.clear()
        #     self.label_principal.setText("Consulta no valida")

        try:
            
            query =self.consulta.toPlainText()
            qres= g.query(query)
            if len(qres) == 0:
                #self.label_principal.setText("No hay resultados")
                con =self.consulta.toPlainText()
                con=list(default_world.sparql(con))
                if len(con) ==  0:
                    self.label_principal.setText("No hay resultados")
                else:
                    for i in con:
                        self.resultado.append(str(i).replace('[', '').replace(']', '').replace('fcc_instancias.', ''))
                        #self.resultado.append(str(i))
                    self.label_principal.setText("Consulta Exitosa!")
            else:
                for row in qres:
                    row = str(row).replace('(', '').replace('rdflib.term.Literal', '').replace("'", '').replace(')', '')
                    row = row.replace('datatype=rdflib.term.URIRefhttp://www.w3.org/2001/XMLSchema#string,', '')
                    row = row.replace('datatype=rdflib.term.URIRefhttp://www.w3.org/2001/XMLSchema#positiveInteger,', '')
                    row = row.replace('rdflib.term.URIRefhttp://www.semanticweb.org/user/ontologies/2021/4/untitled-ontology-42#', '')
                    row = row.replace(', datatype=rdflib.term.URIRefhttp://www.w3.org/2001/XMLSchema#positiveInteger', '')
                    #row.replace(', datatype=rdflib.term.URIRefhttp://www.w3.org/2001/XMLSchema#string.term.URIRefhttp://www.semanticweb.org/user/ontologies/2021/4/untitled-ontology-42','')
                    #row = re.sub("datatype=rdflib.term.URIRefhttp://www.w3.org/2001/XMLSchema#string, rdflib.term.URIRefhttp://www.semanticweb.org/user/ontologies/2021/4/untitled-ontology-42", "", row)
                    #row = re.sub(', datatype.*', '', row)
                    self.resultado.append(row)
                self.label_principal.setText("Consulta Exitosa!")
                

        except:
            #self.resultado.clear()
            ########################
            
            ########################
            self.label_principal.setText("Consulta no valida")

    def limpiar(self):
        self.resultado.clear()
        self.consulta.clear()
        self.label_principal.clear()

    def ventana_profesor(self):
        '''
        Función para abrir la ventana WindowProfesor
        por medio del botón boton_acciones_profesor
        '''
        self.w = WindowProfesor()
        self.w.show()
        #self.hide()
    
    #funcion para abrir la ventana de alumno
    def ventana_alumno(self):
        '''
        Función para abrir la ventana WindowAlumno
        por medio del botón boton_acciones_alumno
        '''
        self.w = WindowAlumno()
        self.w.show()
    
    #funcion para abrir la ventana de materia basica
    def ventana_materia_basica(self):
        '''
        Función para abrir la ventana WindowBasica
        por medio del botón boton_acciones_materia_basica
        '''
        self.w = WindowBasica()
        self.w.show()
    
    #funcion para abriir la ventana de materia formativa
    def ventana_materia_formativa(self):
        '''
        Función para abrir la ventana WindowFormativa
        por medio del botón boton_acciones_materia_formativa
        '''
        self.w = WindowFormativa()
        self.w.show()
    
    def ventana_grafo(self):
        '''
        Función para abrir la ventana WindowFormativa
        por medio del botón boton_acciones_materia_formativa
        '''
        self.w = WindowGrafo()
        self.w.show()
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = Window()
    GUI.show()
    sys.exit(app.exec_())
    

   
