from mcwb.api import polygon

from mciwb import Direction, Item, get_client


def build_pagoda(pos, width=9, floor_height=4, item: Item = Item.GOLD_BLOCK):
    """
    Create a pagoda out of blocks at the given position.
    """

    c = get_client()

    level = 0
    for floor_width in range(width, 2, -2):

        base = pos + Direction.UP * level * floor_height
        balcony = base + Direction.UP * (floor_height - 1)

        polygon(c, balcony, 1, floor_width + 2, sides=4, item=item)
        polygon(c, base, floor_height, floor_width, sides=4, item=item)

        level += 1
