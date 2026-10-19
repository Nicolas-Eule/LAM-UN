# 04 · Problemas frecuentes

[← OPC DA y gemelo en NX MCD](03-opc-da-y-nx-mcd.md) · [Volver a Instalación](README.md)

Busca el síntoma y revisa las causas en orden: la primera suele ser la más probable.

| Síntoma | Causas probables | Qué hacer |
| --- | --- | --- |
| WinRAR falla al final de la descompresión | Falta una parte o alguna quedó incompleta | Verifica que estén las 37 partes con su tamaño completo; vuelve a descargar la que falle |
| VMware: *virtualization is not available* | Virtualización deshabilitada en BIOS, o Hyper-V/WSL ocupando el hipervisor | Habilita Intel VT-x / AMD-V en la BIOS. En Windows 11, prueba desactivando *Plataforma de máquina virtual* e *Hyper-V* |
| La VM arranca pero va muy lenta | Poca RAM o pocos núcleos asignados; disco mecánico | Ajusta memoria y procesadores (guía 01); cierra programas del anfitrión; usa un SSD si es posible |
| Studio 5000 no abre el `.ACD` o pide otra versión | Proyecto de una revisión distinta a la instalada | El archivo base es v32; usa el Studio 5000 v32 de la VM |
| *Who Active* no muestra el controlador emulado | Logix Emulate cerrado; driver Virtual Backplane no configurado | Abre Logix Emulate primero; revisa el driver en RSLinx (guía 02) |
| La descarga falla por revisión o slot | El controlador emulado no coincide con el proyecto | Recrea el Emulate 5570 con la revisión y el slot de *Controller Properties* |
| OPC Test Client no muestra tags | Topic `RS_LOGIX-OPC` apuntando a otro slot, o controlador en *Program* | Revisa *DDE/OPC → Topic Configuration*; pasa el controlador a *Remote Run* |
| Tags con calidad *Bad* | Controlador fuera de línea, o el topic apunta a un controlador sin ese tag | Verifica el path del topic y que el programa descargado sea el correcto |
| NX no abre MCD o falla la licencia | Sin conexión al servidor de licencias | `ping 168.176.36.140`; revisa la red de la VM y la conexión a la red de la universidad |
| El gemelo no se mueve aunque el PLC sí | Señales sin mapear o con sentido invertido | Repite *Break* y el mapeo en *Signal Mapping* (guía 03) |
| El gemelo se desincroniza: cajas que se acumulan o ejes que llegan tarde | Temporizador de aparición de cajas inconsistente con el ritmo de producción; perfiles demasiado justos; equipo sobrecargado | Ajusta el temporizador de `NX_Signals` (rung 4) al tiempo de ciclo + hasta 500 ms; revisa tus perfiles (Parte 1, guía 06) |
| El movimiento en el gemelo es "a saltos" | Actualización OPC más lenta que el movimiento; cuerpos rígidos con colisiones | Es normal en parte. Valida con Trends, que muestran lo que hace el controlador |

## Antes de pedir ayuda

Reúne esta información para que el monitor pueda reproducir el problema:

- Guía y paso donde ocurre.
- Captura del error completo.
- Estado del controlador (*Program*, *Remote Run*, fallas), el path del proyecto y el topic OPC.
- Qué cambiaste justo antes de que apareciera.

Si encontraste la solución a un problema nuevo, agrégala como *issue* para incluirla en esta tabla.
