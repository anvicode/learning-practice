# type: ignore
import logging
import unittest

from main_the_second import find_repeated_values

logging.basicConfig(
    level=logging.DEBUG,
    filename="logs.log",
    format=" %(asctime)s %(levelname)s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8",
)

logger = logging.getLogger(__name__)


class TestFindRepeatedValues(unittest.TestCase):
    # if the function correctly counts repeated values
    def test_find_repeated_values(self):
        values = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
        n = 2
        expected_result = [1, 2, 3, 4, 5]
        try:
            self.assertEqual(find_repeated_values(values, n), expected_result)
            logger.info("Test passed")

        except AssertionError as error:
            logger.error(f"Test failed: {error}")
            self.fail(f"Test failed: {error}")


if __name__ == "__main__":
    unittest.main()
