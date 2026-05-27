# Guía de Supervivencia Pandas: ¿Paréntesis o Corchetes? 🐼

Para quienes están aprendiendo Python y la librería Pandas, la mayor confusión inicial es saber cuándo usar `()`, `[]` o `[[]]`. Esta guía te dará la regla de oro para que nunca más dudes al escribir tu código, basándonos en los datos de NovaMarket.

---

## 1. Los Paréntesis `( )` = "Haz algo" (Acciones / Funciones)

**Regla de oro:** Si quieres que Pandas ejecute una acción matemática, lea un archivo o haga un verbo, **siempre** lleva paréntesis. Los paréntesis pueden estar vacíos o llevar instrucciones adentro.

**Ejemplos en NovaMarket:**
* `pd.read_csv('archivo.csv')` ➡️ Acción: ¡Lee este archivo!
* `df.sum()` ➡️ Acción: ¡Súmame todo! (Van vacíos porque no necesita instrucciones extra).
* `df.round(1)` ➡️ Acción: ¡Redondea! (Lleva un `1` adentro porque le indicas a cuántos decimales).
* `df.groupby('Categoria')` ➡️ Acción: ¡Agrupa la tabla! (Le indicas adentro por cuál columna agrupar).

---

## 2. Un Corchete `[ ]` = "Tráeme una sola cosa" o "Filtra"

**Regla de oro:** Los corchetes simples no hacen acciones matemáticas; se usan como **"Pinzas"** para extraer información o aplicar filtros. 

**Uso A: Extraer una sola columna**
Cuando pides una sola columna con un corchete, Pandas te devuelve una *Serie* (imagínalo como una lista plana, ya no se ve como una tabla bonita).
* `df['Ciudad']` ➡️ "Tráeme solo la columna Ciudad".
* `df['Ingreso_Total']` ➡️ "Tráeme solo la columna de ingresos".

**Uso B: Aplicar un Filtro (Máscara Booleana)**
Como vimos antes, si adentro del corchete le pasas una condición matemática, actúa como un filtro que extrae filas.
* `df[ df['Ciudad'] == 'Leticia' ]` ➡️ "Tráeme de la tabla solo las filas donde la ciudad sea Leticia".

---

## 3. Doble Corchete `[[ ]]` = "Tráeme un subconjunto" (Varias columnas)

**Regla de oro:** Si necesitas extraer **dos o más columnas** al mismo tiempo, obligatoriamente necesitas dos corchetes. Además, esto le dice a Pandas: *"Mantén el formato de tabla (DataFrame) bonita, no me lo vuelvas una lista"*.

* `df[['Ciudad', 'Categoria', 'Ingreso_Total']]` ➡️ "Tráeme una nueva tablita pequeña que solo tenga estas tres columnas".
* *(Incluso si extraes una sola columna, si usas dobles corchetes `df[['Ciudad']]`, Pandas te la devolverá con formato visual de tabla en lugar de lista plana).*

---

## 💡 Armando el Rompecabezas (El ejemplo maestro)

Miremos nuevamente la línea de código que originó esta duda, aplicando las reglas que acabamos de aprender:

```python
cat = df.groupby('Categoria')[['Ingreso_Total', 'Utilidad_Neta']].sum()
```

Así lo lee la computadora de izquierda a derecha:

1. `df` ➡️ Toma la tabla original completa.
2. `.groupby('Categoria')` ➡️ **(ACCIÓN)** Usa *paréntesis* porque le estamos ordenando la acción de agrupar por la columna categoría.
3. `[['Ingreso_Total', 'Utilidad_Neta']]` ➡️ **(EXTRACCIÓN MÚLTIPLE)** Usa *doble corchete* porque le estamos diciendo: "De esa agrupación gigante, ignora las demás columnas y céntrate en esta tablita pequeña de 2 columnas".
4. `.sum()` ➡️ **(ACCIÓN)** Usa *paréntesis vacíos* porque es la orden matemática final: "Suma todo lo que quedó y dame el total".

¡Si dominas estas tres reglas, entenderás y podrás escribir el 90% del código de análisis de datos en Python!

---

## 🏗️ Bonus: Tablas Dinámicas y la diferencia entre `.index` e `.iloc`

Cuando agrupas una tabla (como hicimos arriba con `groupby('Categoria')`), ocurre un cambio arquitectónico importante: la columna por la que agrupaste **deja de ser una columna normal y se convierte en el armazón de la tabla**, llamado **Índice** (los nombres de las filas).

Por eso, la forma de extraer datos cambia dependiendo de si buscas en el Índice o en una Columna normal:

