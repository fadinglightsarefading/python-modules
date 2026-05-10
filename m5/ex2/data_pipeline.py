import typing
import abc

class DataProcessor(abc.ABC):
    def __init__(self):
        self.data = []
        self.rank = 0
        self.processed = 0
        self.remaining = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        self.remaining -= 1
        self.rank += 1
        return (self.rank - 1, self.data.pop(0))


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        elif isinstance(data, list):
            for val in data:
                if not isinstance(val, (int, float)):
                    return False
            return True
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise TypeError("Improper numerical data")
        if isinstance(data, (int, float)):
            self.data.append(str(data))
            self.processed += 1
            self.remaining += 1
        elif isinstance(data, list):
            data = [str(val) for val in data]
            self.data.extend(data)
            self.processed += len(data)
            self.remaining += len(data)


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            for val in data:
                if not isinstance(val, str):
                    return False
            return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise TypeError("Improper numerical data")
        if isinstance(data, str):
            self.data.append(data)
            self.processed += 1
            self.remaining += 1
        elif isinstance(data, list):
            self.data.extend(data)
            self.processed += len(data)
            self.remaining += len(data)


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if not isinstance(data, (dict, list)):
            return False
        if isinstance(data, dict):
            for key in data:
                if not isinstance(key, str) or not isinstance(data[key], str):
                    return False
            return True
        elif isinstance(data, list):
            for d in data:
                if not self.validate(d):
                    return False
            return True

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise TypeError("Improper numerical data")
        if isinstance(data, dict):
            self.data.append(": ".join(data.values()))
            self.processed += 1
            self.remaining += 1
        elif isinstance(data, list):
            for d in data:
                self.ingest(d)

class DataStream():
    def __init__(self):
        self.processors = []


    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)


    def process_stream(self, stream: list[typing.Any]) -> None:
        for data in stream:
            processed = False
            for proc in self.processors:
                if proc.validate(data):
                    proc.ingest(data)
                    processed = True
                    break
            if not processed:
                print(f"DataStream Error: Can't process element in stream: {data}")


    def print_processors_stats(self) -> None:
        print("=== Data Stream Statistics ===")
        if not len(self.processors):
            print("No processor found, no data")
        for proc in self.processors:
            print(f"{proc.__class__.__name__.replace("P", " P")}: "
                  f"total {proc.processed} items processed, "
                  f"remaining {proc.remaining} on processor")


def main() -> None:
    print("=== Code Nexus - Data Stream ===")
    num = NumericProcessor()
    tex = TextProcessor()
    log = LogProcessor()
    print("\nInitialising data stream...")
    ds = DataStream()
    ds.print_processors_stats()
    print("\nRegistering Numeric Processor")
    ds.register_processor(num)
    first_batch = ["Hello World",
                   [3.14, -1, 2.71],
                   [{'log_level': 'WARNING',
                     'log_message': 'Telnet access! Use ssh instead'},
                    {'log_level': 'INFO',
                     'log_message': 'User kit is connected'}],
                   42, ['Hi', 'five']]
    print(f"\nSending first batch of data on stream: {first_batch}")
    ds.process_stream(first_batch)
    ds.print_processors_stats()
    print("\nRegistering other data processors")
    ds.register_processor(tex)
    ds.register_processor(log)
    print(f"Sending the same batch again")
    ds.process_stream(first_batch)
    ds.print_processors_stats()
    print("\nConsuming some elements from the data processors: Numeric 3, Text 2, Log 1")
    num.output()
    num.output()
    num.output()
    tex.output()
    tex.output()
    log.output()
    ds.print_processors_stats()


if __name__ == "__main__":
    main()
