#!/usr/bin/env python3
"""
wifi_monitor.py — Local Network Intruder Monitor
=================================================
Autor   : alemakey (Victor)
Versión : 1.0.0
Uso     : python3 wifi_monitor.py [--interval <segundos>] [--loop]

Descripción
-----------
Usa `arp -a` para obtener la tabla ARP del sistema operativo, extrae
pares (IP, MAC) mediante expresiones regulares y los compara con un
diccionario de dispositivos conocidos (lista blanca).

Si detecta una dirección MAC no registrada, emite una alerta en consola
con la IP y MAC del posible intruso.

Compatibilidad
--------------
  Windows  → arp -a          (formato: <IP>  <MAC>  <tipo>)
  Linux    → arp -a          (formato: ? (<IP>) at <MAC> [ether] ...)
  macOS    → arp -a          (mismo formato que Linux)
"""

import subprocess
import re
import sys
import time
import argparse
import platform
from datetime import datetime

# ─────────────────────────────────────────────────────────────
#  LISTA BLANCA — Edita este diccionario con tus dispositivos
#  Clave : Dirección MAC en minúsculas, separada por ':'
#  Valor : Nombre descriptivo del dispositivo
# ─────────────────────────────────────────────────────────────
DISPOSITIVOS_CONOCIDOS: dict[str, str] = {
    # Router / Gateway principal
    "c8:3a:35:12:ab:01": "Router TP-Link (Gateway)",

    # Computadora del usuario
    "d4:be:d9:f1:22:8c": "VictorHome (PC Principal)",

    # Impresora HP de la hija
    "3c:52:82:6a:44:f7": "HP DeskJet (Impresora Esmeralda)",

    # Agrega más dispositivos aquí:
    # "xx:xx:xx:xx:xx:xx": "Nombre del dispositivo",
}

# ─────────────────────────────────────────────────────────────
#  CONSTANTES DE FORMATO PARA CONSOLA
# ─────────────────────────────────────────────────────────────
COLOR_VERDE   = "\033[92m"
COLOR_ROJO    = "\033[91m"
COLOR_AMARILLO= "\033[93m"
COLOR_CYAN    = "\033[96m"
COLOR_BOLD    = "\033[1m"
COLOR_RESET   = "\033[0m"

SEP_MAYOR = "=" * 62
SEP_MENOR = "-" * 62


# ─────────────────────────────────────────────────────────────
#  FUNCIONES AUXILIARES
# ─────────────────────────────────────────────────────────────

def normalizar_mac(mac: str) -> str:
    """
    Normaliza una dirección MAC al formato xx:xx:xx:xx:xx:xx en minúsculas.

    Acepta formatos comunes:
      - Windows: aa-bb-cc-dd-ee-ff
      - Linux  : aa:bb:cc:dd:ee:ff
      - Sin sep : aabbccddeeff
    """
    # Eliminar separadores y convertir a minúsculas
    limpia = re.sub(r"[:\-\.]", "", mac).lower()
    if len(limpia) != 12:
        return mac.lower()  # Devolver como está si no es válida
    return ":".join(limpia[i:i+2] for i in range(0, 12, 2))


def obtener_tabla_arp() -> str:
    """
    Ejecuta `arp -a` y devuelve la salida como cadena de texto.
    Lanza RuntimeError si el comando falla.
    """
    try:
        resultado = subprocess.run(
            ["arp", "-a"],
            capture_output=True,
            text=True,
            timeout=10,
        )
        if resultado.returncode != 0:
            raise RuntimeError(
                f"arp -a retornó código {resultado.returncode}:\n{resultado.stderr}"
            )
        return resultado.stdout
    except FileNotFoundError:
        raise RuntimeError(
            "Comando 'arp' no encontrado. "
            "Instala net-tools (Linux: sudo apt install net-tools)."
        )
    except subprocess.TimeoutExpired:
        raise RuntimeError("El comando 'arp -a' excedió el tiempo límite de 10 s.")


def parsear_dispositivos(salida_arp: str) -> list[dict[str, str]]:
    """
    Extrae pares (IP, MAC) de la salida de `arp -a` usando regex.

    Soporta:
      - Windows : «192.168.1.1          c8-3a-35-12-ab-01     dinámico»
      - Linux   : «? (192.168.1.1) at c8:3a:35:12:ab:01 [ether] …»
      - macOS   : igual que Linux
    """
    dispositivos: list[dict[str, str]] = []

    # Patrón de dirección IPv4
    patron_ip = r"(\d{1,3}(?:\.\d{1,3}){3})"

    # Patrón de MAC: acepta ':' o '-' como separador
    patron_mac = r"((?:[0-9A-Fa-f]{2}[:\-]){5}[0-9A-Fa-f]{2})"

    # Patrón combinado: busca IP y MAC en la misma línea
    patron_linea = re.compile(
        rf"{patron_ip}.*?{patron_mac}",
        re.IGNORECASE,
    )

    for linea in salida_arp.splitlines():
        coincidencia = patron_linea.search(linea)
        if coincidencia:
            ip  = coincidencia.group(1)
            mac = normalizar_mac(coincidencia.group(2))

            # Ignorar entradas de broadcast/multicast (MAC ff:ff:ff:ff:ff:ff)
            if mac == "ff:ff:ff:ff:ff:ff":
                continue

            dispositivos.append({"ip": ip, "mac": mac})

    return dispositivos


