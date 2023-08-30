# type: ignore
import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="log.log",
    format=" %(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8",
)


def minimum(arr):
    min = arr[0]
    for i in arr:
        if min > i:
            min = i
    return min


def maximum(arr):
    max = arr[0]
    for i in arr:
        if max < i:
            max = i
    return max


def test(arg, res):
    try:
        assert minimum(arg) is res[0]
        assert minimum(arg) != ""
        logging.info(f"minimum({arg}) == {res[0]}")
    except (AssertionError, ValueError):
        logging.error(f"minimum({arg}) == {res[0]}")

    try:
        assert maximum(arg) is res[1]
        assert maximum(arg) != ""
        logging.info(f"maximum({arg}) == {res[1]}")
    except AssertionError:
        logging.error(f"maximum({arg}) == {res[1]}")


test([4, 6, 2, 1, 9, 63, -134, 566], (-134, 566))
test([4, 6, 2, 1, 9, 63, -134, 566], (-1314, 566))
test([4, 6, 2, 1, 9, 63, -134, 566], (-134, 5661))
test([4, 6, 2, 1, 9, 63, -134, 566], ("", ""))
test([-52, 56, 30, 29, -54, 0, -110], (-110, 56))
test([42, 54, 65, 87, 0], (0, 87))
test([42, 54, 65, 87, 0], (0, 65))
test([42, 54, 65, 87, 0], (False, 87))
test([5], (5, 5))
test([42, 54, 65, 87, 0], (0, 87))
test([5], (5, 5))
test([5], (5, False))
test([5], ("", 1))
