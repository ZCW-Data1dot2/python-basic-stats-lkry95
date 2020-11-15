import unittest
from statzcw import zmode,zmean,zmedian,zcount,zstddev,zvariance,zstderr,zcorr

class zcountTest(unittest.TestCase):
    def test_count(self):
        test_cases = [
            ([3,6,9,11,6],5),([1,5,8,9,5,8,5],7),([11,55,33,22,55],5),([6,90,33,27,3,6],6)
             ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, zcount(temp_in))

class zmodeTest(unittest.TestCase):
    def test_mode(self):
        test_cases = [
            ([3,6,9,11,6],6),([1,5,8,9,5,8,5],5),([11,55,33,22,55],55),([6,90,33,27,3,6],6)
             ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, zmode(temp_in))

class zmeanTest(unittest.TestCase):
    def test_mean(self):
        test_cases = [
            ([5,6,9,6],6.5),([1,5,8,9,5,8],6),([11,55,33,22,55],35.2),([6,90,33,27,3,6],27.5)
             ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, zmean(temp_in))

class zstddevTest(unittest.TestCase):
    def test_stddev(self):
        test_cases = [
            ([10,12,23,23,16],5.42),([1,5,8,9,5,8],2.71),([11,55,33,22,55],17.6),([6,90,33,27,3,6],30.17)
             ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, zstddev(temp_in))

class zvarianceTest(unittest.TestCase):
    def test_variance(self):
        test_cases = [
            ([5,6,9,6],2.25),([1,5,8,14,7,10],16.25),([11,55,33,22,55],309.76),([6,90,33,27,3,6],910.25)
             ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, zvariance(temp_in))

class stderrTest(unittest.TestCase):
    def test_stderr(self):
        test_cases = [
            ([5,6,9,6],.75),([1,5,8,9,5,8],1.11),([11,55,33,22,55],7.87),([6,90,33,27,3,6],12.32)
             ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, zstderr(temp_in))

class zmedianTest(unittest.TestCase):
    def test_mode(self):
        test_cases = [
            ([5,6,9,6,7],6),
            ([1,5,8,9,4],5),
            ([11,55,33,22,55],33),
            ([6,90,33,27,3],27)
             ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, zmedian(temp_in))

class zcorrTest(unittest.TestCase):
    def test_corr(self):
        test_cases = [
            ([3,5,8,12,13,33], [3,5,8,12,13,33], 1.0)
             ]
        for temp_in1, temp_in2, expected in test_cases:
            with self.subTest(f"{temp_in1} {temp_in2} -> {expected}"):
                self.assertEqual(expected, zcorr(temp_in1, temp_in2))


