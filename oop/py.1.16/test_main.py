# type: ignore
import logging
import os
import unittest
from zipfile import ZipFile

from main import add_to_zip

logging.basicConfig(
    level=logging.DEBUG,
    filename="logs.log",
    format=" %(asctime)s %(levelname)s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8",
)

logger = logging.getLogger(__name__)


class TestAddToZip(unittest.TestCase):
    def test_add_to_zip(self):
        try:
            add_to_zip("test.zip", ".md")

            # check if zip file exists
            assert os.path.exists("test.zip")

            with ZipFile("test.zip", "r") as zip_file:
                # check if zip file contains only files with the given extension
                for i in ["zip1.md", "zip2.md", "zip3.md"]:
                    assert i in zip_file.namelist()

            os.remove("test.zip")
            logger.info("Test passed")

        except AssertionError as error:
            logger.error(f"Test failed {error}")
            self.fail(f"Test failed {error}")


if __name__ == "__main__":
    unittest.main()
