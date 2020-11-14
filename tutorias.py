# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 09:24:43 2020

@author: Daniel
"""

def registrar_profesor(nombre:str, materia:str, horarios_disponibles:list)->dict:
    profesor = {"nombre": nombre,
                "materia": materia,
                "horarios": horarios_disponibles,
                "disponible": True
                }
    return profesor






def registrar_estudiante(nombre:str, apellido:str, correo: str)->dict:
    estudiante = {"nombre":nombre,
                  "apellido":apellido,
                  "correo":correo
                  }
    
    return estudiante

def busqueda_tutoria(materia:str, horario:list, profesores:list)->dict:
    buscado = None
    for profesor in profesores:
        if materia.lower() == profesor["materia"].lower():
            for hora in horario: 
                if hora in profesor["horarios"]:
                    buscado = profesor
    
    return buscado





#llamar a la funcion registro_profesor
#Hacer una función de get: si esta la hora, mostrar profesaor, sino, mostrar "no disponible"
#For in, condicionales"""
