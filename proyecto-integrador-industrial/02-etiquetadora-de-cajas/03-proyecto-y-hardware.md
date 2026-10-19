# 03 · Proyecto, E/S, drives y ejes en Studio 5000

[← La máquina y la estación](02-la-maquina-y-la-estacion.md) · Siguiente: [Puesta en marcha de los ejes →](04-puesta-en-marcha-de-ejes.md)

**Al terminar:** tienes un proyecto para el PAC de tu estación con las E/S, los tres drives, el grupo de movimiento y los tres ejes configurados, descargado y en línea.

*Basada en las guías de configuración HW/SW I y II de 2015.*

## 1. Crear el proyecto

1. Studio 5000 → **New Project**.
2. Controlador: **CompactLogix 5370 → 1769-L30ERM**.
3. **Revision:** la del firmware del PAC de tu estación. Pregúntala al monitor o léela en línea con *Who Active*.
4. **Security Authority:** *No Protection*.
5. **Description:** nombre de la máquina, equipo, integrantes y fecha. Un proyecto sin descripción es un proyecto que nadie más podrá mantener.

> [!IMPORTANT]
> Un proyecto solo se descarga a un controlador con la **misma revisión mayor**. Si la versión de Studio 5000 del computador no coincide con el firmware del PAC, no actualices firmware por tu cuenta: avísale al monitor.

## 2. Sincronización de tiempo

El control de movimiento integrado sobre EtherNet/IP necesita que el PAC y los drives compartan la misma base de tiempo; el PAC actúa como "director de orquesta".

**Controller Properties → Date/Time →** marca **Enable Time Synchronization** → *OK*.

## 3. Ruta de comunicación

1. Clic en el cuadro de ruta (**Who Active**).
2. Expande el driver EtherNet/IP del laboratorio (en la guía de 2023: `ETHIP-1`).
3. Verás los PAC, las HMI y los drives de la red. Selecciona la IP del PAC de tu estación.
4. **Set Project Path**. El campo *Path in Project* debe mostrar la ruta a esa IP.

Una X roja sobre un dispositivo en *Who Active* indica que no está conectado o no responde.

## 4. Módulos de entradas y salidas

En **I/O Configuration → 1769 Bus**, clic derecho → **New Module** (filtros: *Digital*, *Allen-Bradley*):

| Módulo | Catálogo | Slot | Nombre sugerido |
| --- | --- | --- | --- |
| Entradas digitales | 1769-IQ16 | 4 | `Entradas_Digitales` |
| Salidas digitales | 1769-OW8 | 5 | `Salidas_Digitales` |

Cuenta los slots de izquierda a derecha sin contar la fuente, y confirma la referencia bajo la tapa de cada módulo. Después crea los tags alias del [mapa de E/S](02-la-maquina-y-la-estacion.md#mapa-de-entradas-y-salidas).

## 5. Drives Kinetix 350

1. Verifica que los tres drives estén energizados y sin falla: su display muestra la IP desplazándose.
2. Confirma en *Who Active* que aparecen en la red.
3. En **I/O Configuration → Ethernet**, clic derecho → **New Module** (filtros: *Motion*, *Allen-Bradley*) → **2097-V31PR2-LM**.
4. Configura uno por eje:

   | Nombre | Eje | IP |
   | --- | --- | --- |
   | `Drive_Banda` | Rotacional | La del display del drive |
   | `Drive_X` | X | |
   | `Drive_Y` | Y | |

## 6. Grupo de movimiento

**Motion Groups** → clic derecho → **New Motion Group**. Nombre (por ejemplo `Grupo_Etiquetadora`), descripción de los ejes que agrupa y *External Access* en **Read/Write**.

## 7. Ejes

### Modo C: ejes con drive

En el grupo, clic derecho → **New Axis → AXIS_CIP_DRIVE**. Usa estos nombres: son los que espera el contrato de señales con el gemelo.

| Eje | Nombre | Drive asociado |
| --- | --- | --- |
| Rotacional (banda) | `Eje_Banda` | `Drive_Banda` |
| X | `Eje_X` | `Drive_X` |
| Y | `Eje_Y` | `Drive_Y` |

En **Axis Properties** de cada eje:

| Categoría | Parámetro | Valor | Por qué |
| --- | --- | --- | --- |
| General | Axis Configuration | *Position Loop* | Los tres ejes se controlan en posición (la banda también, aunque se mueva con MAJ) |
| General | Feedback Configuration | *Motor Feedback* | La realimentación es el encoder del motor |
| General | Application Type | *Basic* | Punto de partida; se revisa en la sintonía |
| General | Loop Response | *Medium* | Punto de partida; se revisa en la sintonía |
| General | Motion Group | `Grupo_Etiquetadora` | |
| Associated Module | Module | El drive del eje | El Kinetix 350 maneja un solo eje |
| Motor | Data Source | *Catalog Number* | |
| Motor | Catalog Number | **MPL-A230P-Hxx2** | Es la entrada del catálogo que corresponde al motor MPL-A230P-HJ72AA |

El escalado, los límites y la sintonía se configuran en la [guía 04](04-puesta-en-marcha-de-ejes.md).

### Modos A y B: ejes virtuales

Para probar sin motores, crea los mismos tres nombres como **AXIS_VIRTUAL** en el grupo. Un eje virtual sigue exactamente lo que se le ordena, sin error de seguimiento ni dinámica.

Mantén dos variantes del proyecto (ejes virtuales y ejes con drive) y lleva la lógica entre ellas exportando las rutinas a **`.L5X`** (clic derecho sobre la rutina → *Export*). Como los nombres de ejes y tags son iguales, las rutinas se importan sin cambios.

## 8. Descargar y poner en línea

1. **Go Online → Download**. La primera vez aparece una advertencia porque el programa del PAC va a ser reemplazado; confirma solo si estás en el PAC correcto.
2. Pasa a **Remote Run** y comprueba en la barra de estado *Run Mode* y *Controller OK*.
3. En **Motion Groups**, revisa que los tres ejes no tengan fallas.
4. Al terminar la sesión: *Remote Program* → **Go Offline**.

> [!NOTE]
> En un controlador solo corre un proyecto a la vez. Al descargar el tuyo se reemplaza el anterior; por eso cada equipo trabaja únicamente en el PAC que tiene asignado.

## Evidencia

- [ ] Captura del árbol del proyecto con E/S, drives, grupo y ejes.
- [ ] Captura de *Who Active* con el PAC y los tres drives.
- [ ] Proyecto descargado en *Remote Run* y sin fallas de eje.

**Siguiente:** [Puesta en marcha de los ejes →](04-puesta-en-marcha-de-ejes.md)
