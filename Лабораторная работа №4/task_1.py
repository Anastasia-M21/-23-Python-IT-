# TODO решите задачу
import json


def task() -> float:
    with open("input.json") as f:
        json_data = json.load(f)

    values = (item["score"] * item["weight"] for item in json_data)
    return sum(values)


print(round(task(), 3))
