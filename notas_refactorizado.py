

def calcular_media(nota1, nota2, nota3):
    """
    Calcula la media aritmética de tres notas.

    Args:
        nota1 (float): Primera nota del alumno.
        nota2 (float): Segunda nota del alumno.
        nota3 (float): Tercera nota del alumno.

    Returns:
        float: La media de las tres notas (valor entre 0 y 10).
    """
    return (nota1 + nota2 + nota3) / 3


def obtener_estado_aprobado(nota):
    """
    Determina si una nota específica corresponde a un aprobado o un suspendido.

    Args:
        nota (float): La calificación a evaluar.

    Returns:
        bool: True si está aprobado (nota >= 5), False en caso contrario.
    """
    if nota >= 5:
        print("aprobado")
        return True
    else:
        print("suspendido")
        return False


def mostrar_informe_alumno(nombre, nota1, nota2, nota3):
    """
    Imprime en consola el reporte detallado de las notas de un alumno,
    su promedio obtenido y su calificación cualitativa correspondiente.

    Args:
        nombre (str): Nombre completo del alumno.
        nota1 (float): Primera nota.
        nota2 (float): Segunda nota.
        nota3 (float): Tercera nota.
    """
    print("Alumno: " + nombre)
    print("Nota 1: " + str(nota1))
    print("Nota 2: " + str(nota2))
    print("Nota 3: " + str(nota3))
    
    # Comentario inline 1: Se reutiliza la función extraída para evitar duplicar la fórmula de la media
    media = calcular_media(nota1, nota2, nota3)
    print("Media: " + str(media))
    
    # Comentario inline 2: Estructura optimizada con elif para evitar evaluaciones redundantes
    if media >= 9:
        print("Sobresaliente")
    elif media >= 7:
        print("Notable")
    elif media >= 5:
        print("Aprobado")
    else:
        print("Suspenso")
        
    print("--------")


def main():
    """
    Función principal encargada de ejecutar el flujo del programa
    con los datos de prueba de los alumnos.
    """
    mostrar_informe_alumno("Ana García", 8, 7, 9)
    mostrar_informe_alumno("Luis Pérez", 4, 5, 3)
    mostrar_informe_alumno("Marta Gómez", 6, 7, 5)


if __name__ == "__main__":
    main()