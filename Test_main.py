import unittest
from main import ReservatioManager


class TestReservationManager(unittest.TestCase):

    # -------------------------
    # max_occupancy - normal cases
    # -------------------------

    def test_max_occupancy_ok(self):
        res = ReservatioManager.max_occupancy([
            (9, 12),
            (10, 13),
            (11, 14)
        ])
        self.assertEqual(res, (3, [(11, 12)]))

    def test_max_occupancy_ko(self):
        res = ReservatioManager.max_occupancy([
            (9, 12),
            (10, 13),
            (11, 14),
            (9, 12)
        ])
        self.assertNotEqual(res, (3, [(11, 12)]))

    def test_max_occupancy_empty(self):
        res = ReservatioManager.max_occupancy([])
        self.assertEqual(res, (0, None))

    def test_max_occupancy_single_booking(self):
        res = ReservatioManager.max_occupancy([
            (10, 15)
        ])
        self.assertEqual(res, (1, [(10, 15)]))

    def test_max_occupancy_same_booking_repeated(self):
        res = ReservatioManager.max_occupancy([
            (10, 15),
            (10, 15),
            (10, 15)
        ])
        self.assertEqual(res, (3, [(10, 15)]))

    def test_max_occupancy_same_max(self):
        res = ReservatioManager.max_occupancy([
            (9, 10),
            (10, 11),
            (11, 12)
        ])
        self.assertEqual(res, (1, [(9, 12)]))

    def test_max_occupancy_same_max_multiple(self):
        res = ReservatioManager.max_occupancy([
            (9, 10),
            (10, 11),
            (11, 12),
            (17, 20),
            (20, 21)
        ])
        self.assertEqual(res, (1, [(9, 12), (17, 21)]))

    def test_max_occupancy_multiple_separated_peaks(self):
        res = ReservatioManager.max_occupancy([
            (8, 10),
            (8, 9),
            (12, 14),
            (13, 14)
        ])
        self.assertEqual(res, (2, [(8, 9), (13, 14)]))

    def test_max_occupancy_last_hour(self):
        res = ReservatioManager.max_occupancy([
            (21, 24),
            (23, 24),
            (19, 21)
        ])
        self.assertEqual(res, (2, [(23, 24)]))

    def test_max_occupancy_first_hour(self):
        res = ReservatioManager.max_occupancy([
            (0, 3),
            (0, 1)
        ])
        self.assertEqual(res, (2, [(0, 1)]))

    def test_max_occupancy_full_day(self):
        res = ReservatioManager.max_occupancy([
            (0, 24)
        ])
        self.assertEqual(res, (1, [(0, 24)]))

    def test_max_occupancy_full_day_multiple(self):
        res = ReservatioManager.max_occupancy([
            (0, 24),
            (0, 24)
        ])
        self.assertEqual(res, (2, [(0, 24)]))

    def test_max_occupancy_peak_inside_large_range(self):
        res = ReservatioManager.max_occupancy([
            (8, 18),
            (10, 15),
            (12, 14)
        ])
        self.assertEqual(res, (3, [(12, 14)]))

    def test_max_occupancy_touching_ranges_are_not_concurrent(self):
        res = ReservatioManager.max_occupancy([
            (8, 10),
            (10, 12)
        ])
        self.assertEqual(res, (1, [(8, 12)]))

    def test_max_occupancy_unsorted_bookings(self):
        res = ReservatioManager.max_occupancy([
            (15, 18),
            (9, 12),
            (10, 16)
        ])
        self.assertEqual(res, (2, [(10, 12), (15, 16)]))

    # -------------------------
    # is_valid
    # -------------------------

    def test_is_valid_ok(self):
        self.assertTrue(
            ReservatioManager.is_valid(10, 15)
        )

    def test_is_valid_zero_to_24(self):
        self.assertTrue(
            ReservatioManager.is_valid(0, 24)
        )

    def test_is_valid_start_none(self):
        self.assertFalse(
            ReservatioManager.is_valid(None, 10)
        )

    def test_is_valid_end_none(self):
        self.assertFalse(
            ReservatioManager.is_valid(10, None)
        )

    def test_is_valid_start_negative(self):
        self.assertFalse(
            ReservatioManager.is_valid(-1, 10)
        )

    def test_is_valid_end_negative(self):
        self.assertFalse(
            ReservatioManager.is_valid(5, -1)
        )

    def test_is_valid_end_greater_than_24(self):
        self.assertFalse(
            ReservatioManager.is_valid(10, 25)
        )

    def test_is_valid_start_greater_than_end(self):
        self.assertFalse(
            ReservatioManager.is_valid(15, 10)
        )

    def test_is_valid_same_start_end(self):
        self.assertFalse(
            ReservatioManager.is_valid(10, 10)
        )

    def test_is_valid_start_float(self):
        self.assertFalse(
            ReservatioManager.is_valid(10.5, 15)
        )

    def test_is_valid_end_float(self):
        self.assertFalse(
            ReservatioManager.is_valid(10, 15.5)
        )

    def test_is_valid_start_string(self):
        self.assertFalse(
            ReservatioManager.is_valid("10", 15)
        )

    def test_is_valid_end_string(self):
        self.assertFalse(
            ReservatioManager.is_valid(10, "15")
        )

    def test_is_valid_boolean(self):
        self.assertFalse(
            ReservatioManager.is_valid(True, 10)
        )

    # -------------------------
    # max_occupancy - exceptions
    # -------------------------

    def test_max_occupancy_start_none(self):
        with self.assertRaises(ValueError):
            ReservatioManager.max_occupancy([
                (None, 10)
            ])

    def test_max_occupancy_end_none(self):
        with self.assertRaises(ValueError):
            ReservatioManager.max_occupancy([
                (10, None)
            ])

    def test_max_occupancy_negative_start(self):
        with self.assertRaises(ValueError):
            ReservatioManager.max_occupancy([
                (-1, 10)
            ])

    def test_max_occupancy_negative_end(self):
        with self.assertRaises(ValueError):
            ReservatioManager.max_occupancy([
                (5, -1)
            ])

    def test_max_occupancy_end_greater_than_24(self):
        with self.assertRaises(ValueError):
            ReservatioManager.max_occupancy([
                (10, 25)
            ])

    def test_max_occupancy_start_greater_than_end(self):
        with self.assertRaises(ValueError):
            ReservatioManager.max_occupancy([
                (15, 10)
            ])

    def test_max_occupancy_same_start_end(self):
        with self.assertRaises(ValueError):
            ReservatioManager.max_occupancy([
                (10, 10)
            ])

    def test_max_occupancy_float_value_st(self):
        with self.assertRaises(ValueError):
            ReservatioManager.max_occupancy([
                (10.5, 15)
            ])
            
    def test_max_occupancy_float_value_ed(self):
            with self.assertRaises(ValueError):
                ReservatioManager.max_occupancy([
                    (10, 15.3)
                ])

    def test_max_occupancy_string_value_st(self):
        with self.assertRaises(ValueError):
            ReservatioManager.max_occupancy([
                ("10", 15)
            ])
    
    def test_max_occupancy_string_value_ed(self):
            with self.assertRaises(ValueError):
                ReservatioManager.max_occupancy([
                    (10, "15")
                ])
                
    def test_max_occupancy_invalid_booking_between_valid_ones(self):
        with self.assertRaises(ValueError):
            ReservatioManager.max_occupancy([
                (8, 10),
                (10, 12),
                (15, 30),
                (18, 20)
            ])

    def test_max_occupancy_error_message(self):
        with self.assertRaisesRegex(
            ValueError,
            r"There is an invalid value in the list \(10, 25\)."
        ):
            ReservatioManager.max_occupancy([
                (10, 25)
            ])


if __name__ == '__main__':
    unittest.main()