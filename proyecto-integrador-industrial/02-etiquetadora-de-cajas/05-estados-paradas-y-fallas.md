# 05 · Estados, paradas y fallas

[← Puesta en marcha de los ejes](04-puesta-en-marcha-de-ejes.md) · Siguiente: [Movimientos básicos →](06-movimientos-basicos.md)

**Al terminar:** tu programa habilita y deshabilita los servos, detiene el grupo de ejes de tres maneras distintas, recupera los ejes de una falla, y sabes predecir y medir qué hace cada eje en cada caso.

*Basada en la guía de programación de movimiento I de 2015.* Se programa en modo A o B y se prueba en modo C.

## 1. Estructura de tags de instrucción

Cada instrucción de movimiento necesita su propio tag `MOTION_INSTRUCTION`. En lugar de crear decenas de tags sueltos, crea un tipo de dato definido por el usuario (*Data Types → User-Defined → New Data Type*):

**`UDT_Mov_Eje`**

| Miembro | Tipo | Uso |
| --- | --- | --- |
| `MSO` | MOTION_INSTRUCTION | Habilitar servo |
| `MSF` | MOTION_INSTRUCTION | Deshabilitar servo |
| `MAFR` | MOTION_INSTRUCTION | Borrar fallas del eje |
| `MASR` | MOTION_INSTRUCTION | Salir del estado *shutdown* |
| `MAH` | MOTION_INSTRUCTION | Home |
| `MAJ` | MOTION_INSTRUCTION[2] | Jog (índice 0: secuencia, 1: mando desde el gemelo) |
| `MAM` | MOTION_INSTRUCTION[4] | Movimientos a posición |
| `MAS` | MOTION_INSTRUCTION[4] | Paradas de eje |
| `MAG` | MOTION_INSTRUCTION[2] | Engranaje electrónico |

**`UDT_Mov_Grupo`**: `MGS`, `MGSD` y `MGSR`, cada uno `MOTION_INSTRUCTION`.

Crea los tags `Mov_Banda`, `Mov_X` y `Mov_Y` (tipo `UDT_Mov_Eje`) y `Mov_Grupo` (tipo `UDT_Mov_Grupo`). Así, el MSO del eje X usa `Mov_X.MSO` y el primer MAM del eje Y usa `Mov_Y.MAM[0]`.

> [!NOTE]
> **Corrección a la guía de 2015.** Allí se decía que `MOTION_INSTRUCTION[2]` "crea 3 etiquetas". Un arreglo de dimensión 2 tiene **2** elementos, con índices 0 y 1.

## 2. Las instrucciones

| Instrucción | Qué hace | Detalle que importa |
| --- | --- | --- |
| **MSO** · Motion Servo On | Habilita el drive y cierra el lazo de servo | No mueve el eje. Debe ejecutarse antes de cualquier movimiento |
| **MSF** · Motion Servo Off | Deshabilita el drive y abre el lazo | El controlador sigue leyendo la posición. Un eje en movimiento queda sin par: sin freno mecánico, sigue girando hasta detenerse por fricción |
| **MAFR** · Motion Axis Fault Reset | Borra las fallas del eje | No recupera nada: si la causa sigue, la falla vuelve |
| **MASR** · Motion Axis Shutdown Reset | Saca el eje del estado *shutdown* | |
| **MGS** · Motion Group Stop | Detiene todos los ejes del grupo | Modo *Programmed*: cada eje con su método configurado. *Fast Stop*: desaceleración máxima, servo activo. *Fast Disable*: desaceleración máxima y luego servo deshabilitado |
| **MGSD** · Motion Group Shutdown | Lleva todos los ejes del grupo a *shutdown* | |
| **MGSR** · Motion Group Shutdown Reset | Saca el grupo de *shutdown* | |

## 3. Lógica mínima de estados y paradas

| Rung | Condición | Acción |
| --- | --- | --- |
| 1 | `STOP_ALL` **o** pulsador `Parada_Emergencia` accionado | MGS (*Fast Stop*) y MGSD sobre el grupo; enciende `Testigo_Parada` |
| 2 | `START_ALL` y parada no accionada | MGSR; enciende `Testigo` con enclavamiento |
| 3 | `Reset_Fallas` | MAFR y MASR de cada eje |
| 4 | `Servo_On` y grupo sin parada | MSO de los tres ejes (tres ramas en paralelo) |
| 5 | `Servo_Off` | MAS de cada eje y luego MSF de los tres |

El pulsador de parada de la botonera es **normalmente cerrado**: en reposo la entrada vale 1 y al pulsarlo vale 0. Por eso en el rung 1 se examina con XIO (contacto cerrado). Así, un cable cortado también detiene la máquina.

`STOP_ALL`, `START_ALL` y `Reset_Fallas` son tags internos `BOOL` que puedes accionar desde Studio 5000 (**Toggle Bit**, `Ctrl+T`) o desde el gemelo.

> [!NOTE]
> **Corrección a la guía de 2015.** La guía 5 usaba el pulsador `Servo_On` para ejecutar MSO **y** arrancar un jog al 25 %. Habilitar y mover con el mismo pulsador hace que el eje arranque en el instante en que se energiza. Aquí habilitar y mover son órdenes separadas, y todo movimiento exige `Eje_X.ServoActionStatus = 1`.

## 4. Predecir, observar, explicar

Arranca la banda con un jog lento (guía 06) o, para esta prueba, con un MAJ de prueba a velocidad conocida $v$. Antes de cada prueba, escribe tu predicción.

| Prueba | Predicción: ¿qué hace la banda? | Observado | Distancia de frenado medida [cm] |
| --- | --- | --- | --- |
| MGS *Programmed* | | | |
| MGS *Fast Stop* | | | |
| MGS *Fast Disable* | | | |
| MSF con el eje en movimiento | | | |
| MAS con *Change Decel* = *No* | | | |
| MAS con *Change Decel* = *Yes* y desaceleración $a$ | | | |
| Pulsador de paro de emergencia (hardware) | | | |

Para una desaceleración constante $a$, la distancia de frenado esperada es:

$$d = \frac{v^2}{2a}$$

Compárala con la medida en la tendencia.

> [!NOTE]
> **Corrección a la guía de 2015.** La guía 5 decía que, sin tasa de desaceleración, el motor "se detendrá en el momento". Con *Change Decel* = *No*, MAS usa la **desaceleración máxima configurada del eje**: no es una parada instantánea.

## 5. Fallas inyectadas

Con el monitor, provoca y resuelve:

1. Una falla de eje (por ejemplo, un movimiento fuera de los *soft limits*). ¿Qué bits cambian? ¿Basta MAFR?
2. Un *shutdown* de grupo con MGSD. ¿Qué secuencia exacta lo recupera?
3. Desconexión de la comunicación con el gemelo con la banda en movimiento (en modo B). ¿Qué hace tu programa? (Lo resuelve la vigilancia de la [guía 07](07-gemelo-conectado-al-pac.md).)

## Evidencia

- [ ] Captura de los UDT y de los rungs 1 a 5.
- [ ] Tabla de predicción vs. observado con distancias de frenado.
- [ ] Secuencia de recuperación de una falla y de un *shutdown*.

**Siguiente:** [Movimientos básicos →](06-movimientos-basicos.md)
