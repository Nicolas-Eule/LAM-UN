# Entregables y evaluación

[← Proyecto Integrador Industrial](README.md)

El Proyecto de Control Industrial de Movimiento vale **25 %** de la nota del curso (programa 2026-2S). Lo que sigue resume el enunciado oficial *Proyecto Industrial de la Asignatura v2026-2S*; ante cualquier diferencia, prima el enunciado publicado en Classroom.

## 1. Reporte técnico y de proceso de aprendizaje

Formato libre, con dos secciones.

### 1.1 Producto: informe técnico de ingeniería

Máximo **20 páginas** más anexos complementarios. Los criterios de detalle están en la plantilla de evaluación.

- **Parametrización de la trayectoria.** Cálculos de los perfiles de movimiento. Cada equipo escoge y justifica un **ritmo de producción (RP)** lo más elevado posible, respetando el desempeño del control y la carga computacional del sistema ciberfísico. Habitualmente 5 < RP < 10; se espera **10 ≤ RP ≤ 20 cajas/minuto**.
- **Diseño de rutinas.** Grafcet de la solución e instrucciones Ladder usadas, con capturas de pantalla y explicación del programa y del proceso de ingeniería.
- **Validación.** Rutina completa para el ciclo previsto, soportada con las gráficas de tendencias de Studio 5000. Cada equipo propone, justifica y valida sus propias rutinas.

### 1.2 Proceso

Máximo **6 páginas**.

| Aspecto | Redacción | Ejemplos de qué reflexionar |
| --- | --- | --- |
| Gestión de proyecto | Grupal | Dinámica de las reuniones, manejo del tiempo y los recursos, seguimiento del avance, interacción con el docente |
| Trabajo colaborativo | Grupal | Roles y tareas, compromiso, comunicación, manejo de diferencias |
| Proceso de aprendizaje | Individual | Coherencia con las actividades del curso, competencias desarrolladas, efectividad del trabajo autónomo y colaborativo |
| Recomendaciones | Individual | Mejoras para futuras versiones del proyecto |

## 2. Sustentación

En horario concertado con cada equipo y con participación de todos los integrantes.

| Tramo | Duración | Contenido |
| --- | --- | --- |
| Presentación | 20 min | Diapositiva inicial con nombres (ojalá fotos recientes) y aportes de cada integrante; luego la solución |
| Preguntas | 45 min | Rondas abiertas (responde cualquiera) y dirigidas (a un integrante) |
| Evaluación | 10 min | Autoevaluación del equipo y evaluación del docente en escala porcentual |

Si la autoevaluación y la evaluación del docente difieren en 10 % o menos, se promedian; si difieren más, prima la del docente. Puede haber calificación individual cuando el trabajo colaborativo, el dominio temático o la participación así lo sugieran.

## 3. Evidencias de la Parte 2 (Etiquetadora)

> [!NOTE]
> La forma en que la Parte 2 se integra a la nota se define con el docente. Esta lista es la evidencia mínima que cada guía de la Parte 2 pide dejar registrada, para que pueda incorporarse al informe y a la sustentación.

| Guía | Evidencia |
| --- | --- |
| [01 · Seguridad](02-etiquetadora-de-cajas/01-seguridad-y-reglas.md) | Lista de chequeo firmada por el monitor |
| [04 · Puesta en marcha](02-etiquetadora-de-cajas/04-puesta-en-marcha-de-ejes.md) | Tabla de escalado justificada; resultado de hook-up y polaridad por eje; ganancias antes y después de la sintonía |
| [05 · Paradas y fallas](02-etiquetadora-de-cajas/05-estados-paradas-y-fallas.md) | Tabla predicción vs. observado; distancia de frenado medida |
| [06 · Movimientos básicos](02-etiquetadora-de-cajas/06-movimientos-basicos.md) | Tendencias de posición y velocidad para trapezoidal y S-curve |
| [07 · Gemelo y PAC físico](02-etiquetadora-de-cajas/07-gemelo-conectado-al-pac.md) | Video corto con gemelo y servos moviéndose a la vez; tabla de señales mapeadas |
| [08 · Secuencia coordinada](02-etiquetadora-de-cajas/08-secuencia-coordinada.md) | Grafcet, programa `.L5X` y tendencia del ciclo completo; cálculo de la relación de engranaje |
