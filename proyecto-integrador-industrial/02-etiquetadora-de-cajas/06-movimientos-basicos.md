# 06 · Movimientos básicos

[← Estados, paradas y fallas](05-estados-paradas-y-fallas.md) · Siguiente: [Gemelo digital conectado al PAC →](07-gemelo-conectado-al-pac.md)

**Al terminar:** mueves cada eje con jog, movimiento a posición y home; engranas dos ejes; y sabes leer en una tendencia la diferencia entre un perfil trapezoidal y uno S-curve.

*Basada en la guía de programación de movimiento II de 2015.* Programa en modo A o B; prueba en modo C a velocidad reducida.

## 1. Instrucciones

| Instrucción | Movimiento | Operandos clave | Termina cuando |
| --- | --- | --- | --- |
| **MAJ** · Motion Axis Jog | Velocidad constante, indefinido | Dirección (0 adelante, 1 atrás), Speed, Accel, Decel, Profile | Lo detiene un MAS (tipo *Jog*) o un MSF |
| **MAM** · Motion Axis Move | A una posición | Move Type (0 absoluto, 1 incremental), Position, Speed, Accel, Decel, Profile, Merge | Llega a la posición (`.PC`) |
| **MAH** · Motion Axis Home | Define o busca el origen | Usa la configuración *Homing* del eje | Home completo (`.PC`) |
| **MAS** · Motion Axis Stop | Detiene un tipo de movimiento | Stop Type: 0 todos, 1 jog, 2 move, 3 gear; Change Decel | Eje detenido (`.PC`) |
| **MAG** · Motion Axis Gear | El esclavo sigue al maestro con una relación | Slave, Master, Direction, Ratio, Master Reference, Clutch | Lo detiene un MAS (tipo *Gear*) |

Detalle completo en *Logix 5000 Controllers Motion Instructions* (MOTION-RM002), capítulo 3.

> [!TIP]
> Las instrucciones de movimiento se ejecutan en el **flanco de subida** del rung. Para cambiar la velocidad de un jog en curso, vuelve a ejecutar el MAJ con la nueva velocidad (por ejemplo, detectando el cambio con NEQ y generando un flanco).

## 2. Home con motores sin mecanismo

Los motores del laboratorio no tienen finales de carrera. En **Axis Properties → Homing** de cada eje usa *Mode* = *Active*, *Sequence* = *Immediate* y *Home Position* = 0: MAH toma la posición actual como origen, sin mover el eje. Antes de ejecutarlo, lleva el eje (y el gemelo) a la posición que quieres como cero.

## 3. Ejercicios

### 3.1 Jog de la banda

1. Rung con `Inicio_Operacion` → MAJ sobre `Eje_Banda` con `Mov_Banda.MAJ[0]`, dirección 0, velocidad baja (por ejemplo, 10 % del máximo), perfil trapezoidal.
2. Rung con `Servo_Off` → MAS tipo *Jog* sobre `Eje_Banda`.
3. Tendencia con `ActualVelocity` y `ActualPosition` de la banda.

### 3.2 Movimiento a posición del eje Y

1. MAM absoluto de `Eje_Y` a 10 cm, perfil **trapezoidal**. Captura la tendencia.
2. Mismo movimiento, perfil **S-curve**, *Jerk Units* = *% of Time* con 50 y con 100. Captura las tendencias.
3. Compara las tres: tiempo total, velocidad máxima y forma de la aceleración.

> [!NOTE]
> **Corrección a la guía de 2015.** Las guías 5 y 6 configuraban el *jerk* con perfil trapezoidal y explicaban que "100 % evita al máximo el jerk" y que "0 da un trapezoidal sin suavizado". Con perfil trapezoidal, Logix **ignora** los operandos de jerk; solo se usan con S-curve. Con *% of Time*, el jerk se expresa como porcentaje del tiempo de aceleración.

### 3.3 Error de seguimiento

Repite 3.2 en modo C con los servos reales y agrega a la tendencia la posición comandada, la real y el error de posición del eje (busca los miembros exactos del tag del eje en *Controller Tags*, como `CommandPosition`, `ActualPosition` y `PositionError`).

- ¿Cuál es el error máximo y en qué tramo del perfil ocurre?
- ¿Cambia al usar S-curve?
- ¿Cambia con otra *Loop Response* o *Application Type* (guía 04)?

En modo B (ejes virtuales) el error es cero: esa diferencia es exactamente lo que el gemelo no puede mostrarte si solo trabajas con ejes virtuales.

### 3.4 Engranaje electrónico

El engranaje electrónico simula un acople mecánico entre dos ejes: el **esclavo** sigue al **maestro** con una relación fija, sin detenerse.

1. Con la banda en jog lento, ejecuta MAG con esclavo `Eje_X`, maestro `Eje_Banda`, `Mov_X.MAG[0]`, *Ratio Format* = *Real*, *Ratio* = 1, *Master Reference* = *Actual*, *Clutch* = *Enabled*.
2. Observa en la tendencia las velocidades de ambos ejes.
3. Detén el engranaje con MAS tipo *Gear* sobre `Eje_X`.

Preguntas:

- Con *Ratio Format* = *Real*, la relación se expresa en unidades del esclavo por unidad del maestro. Si ambos ejes están escalados en cm de recorrido lineal, ¿qué relación iguala la velocidad del cabezal con la de la caja?
- ¿Qué cambia si *Master Reference* es *Command* en lugar de *Actual*? Piensa en el ruido de la medición y en el error de seguimiento del maestro.
- ¿Para qué sirve el *Clutch*? Compara el arranque del esclavo con y sin él.

## Evidencia

- [ ] Tendencias trapezoidal vs. S-curve (3.2) con el análisis.
- [ ] Tendencia de error de seguimiento en modo C (3.3).
- [ ] Tendencia del engranaje (3.4) y respuesta a las tres preguntas.

**Siguiente:** [Gemelo digital conectado al PAC →](07-gemelo-conectado-al-pac.md)
