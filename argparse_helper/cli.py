from typing import (
    Union,
    Iterable,
)
import argparse
from argparse_helper.arguments import ArgumentGroup
from argparse_helper.parse_arguments import ParseArgs
from abc import (
    ABC,
)
from dataclasses import (
    dataclass,
    field,
)


class ArgsToParser(ABC):
    def __call__(
        self,
        parser: argparse.ArgumentParser,
        arguments: Iterable[ArgumentGroup],
    ):
        ...


class BasicArgsToParser(ArgsToParser):
    def __call__(
        self,
        parser: argparse.ArgumentParser,
        arguments: Iterable[ArgumentGroup],
    ):
        for argument in arguments:
            argument(parser)


@dataclass
class CLI:
    name: str
    argument_groups: Iterable[ArgumentGroup]
    arg_parser: Union[ParseArgs, None]
    args_to_parser: ArgsToParser = field(default=BasicArgsToParser())

    def __call__(self, args=None, name_space=None):
        parser = argparse.ArgumentParser(self.name)
        self.args_to_parser(parser, self.argument_groups)

        user_input = parser.parse_args(args, name_space)

        if self.arg_parser:
            return self.arg_parser(user_input)

        return user_input
