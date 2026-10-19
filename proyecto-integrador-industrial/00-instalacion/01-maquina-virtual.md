# 01 · Máquina virtual

[← Instalación](README.md) · Siguiente: [Studio 5000, Logix Emulate y RSLinx →](02-studio5000-emulate-rslinx.md)

**Resultado:** la máquina virtual arranca y el programa base de la formadora está copiado en su carpeta de trabajo.

## 1. Descargar los archivos

Por el límite de almacenamiento de Google, la máquina virtual está dividida en **37 archivos** repartidos en dos carpetas compartidas en Classroom:

- Carpeta 1: `VM_DIGITAL-TWIN_WIN10X64.zip.001` a `.020`
- Carpeta 2: `VM_DIGITAL-TWIN_WIN10X64.zip.021` a `.037`

Descarga los 37 archivos en **una misma carpeta** de un disco con al menos 100 GB libres.

> [!TIP]
> Antes de descomprimir, verifica que estén los 37 archivos y que ninguno haya quedado como descarga parcial (`.crdownload` o tamaño 0). Un archivo incompleto hace fallar la descompresión al final del proceso.

## 2. Descomprimir con WinRAR

1. Ubica el primer archivo, `VM_DIGITAL-TWIN_WIN10X64.zip.001`. WinRAR debe reconocerlo como archivo comprimido.
2. Clic derecho → **Extraer en VM_DIGITAL-TWIN_WIN10X64\\**.
3. WinRAR toma automáticamente los archivos `.002` a `.037` hasta terminar. No abras ni muevas los archivos mientras tanto.

## 3. Instalar VMware Workstation Player

Usa **VMware Workstation Player 16.2.5** (`VMware-player-full-16.2.5-20904516.exe`, disponible en Classroom). Es la versión probada en semestres anteriores y ejecuta la máquina virtual sin inconvenientes en distintos computadores.

1. Ejecuta el instalador y avanza con **Next**.
2. Acepta los términos de licencia.
3. Marca las opciones de **controlador de teclado mejorado** y de **herramientas de consola** que ofrece el asistente.
4. Termina la instalación.
5. Al abrir el programa por primera vez, elige **uso gratuito no comercial**.

> [!NOTE]
> Broadcom publica versiones más recientes (VMware Workstation Pro 17 y 25H2) en su portal, que exige crear una cuenta (con el correo institucional) en [profile.broadcom.com](https://profile.broadcom.com/web/registration). **No se han probado con esta máquina virtual.** Si decides usarlas, documenta tu experiencia en un *issue* para el resto del curso. Guía de descarga de Broadcom: [artículo 397417](https://knowledge.broadcom.com/external/article/397417).

## 4. Abrir y configurar la máquina virtual

1. En VMware Player: **Open a Virtual Machine** → entra a la carpeta descomprimida → doble clic en `VM_DIGITAL-TWIN_WIN10X64.vmx`.
2. Aparece la máquina `VM_DIGITAL-TWIN_V32`. Antes de encenderla, entra a **Edit virtual machine settings**:

   | Parámetro | Valor sugerido |
   | --- | --- |
   | Memoria | La RAM física menos unos 2 GB (por ejemplo, 6 GB en un equipo de 8 GB; 12–14 GB en uno de 16 GB) |
   | Procesadores | La mitad de los núcleos físicos (mínimo 2) |
   | Adaptador de red | Déjalo como viene para la Parte 1. La Parte 2 lo cambia (ver [guía 07](../02-etiquetadora-de-cajas/07-gemelo-conectado-al-pac.md)) |

3. **Play virtual machine**.
4. Si aparece un mensaje informativo, continúa con **OK**.
5. Si pregunta si la máquina fue movida o copiada, responde **I Copied It**.
6. El primer arranque puede tardar varios minutos: primero una pantalla negra con el logo de Windows y luego el escritorio.

En el menú Inicio de la VM deben aparecer NX (Siemens), RSLinx Classic y OPC Test Client, Studio 5000 Logix Emulate y Studio 5000.

## 5. Copiar el programa base

1. Descarga de Classroom (carpeta *Proyecto Industrial*) el archivo `BOX_FORMING_LADDER_RS32_logixEmulate.ACD`.
2. Dentro de la VM, en **Documentos**, abre `BOX_FORMING_CPS_CONTROL_EMULATED`. Tiene dos subcarpetas:
   - `BOX_FORMING_DIGITAL_TWIN-NX-12_V0.5`: archivos de NX del gemelo.
   - `BOX_FORMING_LADDER -RS32_LogixEmulate`: inicialmente vacía.
3. Copia el `.ACD` en `BOX_FORMING_LADDER -RS32_LogixEmulate`. La VM admite copiar y pegar (o arrastrar) archivos desde el computador anfitrión.

```text
Documentos\
└── BOX_FORMING_CPS_CONTROL_EMULATED\
    ├── BOX_FORMING_DIGITAL_TWIN-NX-12_V0.5\
    │   └── 000 - CASE ERECTOR CYBER PHYSICAL SYSTEM   ← gemelo
    └── BOX_FORMING_LADDER -RS32_LogixEmulate\
        └── BOX_FORMING_LADDER_RS32_logixEmulate.ACD   ← programa base
```

> [!TIP]
> Guarda una copia sin modificar del `.ACD` base fuera de la VM. Si algo se daña, vuelves a empezar desde ahí sin descargar de nuevo.

**Siguiente:** [Studio 5000, Logix Emulate y RSLinx →](02-studio5000-emulate-rslinx.md)
