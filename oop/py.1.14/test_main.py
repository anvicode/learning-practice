# type: ignore
import logging
import unittest

from main import sum_of_two_files

logging.basicConfig(
    level=logging.DEBUG,
    filename="log.log",
    format=" %(asctime)s %(levelname)s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8",
)

logger = logging.getLogger(__name__)


class TestSumOfTwoFiles(unittest.TestCase):
    def test_regression(self):
        try:
            self.assertEqual(sum_of_two_files("file1.txt", "file2.txt"), 38)
            logging.info("Test passed")
        except AssertionError as error:
            logging.error(f"Test failed {error}")
            self.assertEqual(sum_of_two_files("file1.txt", "file2.txt"), 38)

    def test_null(self):
        try:
            self.assertEqual(sum_of_two_files("file3.txt", "file4.txt"), 0)
            logging.info("Test passed")
        except AssertionError as error:
            logging.error(f"Test failed {error}")
            self.assertEqual(sum_of_two_files("file3.txt", "file4.txt"), 0)


if __name__ == "__main__":
    unittest.main()
