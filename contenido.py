"""Contenido de la app (extraído de los módulos originales de Tkinter)."""

TEXTO_DEFINICION_IA = ('La Inteligencia Artificial es un campo interdisciplinario dedicado al diseño de sistemas capaces '
 'de realizar tareas asociadas con la inteligencia humana, como aprender, razonar, reconocer '
 'patrones, comprender lenguaje, resolver problemas y tomar decisiones.')

IMAGENES_BANNER = [('imagen1.png', 300), ('imagen2.png', 300)]

INTRO = ('La Inteligencia Artificial se construyó en base a conocimientos y teorías existentes en otras '
 'áreas del conocimiento.')

DISCIPLINAS = [('Filosofía',
  'Aristóteles (300 a.C.) describe de forma estructurada la forma como el ser humano produce '
  'conclusiones racionales a partir de un grupo de premisas (silogismos).'),
 ('Matemáticas',
  'Razonamiento con algoritmos. El cálculo brindó las herramientas que nos permiten la modelación '
  'de diferentes tipos de fenómenos.'),
 ('Psicología',
  'Refuerza la idea de que los humanos y otros animales pueden ser considerados como máquinas para '
  'el procesamiento de información; psicólogos como Piaget y Craik definieron teorías como el '
  'conductismo y la psicología cognitiva.'),
 ('Computación',
  'Las teorías de la IA encuentran un medio para su implementación de artefactos y modelado '
  'cognitivo a través de las computadoras.'),
 ('Lingüística',
  'Aporta un área híbrida conocida como lingüística computacional o procesamiento del lenguaje '
  'natural.'),
 ('Economía',
  'Área experta en la toma de decisiones, debido a que éstas implican la pérdida o ganancia de '
  'rendimiento (Teoría de la decisión, que combina la Teoría de la probabilidad y la Teoría de la '
  'utilidad; Teoría de juegos, para pequeñas economías; Procesos de decisión de Markov, para '
  'procesos secuenciales; entre otras).'),
 ('Neurociencia',
  'Ha contribuido a la IA con los conocimientos recabados hasta la fecha sobre la forma como el '
  'cerebro procesa la información.')]

TIPOS_IA = {'IA débil o estrecha': {'imagen': 'imagenes/clasificacion/1.png',
                         'descripcion': 'Está diseñada para resolver tareas específicas: '
                                        'traducción, recomendación, reconocimiento de imágenes, '
                                        'reconocimiento de voz, generación de texto, '
                                        'recomendaciones de productos. Impulsa la mayor parte de '
                                        'la IA que nos rodea hoy, no tiene nada de débil.'},
 'IA fuerte o general': {'imagen': 'imagenes/clasificacion/2.png',
                         'descripcion': 'Busca crear máquinas con inteligencia humana completa, '
                                        'capaces de realizar cualquier tarea intelectual que un '
                                        'humano pueda hacer. Es teórica y no existe de manera '
                                        'práctica. Es una categoría hipotética.'},
 'IA superinteligente': {'imagen': 'imagenes/clasificacion/3.png',
                         'descripcion': 'Hace referencia a un sistema que superaría a los humanos '
                                        'en absolutamente todas las áreas cognitivas, sería '
                                        'autoconsciente y tendría la capacidad de resolver '
                                        'problemas, aprender y planificar para el futuro. Es una '
                                        'categoría especulativa.'}}

