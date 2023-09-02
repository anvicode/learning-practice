# type: ignore
import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="log.log",
    format=" %(asctime)s %(levelname)s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8",
)

logger = logging.getLogger(__name__)


class Cat:
    def __init__(self, name, weight, frequency):
        self.__name = name
        self.__weight = weight
        self.__frequency = frequency

    def __str__(self):
        return f"{self.__name} {self.__weight} {self.__frequency}"

    def get_name(self):
        return self.__name

    def get_weight(self):
        return self.__weight

    def get_frequency(self):
        return self.__frequency


def make_cats():
    # read lines from file
    with open("cat.txt", "rt") as f:
        lines = f.readlines()
        cats = []
        try:
            for line in lines:
                name, weight, frequency = line.split()
                weight = float(weight)
                frequency = int(frequency)
                cats.append(Cat(name, weight, frequency))
                logger.info(f"'{name} {weight} {frequency}' has added")
            logger.info(f"Cats: {[cat.__str__() for cat in cats]}")
            return [(i.get_name(), i.get_weight(), i.get_frequency()) for i in cats]
        except Exception as error:
            logger.error(error)
            return error


print(make_cats())
