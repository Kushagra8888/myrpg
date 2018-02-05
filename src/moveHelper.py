def toLeft(position):
    return (position[0], position[1] - 1)

def toRight(position):
    return (position[0], position[1] + 1)

def toUp(position):
    return (position[0] - 1, position[1])

def toDown(position):
    return (position[0] + 1, position[1])