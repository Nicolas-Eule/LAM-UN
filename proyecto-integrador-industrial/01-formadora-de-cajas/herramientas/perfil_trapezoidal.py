#!/usr/bin/env python3
"""
Verificador de perfiles de velocidad trapezoidales simétricos.

Uso típico: primero haz el cálculo a mano (es lo que se evalúa en el informe)
y luego usa este script para comprobar los números y graficar el perfil.

Un segmento se define por su recorrido L y su duración t, más UNA de estas
condiciones de diseño:
    --t1    tiempo de aceleración (= tiempo de desaceleración)
    --frac  fracción t1/t (por ejemplo 0.3333 para el perfil 1/3-1/3-1/3)
    --a     aceleración (= desaceleración)
    --vmax  velocidad crucero

Las unidades son las del eje en Studio 5000 (Axis Properties > Scaling >
Position Units). Si el eje está en grados, L va en grados; si está en mm, en mm.

Ejemplos:
    python perfil_trapezoidal.py --L 1500 --t 1.25 --frac 0.3333
    python perfil_trapezoidal.py --L 90 --t 1.0 --a 500 --plot perfil_z.png
    python perfil_trapezoidal.py --rp 12
"""

from __future__ import annotations

import argparse
import math
import sys
from dataclasses import dataclass


@dataclass
class Perfil:
    L: float      # recorrido
    t: float      # duración total
    t1: float     # tiempo de aceleración (= desaceleración)
    t2: float     # tiempo de crucero
    a: float      # aceleración
    vmax: float   # velocidad crucero

    @property
    def triangular(self) -> bool:
        return self.t2 <= 1e-12


def desde_t1(L: float, t: float, t1: float) -> Perfil:
    """L = a*t1*(t - t1)  ->  a = L / (t1*(t - t1)),  Vmax = a*t1."""
    if not 0 < t1 <= t / 2:
        raise ValueError(f"t1 debe cumplir 0 < t1 <= t/2 = {t / 2:.6g} s (t1 = {t1:.6g} s)")
    a = L / (t1 * (t - t1))
    return Perfil(L, t, t1, t - 2 * t1, a, a * t1)


def desde_a(L: float, t: float, a: float) -> Perfil:
    """Vmax = (a/2) * (t - sqrt(t^2 - 4L/a)), con a >= 4L/t^2 (rama de menor Vmax)."""
    a_min = 4 * L / t**2
    if a < a_min * (1 - 1e-12):
        raise ValueError(
            f"Aceleración insuficiente: a = {a:.6g} < 4L/t^2 = {a_min:.6g}. "
            "No existe perfil que recorra L en el tiempo t."
        )
    disc = max(t**2 - 4 * L / a, 0.0)
    vmax = (a / 2) * (t - math.sqrt(disc))
    t1 = vmax / a
    return Perfil(L, t, t1, t - 2 * t1, a, vmax)


def desde_vmax(L: float, t: float, vmax: float) -> Perfil:
    """L = Vmax*(t - t1)  ->  t1 = t - L/Vmax; exige L/t < Vmax <= 2L/t."""
    if not L / t < vmax <= 2 * L / t * (1 + 1e-12):
        raise ValueError(
            f"Vmax debe cumplir L/t < Vmax <= 2L/t, es decir {L / t:.6g} < Vmax <= {2 * L / t:.6g}"
        )
    t1 = min(t - L / vmax, t / 2)
    return Perfil(L, t, t1, t - 2 * t1, vmax / t1, vmax)


def verificar(p: Perfil) -> list[str]:
    """Comprobaciones independientes de la fórmula usada."""
    notas = []
    area = p.vmax * p.t1 + p.vmax * p.t2          # 2 triángulos + rectángulo
    err = abs(area - p.L) / abs(p.L)
    notas.append(f"Área bajo v(t) = {area:.6g}  (error relativo {err:.1e} respecto a L)")
    notas.append(f"a mínima para este (L, t): 4L/t^2 = {4 * p.L / p.t**2:.6g}")
    if p.triangular:
        notas.append("Perfil TRIANGULAR: no hay tramo a velocidad constante.")
    if abs(p.t1 - p.t / 3) < 1e-3 * p.t:
        notas.append("Perfil 1/3-1/3-1/3: mínima aceleración RMS y mínima potencia pico "
                     "para una carga inercial, entre los perfiles trapezoidales.")
    return notas


