# 00 · Instalación y uso del software

[← Proyecto Integrador Industrial](../README.md)

Al terminar esta sección tendrás la máquina virtual corriendo, el programa base de la formadora descargado al controlador emulado, sus tags visibles por OPC y el gemelo digital abierto en NX. Es la base de la Parte 1 y también de la conexión con el PAC físico en la Parte 2.

## Qué hay en la máquina virtual

La máquina virtual `VM_DIGITAL-TWIN_WIN10X64` (Windows 10 de 64 bits) trae instalado:

| Software | Versión | Función |
| --- | --- | --- |
| Studio 5000 Logix Designer | v32 | Programar el controlador en Ladder y ver tendencias (Trends) |
| Studio 5000 Logix Emulate | — | Emular un controlador ControlLogix 5570 con ejes virtuales |
| RSLinx Classic | — | Drivers de comunicación y servidor OPC DA (*RSLinx OPC Server*) |
| OPC Test Client | — | Verificar que los tags del controlador se publican por OPC |
| OPC Core Components | x86 y x64 | Librerías OPC DA para Windows 10 |
| Siemens NX Mechatronics Concept Designer | NX 12, modelo v0.5 | Gemelo digital de la formadora de cajas |

## Requisitos del computador

| Recurso | Mínimo | Recomendado |
| --- | --- | --- |
| Memoria RAM | 8 GB | 16 GB |
| Disco libre | 100 GB | 100 GB en SSD |
| Procesador | Intel Core i5 de 6.ª generación o equivalente | 4 núcleos o más |
| Sistema operativo | Windows 10 u 11 | — |
| BIOS/UEFI | Virtualización habilitada (Intel VT-x / AMD-V) | — |

> [!IMPORTANT]
> Si la máquina virtual no arranca o VMware indica que la virtualización no está disponible, revisa primero que esté habilitada en la BIOS del computador.

## Pasos

| # | Guía | Resultado |
| --- | --- | --- |
| 1 | [Máquina virtual](01-maquina-virtual.md) | La VM arranca y el archivo base `.ACD` está en su carpeta |
| 2 | [Studio 5000, Logix Emulate y RSLinx](02-studio5000-emulate-rslinx.md) | El programa base corre en el controlador emulado (*Remote Run*) |
| 3 | [OPC DA y gemelo en NX MCD](03-opc-da-y-nx-mcd.md) | Los tags se ven en OPC Test Client y el gemelo los recibe |
| 4 | [Problemas frecuentes](04-problemas-frecuentes.md) | Consulta cuando algo no funcione |

### Prueba de humo

Antes de pasar a la Parte 1, verifica las cinco condiciones:

- [ ] La VM arranca y muestra el escritorio de Windows.
- [ ] `BOX_FORMING_LADDER_RS32_logixEmulate.ACD` abre en Studio 5000 sin errores.
- [ ] El controlador emulado está en *Remote Run* con el programa base descargado.
- [ ] OPC Test Client muestra `Eje_X_Posicion_Actual`, `Eje_Y_Posicion_Actual` y `Eje_Z_Posicion_Actual` con calidad *Good*.
- [ ] NX abre `000 - CASE ERECTOR CYBER PHYSICAL SYSTEM` y la licencia responde.