```python
# 1. Extraer el nombre de la fila ganadora
estrella = cat.index[0]

# 2. Extraer el valor ganador
pct = cat['Margen%'].iloc[0]
```

**¿Por qué son diferentes?**
* **`.index[0]`**: Como 'Categoria' se volvió el índice de la tabla, usamos la palabra `.index` para pedirle las etiquetas de las filas. El `[0]` significa *"dame la etiqueta de la primera fila"*. (Si intentarás usar `cat['Categoria']` te daría un error, porque esa columna ya no existe como columna regular).
* **`.iloc[0]`**: 'Margen%' sí sigue siendo una columna normal. Entonces primero la aislamos `cat['Margen%']` y luego usamos `.iloc` (que significa *Integer Location* o Ubicación por número). Al decirle `.iloc[0]` le ordenas: *"Tráeme la celda que está en el piso cero (la primera fila) de esta columna específica"*.

---

## 🎩 Magia Avanzada: Filtros Múltiples y el Inversor (~)

A veces necesitamos hacer filtros complejos, como si en Excel hiciéramos clic en varios embudos al mismo tiempo. Veamos este ejemplo maestro:

```python
mask = (df['Ciudad']=='Leticia') & (df['Categoria'].isin(['Audio','Wearables']))
```

### Paso 1: ¿Qué hay guardado en la palabra `mask`?
Si pensamos en Excel, la línea de arriba es exactamente igual a ir a la columna "Ciudad" y filtrar solo "Leticia", y luego ir a la columna "Categoria" y chulear solo "Audio" y "Wearables".

Lo que hace Pandas por debajo es revisar las 500 ventas de la empresa una por una y ponerles un sello invisible:
- Sello **Verdadero:** "Sí, esta venta es de Leticia Y ADEMÁS es de Audio o Wearables".
- Sello **Falso:** "No, esta venta es de otra ciudad, o es de Laptops/Smartphones".

Guardamos todos esos sellos dentro de un cofre llamado `mask` (máscara).

### Paso 2: Usar el filtro al derecho `df[mask]`
Si le aplicamos esa máscara a la tabla escribiendo `df[mask]`, Pandas actuará como unas pinzas. Sacará las ventas con sello Verdadero y nos entregará una tablita pequeña **solamente** con las ventas de Leticia de Audio y Wearables. Estaríamos aislando el problema.

### Paso 3: Usar el filtro al revés con la tilde `df[~mask]` (Nivel Dios)
Aquí está la duda de muchos, ¡pero la lógica es simple! 
El símbolo **`~`** (la tilde de la eñe) significa en programación **"Haz exactamente lo contrario"** (Invierte el filtro).

Imagina que en Excel tienes filtrada a Leticia (Audio/Wearables). Poner el símbolo `~` es el equivalente a hacer clic en un botón mágico que dice: *"Oculta exactamente esas filas problemáticas que tengo en pantalla, y muéstrame el resto de la empresa limpia"*.

Entonces, analicemos tu escenario de simulación:
`util_sin = df[~mask]['Utilidad_Neta'].sum()`

1. `df` ➡️ Agarra la tabla completa de la empresa.
2. `[~mask]` ➡️ Filtra AL REVÉS. Es decir, destruye y oculta las ventas de Audio/Wearables en Leticia, y quédate con el resto de ventas "sanas" de todo el país.
3. `['Utilidad_Neta']` ➡️ De esa empresa hipotética y sana, aísla la columna de utilidades.
4. `.sum()` ➡️ Suma todo el dinero.

¡Acabas de calcular en un segundo cuánta plata ganaría toda la empresa si esos productos problemáticos en Leticia jamás hubieran existido!

### Paso 4: Reciclar la máscara y aislar a los villanos
Para saber exactamente cuánta de la pérdida es culpa exclusiva de "Audio" y cuánta de "Wearables", reciclamos nuestra máscara y le agregamos un filtro extra:

```python
audio_let = df[mask & (df['Categoria']=='Audio')]['Utilidad_Neta'].sum()
wear_let  = df[mask & (df['Categoria']=='Wearables')]['Utilidad_Neta'].sum()
```

1. **`mask`**: Agarramos el cofre que ya tiene a las ventas de Leticia (Audio/Wearables).
2. **`& (df['Categoria']=='Audio')`**: Le decimos a Pandas: *"De ese grupo problemático, aprieta el filtro y quédate ESTRICTAMENTE con los de Audio"*.
3. **`['Utilidad_Neta']`**: Extraemos la columna de utilidades de ese micro-grupo.
4. **`.sum()`**: Sumamos todo el dinero.

¡Así logramos reutilizar el código sin tener que volver a escribir una ecuación gigante de filtros desde cero!
