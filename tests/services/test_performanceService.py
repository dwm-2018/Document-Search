from unittest import TestCase

from services.performanceService import PerformanceService


class PerformanceServiceTests(TestCase):
    def setUp(self):
        self.ps = PerformanceService()

