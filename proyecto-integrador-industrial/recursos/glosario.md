# Glosario

[← Proyecto Integrador Industrial](../README.md)

| Término | Significado |
| --- | --- |
| **PAC** | *Programmable Automation Controller*. Controlador industrial que combina la robustez de un PLC con capacidades de cómputo y comunicación; aquí, el CompactLogix 1769-L30ERM |
| **Studio 5000 Logix Designer** | Software de Rockwell Automation para configurar y programar controladores Logix |
| **Logix Emulate** | Emulador de un controlador Logix (5570) en el PC; permite ejecutar el programa sin hardware |
| **RSLinx Classic** | Software de comunicaciones de Rockwell: drivers de red y servidor OPC DA |
| **OPC DA** | *Open Platform Communications – Data Access*. Estándar cliente–servidor para leer y escribir datos de proceso entre aplicaciones en Windows |
| **Topic (RSLinx)** | Nombre con el que RSLinx publica por OPC los tags de un controlador específico |
| **NX MCD** | *Mechatronics Concept Designer*, módulo de Siemens NX para simular máquinas con física, sensores, actuadores y señales |
| **Gemelo digital** | Modelo virtual de la máquina que se comporta como ella y se conecta al controlador real o emulado |
| **Sistema ciberfísico** | Integración de control, cómputo y proceso físico (real o simulado) acoplados por comunicaciones |
| **Grafcet** | Método gráfico para especificar automatismos secuenciales con etapas y transiciones (IEC 60848) |
| **SFC** | *Sequential Function Chart*, lenguaje de la IEC 61131-3 derivado del Grafcet |
| **Ladder (LD)** | Lenguaje gráfico de contactos y bobinas de la IEC 61131-3 |
| **Tag** | Variable con nombre en un controlador Logix |
| **UDT** | Tipo de dato definido por el usuario: una estructura de tags |
| **MOTION_INSTRUCTION** | Tipo de dato que guarda el estado de una instrucción de movimiento (`.EN`, `.DN`, `.ER`, `.IP`, `.PC`) |
| **Eje virtual** (`AXIS_VIRTUAL`) | Eje sin drive ni motor; sigue exactamente la trayectoria comandada |
| **Eje CIP** (`AXIS_CIP_DRIVE`) | Eje asociado a un drive con movimiento integrado sobre EtherNet/IP |
| **Grupo de movimiento** | Conjunto de ejes que el controlador planifica con la misma base de tiempo |
| **Perfil trapezoidal** | Perfil de velocidad con aceleración constante, crucero y desaceleración constante |
| **Perfil S-curve** | Perfil con jerk limitado: la aceleración cambia gradualmente |
| **Jerk** | Derivada de la aceleración respecto al tiempo |
| **Engranaje electrónico** | Relación fija programada entre la posición de un eje esclavo y la de un maestro (MAG) |
| **Embrague** (*clutch*) | Opción de MAG que lleva el esclavo a la velocidad del maestro con una aceleración definida |
| **Error de seguimiento** | Diferencia entre la posición comandada y la real de un eje |
| **Hookup tests** | Pruebas de conexión de motor y encoder en Studio 5000 |
| **Autotune** | Sintonía automática de las ganancias de los lazos del eje |
| **STO** | *Safe Torque-Off*. Función de seguridad del drive que quita el par del motor por hardware |
| **Soft travel limits** | Límites de recorrido de un eje verificados por el controlador |
| **Ritmo de producción (RP)** | Cajas por minuto que produce la máquina |
| **Tiempo unitario ($t_u$)** | Tiempo para producir una caja: $t_u = 60/RP$ s |
| **L5X** | Formato de exportación de Studio 5000 en XML; útil para versionar rutinas |
