# Reglas por 1 área (actualizado y verificado)
reglas_una_area = {
    "Aire Libre": [
        "Licenciatura en Gestión del Turismo",
        "Técnico en Turismo",
        "Técnico en Salvamentos y Extinción de Incendios"
    ],
    "Mecanico": [
        "Ingeniería en Sistemas y Computación",
        "Técnico en Computación",
        "Licenciatura en Radiología e Imágenes"
    ],
    "Calculo": [
        "Licenciatura en Contaduría Pública",
        "Técnico en Contabilidad",
        "Licenciatura en Administración de Empresas"
    ],
    "Cientifico": [
        "Licenciatura en Psicología",
        "Licenciatura en Laboratorio Clínico",
        "Licenciatura en Nutrición"
    ],
    "Persuasivo": [
        "Licenciatura en Mercadeo Estratégico",
        "Licenciatura en Relaciones Públicas",
        "Técnico en Marketing Digital"
    ],
    "Artistico-Plastico": [
        "Licenciatura en Diseño Gráfico Multimedia",
        "Técnico en Diseño Gráfico",
        "Licenciatura en Comunicaciones"
    ],
    "Literario": [
        "Licenciatura en Comunicaciones",
        "Licenciatura en Ciencias Jurídicas",
        "Licenciatura en Idioma Inglés"
    ],
    "Musical": [
        "Licenciatura en Comunicaciones",
        "Licenciatura en Psicología"
    ],
    "Servicio Social": [
        "Licenciatura en Trabajo Social",
        "Licenciatura en Enfermería",
        "Licenciatura en Psicología"
    ],
    "Trabajo de Oficina": [
        "Licenciatura en Administración de Empresas",
        "Técnico en Contabilidad",
        "Licenciatura en Computación Gerencial"
    ]
}

# Reglas por combinación de 2 áreas (completo según PDF)
reglas_combinadas2 = {
    ("Aire Libre", "Mecanico"): [
        "Técnico en Salvamentos y Extinción de Incendios",
        "Técnico en Gestión de Riesgo de Desastres"
    ],
    ("Aire Libre", "Servicio Social"): [
        "Licenciatura en Enfermería",
        "Licenciatura en Trabajo Social",
        "Licenciatura en Nutrición"
    ],
    ("Aire Libre", "Cientifico"): [
        "Técnico en Salvamentos y Extinción de Incendios",
        "Licenciatura en Radiología e Imágenes"
    ],
    ("Mecanico", "Calculo"): [
        "Ingeniería en Sistemas y Computación",
        "Licenciatura en Computación Gerencial"
    ],
    ("Mecanico", "Cientifico"): [
        "Licenciatura en Radiología e Imágenes",
        "Licenciatura en Optometría"
    ],
    ("Calculo", "Cientifico"): [
        "Licenciatura en Laboratorio Clínico",
        "Licenciatura en Contaduría Pública"
    ],
    ("Cientifico", "Servicio Social"): [
        "Licenciatura en Psicología",
        "Licenciatura en Nutrición",
        "Licenciatura en Enfermería"
    ],
    ("Persuasivo", "Literario"): [
        "Licenciatura en Comunicaciones",
        "Licenciatura en Relaciones Públicas"
    ],
    ("Persuasivo", "Artistico-Plastico"): [
        "Licenciatura en Diseño Gráfico Multimedia",
        "Técnico en Marketing Digital"
    ],
    ("Artistico-Plastico", "Literario"): [
        "Licenciatura en Diseño Gráfico Multimedia",
        "Licenciatura en Comunicaciones"
    ],
    ("Artistico-Plastico", "Servicio Social"): [
        "Licenciatura en Psicología",
        "Licenciatura en Nutrición",
        "Licenciatura en Enfermería"
    ],
    ("Musical", "Artistico-Plastico"): [
        "Licenciatura en Diseño Gráfico Multimedia",
        "Licenciatura en Comunicaciones"
    ],
    ("Servicio Social", "Trabajo de Oficina"): [
        "Licenciatura en Trabajo Social",
        "Licenciatura en Administración de Empresas"
    ],
    ("Trabajo de Oficina", "Calculo"): [
        "Licenciatura en Contaduría Pública",
        "Técnico en Contabilidad"
    ],
    ("Literario", "Cientifico"): [
        "Licenciatura en Psicología",
        "Licenciatura en Comunicaciones"
    ],
    ("Literario", "Servicio Social"): [
        "Licenciatura en Trabajo Social",
        "Licenciatura en Psicología"
    ],
    ("Musical", "Literario"): [
        "Licenciatura en Comunicaciones",
        "Licenciatura en Psicología (énfasis en musicoterapia)"
    ],
    # Combinaciones adicionales encontradas en el PDF
    ("Aire Libre", "Calculo"): [
        "Técnico en Gestión de Riesgo de Desastres",
        "Licenciatura en Gestión del Turismo"
    ],
    ("Mecanico", "Servicio Social"): [
        "Licenciatura en Radiología e Imágenes",
        "Licenciatura en Optometría"
    ]
}

