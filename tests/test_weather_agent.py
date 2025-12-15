import unittest

from weather_agent import (
    SIMULATED_WEATHER,
    normalize,
    extract_city,
    get_weather,
    build_response,
)


class TestWeatherAgent(unittest.TestCase):
    def test_normalize(self):
        self.assertEqual(normalize("  Madrid! "), "madrid")
        self.assertEqual(normalize("¿Qué tal, BOGOTA?"), "qué tal bogota")

    def test_extract_city(self):
        self.assertEqual(extract_city("¿Qué tiempo hay en Madrid?", SIMULATED_WEATHER), "madrid")
        self.assertEqual(extract_city("Londres", SIMULATED_WEATHER), "londres")
        self.assertIsNone(extract_city("¿Qué tal en Tokio?", SIMULATED_WEATHER))

    def test_get_weather(self):
        self.assertIsNotNone(get_weather("madrid", SIMULATED_WEATHER))
        self.assertIsNone(get_weather("tokio", SIMULATED_WEATHER))

    def test_build_response(self):
        resp = build_response("madrid", get_weather("madrid", SIMULATED_WEATHER))
        self.assertIn("Madrid", resp)
        self.assertIn("5°C", resp)
        self.assertEqual(build_response(None, None), "No pude identificar la ciudad en tu mensaje. ¿Puedes decirme la ciudad?")


if __name__ == "__main__":
    unittest.main()
