import unittest
from vice.statistics import get_job_statistics


class MyTestCase(unittest.TestCase):
    def test_j1(self):
        stats = get_job_statistics(1)

        self.assertDictEqual(stats, {
            "job_name": "Fixture J1",
            "expected_revenue": 30.00,
            "total_revenue": 30.00,
            "revenue_target_met": True,
            "month_of_service_count": 2,
            "orders": {
                1: {
                    "order_name": "Fixture O1",
                    "total_revenue": 30.00,
                    "average_ecpm": 10.00,
                    "total_ecpm": 10.00
                }
            }
        })

    def test_j2(self):
        stats = get_job_statistics(2)

        self.assertDictEqual(stats, {
            "job_name": "Fixture J2",
            "expected_revenue": 40.00,
            "total_revenue": 0.00,
            "revenue_target_met": False,
            "month_of_service_count": 1,
            "orders": {
                2: {
                    "order_name": "Fixture O2",
                    "total_revenue": 0.00,
                    "average_ecpm": 0.00,
                    "total_ecpm": 0.00
                }
            }
        })

    def test_j3(self):
        stats = get_job_statistics(3)

        self.assertDictEqual(stats, {
            "job_name": "Fixture J3",
            "expected_revenue": 50.00,
            "total_revenue": 1068.38,
            "revenue_target_met": True,
            "month_of_service_count": 3,
            "orders": {
                3: {
                    "order_name": "Fixture O3",
                    "total_revenue": 30.00,
                    "average_ecpm": 10.00,
                    "total_ecpm": 10.00
                },
                4: {
                    "order_name": "Fixture O4",
                    "total_revenue": 1038.38,
                    "average_ecpm": 3.67,
                    "total_ecpm": 10.70
                }
            }
        })


if __name__ == '__main__':
    unittest.main()
