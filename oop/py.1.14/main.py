# type: ignore
import logging
from random import randint

logging.basicConfig(
    level=logging.DEBUG,
    filename="log.log",
    format=" %(asctime)s %(levelname)s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8",
)

logger = logging.getLogger(__name__)


def make_files():
    for i in range(10):
        with open(f"file{i + 1}.txt", "wt") as f:
            f.write(f"{randint(1, 10)}\n{randint(1, 10)}\n{randint(1, 10)}")
            logging.info(f"file{i + 1}.txt created")


make_files()


def sum_of_two_files(file1, file2):
    try:
        with open(file1, "rt") as f1, open(file2, "rt") as f2:
            fl1 = (int(line) for line in f1)
            fl2 = (int(line) for line in f2)
            res = sum(fl1) + sum(fl2)
            logging.info(f"Sum of {file1} and {file2} = {res}")
            return res
    except Exception as error:
        logger.error(error)
        return error


file1 = f"file{randint(1, 10)}.txt"
file2 = f"file{randint(1, 10)}.txt"
print(sum_of_two_files(file1, file2))
