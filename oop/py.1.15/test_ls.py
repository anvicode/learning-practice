# type: ignore
import logging
import unittest

from ls import get_files_subdirs_list

logging.basicConfig(
    level=logging.DEBUG,
    filename="log.log",
    format=" %(asctime)s %(levelname)s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8",
)

logger = logging.getLogger(__name__)


class TestGetFilesSubdirsList(unittest.TestCase):
    def test_get_files_subdirs_list(self):
        try:
            self.assertEqual(
                get_files_subdirs_list(".", "md", True),
                [
                    ["./readme.md", "./del/del.md"],
                    ["./__pycache__", "./del", "./ls", "./del/del2"],
                ],
            )
            logging.info("Test passed")

        except AssertionError as error:
            logging.error(f"Test failed: {error}")
            self.assertEqual(
                get_files_subdirs_list(".", "md", True),
                [
                    ["./readme.md", "./del/del.md"],
                    ["./__pycache__", "./del", "./ls", "./del/del2"],
                ],
            )

    def test_get_files_subdirs_list2(self):
        try:
            self.assertEqual(
                get_files_subdirs_list(".", "md", False),
                [["./readme.md"], ["./__pycache__", "./del", "./ls"]],
            )
            logging.info("Test passed")

        except AssertionError as error:
            logging.error(f"Test failed: {error}")
            self.assertEqual(
                get_files_subdirs_list(".", "md", False),
                [["./readme.md"], ["./__pycache__", "./del", "./ls"]],
            )


if __name__ == "__main__":
    unittest.main()
