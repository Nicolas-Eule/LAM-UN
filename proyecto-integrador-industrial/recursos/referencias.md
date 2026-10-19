# Referencias y material original

[← Proyecto Integrador Industrial](../README.md)

## Material del curso (Classroom)

Estos documentos son la base de las guías de este repositorio. Se distribuyen por Google Classroom.

| Documento | Autores | Usado en |
| --- | --- | --- |
| *Proyecto Industrial de la Asignatura v2026-2S: Programación de Control de Movimiento Industrial* | V. H. Grisales Palacio | [Entregables y evaluación](../entregables-y-evaluacion.md) |
| *Programa de la Asignatura Servomecanismos v2026-2S* | V. H. Grisales Palacio | Cronograma |
| *Guía de Box Forming Motion Control Project* (actualización junio 2023) | H. Forero Correa, V. H. Grisales Palacio | Parte 1 e instalación |
| *Recomendaciones Proyecto Industrial Servomecanismos v25-2S* | V. H. Grisales Palacio | Instalación y Parte 1 |
| *Guía de comunicación Logix Emulate con Studio 5000* (v32) | Laboratorio de Automatización de Máquinas | Instalación |
| *Guías para Control de Movimiento de Servomecanismos usando la Plataforma Industrial CompactLogix de Allen Bradley*, guías 0 a 6 (2015) | E. H. Sepúlveda Oviedo, D. A. Sáenz Ardila, K. A. Pulido, V. H. Grisales Palacio | Parte 2 |

### Correspondencia con las guías de 2015

| Guía 2015 | Contenido | Guía de este repositorio |
| --- | --- | --- |
| 0 · Presentación general | Arquitectura, PAC, Studio 5000, red del laboratorio | [Parte 2 · 02](../02-etiquetadora-de-cajas/02-la-maquina-y-la-estacion.md) |
| 1 · Configuración HW/SW I | Proyecto, CPU, red, módulos de E/S | [Parte 2 · 03](../02-etiquetadora-de-cajas/03-proyecto-y-hardware.md) |
| 2 · Configuración HW/SW II | Drives, grupo de movimiento, ejes, descarga | [Parte 2 · 03](../02-etiquetadora-de-cajas/03-proyecto-y-hardware.md) |
| 3 · Configuración HW/SW III | Escalado, hookup, polaridad, autotune | [Parte 2 · 04](../02-etiquetadora-de-cajas/04-puesta-en-marcha-de-ejes.md) |
| 4 · Programación de movimiento I | Lenguajes, tags, instrucciones de estado y parada | [Parte 2 · 05](../02-etiquetadora-de-cajas/05-estados-paradas-y-fallas.md) |
| 5 · Programación de movimiento II | UDT, MAS, MAH, MAJ, MAM, MAG | [Parte 2 · 06](../02-etiquetadora-de-cajas/06-movimientos-basicos.md) |
| 6 · Programación de movimiento III | Secuenciador, engranaje, ventana de pegante | [Parte 2 · 08](../02-etiquetadora-de-cajas/08-secuencia-coordinada.md) |

### Correcciones aplicadas al material original

| Origen | Corrección | Dónde |
| --- | --- | --- |
| Guía 2023, ec. 12 | El término $(V_{max}/a)^2$ debe ser $V_{max}^2/a$ | [Parte 1 · 02](../01-formadora-de-cajas/02-perfiles-trapezoidales.md) |
| Guía 2015-3 | Escalado "1 cm por revolución" sin base mecánica; ahora sale de la transmisión | [Parte 2 · 04](../02-etiquetadora-de-cajas/04-puesta-en-marcha-de-ejes.md) |
| Guía 2015-4 | MGS, MGSD, MSO… son instrucciones de estado, no de seguridad funcional | [Parte 2 · 01](../02-etiquetadora-de-cajas/01-seguridad-y-reglas.md) |
| Guía 2015-5 | MAS con *Change Decel* = No usa la desaceleración máxima del eje, no para en seco | [Parte 2 · 05](../02-etiquetadora-de-cajas/05-estados-paradas-y-fallas.md) |
| Guía 2015-5 | Habilitar el servo y arrancar un jog con el mismo pulsador | [Parte 2 · 05](../02-etiquetadora-de-cajas/05-estados-paradas-y-fallas.md) |
| Guías 2015-5 y 6 | El jerk se ignora con perfil trapezoidal | [Parte 2 · 06](../02-etiquetadora-de-cajas/06-movimientos-basicos.md) |
| Guía 2015-6 | `MOTION_INSTRUCTION[2]` tiene 2 elementos, no 3 | [Parte 2 · 05](../02-etiquetadora-de-cajas/05-estados-paradas-y-fallas.md) |
| Guía 2015-6 | Relación de engranaje 2 no sigue a la caja; con ejes en cm es 1 | [Parte 2 · 08](../02-etiquetadora-de-cajas/08-secuencia-coordinada.md) |
| Guía 2015-6 | Límite blando movido a −1 cm sin diagnosticar el error de seguimiento | [Parte 2 · 04](../02-etiquetadora-de-cajas/04-puesta-en-marcha-de-ejes.md) |
| Guía 2015-4 | La lista de instrucciones (IL) fue declarada obsoleta en la IEC 61131-3 ed. 3 (2013) y retirada en la ed. 4 (2025) | Este documento |

## Manuales del fabricante

- *Logix 5000 Controllers Motion Instructions*, Rockwell Automation, MOTION-RM002 (capítulo 3: MAS, MAH, MAJ, MAM). Disponible en Classroom y en [Rockwell Literature Library](https://literature.rockwellautomation.com).
- Documentación en línea de las instrucciones de Studio 5000 Logix Designer: [MAM](https://www.rockwellautomation.com/en-dk/docs/studio-5000-logix-designer/38-00/contents-ditamap/instruction-set/instructions/motion-axis-move--mam-.html) · [MAJ](https://www.rockwellautomation.com/en-hu/docs/studio-5000-logix-designer/37-00/contents-ditamap/instruction-set/instructions/motion-move-instructions/motion-axis-jog--maj-.html) · [MAS](https://www.rockwellautomation.com/en-fi/docs/studio-5000-logix-designer/37-00/contents-ditamap/instruction-set/instructions/motion-move-instructions/motion-axis-stop--mas-.html)
- *Integrated Motion on the EtherNet/IP Network: Configuration and Startup*, Rockwell Automation, MOTION-UM003.
- [Ficha del controlador 1769-L30ERM](https://www.rockwellautomation.com/en-us/products/details.1769-L30ERM.html), Rockwell Automation.

## Normas

- IEC 61131-3:2025, *Programmable controllers – Part 3: Programming languages* (edición 4).
- [PLCopen: IEC 61131-3](https://plcopen.org/iec-61131-3).

## Bibliografía del curso sobre control de movimiento

- Gurocak, H. *Industrial Motion Control: Motor Selection, Drives, Controller Tuning, Applications*. Wiley, 2015.
- Ellis, G. *Control System Design Guide*, 4.ª ed. Elsevier, 2012.
- Kirckof, G. *Servomotor Sizing and Application*. ISA, 2012.
- Moritz, F. G. *Electromechanical Motion Systems: Design and Simulation*. Wiley, 2014.
