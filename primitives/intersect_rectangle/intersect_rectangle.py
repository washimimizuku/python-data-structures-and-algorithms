import collections

Rectangle = collections.namedtuple('Rectangle', ('x', 'y', 'width', 'height'))

def intersect_rectangle(R1, R2): # O(1)
    def is_intersect(R1, R2):
        return (R1.x <= R2.x + R2.width and R1.x + R1.width >= R2.x
                and R1.y + R2.height and R1.y + R1.height >= R2.y)
    
    if not is_intersect(R1, R2):
        return Rectangle(0, 0, -1, -1) # No intersection.
    
    return Rectangle(
        max(R1.x, R2.x),
        max(R1.y, R2.y),
        max(R1.x + R1.width, R2.x + R2.width) - max(R1.x, R2.x),
        max(R1.y + R1.height, R2.y + R2.height) - max(R1.y, R2.y)
    )

assert(intersect_rectangle(Rectangle(1, 2, 3 ,4), Rectangle(5, 3, 2 ,4))) == Rectangle(0, 0, -1, -1)
assert(intersect_rectangle(Rectangle(1, 2, 3 ,4), Rectangle(2, 2, 2 ,4))) == Rectangle(2, 2, 2, 4)