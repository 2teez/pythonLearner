#!/usr/bin/env python3

import datetime


class MyLooger:
    def __init__(self, filename: str):
        self.filename = filename
        self.file = None

    def log(self, message: str) -> None:
        if self.file is None:
            raise ValueError("Log file is not open")
        self.file.write(f"{datetime.datetime.now(tz=datetime.timezone.utc)} {message}")

    def __enter__(self):
        self.file = open(self.filename, "w")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


def main() -> None:
    with MyLooger("log.txt") as logger:
        logger.log("Hello, World!")
        logger.log("Howdy! Earth...")


if __name__ == "__main__":
    main()
