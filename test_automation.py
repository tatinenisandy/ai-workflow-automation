import unittest
from datetime import date
from automation import classify


class TestClassification(unittest.TestCase):
    def test_resolved(self):
        self.assertEqual(classify({'status': 'Resolved', 'severity': 'High', 'follow_up_date': '2026-10-01'}, date(2026, 10, 25))[0], 'None')

    def test_high_severity(self):
        self.assertEqual(classify({'status': 'Open', 'severity': 'High', 'follow_up_date': '2026-10-30'}, date(2026, 10, 25))[0], 'High')

    def test_overdue(self):
        self.assertEqual(classify({'status': 'Open', 'severity': 'Low', 'follow_up_date': '2026-10-20'}, date(2026, 10, 25))[0], 'Medium')

    def test_future(self):
        self.assertEqual(classify({'status': 'Open', 'severity': 'Low', 'follow_up_date': '2026-10-30'}, date(2026, 10, 25))[0], 'Low')


if __name__ == '__main__':
    unittest.main()
