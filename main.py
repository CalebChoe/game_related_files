
print("cool code written by Caleb")
def poison(damage, duration):
    def attack(damage, count):
        if count == duration // 4:
            print("meow")
            return

        else:
            # time.sleep(duration//4)
            print(f"Poison dealt {damage} damage.")
            count += 1
            damage += 2
            attack(damage, count)

    attack(damage, 0)


poison(10, 20)

lst = ["Joshua", "Jin", "Sa,", "Sa,", "meow", "meow", "Witch"]


def simplify(d):
    c = dict()
    for value in d:
        if value in c:
            c[value] += 1
        else:
            c[value] = 1
    return c


print(simplify(lst))


def solve_maze(maze, start, end):
    """
    Solve the maze using recursion.

    Parameters:
        maze (list): 2D list representing the maze.
        start (tuple): Starting position in the maze.
        end (tuple): Ending position in the maze.

    Returns:
        (list): List of positions representing the path from start to end, or None if no path is found.
    """

    # Define the recursive function.
    def solve(current):
        # Check if we've reached the end of the maze.
        if current == end:
            return [current]

        # Check if the current position is a valid move.
        row, col = current
        if 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] == 0:
            # Mark the current position as visited.
            maze[row][col] = -1

            # Recursively check the neighboring positions.
            for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):

                next_pos = (row + dr, col + dc)
                path = solve(next_pos)
                if path is not None:
                    # Add the current position to the path and return it.
                    return [current] + path

            # If no valid path is found, un mark the current position and return None.
            maze[row][col] = 0

        return None

    # Call the recursive function starting from the starting position.
    return solve(start)


print(solve_maze(
    [[0, 0, 0, 1, 1, 1, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1],
     [0, 0, 0, 1, 1, 1, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1]], (0, 0),
    (7, 7)))


class monster:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.dx = x - 0.5 * w
        self.dx2 = x + 0.5 * w
        self.dy = y - 0.5 * w
        self.dy2 = y + 0.5 * w


class player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def collision_detect(self, x, y, otx, otx2, oty, oty2):
        self.x = x
        self.y = y
        print(x, y, otx, otx2, oty, oty2)

        def pois(damage, duration):
            def attack(damage, count):
                if count == duration // 4:
                    print("meow")
                    return

                else:
                    # time.sleep(duration//4)
                    print(f"Poison dealt {damage} damage.")
                    count += 1
                    damage += 2
                    attack(damage, count)

            attack(damage, 0)

        if otx >= x >= otx2 and oty >= y >= oty2:
            print("Collision detected")
            pois(10, 20)
        else:
            print("No collision detected")


me = player(3, 5)
witch = monster(8, 6, 20, 30)

me.collision_detect(me.x, me.y, witch.dx2, witch.dx, witch.dy2, witch.dy)


def slime():
    global slime
    slime_t = [100]
    slime = slime_t[0]
    each = {}
    print(slime_t)
    while slime_t != []:
        '''
        for slime in slime_t:
            if slime in slime_t:
                print(each[slime])
                each[slime] += 1
            else:
                each[slime] = 1
        print(each)
        '''
        if slime == 100:
            print("A")
            slime_t.append(25)
            slime_t.append(25)
            slime_t.append(25)
            slime_t.append(25)
            slime_t.remove(100)
            slime = 25
        elif slime == 25:
            print("B")
            slime_t.remove(25)
            slime_t.append(5)
            slime_t.append(5)
            slime_t.append(5)
            slime_t.append(5)
            slime_t.append(5)
            slime = 5
            if 25 in slime_t:
                slime = 25
        elif slime == 5:
            print("C")
            slime_t.remove(5)
        print(f"You attacked the {slime}.")
        print(slime_t)

slime()

'''
-//
-%
-recursion
-tuples

Refer to my code and create maze solver for 8x8 maze.
pygame collision practice
witch poison collision

Code that starts with 100x100 sized slime. When dealt damage, it becomes four of 25x25 slimes. Afterward, if slime gets hit when it is less than 5x5 size, it dies.
Use recursion to get this done. Also use dictionary to keep track of how many slimes there are for each size. Can use class or list. 

'''