# Reglas por combinación de 3 áreas (completo según PDF)
reglas_combinadas3 = {
    ("Aire Libre", "Mecanico", "Calculo"): [
        "Técnico en Gestión de Riesgo de Desastres",
        "Licenciatura en Gestión del Turismo"
    ],
    ("Aire Libre", "Mecanico", "Cientifico"): [
        "Técnico en Salvamentos y Extinción de Incendios",
        "Licenciatura en Radiología e Imágenes"
    ],
    ("Aire Libre", "Servicio Social", "Cientifico"): [
        "Licenciatura en Enfermería",
        "Licenciatura en Nutrición"
    ],
    ("Mecanico", "Calculo", "Cientifico"): [
        "Ingeniería en Sistemas y Computación",
        "Licenciatura en Computación Gerencial"
    ],
    ("Mecanico", "Cientifico", "Servicio Social"): [
        "Licenciatura en Radiología e Imágenes",
        "Licenciatura en Optometría"
    ],
    ("Calculo", "Cientifico", "Servicio Social"): [
        "Licenciatura en Laboratorio Clínico",
        "Licenciatura en Nutrición"
    ],
    ("Persuasivo", "Literario", "Artistico-Plastico"): [
        "Licenciatura en Comunicaciones",
        "Licenciatura en Diseño Gráfico Multimedia"
    ],
    ("Persuasivo", "Artistico-Plastico", "Musical"): [
        "Licenciatura en Comunicaciones",
        "Técnico en Marketing Digital"
    ],
    ("Artistico-Plastico", "Literario", "Musical"): [
        "Licenciatura en Diseño Gráfico Multimedia",
        "Licenciatura en Comunicaciones"
    ],
    ("Servicio Social", "Trabajo de Oficina", "Calculo"): [
        "Licenciatura en Administración de Empresas",
        "Licenciatura en Trabajo Social"
    ],
    ("Servicio Social", "Trabajo de Oficina", "Literario"): [
        "Licenciatura en Psicología",
        "Licenciatura en Trabajo Social"
    ],
    ("Trabajo de Oficina", "Calculo", "Cientifico"): [
        "Licenciatura en Contaduría Pública",
        "Licenciatura en Computación Gerencial"
    ],
    ("Literario", "Cientifico", "Servicio Social"): [
        "Licenciatura en Psicología",
        "Licenciatura en Comunicaciones"
    ],
    ("Literario", "Musical", "Artistico-Plastico"): [
        "Licenciatura en Comunicaciones",
        "Licenciatura en Diseño Gráfico Multimedia"
    ],
    ("Musical", "Artistico-Plastico", "Persuasivo"): [
        "Licenciatura en Comunicaciones",
        "Técnico en Marketing Digital"
    ],
    # Combinaciones adicionales encontradas en el PDF
    ("Aire Libre", "Calculo", "Cientifico"): [
        "Licenciatura en Laboratorio Clínico",
        "Licenciatura en Nutrición"
    ],
    ("Persuasivo", "Cientifico", "Servicio Social"): [
        "Licenciatura en Psicología",
        "Licenciatura en Trabajo Social"
    ],
    ("Artistico-Plastico", "Cientifico", "Servicio Social"): [
        "Licenciatura en Psicología",
        "Licenciatura en Nutrición"
    ]
}