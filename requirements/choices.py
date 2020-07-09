ASTRONOMIA = 'AS'
FISICA = 'FI'
GEOFISICA = 'GF'
GEOLOGIA = 'GL'
ESTRUCTURAS = 'ES'
HIDRAULICA = 'HI'
TRANSPORTE = 'TR'
BIOTECNOLOGIA = 'BT'
COMPUTACION = 'CC'
ELECTRICA = 'EL'
INDUSTRIAL = 'IN'
MATEMATICA = 'MA'
MECANICA = 'ME'
MINAS = 'MI'
QUIMICA = 'IQ'

DEGREE_CHOICES = (
    #(ASTRONOMIA, 'Licenciatura en Ciencias, Mención Astronomía'),
    #(FISICA, 'Licenciatura en Ciencias, Mención Física'),
    #(GEOFISICA, 'Licenciatura en Ciencias, Mención Geofísica'),
    (GEOLOGIA, 'Geología'),
    (ESTRUCTURAS, 'Ingeniería Civil, Mención Estructuras y Construcción'),
    (HIDRAULICA, 'Ingeniería Civil, Mención Hidráulica, Sanitaria y Ambiental'),
    (TRANSPORTE, 'Ingeniería Civil, Mención Transporte'),
    (BIOTECNOLOGIA, 'Ingeniería Civil en Biotecnología'),
    (COMPUTACION, 'Ingeniería Civil en Computación'),
    (ELECTRICA, 'Ingeniería Civil Eléctrica'),
    (INDUSTRIAL, 'Ingeniería Civil Industrial'),
    (MATEMATICA, 'Ingeniería Civil Matemática'),
    (MECANICA, 'Ingeniería Civil Mecánica'),
    (MINAS, 'Ingeniería Civil de Minas'),
    (QUIMICA, 'Ingeniería Civil Química'),
)

PRACTICA1 = 'P1'
PRACTICA2 = 'P2'
PRACTICA3 = 'P3'
MEMORIA = 'ME'
FULLTIME = 'FT'
PARTIME = 'PT'

TYPES_CHOICES = (
    (None, 'Seleccione una'),
    (PRACTICA1, 'Práctica 1'),
    (PRACTICA2, 'Práctica 2'),
    (PRACTICA3, 'Práctica 3'),
    (MEMORIA, 'Memoria'),
    (FULLTIME, 'Fulltime'),
    (PARTIME, 'Partime'),
)


BRING_STAND_CHOICES = (
    ('0', '---------'),
    ('1', 'Stand Propio'),
    ('2', 'Stand Feria'),
)

STAND_TYPE_CHOICES = (
    ('0', '---------'),
    ('1', 'Stand reducido (2m x 3m)'),  #2 entrevistadores
    ('2', 'Stand simple (3m x 3m)'), #2 
    ('3', 'Stand especial 4 (4m x 3m)'), #3
    ('4', 'Stand especial 5 (5m x 3m)'), #4
    ('5', 'Stand doble (6m x 3m)'), #4
)

STAND_CHOICES= (
    ('A', 'Stand A'),
    ('B', 'Stand B'),
    ('1', 'Stand 1'),
    ('2', 'Stand 2'),
    ('3', 'Stand 3'),
    ('4', 'Stand 4'),
    ('5', 'Stand 5'),
    ('6', 'Stand 6'),
    ('7', 'Stand 7'),
    ('8', 'Stand 8'),
    ('9', 'Stand 9'),
)

TIPE_CHOICES=(
('1','Entrevistas Individuales cada 15 minutos'),
('2','Otra Modalidad'),
)

DAY_CHOICES = (
    ('1', 'Lunes (08/10/2018)'),
    ('2', 'Martes (09/10/2018)'),
    ('3', 'Miercoles (10/10/2018)'),
)

TIME_CHOICES = (
    (True, 'Horario Mañana'),
    (False, 'Horario Tarde'),
)

