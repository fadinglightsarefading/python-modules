import typing
import abc


class DataProcessor(abc.ABC):
    def __init__(self):
        self.data = []
        self.rank = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
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
        elif isinstance(data, list):
            data = [str(val) for val in data]
            self.data.extend(data)


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
        elif isinstance(data, list):
            self.data.extend(data)


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
        elif isinstance(data, list):
            for d in data:
                self.ingest(d)


def main() -> None:
    print("=== Code Nexus - Data Processor ===")
    print("\nTesting Numeric Processor...")
    num = NumericProcessor()
    print(f"Trying to validate input \'42\': {num.validate(42)}")
    print(f"Trying to validate input \'Hello\': {num.validate("Hello")}")
    print("Testing invalid ingestion of string \'foo\'"
          "without prior validation:")
    try:
        num.ingest("foo")
    except TypeError as e:
        print(f"Got exception: {e}")
    num_data = [1, 2, 3, 4, 5]
    print(f"Processing data: {num_data}")
    num.ingest(num_data)
    print("Extracting 3 values...")
    for i in range(0, 3):
        num_extract = num.output()
        print(f"Numeric value {num_extract[0]}: {num_extract[1]}")
    print("\nTesting Text Processor...")
    tex = TextProcessor()
    print(f"Trying to validate input \'42\': {tex.validate(42)}")
    tex_data = ["Hello", "Nexus", "World"]
    print(f"Processing data: {tex_data}")
    tex.ingest(tex_data)
    print("Extracting 1 value...")
    tex_extract = tex.output()
    print(f"Numeric value {tex_extract[0]}: {tex_extract[1]}")
    print("\nTesting Log Processor...")
    log = LogProcessor()
    print(f"Trying to validate input \'Hello\': {log.validate("Hello")}")
    log_data = [{"log_level": "NOTICE", "log_message": "Connection to server"},
                {"log_level": "ERROR", "log_message": "Unauthorised access!!"}]
    print(f"Processing data: {log_data}")
    log.ingest(log_data)
    print("Extracting 2 values...")
    for i in range(0, 2):
        log_extract = log.output()
        print(f"Log entry {log_extract[0]}: {log_extract[1]}")


if __name__ == "__main__":
    main()
