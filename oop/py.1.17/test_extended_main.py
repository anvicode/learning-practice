# type: ignore
import logging
import os
import unittest

from extended_main import convert_img_draw

logging.basicConfig(
    level=logging.DEBUG,
    filename="logs.log",
    format=" %(asctime)s %(levelname)s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8",
)

logger = logging.getLogger(__name__)


class TestExtendedMain(unittest.TestCase):
    def test_convert_img_one_file(self):
        # png to jpg
        try:
            convert_img_draw(".png", ".jpg")
            self.assertTrue(os.path.exists("lambda-symbol.jpg"))
            logger.info("Test passed")

        except AssertionError as error:
            logger.error(f"Test failed {error}")
            self.fail(f"Test failed {error}")

    def test_convert_img_one_file2(self):
        # jpg to png
        try:
            convert_img_draw(".jpg", ".png")
            self.assertTrue(os.path.exists("lambda-symbol.png"))
            logger.info("Test passed")

        except AssertionError as error:
            logger.error(f"Test failed {error}")
            self.fail(f"Test failed {error}")

    # def test_convert_img_many(self):
    #     try:
    #         convert_img_draw(".png", ".jpg")
    #         self.assertTrue(os.path.exists("lambda-symbol.jpg"))
    #         self.assertTrue(os.path.exists("lambda-symbol2.jpg"))
    #         self.assertTrue(os.path.exists("lambda-symbol3.jpg"))
    #         logger.info("Test passed")

    #     except AssertionError as error:
    #         logger.error(f"Test failed {error}")
    #         self.fail(f"Test failed {error}")


if __name__ == "__main__":
    unittest.main()
