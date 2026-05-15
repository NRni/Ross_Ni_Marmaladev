from typing import Optional, Tuple
import requests

# Fallback coordinates for common game dev cities
CITY_COORDS = {
    "new york": (40.7128, -74.0060),
    "los angeles": (34.0522, -118.2437),
    "san francisco": (37.7749, -122.4194),
    "seattle": (47.6062, -122.3321),
    "london": (51.5074, -0.1278),
    "paris": (48.8566, 2.3522),
    "berlin": (52.5200, 13.4050),
    "tokyo": (35.6762, 139.6503),
    "toronto": (43.6532, -79.3832),
    "montreal": (45.5017, -73.5673),
    "vancouver": (49.2827, -123.1207),
    "sydney": (-33.8688, 151.2093),
    "melbourne": (-37.8136, 144.9631),
    "stockholm": (59.3293, 18.0686),
    "helsinki": (60.1699, 24.9384),
    "amsterdam": (52.3676, 4.9041),
    "singapore": (1.3521, 103.8198),
    "seoul": (37.5665, 126.9780),
    "shanghai": (31.2304, 121.4737),
    "beijing": (39.9042, 116.4074),
    "bangalore": (12.9716, 77.5946),
    "dublin": (53.3498, -6.2603),
    "austin": (30.2672, -97.7431),
    "chicago": (41.8781, -87.6298),
    "boston": (42.3601, -71.0589),
    "portland": (45.5155, -122.6789),
    "denver": (39.7392, -104.9903),
    "atlanta": (33.7490, -84.3880),
    "dallas": (32.7767, -96.7970),
    "miami": (25.7617, -80.1918),
    "washington": (38.9072, -77.0369),
    "philadelphia": (39.9526, -75.1652),
    "san diego": (32.7157, -117.1611),
    "minneapolis": (44.9778, -93.2650),
    "detroit": (42.3314, -83.0458),
    "madrid": (40.4168, -3.7038),
    "barcelona": (41.3874, 2.1686),
    "rome": (41.9028, 12.4964),
    "milan": (45.4642, 9.1900),
    "munich": (48.1351, 11.5820),
    "cologne": (50.9375, 6.9603),
    "hamburg": (53.5511, 9.9937),
    "kyoto": (35.0116, 135.7681),
    "osaka": (34.6937, 135.5023),
    "shenzhen": (22.5431, 114.0579),
    "guangzhou": (23.1291, 113.2644),
    "mumbai": (19.0760, 72.8777),
    "hyderabad": (17.3850, 78.4867),
    "cape town": (-33.9249, 18.4241),
    "johannesburg": (-26.2041, 28.0473),
    "moscow": (55.7558, 37.6173),
    "warsaw": (52.2297, 21.0122),
    "prague": (50.0755, 14.4378),
    "budapest": (47.4979, 19.0402),
    "bucharest": (44.4268, 26.1025),
    "istanbul": (41.0082, 28.9784),
    "tel aviv": (32.0853, 34.7818),
    "doha": (25.2854, 51.5310),
    "riyadh": (24.7136, 46.6753),
    "bangkok": (13.7563, 100.5018),
    "kuala lumpur": (3.1390, 101.6869),
    "jakarta": (-6.2088, 106.8456),
    "ho chi minh": (10.8231, 106.6297),
    "taipei": (25.0330, 121.5654),
    "auckland": (-36.8485, 174.7633),
    "wellington": (-41.2865, 174.7762),
    "bristol": (51.4545, -2.5879),
    "edinburgh": (55.9533, -3.1883),
    "manchester": (53.4808, -2.2426),
    "leeds": (53.8008, -1.5491),
    "brighton": (50.8225, -0.1372),
    "nottingham": (52.9548, -1.1581),
    "cambridge": (52.2053, 0.1218),
    "oxford": (51.7520, -1.2577),
}


def geocode_city(city: str) -> Optional[Tuple[float, float]]:
    """Convert a city name to (lat, lon). Returns None if not found."""
    if not city.strip():
        return None

    # Try local lookup first (fast, no network)
    key = city.strip().lower()
    if key in CITY_COORDS:
        return CITY_COORDS[key]

    # Try Nominatim as fallback
    try:
        resp = requests.get(
            "https://nominatim.openstreetmap.org/search",
            params={"q": city, "format": "json", "limit": 1},
            headers={"User-Agent": "Marmaladev/1.0"},
            timeout=5,
        )
        data = resp.json()
        if data:
            return float(data[0]["lat"]), float(data[0]["lon"])
    except Exception:
        pass

    return None
