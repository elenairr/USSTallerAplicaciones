# Instructivo de Visualización en Tableau Public
## 1. Conexión de Datos
1.  Abra **Tableau Public** (Web: https://public.tableau.com/app/discover).
2.  Haga clic en **"Crear"** > **"Visualización web"**.
3.  En la pestaña "Conectar a datos", seleccione la pestaña "Archivos" y **Arrastre y suelte** el archivo generado: `data/processed/bank_marketing_tableau.xlsx`.
4.  Verá dos tablas a la izquierda: `Data` y `Verificacion`.
5.  Arrastre la tabla **`Data`** al canvas central.
    *   *Nota*: Si arrastra también `Verificacion`, asegúrese de no hacer un JOIN incorrecto. Para las gráficas, solo necesitamos `Data`.

## 2. Implementación de los 4 Controles (Rúbrica 1.2)
Arrastre los siguientes campos al área de **Filtros** (panel de tarjetas a la izquierda de la gráfica):

1.  **Educación (Education)**:
    *   Arrastre `education` a Filtros.
    *   Seleccione "All" (Todos) > Aceptar.
    *   Clic derecho en el filtro en la tarjeta > **"Mostrar Filtro"**.
    *   En el menú del filtro (esquina superior derecha de la lista), cambie el tipo a **"Valor individual (lista desplegable)"**.

2.  **Estado Civil (Marital)**:
    *   Arrastre `marital` a Filtros.
    *   Seleccione "All" > Aceptar.
    *   Clic derecho > **"Mostrar Filtro"**.
    *   Cambie el tipo a **"Valor individual (lista)"** (Radio Buttons).

3.  **Edad (Age)**:
    *   Arrastre `age` a Filtros.
    *   Seleccione "Todos los valores" > Siguiente.
    *   Deje el rango por defecto > Aceptar.
    *   Clic derecho > **"Mostrar Filtro"**.
    *   Esto creará automáticamente un **Slider (Deslizador)**.

4.  **Trabajo (Job)** - Opcional/Extra:
    *   Arrastre `job` a Filtros > Mostrar Filtro.
    *   Elija **"Lista de valores múltiples (lista desplegable)"** para permitir seleccionar varias profesiones.

## 3. Creación de Gráficas (Rúbrica 1.1)

### Visualización A: Distribución de Suscripciones por Trabajo
1.  Arrastre `job` a **Columnas**.
2.  Arrastre `y` a **Color**.
3.  Arrastre el campo autogenerado `Recuento de Data` (Count) a **Filas**.
4.  Cambie el tipo de gráfico a **"Barras apiladas"**.

### Visualización B: Perfil de Edad y Balance
1.  Arrastre `age` a **Columnas** (asegúrese que sea Dimensión, no Medida). *Tip: Si sale como suma, clic derecho > Dimensión*.
2.  Arrastre `balance` a **Filas** (Promedio). *Tip: Clic derecho > Medida > Promedio*.
3.  Arrastre `y` a **Color**.

## 4. Dashboard Final
1.  Haga clic en el icono de **"Nuevo Dashboard"** (abajo a la izquierda, cuadrado con cruces).
2.  Arrastre sus hojas (Vis A, Vis B) al canvas.
3.  Los filtros creados aparecerán a la derecha. Asegúrese de que afecten a todas las gráficas:
    *   Clic en la flechita de cada filtro > **"Aplicar a hojas de trabajo"** > **"Todas las que usen esta fuente de datos"**.

## 5. Verificación de Datos (Rúbrica 1.3)
Verifique vs la Hoja `Verificacion` del Excel:
1.  Cree una nueva Hoja de trabajo llamada "Control".
2.  Arrastre `Recuento de data` al texto. El número debe coincidir con **Total Registros** (45,211).
3.  Arrastre `Age` (Suma) al texto. Compare con **Suma de Edad**.

## 6. Publicación
1.  Clic en **"Publicar como..."** (arriba a la derecha).
2.  Asigne nombre: `Marco03_BankMarketing`.
3.  Copie el enlace para la entrega.
