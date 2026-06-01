# Mega-Prompt para Claude: Contexto Maestro EXPLO-RA 2026

**Instrucción para el Usuario:** Copia todo el contenido desde la siguiente línea y pégalo directamente en tu chat con Claude para que regenere los 4 guiones (`.docx`) basándose en la versión final y definitiva de nuestro trabajo.

---
*(Copia desde aquí)*

**ACTÚA COMO UN EXPERTO EN DISEÑO DE JUEGOS DE ROL CORPORATIVOS Y PEDAGOGÍA.**
Tu tarea es reescribir y actualizar 4 guiones para una sustentación universitaria tipo "Juego de Roles" llamada EXPLO-RA 2026. Los guiones actuales están en los archivos `.docx` que te he adjuntado o referenciado, pero **están desactualizados en sus cifras y enfoques técnicos**. 

Necesito que reescribas esos 4 guiones utilizando **ESTRICTAMENTE** el contexto técnico, las cifras ("Números de Oro") y las dinámicas de roles que te detallo a continuación. No inventes cifras nuevas, no cambies la narrativa principal y asegúrate de que los guiones estén diseñados para que cada participante brille en su rol.

## 1. EL CONTEXTO TÉCNICO Y LOS "NÚMEROS DE ORO" (INMUTABLES)
La empresa "NovaMarket" tiene problemas de rentabilidad. Venden mucho, pero ganan poco. Los equipos de consultoría han procesado un dataset de ventas (S01) de septiembre a noviembre de 2023.

Debes incluir estas cifras exactas en los guiones de los consultores (no en el del Gerente):
- **Datos Limpios:** El dataset original tenía 662 registros. Tras eliminar duplicados y limpiar ciudades ("BOGOTÁ" = "Bogotá"), quedaron **650 transacciones reales**. Los datos en blanco se imputaron usando la mediana.
- **Utilidad Total Actual:** La empresa tiene una utilidad neta raquítica de **~$39,740**.
- **El Problema de Leticia:** La ciudad de Leticia genera una pérdida exacta de **-$79,342** con un margen de **-50.4%**.
- **La Causa de Leticia:** No es falta de ventas. Es el **Costo de Envío** ($1,650 por transacción) que devora el 73% del ingreso bruto.
- **El Efecto Black Friday (24 de Noviembre):** Hubo un pico masivo de ventas ese día, pero las utilidades cayeron estrepitosamente debido a **descuentos agresivos del 40% al 60%**.
- **El Simulador (Plan de Acción):** Si se cierra la operación en Leticia hoy, la utilidad global saltaría de ~$39,740 a **~$119,082**.

## 2. LAS HERRAMIENTAS VISUALES CREADAS (DASHBOARD COMPLETO)
Ambos equipos de consultoría (uno en Python/Streamlit, otro en Power BI) lograron replicar **todo el dashboard completo**. En sus guiones, deben presumir de cómo usan TODO el entorno visual para responder a la Junta:
1. **KPIs Principales:** Ventas Totales, Utilidad Neta, Margen Global y Transacciones.
2. **Mapa de Calor (Heatmap) / Gráficos:** Para identificar rápidamente que Leticia está en rojo frente al resto del país.
3. **Gráfico de Cascada de Costos (Waterfall):** Demuestra visualmente cómo el "Costo de Envío" destruye los ingresos en Leticia, y cómo los "Descuentos" destruyen la ganancia en Black Friday.
4. **Boxplot (Cajas y Bigotes):** Usado para detectar anomalías. Demuestra que noviembre no tuvo un crecimiento real, sino *outliers* generados en un solo fin de semana.
5. **Serie de Tiempo Diaria:** Muestra una línea de tendencia con un enorme marcador rojo el 24 de noviembre, localizando la fuga de rentabilidad.
6. **Simulador de Escenarios:** Un botón/filtro interactivo que permite excluir ciudades (como Leticia) y recalcular KPIs en vivo.

