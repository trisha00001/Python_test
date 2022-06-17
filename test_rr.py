import unittest
import sq.myapp.rr

class Test_rr(unittest.TestCase):
    def test_pl(self):
        self.assertEqual(sq.myapp.rr.pl(1), 3.141592653589793)

        with self.assertRaises(ValueError):
            sq.myapp.rr.pl(-1), "r<0"

        with self.assertRaises(TypeError):
            sq.myapp.rr.pl('a'), "Only numbers"
