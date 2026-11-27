import csv
import statistics


class DataTable:
    def __init__(self, table: list[list[str]]) -> None:
        self.table = table

    @classmethod
    def load(cls, path: str) -> "DataTable":
        with open(path) as file:
            table = list(csv.reader(file))
        return cls(table)

    def mean(self, col_idx: int) -> float:
        return statistics.mean(float(row[col_idx]) for row in self.table)

    def stddev(self, col_idx: int) -> float:
        return statistics.stdev(float(row[col_idx]) for row in self.table)

    def save(self, path: str) -> None:
        with open(path, "w", newline="") as file:
            csv.writer(file).writerows(self.table)