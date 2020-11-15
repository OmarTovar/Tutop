# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 09:11:54 2020

@author: Daniel
"""
import tutorias as mod

def mostrar_profesores(profesores:list)->None:
    indice = 1
    for profesor in profesores:
        nombre = profesor["nombre"]
        materia = profesor["materia"]
        horarios = profesor["horarios"]
        disponible = profesor["disponible"]
        print(str(indice) + ". Nombre: " + nombre + " - Materia: " + materia + " - Horarios: " + str(horarios) + " - Disponible: " + str(disponible) + "\n")
        indice += 1
        
def mostrar_estudiantes(estudiantes:list)->None:
    for estudiante in estudiantes:
        print(estudiante)
        
def ejecutar_registrar_profesor(profesores:list)->None:
    nombre = input("Ingrese el nombre del profesor: ")
    materia = input("Ingrese la materia que enseña el profesor: ")
    horarios = input("Ingrese los horarios que dispone para enseñar separados por coma: ")
    if "," in horarios:
        horarios = horarios.split(",")
    else:
        horarios = [horarios]
    
    profesor = mod.registrar_profesor(nombre, materia, horarios)
    profesores.append(profesor)


def ejecutar_registrar_estudiante(profesores:list)->None:
    return None

def ejecutar_busqueda_tutoria(profesores:list)->None:
    materia = input("Ingrese la materia que desea buscar: ")
    horario = input("Ingrese el horario que desea buscar: ")
    if "," in horario:
        horario = horario.split(",")
    else:
        horario = [horario]
    profesor = mod.busqueda_tutoria(materia,horario,profesores)
    
    if profesor == None:
        print("No se pudo encontrar un profesor con sus parámetros")
    else:
        print("Nombre: " + profesor["nombre"] + " - Disponible: " + str(profesor["disponible"]))

def iniciar_aplicacion():
    """Inicia la ejecucion de la aplicacion por consola.
    Esta funcion primero crea los cuatro bancos de sangre.
    Luego la funcion le muestra el menu al usuario y espera a que seleccione una opcion.
    Esta operacion se repite hasta que el usuario seleccione la opcion de salir.
    """
    profesores = []
    profesores.append(mod.registrar_profesor("Jimmy","Ciencias",["11","14"]))
    profesores.append(mod.registrar_profesor("Walter","Musica",["11","23"]))
    estudiantes = []
    
    ejecutando = True
    while ejecutando:
        print("\n\n" + ("-"*25) + "Estado de los profesores" + ("-"*25))
        print("\nProfesores:\n")
        mostrar_profesores(profesores)
        print("-"*74)
        print("\nEstudiantes:\n")
        mostrar_estudiantes(estudiantes)
        print("-"*74)

        ejecutando = mostrar_menu_aplicacion(profesores, estudiantes)

        if ejecutando:
            input("Presione cualquier tecla para continuar ... ")
    
def mostrar_menu_aplicacion(profesores:list, estudiantes:list) -> bool:
    """Le muestra al usuario las opciones de ejecucion disponibles.
    Parametros:
        b1 (dict): Diccionario que contiene la informacion del banco 1.
        b2 (dict): Diccionario que contiene la informacion del banco 2.
        b3 (dict): Diccionario que contiene la informacion del banco 3.
        b4 (dict): Diccionario que contiene la informacion del banco 4.
    Retorno:
        Esta funcion retorna True si el usuario selecciono una opcion diferente
        a la opcion que le permite salir de la aplicacion.
        Esta funcion retorna False si el usuario selecciono la opcion para salir
        de la aplicacion.

    """
    print("Menu de opciones")
    print(" 1 - Registrar profesor.")
    print(" 2 - Buscar tutoría.")
    print(" 3 - Salir de la aplicacion.")
    
    opcion_elegida = input("Ingrese la opcion que desea ejecutar: ").strip()#.strip quita un caracter definido de la izquierda y la derecha del string, si no se especifica se borran los espacios. ejemplo "   hola  ".strip() da return "hola"

    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_registrar_profesor(profesores)
    elif opcion_elegida == "2":
        ejecutar_busqueda_tutoria(profesores)
    elif opcion_elegida == "3":
        continuar_ejecutando = False
    else:
        print("La opcion " + opcion_elegida + " no es una opcion valida.")
    return continuar_ejecutando


iniciar_aplicacion()