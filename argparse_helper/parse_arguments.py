import argparse

from abc import (
    ABC,
    abstractmethod,
)


class ParseArgs(ABC):
    @abstractmethod
    def __call__(self, args: argparse.Namespace):
        ...
