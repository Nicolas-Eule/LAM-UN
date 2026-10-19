# 01 · Seguridad y reglas de la estación

[← Parte 2](README.md) · Siguiente: [La máquina y la estación →](02-la-maquina-y-la-estacion.md)

**Al terminar:** sabes cómo se detiene la estación en cualquier situación y tienes firmada la lista de chequeo que habilita el modo C (servos energizados).

> [!WARNING]
> Lo primero que se diseña en una máquina es **cómo se detiene**. Ningún servomotor se energiza sin esta lista de chequeo completa y revisada por el monitor o el docente.

## Dos niveles de parada: no son lo mismo

| | Parada por programa | Seguridad funcional |
| --- | --- | --- |
| Quién la ejecuta | La lógica Ladder del PAC | Circuito cableado y función Safe Torque-Off (STO) del Kinetix 350 |
| Ejemplos | MAS, MGS, MGSD, MSF, un botón de parada leído por una entrada digital | Paro de emergencia que corta el par del motor sin pasar por el programa |
| Depende de | Que el programa, el PAC y la red funcionen | Solo del cableado y del drive |
| Sirve para | Detener la secuencia de forma ordenada | Proteger a las personas ante cualquier falla |

Las instrucciones MGS, MGSD, MSF y similares son **instrucciones de estado del eje y del grupo**. Las guías de 2015 las llamaban "bloques de seguridad"; son necesarias, pero no reemplazan el paro de emergencia cableado.

> [!IMPORTANT]
> Antes de la primera sesión, el monitor confirma con el ingeniero laboratorista cómo está cableado el paro de emergencia de la estación y si actúa sobre la entrada STO de los drives. Esa información se registra aquí: **[pendiente de completar por el monitor]**.

## Reglas de la estación

1. **Una persona opera.** Solo quien tiene el mando cambia el modo del PAC, habilita servos o activa movimientos. Anuncia en voz alta antes de hacerlo.
2. **Manos fuera.** Nadie toca ejes, acoples ni cables con los servos habilitados.
3. **Velocidad reducida primero.** Toda prueba nueva arranca a baja velocidad (por ejemplo, 10 % del máximo) y sube solo después de verla funcionar.
4. **Límites antes que movimiento.** Los *soft travel limits* de cada eje se configuran antes de la primera prueba de movimiento.
5. **El gemelo no es una parada.** Cerrar NX o perder la comunicación OPC no detiene los motores; para eso está la lógica de vigilancia de la [guía 07](07-gemelo-conectado-al-pac.md) y, por encima de todo, el paro de emergencia.
6. **Al terminar:** servos deshabilitados (MSF), PAC en *Program*, *Go Offline*, botonera en reposo.

## Puerta de seguridad: lista de chequeo para el modo C

Se completa en cada sesión, antes de energizar los servos.

| # | Verificación | ✓ |
| --- | --- | --- |
| 1 | PAC y drives asignados al equipo identificados (número de tablero e IP) | |
| 2 | Paro de emergencia probado: al pulsarlo, los drives quedan sin par | |
| 3 | Pulsador `Parada_Emergencia` de la botonera probado en el programa (MGS / MGSD) | |
| 4 | Ejes libres de obstáculos; acoples y cargas sujetos | |
| 5 | *Soft travel limits* configurados y revisados en cada eje | |
| 6 | Velocidades de prueba reducidas en todas las instrucciones nuevas | |
| 7 | Rutina de fallas (MAFR / MASR) programada y probada | |
| 8 | Si el gemelo puede mandar movimientos: vigilancia de comunicación activa y velocidad limitada (guía 07) | |
| 9 | Todo el equipo sabe dónde está el paro de emergencia | |

Equipo: ____________________ · Fecha: ____________ · Revisó: ____________________

**Siguiente:** [La máquina y la estación →](02-la-maquina-y-la-estacion.md)
