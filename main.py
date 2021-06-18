#!/usr/bin/env python3
import argparse
import random
import time
import uuid
from random import randrange

from rich import inspect
from rich.console import Console
from rich.live import Live
from rich.progress import track
from rich.tree import Tree

from arg_types import network_port, positive_int, non_empty_string

EMOJIS = [
    ':baby_chick:',
    ':blowfish:',
    ':cow:',
    ':dog:',
    ':elephant:',
    ':gorilla:',
    ':monkey:',
    ':see_no_evil:',
    ':hear_no_evil:',
    ':speak_no_evil:',
    ':ox:',
    ':pig:',
    ':ram:',
    ':rat:',
    ':tiger:',
    ':tropical_fish:',
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-n',
        action='store',
        type=positive_int,
        required=False,
        default=4,
        help='positive integer'
    )
    parser.add_argument(
        '-p', '--port',
        action='store',
        type=network_port,
        required=False,
        default=5000,
        help='network port (default 5000)'
    )
    parser.add_argument(
        '--string',
        action='store',
        type=non_empty_string,
        required=False,
        metavar='FOO',
        help='non empty string'
    )
    parser.add_argument(
        '--strings',
        action='extend',
        type=non_empty_string,
        nargs='+',
        required=False,
        default=list(),
        metavar='BAR',
        help='multiple non emptpy strings'
    )
    return parser.parse_args()


# pyz entrypoint
def main():
    inspect(parse_args(), value=False)
    hello_world(Console())


def hello_world(console: Console):
    tree_of_live = Tree("thinking")
    with Live(tree_of_live, refresh_per_second=4) as display:
        for _ in range(2, 5):
            node = tree_of_live.add(random.choice(EMOJIS) + ' ' + uuid.uuid4().hex)
            for i1 in range(randrange(1, 2)):
                sub_node = node.add(random.choice(EMOJIS) + ' ' + uuid.uuid4().hex)
                for j in range(randrange(2, 4)):
                    sub_sub_node = sub_node.add(random.choice(EMOJIS) + ' ' + uuid.uuid4().hex)
                    for k in range(randrange(2, 4)):
                        sub_sub_node.add(random.choice(EMOJIS) + ' ' + uuid.uuid4().hex)
            time.sleep(0.5)
            display.update(tree_of_live)
    for _ in track(range(42), description="asking..."):
        time.sleep(0.1)
    console.print(''.join([random.choice(EMOJIS) for _ in EMOJIS]))
    import this
    console.print(''.join([random.choice(EMOJIS) for _ in EMOJIS]))
    result = 0x17, 0o23
    this.i, this.s = result
    inspect(this.i + this.s)


# this will not be invoked, when called in pyz context
if __name__ == '__main__':
    main()