def imprimir(p: Perfil) -> None:
    print("Perfil trapezoidal simétrico")
    print(f"  L     = {p.L:.6g}   [unidades]")
    print(f"  t     = {p.t:.6g}   [s]")
    print(f"  t1    = {p.t1:.6g}   [s]   aceleración (= desaceleración)")
    print(f"  t2    = {p.t2:.6g}   [s]   crucero")
    print(f"  a     = {p.a:.6g}   [unidades/s^2]   -> Accel Rate y Decel Rate del MAM")
    print(f"  Vmax  = {p.vmax:.6g}   [unidades/s]     -> Speed del MAM")
    print("Verificación")
    for n in verificar(p):
        print("  - " + n)
    print("Recuerda: compara Speed y Accel con los límites del eje "
          "(Axis Properties > Dynamics) antes de cargarlos en el MAM.")


def graficar(p: Perfil, archivo: str) -> None:
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib no está instalado: pip install matplotlib", file=sys.stderr)
        return
    ts = [0, p.t1, p.t1 + p.t2, p.t]
    vs = [0, p.vmax, p.vmax, 0]
    fig, ax = plt.subplots(figsize=(7, 3.5))
    ax.plot(ts, vs, color="black", linewidth=1.5)
    ax.fill_between(ts, vs, color="0.85")
    ax.set_xlabel("tiempo [s]")
    ax.set_ylabel("velocidad [unidades/s]")
    ax.set_title(f"L = {p.L:g}, t = {p.t:g} s, t1 = {p.t1:.3g} s, "
                 f"Vmax = {p.vmax:.4g}, a = {p.a:.4g}")
    ax.grid(True, color="0.9")
    fig.tight_layout()
    fig.savefig(archivo, dpi=150)
    print(f"Gráfica guardada en {archivo}")


def ritmo(rp: float, margen_ms: float = 500) -> None:
    tu = 60.0 / rp
    print(f"Ritmo de producción RP = {rp:g} cajas/min")
    print(f"  Tiempo unitario tu = 60/RP = {tu:.4g} s por caja")
    print(f"  Si t_formado = t_home = tu/2       -> {tu / 2:.4g} s cada fase")
    print(f"  Si además t_b = t_c = t_formado/2  -> {tu / 4:.4g} s cada etapa de formado")
    print(f"  Temporizador de aparición de cajas (NX_Signals, rung 4): "
          f"{1000 * tu:.0f} ms + hasta {margen_ms:.0f} ms de margen")
    print("Estos repartos son el punto de partida de la guía; tu equipo puede proponer otros.")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--L", type=float, help="recorrido del segmento (unidades del eje)")
    ap.add_argument("--t", type=float, help="duración del segmento [s]")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--t1", type=float, help="tiempo de aceleración [s]")
    g.add_argument("--frac", type=float, help="fracción t1/t (0 < frac <= 0.5)")
    g.add_argument("--a", type=float, help="aceleración [unidades/s^2]")
    g.add_argument("--vmax", type=float, help="velocidad crucero [unidades/s]")
    ap.add_argument("--plot", metavar="ARCHIVO.png", help="guarda la gráfica v(t)")
    ap.add_argument("--rp", type=float, help="ritmo de producción [cajas/min] para el presupuesto de tiempo")
    args = ap.parse_args()

    if args.rp is not None:
        ritmo(args.rp)
        if args.L is None:
            return
        print()

    if args.L is None or args.t is None:
        ap.error("indica --L y --t (y una condición: --t1, --frac, --a o --vmax), o solo --rp")
    if args.L <= 0 or args.t <= 0:
        ap.error("L y t deben ser positivos (para recorridos negativos usa |L| y el signo en la posición)")

    try:
        if args.t1 is not None:
            p = desde_t1(args.L, args.t, args.t1)
        elif args.frac is not None:
            p = desde_t1(args.L, args.t, args.frac * args.t)
        elif args.a is not None:
            p = desde_a(args.L, args.t, args.a)
        elif args.vmax is not None:
            p = desde_vmax(args.L, args.t, args.vmax)
        else:
            ap.error("falta la condición de diseño: --t1, --frac, --a o --vmax")
    except ValueError as e:
        sys.exit(f"Error: {e}")

    imprimir(p)
    if args.plot:
        graficar(p, args.plot)


if __name__ == "__main__":
    main()
