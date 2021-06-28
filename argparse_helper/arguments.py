import argparse

from abc import (
    ABC,
    abstractmethod,
)


class ArgumentGroup(ABC):
    name: str

    @abstractmethod
    def __call__(self, parser: argparse.ArgumentParser):
        ...
