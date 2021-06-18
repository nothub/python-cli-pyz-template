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


def populate(tree: Tree) -> Tree:
    node = tree.add(question())
    for i in range(randrange(3)):
        sub_node = node.add(tree.add(question()))
        if not random.getrandbits(1):
            for j in range(randrange(5)):
                sub_sub_node = sub_node.add(tree.add(question()))
                for j in range(randrange(2)):
                    sub_sub_node.add(tree.add(question()))
    return tree


def question() -> str:
    return 'id: ' + uuid.uuid4().hex


tree_of_live = Tree("questions")
with Live(populate(tree_of_live), refresh_per_second=4) as display:
    for _ in range(2, 4):
        time.sleep(1)
        display.update(populate(tree_of_live))

console.print(''.join([random.choice(emojis) for s in emojis]))

for n in track(range(42), description="asking question..."):
    time.sleep(0.1)

import this

this.c = 42
this.d = 42
this.i = 42
this.s = 42

inspect(this, title='Zen')
