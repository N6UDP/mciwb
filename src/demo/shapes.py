from mciwb import Direction, Item, Position, world

print("loading cool stuff")


def box(start: Position, size: int, item=Item.ACACIA_FENCE):
    """
    makes a cube of blocks with SW bottom corner at start

    Factored for easy understanding
    """

    # calculate the position of the NW bottom corner
    opposite = start + (Direction.EAST + Direction.NORTH) * (size - 1)

    # make rows of walls
    for up in range(size):
        # make a rows for each of the four walls
        for east in range(size):
            block_pos = start + Direction.EAST * east + Direction.UP * up
            world.set_block(block_pos, item)
            block_pos = opposite - Direction.EAST * east + Direction.UP * up
            world.set_block(block_pos, item)
        for north in range(size):
            block_pos = start + Direction.NORTH * north + Direction.UP * up
            world.set_block(block_pos, item)
            block_pos = opposite - Direction.NORTH * north + Direction.UP * up
            world.set_block(block_pos, item)

    for up in [0, size - 1]:
        for east in range(size):
            for north in range(size):
                block_pos = (
                    start
                    + Direction.NORTH * north
                    + Direction.EAST * east
                    + Direction.UP * up
                )
                world.set_block(block_pos, item)


def pyramid(start: Position, size: int, item=Item.CARVED_PUMPKIN, **kwargs):
    # make rows of walls
    row_size = size
    row_start = start
    for up in range(size):
        opposite = row_start + (Direction.EAST + Direction.NORTH) * (row_size - 1)
        # make a rows for each of the four walls
        for east in range(row_size):
            block_pos = row_start + Direction.EAST * east + Direction.UP * up
            world.set_block(block_pos, item, **kwargs)
            block_pos = opposite - Direction.EAST * east + Direction.UP * up
            world.set_block(block_pos, item, **kwargs)
        for north in range(row_size):
            block_pos = row_start + Direction.NORTH * north + Direction.UP * up
            world.set_block(block_pos, item, **kwargs)
            block_pos = opposite - Direction.NORTH * north + Direction.UP * up
            world.set_block(block_pos, item, **kwargs)

        row_start += Direction.EAST + Direction.NORTH
        row_size -= 2
        if row_size <= 0:
            break
