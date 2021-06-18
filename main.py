#!/usr/bin/env python3
import random
import time
import uuid
from random import randrange

from rich import inspect
from rich.console import Console
from rich.live import Live
from rich.progress import track
from rich.tree import Tree

console = Console()

emojis = [
    ':baby_chick:',
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
]


def hack(cia: Tree) -> Tree:
    node = cia.add(uuid.uuid4().hex)
    for i in range(randrange(3)):
        sub_node = node.add(cia.add(uuid.uuid4().hex))
        if not random.getrandbits(1):
            for j in range(randrange(5)):
                sub_node.add(cia.add(uuid.uuid4().hex))
    return cia


tree = Tree("heck CIA")
with Live(hack(tree), refresh_per_second=4) as live:
    for _ in range(4):
        time.sleep(0.5)
        live.update(hack(tree))

console.print(''.join([random.choice(emojis) for emoji in emojis]))

for n in track(range(42), description="dumping..."):
    time.sleep(0.1)

import this

inspect(this, title='Zen', docs=True)
