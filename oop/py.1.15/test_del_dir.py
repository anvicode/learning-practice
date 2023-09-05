# type: ignore
import logging
import unittest

from del_dir import delete_directory

logging.basicConfig(
    level=logging.DEBUG,
    filename="log.log",
    format=" %(asctime)s %(levelname)s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8",
)

logger = logging.getLogger(__name__)


class TestDelDir(unittest.TestCase):
    def test_del_dir(self):
        try:
            self.assertEqual(delete_directory("del/del2/del2.md"), False)
            logger.info("Test passed")

        except AssertionError as error:
            logging.error(f"Test failed: {error}")
            self.assertEqual(delete_directory("del/del2/del2.md"), False)

    def test_del_dir2(self):
        try:
            self.assertEqual(delete_directory("del/del2"), True)
            logger.info("Test passed")

        except AssertionError as error:
            logging.error(f"Test failed: {error}")
            self.assertEqual(delete_directory("del/del2"), True)


if __name__ == "__main__":
    unittest.main()
