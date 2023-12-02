import abc
import sys
from io import StringIO
from typing import List


class ILogger(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def log(self, message: str) -> None:
        raise NotImplementedError()


class StdoutLogger(ILogger):
    def log(self, message: str) -> None:
        print(message)


class ArrayLogger(ILogger):
    def __init__(self) -> None:
        self.__buffer: List[str] = []

    def log(self, message: str) -> None:
        self.__buffer.append(message)

    @property
    def buffer(self) -> List[str]:
        return self.__buffer

def get_default_logger() -> ILogger:
    return StdoutLogger()
