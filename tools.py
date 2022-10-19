class API:
    FILE_PATH = "nums.txt"

    @classmethod
    def get_data(cls):
        file = open(cls.FILE_PATH, 'r')
        lines = file.read().splitlines()
        return lines


def load_nums_from_file():
    nums = []
    for line in API.get_data():
        pair = line.split(",")
        if len(pair) == 2:
            x = float(pair[0].strip())
            y = float(pair[1].strip())
            nums.append((x, y))
    return nums