def analizar_red(dispositivos: list[dict[str, str]]) -> tuple[list, list]:
    """
    Compara la lista de dispositivos detectados con DISPOSITIVOS_CONOCIDOS.

    Returns
    -------
    conocidos  : lista de dicts con {ip, mac, nombre}
    intrusos   : lista de dicts con {ip, mac}
    """
    conocidos: list[dict] = []
    intrusos:  list[dict] = []

    for dispositivo in dispositivos:
        mac    = dispositivo["mac"]
        nombre = DISPOSITIVOS_CONOCIDOS.get(mac)

        if nombre:
            conocidos.append({**dispositivo, "nombre": nombre})
        else:
            intrusos.append(dispositivo)

    return conocidos, intrusos


def imprimir_encabezado() -> None:
    """Imprime el encabezado del monitor en consola."""
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n{COLOR_BOLD}{COLOR_CYAN}{SEP_MAYOR}{COLOR_RESET}")
    print(f"  📡 {COLOR_BOLD}Wi-Fi Intruder Monitor{COLOR_RESET}  —  {ts}")
    print(f"{COLOR_BOLD}{COLOR_CYAN}{SEP_MAYOR}{COLOR_RESET}")


def imprimir_resultado(
    conocidos: list[dict],
    intrusos:  list[dict],
    total:     int,
) -> None:
    """Imprime los dispositivos conocidos e intrusos detectados."""

    # ── Dispositivos conocidos ──────────────────────────────
    print(f"\n{COLOR_BOLD}Dispositivos conocidos ({len(conocidos)}/{total}):{COLOR_RESET}")
    print(SEP_MENOR)
    if conocidos:
        for d in conocidos:
            print(
                f"  {COLOR_VERDE}✔  {d['ip']:<18}{COLOR_RESET}"
                f"  {d['mac']}  →  {d['nombre']}"
            )
    else:
        print(f"  {COLOR_AMARILLO}(ninguno encontrado en la red actualmente){COLOR_RESET}")

    # ── Posibles intrusos ───────────────────────────────────
    print(f"\n{COLOR_BOLD}Posibles intrusos / dispositivos desconocidos ({len(intrusos)}):{COLOR_RESET}")
    print(SEP_MENOR)
    if intrusos:
        for d in intrusos:
            print(
                f"  {COLOR_ROJO}{COLOR_BOLD}⚠  ALERTA │ IP: {d['ip']:<18}"
                f"MAC: {d['mac']}{COLOR_RESET}"
            )
        print(
            f"\n  {COLOR_ROJO}{COLOR_BOLD}[!] Se detectaron {len(intrusos)} "
            f"dispositivo(s) NO registrado(s) en la lista blanca.{COLOR_RESET}"
        )
        print(
            f"  {COLOR_AMARILLO}Agrega su MAC a DISPOSITIVOS_CONOCIDOS si es de confianza.{COLOR_RESET}"
        )
    else:
        print(
            f"  {COLOR_VERDE}✔  Sin intrusos detectados. "
            f"Todos los dispositivos están registrados.{COLOR_RESET}"
        )

    print(f"\n{SEP_MAYOR}\n")


# ─────────────────────────────────────────────────────────────
#  PUNTO DE ENTRADA
# ─────────────────────────────────────────────────────────────

def parsear_argumentos() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Monitorea la red local y alerta sobre MACs desconocidas.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Ejemplos:\n"
            "  python3 wifi_monitor.py\n"
            "  python3 wifi_monitor.py --loop --interval 30\n"
        ),
    )
    parser.add_argument(
        "--loop",
        action="store_true",
        help="Ejecutar en bucle continuo (terminar con Ctrl+C).",
    )
    parser.add_argument(
        "--interval",
        type=int,
        default=60,
        metavar="SEG",
        help="Intervalo en segundos entre escaneos en modo --loop (default: 60).",
    )
    return parser.parse_args()


def escanear_una_vez() -> None:
    """Ejecuta un único ciclo de escaneo e imprime el resultado."""
    imprimir_encabezado()

    try:
        salida_arp = obtener_tabla_arp()
    except RuntimeError as exc:
        print(f"{COLOR_ROJO}Error al ejecutar arp -a: {exc}{COLOR_RESET}")
        sys.exit(1)

    dispositivos = parsear_dispositivos(salida_arp)

    if not dispositivos:
        print(
            f"{COLOR_AMARILLO}No se encontraron dispositivos en la tabla ARP.\n"
            f"Comprueba que estás conectado a la red.{COLOR_RESET}"
        )
        return

    conocidos, intrusos = analizar_red(dispositivos)
    imprimir_resultado(conocidos, intrusos, len(dispositivos))

    # Código de salida: 0 = sin intrusos, 1 = intrusos detectados
    if intrusos:
        sys.exit(1)


def main() -> None:
    # Verificar compatibilidad
    so = platform.system()
    if so not in ("Windows", "Linux", "Darwin"):
        print(f"{COLOR_AMARILLO}Advertencia: sistema operativo '{so}' no probado.{COLOR_RESET}")

    args = parsear_argumentos()

    if args.loop:
        print(
            f"{COLOR_CYAN}Modo continuo activado. "
            f"Intervalo: {args.interval} s. "
            f"Presiona Ctrl+C para detener.{COLOR_RESET}"
        )
        try:
            while True:
                escanear_una_vez()
                time.sleep(args.interval)
        except KeyboardInterrupt:
            print(f"\n{COLOR_AMARILLO}Monitor detenido por el usuario.{COLOR_RESET}")
    else:
        escanear_una_vez()


if __name__ == "__main__":
    main()