## 3. DINÁMICA DE LOS 4 ROLES A REESCRIBIR

### ROL 1: El Gerente de NovaMarket
- **Misión:** Abrir la presentación, dar la bienvenida a la Junta Directiva y plantear el drama corporativo. 
- **Restricción CRÍTICA:** El Gerente **NO CONOCE LAS CAUSAS** del problema. No sabe nada de los envíos a Leticia ni del desastre del Black Friday. Solo sabe los síntomas: *"Vendedores, estamos facturando mucho volumen, pero las cuentas bancarias están vacías y los márgenes caen. ¿Qué está pasando?"*.
- **Cierre:** Al final de la sesión, el Gerente debe pedirle a la Junta Directiva su votación final: *"Con base en lo que mostraron los consultores, ¿cerramos Leticia o la reestructuramos?"*.

### ROL 2: Equipo "Quantum Analytics Galácticos" (Python + Antigravity)
- **Misión:** Demostrar superioridad tecnológica mediante código y agilidad.
- **Guion Técnico:** Deben explicar con orgullo su proceso técnico de aseguramiento de calidad: cómo usaron Python (pandas) para limpiar la data y cómo una IA Agéntica llamada **Antigravity** (herramienta del equipo DeepMind) les ayudó a programar en vivo, arreglar bugs y compilar el código.
- **Guion Analítico:** Deben ser capaces de recorrer y explicar **todo el dashboard** (KPIs, Cascada, Boxplot, Serie de Tiempo, Simulador) para dar una respuesta integral a la Junta.

### ROL 3: Equipo "Legacy Insight Prehistóricos" (Power BI)
- **Misión:** Defender el enfoque empresarial tradicional del Self-Service BI y competir de tú a tú con el equipo de Python.
- **Guion Técnico:** Deben contar su propio **proceso técnico riguroso** para asegurar la calidad del análisis. Explicarán cómo usaron Power Query (lenguaje M) para auditar y limpiar la data de origen, y cómo modelaron las relaciones y crearon medidas DAX complejas para garantizar exactitud matemática perfecta.
- **Guion Analítico:** Al igual que el otro equipo, deben usar **todo su dashboard interactivo en Power BI** (que incluye las mismas visuales: Cascada, Boxplot, Serie de Tiempo, KPIs) llegando a los mismos "Números de Oro". Su argumento es la robustez, la facilidad de uso corporativo y la democratización del dato sin depender de código duro.

### ROL 4: La Junta Directiva (Jurados, Profesores y Estudiantes invitados)
- **Dinámica de Competencia (Bake-off):** La Junta debe realizar **las mismas preguntas de negocio a ambas firmas consultoras**. Esto creará una competencia sana ("bake-off") donde la verdad de los datos es la misma, pero se evaluará qué equipo argumenta mejor y usa su respectiva herramienta (Streamlit vs Power BI) con mayor fluidez. Además, pueden hacer preguntas técnicas específicas a cada firma sobre su metodología de limpieza.
- **Preguntas obligatorias a incluir en el guion:**
  1. *"¿Por qué Leticia pierde dinero? ¿Es un problema de ventas o de costos?"* (Obliga a mostrar KPIs y Heatmap).
  2. *"Consultores, muéstrenme en su Dashboard exactamente qué rubro financiero nos está quebrando en Leticia"* (Obliga a interactuar con la Cascada de Costos).
  3. *"¿El Black Friday mejoró nuestras utilidades generales?"*
  4. *"¿Cómo sabemos que noviembre no fue un mes de crecimiento orgánico sino un pico anormal?"* (Obliga a explicar el Boxplot).
  5. *"Si el margen cayó en noviembre, ¿en qué momento exacto ocurrió esta fuga de capital?"* (Obliga a mostrar la Serie de Tiempo Diaria).
  6. *"Si cerramos Leticia hoy mismo, ¿cuánto mejora el margen total de la empresa?"* (Obliga a usar el Simulador de Escenarios).
