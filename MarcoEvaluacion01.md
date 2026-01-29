#### Contexto
Universidad San Sebastián
Magíster en Data Science
Asignatura: Taller de Aplicaciones
Docente: Dr. Mauricio Sepúlveda
Alumna: Maria Elena Irribarra Aguilera



#### Tarea: Aplicación de método de ciencia de datos

Objetivo: Aplicar las técnicas vistas en el curso para extraer información/conocimiento.

1. De acuerdo al set de datos y al panorama de métodos a estudiar, establecer el problema y las hipótesis de trabajo, con visión de negocio.

2. Cargue los datos, realice EDA y visualizaciones e indique conclusiones que impacten en los modelos.

3. Justifique y realice transformaciones a los datos que impacten en los modelos, para mejorar las métricas.

4. Utilizar algún algoritmo de agrupamiento: Justifique el número de cluster propuesto e interprete cada grupo.

5. Utilizar algoritmos de clasificación: Determinar que algoritmo tiene mejores predicciones con datos de testeo. Indique mejoras que podría realizar a futuro a sus datos o proceso para mejorar los indicadores.

6. Aplicar el algoritmo Apriori para descubrir reglas de asociación entre los datos. Explicar las 6 reglas con mejores indicadores para soporte y confianza. Explique el lift.

7. Resumir en una presentación de máximo 10 páginas el trabajo realizado y los hallazgos.


#### Rúbrica:

Criterio 1: Completitud de la tarea para la casa
Usa agrupamiento, justificando el número de clúster e interpretando cada grupo.
Usa clasificación determinando métricas más adecuadas para el negocio.
Aplica Apriori y explica seis reglas.

Criterio 2: Comprensión del Modelo y Metodología
Demuestra una comprensión profunda de los conceptos del modelo, incluyendo los algoritmos utilizados y las métricas de evaluación. Usa adecuadamente CRIPS_DM.

Criterio 3: Análisis y transformación de datos.
Analiza y transforma los datos para mejorar los indicadores del modelo.

Criterio 4: Presentación de resultados.
Los resultados se presentan de manera clara, concisa y visualmente atractiva, utilizando gráficas y tablas apropiados.

Criterio 5: Interpretación y Conclusiones.


#### Dataset.

1. Bank Marketing 
El dataset Bank Marketing contiene datos de campañas de marketing telefónico de un banco portugués, con información del cliente (edad, profesión, educación, situación financiera), detalles de la campaña (número de contactos, tipo, mes, duración) y una etiqueta binaria que indica si el cliente contrató o no un depósito a plazo. Es un problema de clasificación con desbalance  y  muchas  variables  categóricas,  ideal  para  probar  modelos  de  marketing  y técnicas de preprocesamiento. 
Publicación en UCI: Moro, S., Laureano, R., & Cortez, P. (2014). “Using Data Mining for Bank Direct  Marketing:  An  Application  of  the  CRISP-DM  Methodology”.  Expert  Systems  with Applications.

https://archive.ics.uci.edu/dataset/222/bank+marketing 


#### Plan Propuesto para el desarrollo

1. Crear un documento denominado PlanTrabajo.md

2. Siguiendo la estructura tìpica de un proyecto de ciencia de datos (que comienza con el EDA, aplica transformaciones, aplica métodos y concluye) y siguiendo los cinco criterios de la Rúbrica, planificar el contenido de la presentación que se solicita y un informe que detalla el problema, metodología y resultados. Se escribe en el PlanTrabajo.md.

3. Se planifica bloque a bloque un jupiter notebook que identifique claramente las secciones necesarias, partiendo por la importación de los datos, luego el EDA, y agregando secciones especiales para los analisis de agrupamiento, clasificación y Apriori. Se considera guardar ordenadamente las figuras que requerirá la presentación y los datos que requerirá el informe. Se escribe en el PlanTrabajo.md.

4. Se planifica el contenido del informe el que se elabora en LaTeX y formato carta. Se incluyen las figuras que se generan durante la ejecución del jupiter notebook. Se escribe en el PlanTrabajo.md.

5. Se planifica el contenido de la presentación que se elabora en LaTeX y formato Beamer con tema Metropolis. Se incluyen las figuras que se generan durante la ejecución del jupiter notebook. Se escribe en el PlanTrabajo.md.

6. Se procede a la construcción del jupyter notebook, comprobando y depurando cada bloque en la medida que se avanza. 

6.1. Antecedente para la importación de datos:

                    pip install ucimlrepo

                    from ucimlrepo import fetch_ucirepo 
                    
                    # fetch dataset 
                    bank_marketing = fetch_ucirepo(id=222) 
                    
                    # data (as pandas dataframes) 
                    X = bank_marketing.data.features 
                    y = bank_marketing.data.targets 
                    
                    # metadata 
                    print(bank_marketing.metadata) 
                    
                    # variable information 
                    print(bank_marketing.variables) 

6.2 EDA y transformaciones

    - Se guardan las figuras en png.

6.3 Agrupamiento

    - Se guardan las figuras en png.
    - Consider k-means, clúster jerárquicos, DBScan
    - Considerar medidas propias de cada método
    - Mostrar regla del codo
    - Considerar comparación de medidas entre métodos
    - Conclusiones e Interpretación mirando hacia el problema e hipótesis
    

6.4 Clasificación

    - Se guardan las figuras en png.
    - Considerar árboles de decisión
    - Random Forest
    - Regresión Logística, con y sin regularizaciones
    - Mostrar métricas comparativas
    - Conclusiones e Interpretación mirando hacia el problema e hipótesis

6.5 Apriori

    - Se guardan las figuras en png.
    - Idenficar reglas bajo un método razonable y luego las 6 principales.
    - Explicar el lift de las reglas principales
    - Interpretarlas bajo la idea de antecedente consecuente
    - Mostrar métricas comparativas
    - Conclusiones e Interpretación mirando hacia el problema e hipótesis

6.6 Conclusiones consolidadas

    - Revisar el objetivo general y pregunta de investigación
    - Revisar los objetivos específicos tenidos en cuenta
    - Prepara cuadros comparativos que ilustren lo que se busca

7. Se procede a la construccion del informe 

    - Se prepara un informe bien estruturado
    - Se explican las figuras y tablas

8. Se procede a la construcción de la presentación.

    - Se seleccionan las 10 figura relevantes que hilen el relato
    - Se desarrollan las láminas respectivas, livianas en contenido
    - Cada lamina contiene una de las figuras



