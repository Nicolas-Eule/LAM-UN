# 5 · Corrida con el gemelo digital

[← Completar Formado y Home](04-completar-formado-y-home.md) · Siguiente: [Validación y optimización →](06-validacion-y-optimizacion.md)

**Al terminar:** el gemelo forma cajas de forma continua, al ritmo que escogiste, movido por tu programa.

## 1. Ajustar la aparición de cajas al ritmo de producción

En `NX_Signals`, **rung 4**, un temporizador fija cada cuánto aparece una caja en el gemelo. Su preset está en **milisegundos** y debe ser coherente con tu tiempo unitario:

$$\text{Preset} \approx 1000\,t_u + \Delta, \qquad 0 < \Delta \le 500\ \text{ms}$$

El margen $\Delta$ absorbe el retardo de la comunicación OPC entre Studio 5000 y NX. Empieza con 500 ms y redúcelo mientras la simulación siga sincronizada.

| RP [cajas/min] | $t_u$ [s] | Preset de partida [ms] |
| --- | --- | --- |
| 10 | 6,0 | 6500 |
| 12 | 5,0 | 5500 |
| 15 | 4,0 | 4500 |
| 20 | 3,0 | 3500 |

> [!NOTE]
> Si las cajas aparecen más rápido de lo que la máquina las forma, se acumulan y el gemelo se desincroniza. Si aparecen mucho más lento, el ritmo medido será menor que el de diseño. El preset no reemplaza los perfiles: si el ciclo de los ejes dura más que $t_u$, el problema está en tus cálculos.

## 2. Orden de arranque

1. **Logix Emulate** abierto, con el controlador en su slot.
2. **RSLinx Classic** corriendo (driver Virtual Backplane y topic `RS_LOGIX-OPC`).
3. **Studio 5000**: descarga tu programa y pasa a *Remote Run*.
4. **OPC Test Client**: verifica las posiciones de X, Y, Z con calidad *Good*. Ciérralo después para no cargar el servidor.
5. **NX**: abre el gemelo, revisa *Signal Mapping* y pulsa **Play**.
6. **Studio 5000**: activa `START_ALL`.

La primera vez, sigue la configuración de señales de la [guía de instalación 03](../00-instalacion/03-opc-da-y-nx-mcd.md#3-abrir-el-gemelo-y-conectar-las-señales).

## 3. Qué observar

Durante los primeros ciclos, uno del equipo mira el gemelo y otro el programa en línea:

- [ ] La banda arranca y aparecen cajas al ritmo del temporizador.
- [ ] Con la caja, arrancan Y y Z; X arranca cuando Z termina.
- [ ] La caja queda sobre la banda y el brazo se repliega sin colisionar.
- [ ] Los tres ejes vuelven a Home y el ciclo siguiente arranca solo.
- [ ] El tag de etapa avanza E2 → E3 → E4 → E5 → condición principal, sin quedarse en ninguna.
- [ ] `STOP_ALL` detiene todo y el sistema puede volver a arrancar.

Agrega las señales de los ejes al **Runtime Inspector** de NX para ver sus valores mientras corre la simulación.

## 4. Si el gemelo se desincroniza

| Observación | Revisa |
| --- | --- |
| Cajas que se acumulan o se superponen | Preset del temporizador menor que la duración real del ciclo |
| El brazo llega a la banda antes o después que la caja | Reparto de tiempos entre Y y Z en la etapa 1.b |
| El movimiento se ve a saltos | Carga del computador; cierra programas y OPC Test Client |
| El gemelo se mueve distinto que las tendencias | Mapeo o unidades de las señales en NX; las tendencias muestran lo que hace el controlador |

El gemelo trata los cuerpos como rígidos y simula colisiones; con limitaciones de hardware o de comunicación puede perder fluidez. Lo que se evalúa es el **movimiento coordinado que genera tu programa**, validado con las tendencias. Las mejoras al gemelo son bienvenidas como propuesta, no como requisito.

**Siguiente:** [Validación y optimización →](06-validacion-y-optimizacion.md)
