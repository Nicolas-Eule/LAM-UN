# 04 · Puesta en marcha de los ejes

[← Proyecto, E/S, drives y ejes](03-proyecto-y-hardware.md) · Siguiente: [Estados, paradas y fallas →](05-estados-paradas-y-fallas.md)

**Al terminar:** cada eje trabaja en unidades de ingeniería que coinciden con el gemelo, tiene límites de recorrido, su sentido positivo coincide con el del gemelo y está sintonizado.

*Basada en la guía de configuración HW/SW III de 2015.* Modo C: requiere la [lista de chequeo de seguridad](01-seguridad-y-reglas.md#puerta-de-seguridad-lista-de-chequeo-para-el-modo-c).

## 1. Escalado: de revoluciones a centímetros

El escalado define cuántas unidades de ingeniería (aquí, cm) avanza la carga por cada revolución del motor. **Debe salir de la mecánica**, y esa mecánica es la del gemelo ([parámetros de la guía 02](02-la-maquina-y-la-estacion.md#parámetros-mecánicos-que-debes-definir)).

| Transmisión | *Load Type* en Studio 5000 | Avance por revolución del motor |
| --- | --- | --- |
| Rodillo o polea de diámetro $D$ | *Linear Actuator → Belt and Pulley* (o *Rack and Pinion*) | $\dfrac{\pi D}{i}$ |
| Tornillo de paso $p$ | *Linear Actuator → Screw* | $\dfrac{p}{i}$ |
| Rotación sin conversión a lineal | *Rotary Transmission* (o *Direct Coupled Rotary* si $i = 1$) | $\dfrac{360°}{i}$ |

donde $i$ es la relación de reducción (vueltas del motor por vuelta de la salida).

> [!NOTE]
> **Corrección a la guía de 2015.** Allí se usaba *Direct Coupled Rotary* con "1 cm por revolución" en los tres ejes. Ese valor no corresponde a ningún mecanismo: con él, las velocidades y aceleraciones programadas no tienen significado físico, y la relación de engranaje de la guía 6 quedó mal calculada. Aquí el escalado sale del rodillo, la polea o el tornillo del gemelo.

En **Axis Properties → Scaling**:

1. *Load Type* según la tabla.
2. *Position Units*: **cm**.
3. El avance por revolución que calculaste.

### Recorrido y límites

| Eje | *Travel Mode* | *Soft Travel Limits* |
| --- | --- | --- |
| `Eje_Banda` | *Unlimited* (la banda gira indefinidamente) | No aplica |
| `Eje_X` | *Limited* | Mínimo y máximo de la carrera útil de X, con margen |
| `Eje_Y` | *Limited*, rango 60 cm | Mínimo y máximo dentro de 0–60 cm, con margen |

Deja un margen razonado entre la posición más lejana que programarás y el límite, y justifícalo. En la [guía 06](06-movimientos-basicos.md) medirás el error de seguimiento real: el margen debe cubrirlo.

> [!NOTE]
> **Corrección a la guía de 2015.** La guía 6 cambiaba el límite mínimo de 0 a −1 cm para absorber un "pequeño desfase negativo" al volver a 0. Ese desfase es error de seguimiento o sobreimpulso. Se diagnostica con la tendencia de posición comandada vs. real y se resuelve con sintonía y márgenes de diseño, no moviendo el límite después de que falla.

Descarga el proyecto antes de las pruebas siguientes.

## 2. Pruebas de conexión (*Hookup Tests*)

Primer contacto con cada motor. Se hacen **eje por eje**, con el motor sin carga.

| Prueba | Qué hace | Qué haces tú |
| --- | --- | --- |
| *Marker* | Busca el pulso de referencia del encoder | Gira el eje del motor a mano hasta que la prueba termine |
| *Motor Feedback* | Verifica que el encoder cuente | Gira a mano la distancia de prueba (usa una pequeña, por ejemplo 1 cm) |
| *Motor and Feedback* | El drive mueve el motor la distancia de prueba | Observa hacia dónde gira y responde si el movimiento fue en sentido positivo |

### Polaridad: el sentido positivo debe ser el mismo en el motor y en el gemelo

Antes de responder la última pregunta de la prueba, decide con el gemelo abierto **qué sentido de giro del motor corresponde al sentido positivo del eje en el gemelo** (por ejemplo, Y positivo = el cabezal se aleja del borde de la banda). Responde según ese criterio. El resultado queda en **Polarity** como *Normal* o *Inverted*.

> [!WARNING]
> Si la polaridad del eje no coincide con la del gemelo, el gemelo se moverá al revés que el servo real. Compruébalo en la [guía 07](07-gemelo-conectado-al-pac.md) con un movimiento corto y lento antes de cualquier secuencia.

## 3. Sintonía automática (*Autotune*)

**Axis Properties → Autotune**, con estos valores de partida (guía de 2015):

| Parámetro | Valor |
| --- | --- |
| Carga | *Uncoupled Motor* (motor sin carga acoplada) |
| Travel Limit | 5 cm |
| Speed | 10 cm/s |
| Torque | 100 % |
| Dirección | *Forward Bi-directional* |

1. Anota las ganancias actuales.
2. **Start**. Al terminar, compara *Current* contra *Tuned*: un asterisco marca los parámetros que cambian.
3. **Accept Tuned Values** y *OK*.
4. Repite para cada eje.

Cambiar *Application Type* (por ejemplo, de *Basic* a *Tracking*), *Loop Response* o el tipo de acople modifica qué ganancias se calculan (integrador de velocidad, *feedforward* de velocidad y de aceleración, filtro pasa-bajo de torque). Elige y justifica: X debe **seguir** a la banda con poco error.

> [!TIP]
> Relaciónalo con el Módulo 3 del curso: el *feedforward* de velocidad y aceleración reduce el error de seguimiento durante las rampas, que es justo lo que necesita un eje que sigue a otro.

## Evidencia

| Eje | Avance por rev. [cm] | Límites [cm] | Hookup | Polaridad | Ganancias antes → después |
| --- | --- | --- | --- | --- | --- |
| `Eje_Banda` | | — | | | |
| `Eje_X` | | | | | |
| `Eje_Y` | | | | | |

**Siguiente:** [Estados, paradas y fallas →](05-estados-paradas-y-fallas.md)
