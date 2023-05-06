import unittest

from engine import sternman_engine

class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_is_on = True

        engine = sternman_engine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False

        engine = sternman_engine(warning_light_is_on)
        self.assertFalse(engine.needs_service())