def verificar_calificacion(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3
    
    if promedio >= 6:
        return "APROBADO"
    else:
        return "DESAPROBADO"
    
resultado = verificar_calificacion(7, 6, 6)
print (resultado)