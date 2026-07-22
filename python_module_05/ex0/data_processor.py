#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._queue: list[tuple[int, str]] = []
        self._total: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        return self._queue.pop(0)

    def _store(self, value: str) -> None:
        self._queue.append((self._total, value))
        self._total += 1

    def total_processed(self) -> int:
        return self._total

    def remaining(self) -> int:
        return len(self._queue)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        def is_number(item: Any) -> bool:
            return (
                isinstance(item, (int, float)) and not isinstance(item, bool)
            )

        if isinstance(data, list):
            return len(data) > 0 and all(is_number(item) for item in data)
        return is_number(data)

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        items: list[int | float] = data if isinstance(data, list) else [data]
        for item in items:
            self._store(str(item))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return len(data) > 0 and all(
                isinstance(item, str) for item in data
            )
        return isinstance(data, str)

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        items: list[str] = data if isinstance(data, list) else [data]
        for item in items:
            self._store(item)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        def is_log_entry(entry: Any) -> bool:
            return isinstance(entry, dict) and all(
                isinstance(key, str) and isinstance(value, str)
                for key, value in entry.items()
            )

        if isinstance(data, list):
            return len(data) > 0 and all(is_log_entry(item) for item in data)
        return is_log_entry(data)

    def ingest(
        self, data: dict[str, str] | list[dict[str, str]]
    ) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        entries: list[dict[str, str]] = (
            data if isinstance(data, list) else [data]
        )
        for entry in entries:
            self._store(f"{entry['log_level']}: {entry['log_message']}")


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")

    print("Testing Numeric Processor...")
    numeric = NumericProcessor()
    print(f"Trying to validate input '42': {numeric.validate(42)}")
    print(f"Trying to validate input 'Hello': {numeric.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest("foo")
    except ValueError as error:
        print(f"Got exception: {error}")
    numeric_data: list[int | float] = [1, 2, 3, 4, 5]
    print(f"Processing data: {numeric_data}")
    numeric.ingest(numeric_data)
    print("Extracting 3 values...")
    for i in range(3):
        _, value = numeric.output()
        print(f"Numeric value {i}: {value}")

    print("\nTesting Text Processor...")
    text = TextProcessor()
    print(f"Trying to validate input '42': {text.validate(42)}")
    text_data = ["Hello", "Nexus", "World"]
    print(f"Processing data: {text_data}")
    text.ingest(text_data)
    print("Extracting 1 value...")
    _, value = text.output()
    print(f"Text value 0: {value}")

    print("\nTesting Log Processor...")
    log = LogProcessor()
    print(f"Trying to validate input 'Hello': {log.validate('Hello')}")
    log_data = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f"Processing data: {log_data}")
    log.ingest(log_data)
    print("Extracting 2 values...")
    for i in range(2):
        _, value = log.output()
        print(f"Log entry {i}: {value}")


if __name__ == "__main__":
    main()
