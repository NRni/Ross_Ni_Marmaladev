from typing import Optional, Tuple
import requests

NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"
HEADERS = {"User-Agent": "Marmaladev/1.0 (game-dev-finder)"}


def geocode_city(city: str) -> Optional[Tuple[float, float]]:
    """Convert a city name to (lat, lon) using Nominatim. Returns None if not found."""
    if not city.strip():
        return None
    resp = requests.get(
        NOMINATIM_URL,
        params={"q": city, "format": "json", "limit": 1},
        headers=HEADERS,
        timeout=10,
    )
    resp.raise_for_status()
    data = resp.json()
    if not data:
        return None
    return float(data[0]["lat"]), float(data[0]["lon"])
