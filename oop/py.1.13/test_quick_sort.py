# type: ignore
import logging
import unittest
from random import randint

from py_1_13 import quick_sort

logging.basicConfig(
    level=logging.DEBUG,
    filename="log.log",
    format=" %(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8",
)

logger = logging.getLogger(__name__)


class TestQuickSort(unittest.TestCase):
    def test_regression(self):
        lst = [8, -1, 2, 7, 0, 5, 9, 3, 6, 4, 10, 1]
        regr = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        logging.info("Running regression test")
        self.assertEqual(quick_sort(lst), regr)

    def test_random(self):
        lst = [randint(-100, 100) for _ in range(10)]
        logging.info("Running random test")
        self.assertEqual(quick_sort(lst), sorted(lst))

    def test_null(self):
        logging.info("Running null test")
        self.assertEqual(quick_sort([0, 0, 0]), [0, 0, 0])

    def test_boundary(self):
        arr = [1000000000000, -1000000000000, 0, -1, 1]
        result = quick_sort(arr)
        logging.info("Running boundary test")
        self.assertEqual(result, [-1000000000000, -1, 0, 1, 1000000000000])


if __name__ == "__main__":
    unittest.main()
