# type: ignore
import logging
import unittest

from make_cat import make_cats

logging.basicConfig(
    level=logging.DEBUG,
    filename="log.log",
    format=" %(asctime)s %(levelname)s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8",
)

logger = logging.getLogger(__name__)


class TestMakeCat(unittest.TestCase):
    def test_regression(self):
        try:
            self.assertEqual(
                make_cats(),
                [
                    ("Барсик", 5.0, 75),
                    ("Марсик", 6.0, 65),
                    ("Парсик", 4.0, 55),
                ],
            )
            logging.info("Test passed")
        except AssertionError:
            logging.error("Test failed")
            self.assertEqual(
                make_cats(),
                [
                    ("Барсик", 5.0, 75),
                    ("Марсик", 6.0, 65),
                    ("Парсик", 4.0, 55),
                ],
            )


if __name__ == "__main__":
    unittest.main()
