# 4 · Completar las rutinas de Formado y Home

[← Programa base y Grafcet](03-programa-base-y-grafcet.md) · Siguiente: [Corrida con el gemelo →](05-corrida-con-el-gemelo.md)

**Al terminar:** `B_Process_Formado` y `C_Process_Home` ejecutan el ciclo completo con los perfiles que calculaste, y la secuencia avanza sola de E2 a E5.

Esta guía describe **qué** debe hacer cada rung y **cómo** se parametrizan los bloques. La lógica concreta la diseña el equipo; en el informe deben poder explicar cada rung.

## Instrucciones que vas a usar

| Instrucción | Para qué | Bits de estado útiles |
| --- | --- | --- |
| **MAM** · Motion Axis Move | Mover un eje a una posición con un perfil definido | `.IP` en proceso · `.PC` movimiento completo · `.ER` error |
| **MAS** · Motion Axis Stop | Detener de forma controlada un tipo de movimiento del eje | `.PC` parada completa · `.ER` error |
| XIC, OTE, OTL, OTU | Condiciones, bobinas, enclavar y desenclavar bits de etapa | — |

> [!IMPORTANT]
> Las instrucciones de movimiento son **transicionales**: se ejecutan cuando la condición del rung pasa de falso a verdadero. Si el rung se queda en verdadero, la instrucción no se vuelve a ejecutar en el ciclo siguiente. Por eso Process Reset desenergiza las etapas al final de cada ciclo: sin ese flanco, la segunda caja nunca arrancaría.

## Parámetros del MAM

| Operando | Valor en este proyecto | Comentario |
| --- | --- | --- |
| Axis | `Eje_X`, `Eje_Y` o `Eje_Z` | El eje del proyecto base |
| Motion Control | `Eje_Y.MAM[0]` en Formado, `[1]` en Home | Un tag distinto por bloque |
| Move Type | `0` absoluto | Las posiciones de la tabla de etapas son absolutas |
| Position | Posición destino | En las unidades del eje (*Scaling*) |
| Speed / Speed Units | $V_{max}$ / *Units per sec* | De tu tabla de perfiles |
| Accel Rate, Decel Rate / Units | $a$ / *Units per sec²* | Igual en ambos para un perfil simétrico |
| Profile | *Trapezoidal* | |
| Accel Jerk, Decel Jerk, Jerk Units | Cualquier valor válido | Solo se usan con *S-curve*; el bloque exige llenarlos |
| Merge / Merge Speed | *Disabled* / *Programmed* | Sin fusión de movimientos |
| Lock Position, Lock Direction, Event Distance, Calculated Data | `0`, *None*, `0`, `0` | No se usan aquí |

Referencia completa: *Logix 5000 Controllers Motion Instructions* (MOTION-RM002), capítulo 3.

## Parámetros del MAS

| Operando | Valor | Comentario |
| --- | --- | --- |
| Stop Type | *Move* | Detiene el movimiento iniciado por MAM |
| Change Decel | *No* o *Yes* | Con *No* usa la desaceleración máxima configurada en el eje; con *Yes* usa la que indiques |
| Decel Rate / Units | Si Change Decel = *Yes* | |

## Rutina `B_Process_Formado`

Organízala en rungs cortos, uno por acción, siguiendo el Grafcet:

| # | Condición | Acción | Resultado |
| --- | --- | --- | --- |
| 1 | Etapa E2 activa | MAM de **Z** a 90° y MAM de **Y** hasta el final de la guía | Arrancan Y y Z |
| 2 | E2 activa y MAM de Z completo (`.PC`) | Cumplir C2 y activar E3 | Se habilita el giro de X |
| 3 | Etapa E3 activa | MAM de **X** a 90° | X gira mientras Y sigue |
| 4 | E3 activa y los tres MAM completos | MAS de X, Y y Z | Frenado controlado |
| 5 | Los tres MAS completos | Activar las bobinas `Eje_X.MAS`, `Eje_Y.MAS`, `Eje_Z.MAS` | Se cumple C3 y pasa a Home |

Patrón de un rung de movimiento (los nombres entre `< >` son los bits que identificaste en la guía 3):

```text
      <Etapa E2>                               +-MAM------------------------+
|-------] [------------------------------------+ Axis           Eje_Z       +-|
|                                              | Motion Control Eje_Z.MAM[0]|
|                                              | Move Type      0           |
|                                              | Position       <90° en unidades del eje>
|                                              | Speed          <Vmax>      |
|                                              | Accel / Decel  <a> / <a>   |
|                                              | Profile        Trapezoidal |
|                                              +----------------------------+
```

## Rutina `C_Process_Home`

| # | Condición | Acción |
| --- | --- | --- |
| 1 | Etapa E4 activa | MAM de X, Y y Z a la posición 0, con índice `[1]` |
| 2 | E4 activa y los tres MAM de Home completos | MAS de los tres ejes, con índice `[1]` |
| 3 | Los tres MAS completos | Bobinas `Eje_X.MAS`, `Eje_Y.MAS`, `Eje_Z.MAS`; se cumple C4 |

El retorno simultáneo es la primera opción. Si propones otra secuencia de retorno (por ejemplo, X y Z primero para liberar espacio, o un retorno más rápido de Y), dibújala en el Grafcet antes de programarla.

## Probar por partes

No esperes a tener todo para probar. En *Remote Run*, con el gemelo detenido:

1. Programa solo el rung 1 de Formado. Fuerza la etapa E2 y mira en *Controller Tags* que `Eje_Y.MAM[0].IP` y luego `.PC` se activen.
2. Abre la tendencia y compara el perfil de velocidad con el que calculaste.
3. Agrega el rung siguiente y repite.

## Errores frecuentes

| Síntoma | Causa probable |
| --- | --- |
| El MAM no hace nada y `.ER` se activa | Velocidad o aceleración por encima del límite del eje, o eje no habilitado. Revisa el código de error en el tag de la instrucción |
| El primer ciclo funciona y el segundo no arranca | El rung del MAM nunca volvió a falso: revisa el reinicio de etapas en Process Reset |
| La secuencia salta etapas | Dos bloques comparten tag de instrucción, o una condición usa `.IP` en lugar de `.PC` |
| Y llega a L1 antes o después de que Z termine | Tiempos de Y y Z inconsistentes en tu tabla de perfiles |
| Posición final con un pequeño error | Normal en el emulador; si es grande, revisa unidades y tipo de movimiento (absoluto o incremental) |

**Siguiente:** [Corrida con el gemelo →](05-corrida-con-el-gemelo.md)
