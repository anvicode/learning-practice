# type: ignore
import logging
import unittest

from main import create_dict_with_random_pairs

logging.basicConfig(
    level=logging.DEBUG,
    filename="logs.log",
    format=" %(asctime)s %(levelname)s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8",
)

logger = logging.getLogger(__name__)


class TestMain(unittest.TestCase):
    # if the len of my_dict is 100
    def test_create_dict_with_random_pairs(self):
        try:
            self.assertEqual(len(create_dict_with_random_pairs()), 100)
            logger.info("Test passed")

        except AssertionError as error:
            logger.error(f"Test failed: {error}")
            self.fail(f"Test failed: {error}")


if __name__ == "__main__":
    unittest.main()
