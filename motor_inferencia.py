from conocimiento import reglas_una_area, reglas_combinadas2, reglas_combinadas3

def evaluar(areas, puntajes):
    # Ensure areas and puntajes are of the same length
    if len(areas) != len(puntajes):
        return ["Error: Número de áreas y puntajes no coinciden."], []
    
    # Create a list of tuples (area, puntaje) and sort by puntaje descending
    areas_puntajes = sorted(zip(areas, puntajes), key=lambda x: x[1], reverse=True)
    
    # Extract top 3 areas with highest scores
    top_areas = [area for area, puntaje in areas_puntajes[:3]]
    top_puntajes = [puntaje for area, puntaje in areas_puntajes[:3]]
    
    # Check for 3-area combinations first
    if len(top_areas) >= 3:
        # Try exact combination first
        clave = tuple(sorted(top_areas[:3]))
        if clave in reglas_combinadas3:
            return reglas_combinadas3[clave], top_areas[:3]
        
        # Try all possible 3-area combinations
        for i in range(len(top_areas)):
            for j in range(i+1, len(top_areas)):
                for k in range(j+1, len(top_areas)):
                    clave = tuple(sorted([top_areas[i], top_areas[j], top_areas[k]]))
                    if clave in reglas_combinadas3:
                        return reglas_combinadas3[clave], [top_areas[i], top_areas[j], top_areas[k]]
    
    # Check for 2-area combinations
    if len(top_areas) >= 2:
        # Try exact combination first
        clave = tuple(sorted(top_areas[:2]))
        if clave in reglas_combinadas2:
            return reglas_combinadas2[clave], top_areas[:2]
        
        # Try all possible 2-area combinations
        for i in range(len(top_areas)):
            for j in range(i+1, len(top_areas)):
                clave = tuple(sorted([top_areas[i], top_areas[j]]))
                if clave in reglas_combinadas2:
                    return reglas_combinadas2[clave], [top_areas[i], top_areas[j]]
    
    # Check for single area
    if len(top_areas) >= 1:
        for area in top_areas:
            if area in reglas_una_area:
                return reglas_una_area[area], [area]
    
    return ["No se encontraron recomendaciones para las áreas seleccionadas."], []

def obtener_maximos(puntajes, areas):
    max_puntaje = max(puntajes)
    return [areas[i] for i, puntaje in enumerate(puntajes) if puntaje == max_puntaje]