TERMINOS = {'Redes neuronales artificiales': 'Modelos computacionales inspirados en el funcionamiento del '
                                  'cerebro humano, compuestos por capas de nodos interconectados '
                                  '("neuronas") que procesan información y aprenden patrones a '
                                  'partir de datos, utilizados como base de muchas aplicaciones de '
                                  'IA.',
 'Big Data': 'Conjunto de datos de gran volumen, velocidad y variedad, generados por instituciones '
             'educativas y estudiantes, cuyo análisis permite extraer patrones útiles para la toma '
             'de decisiones y la personalización del aprendizaje.',
 'Aprendizaje personalizado': 'Enfoque educativo que utiliza IA para adaptar contenidos, ritmos y '
                              'metodologías de enseñanza a las necesidades, capacidades e '
                              'intereses individuales de cada estudiante.',
 'Minería de datos educativa': 'Técnica que aplica métodos estadísticos y algorítmicos para '
                               'analizar grandes bases de datos educativos con el fin de predecir '
                               'el desempeño, detectar riesgo de deserción o identificar patrones '
                               'de comportamiento estudiantil.',
 'Tutores virtuales': 'Sistemas o agentes basados en IA que simulan el rol de un tutor humano, '
                      'brindando explicaciones, retroalimentación y apoyo personalizado a los '
                      'estudiantes durante su proceso de aprendizaje.',
 'Gamificación': 'Estrategia pedagógica que incorpora elementos y mecánicas propias de los juegos '
                 '(puntos, niveles, recompensas) en contextos educativos para aumentar la '
                 'motivación y el compromiso del estudiante.',
 'Robótica educativa': 'Uso de robots y dispositivos robóticos como herramientas didácticas para '
                       'enseñar conceptos de programación, lógica y ciencias, fomentando el '
                       'aprendizaje práctico y experimental.',
 'Machine Learning': 'Rama de la IA que permite a los sistemas aprender y mejorar automáticamente '
                     'a partir de la experiencia y los datos, sin ser programados explícitamente '
                     'para cada tarea.',
 'Realidad virtual': 'Tecnología que crea entornos digitales tridimensionales e inmersivos, '
                     'permitiendo a los estudiantes interactuar con simulaciones realistas como '
                     'parte de su proceso de aprendizaje.',
 'Aprendizaje profundo': 'Subcampo del Machine Learning que utiliza redes neuronales de múltiples '
                         'capas para procesar grandes volúmenes de datos y resolver tareas '
                         'complejas como el reconocimiento de patrones o lenguaje.',
 'Chatbots': 'Programas informáticos basados en IA capaces de simular conversaciones con usuarios, '
             'utilizados en educación para resolver dudas, guiar procesos de aprendizaje o brindar '
             'soporte administrativo.',
 'Automatización de procesos': 'Aplicación de tecnologías de IA para ejecutar tareas '
                               'administrativas o pedagógicas de manera autónoma, optimizando '
                               'tiempo y recursos en las instituciones educativas.',
 'Sistemas de tutoría inteligente': 'Plataformas de IA diseñadas para ofrecer instrucción '
                                    'personalizada, evaluando el progreso del estudiante y '
                                    'ajustando el contenido según su desempeño (Intelligent '
                                    'Tutoring Systems).',
 'Procesamiento del lenguaje natural': 'Rama de la IA enfocada en que las máquinas comprendan, '
                                       'interpreten y generen lenguaje humano, aplicada en '
                                       'chatbots, corrección automática y sistemas de '
                                       'retroalimentación textual (Natural Language Processing).',
 'E-learning': 'Modalidad de enseñanza y aprendizaje mediada por tecnologías digitales, que se '
               'apoya en plataformas virtuales, permitiendo el acceso a la educación de manera '
               'remota y flexible.',
 'Analítica de aprendizaje': 'Proceso de medición, recopilación y análisis de datos sobre los '
                             'estudiantes y sus contextos, con el objetivo de comprender y '
                             'optimizar el aprendizaje y los entornos educativos (Learning '
                             'Analytics).',
 'Innovación educativa': 'Introducción de nuevas metodologías, herramientas o enfoques pedagógicos '
                         '—frecuentemente apoyados en tecnología— que transforman los procesos '
                         'tradicionales de enseñanza-aprendizaje.',
 'Sistemas de aprendizaje': 'Plataformas o infraestructuras tecnológicas que integran herramientas '
                            'de IA para gestionar, entregar y evaluar contenidos educativos de '
                            'manera eficiente (Learning Systems).',
 'Tecnología educativa': 'Conjunto de herramientas, recursos y aplicaciones digitales utilizadas '
                         'para facilitar y mejorar los procesos de enseñanza y aprendizaje '
                         '(Educational Technology).',
 'Generación automática de preguntas': 'Técnica de IA que crea de manera automática preguntas de '
                                       'evaluación a partir de un contenido dado, utilizada para '
                                       'optimizar la creación de exámenes y actividades educativas '
                                       '(Automatic Question Generation).',
 'Sistema Inteligente': 'Es un conjunto de tecnología industrial avanzada, sensores y algoritmos, '
                        'que trabajan conjuntamente para llevar a cabo tareas específicas de '
                        'manera autónoma y eficiente. Estos sistemas son capaces de percibir su '
                        'entorno, procesar información y tomar decisiones con poca o ninguna '
                        'intervención humana. En la que resuelven problemas complejos de manera '
                        'automática y eficaz en ambientes específicos.La inteligencia artificial '
                        'es la base de los sistemas inteligentes. Estos sistemas, además de '
                        'utilizar redes neuronales y algoritmos de aprendizaje profundo para '
                        'analizar grandes volúmenes de datos (big data), también se apoyan del '
                        'aprendizaje automático para adaptarse y mejorar continuamente sus '
                        'capacidades sin intervención humana.'}

HERRAMIENTAS = [('Gemini',
  'Asistente de inteligencia artificial generativa desarrollado por Google. Puede conversar, '
  'redactar textos, analizar imágenes y apoyar tareas de investigación y programación.',
  'https://gemini.google.com',
  'gemini.png'),
 ('Claude',
  'Asistente de inteligencia artificial desarrollado por Anthropic. Permite conversar, redactar, '
  'analizar documentos y escribir código, con énfasis en respuestas seguras y confiables.',
  'https://claude.ai',
  'claude.png'),
 ('Copilot',
  'Asistente de inteligencia artificial de Microsoft, integrado en Windows, el navegador Edge y '
  'aplicaciones de Office como Word, Excel y PowerPoint, que ayuda a redactar, resumir y generar '
  'contenido.',
  'https://copilot.microsoft.com',
  'copilot.png'),
 ('DeepSeek',
  'Asistente de inteligencia artificial de la empresa china DeepSeek, basado en modelos de '
  'lenguaje con capacidad de razonamiento. Se utiliza para conversar, programar y resolver '
  'problemas.',
  'https://chat.deepseek.com',
  'deepseek.png')]
