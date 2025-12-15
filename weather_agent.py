"""Agente de consola simple para consultar clima simulado.

Funcionalidades:
- Pide al usuario una ciudad o pregunta sobre el clima
- Usa datos simulados en un diccionario
- Contiene funciones: normalizar, extraer ciudad, obtener clima, construir respuesta
- Bucle para múltiples consultas hasta que el usuario escriba 'salir'
"""
from typing import Dict, Optional
import resa


SIMULATED_WEATHER: Dict[str, Dict[str, str]] = {
    "madrid": {"temp": "5°C", "condition": "soleado"},
    "barcelona": {"temp": "12°C", "condition": "nublado"},
    "londres": {"temp": "8°C", "condition": "lluvioso"},
    "paris": {"temp": "9°C", "condition": "ventoso"},
    "bogota": {"temp": "18°C", "condition": "templado"},
}


def normalize(text: str) -> str:
    """Normaliza el texto: pasa a minúsculas y elimina puntuación extra."""
    text = text.lower().strip()
    # eliminar caracteres no alfanuméricos excepto espacios y acentos comunes
    text = re.sub(r"[^a-záéíóúüñ0-9\s]", "", text)
    return text


def extract_city(text: str, known_cities: Dict[str, Dict[str, str]]) -> Optional[str]:
    """Extrae el nombre de la ciudad del texto si está en known_cities.

    Busca coincidencias simples: si alguno de los nombres conocidos aparece en el texto.
    """
    normalized = normalize(text)
    # buscar coincidencia por palabra completa para evitar falsos positivos
    for city in known_cities.keys():
        if re.search(rf"\b{re.escape(city)}\b", normalized):
            return city
    # si el usuario escribió solo una palabra (p. ej. 'Madrid'), revisarla
    tokens = normalized.split()
    if len(tokens) == 1 and tokens[0] in known_cities:
        return tokens[0]
    return None


def get_weather(city: str, data: Dict[str, Dict[str, str]]) -> Optional[Dict[str, str]]:
    """Devuelve los datos de clima simulados para la ciudad, o None si no existe."""
    return data.get(city)


def build_response(city: Optional[str], weather: Optional[Dict[str, str]]) -> str:
    """Construye una respuesta de texto para el usuario según si se conoce la ciudad."""
    if city is None:
        return "No pude identificar la ciudad en tu mensaje. ¿Puedes decirme la ciudad?"
    if weather is None:
        return f"Lo siento, no tengo datos para la ciudad '{city.title()}'."
    return f"En {city.title()} hace {weather['temp']} y está {weather['condition']}."


def main() -> None:
    print("Agente de Clima — Escribe una ciudad o pregunta (escribe 'salir' para terminar)")
    while True:
        try:
            user = input("> ")
        except (EOFError, KeyboardInterrupt):
            print("\nSaliendo. ¡Hasta luego!")
            break

        if not user:
            continue

        if user.strip().lower() in {"salir", "exit", "quit"}:
            print("Saliendo. ¡Hasta luego!")
            break

        city = extract_city(user, SIMULATED_WEATHER)
        weather = get_weather(city, SIMULATED_WEATHER) if city else None
        response = build_response(city, weather)
        print(response)


if __name__ == "__main__":
    main()
