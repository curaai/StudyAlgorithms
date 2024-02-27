from itertools import product

def escape(maze):
    if not any(maze) or not any(map(any, maze)):
        return []

    h,w = len(maze), len(maze[0])
    start = next( filter(lambda p: maze[p[0]][p[1]] not in [' ', '#'], product( range(h), range(w))), None)
    exits = list( 
        filter(lambda p: maze[p[0]][p[1]] == ' ', 
        filter(lambda p: p[0] == 0 or p[1] == 0 or p[0] == (h-1) or p[1] == (w-1),
            product( range(h), range(w)))))

    if start is None or not len(exits):
        return []

    def dijkstra():
        seen = [[False for _ in range(w)] for _ in range(h)]
        path = []

        def walk(p, path):
            y,x = p
            if p in exits: 
                path.append(p)
                return True

            if y <= 0 or x <= 0 or h <= y or w <= x: return False
            if maze[y][x] == '#': return False
            if seen[y][x]: return False

            seen[y][x] = True
            _next = [
                walk((y, x-1), path),
                walk((y, x+1), path),
                walk((y-1, x), path),
                walk((y+1, x), path)]

            if any(_next):
                path.append(p)
                return True 

            return False

        walk(start, path)
        return path[::-1]

    def path2instruction(path, start_face):
        def f(cur_dir, cur_pos, next_pos):
            def inverse(dir): return (-dir[0], -dir[1])
            def swap(dir): return (dir[1], dir[0])
            next_dir  = next_pos[0] - cur_pos[0], next_pos[1] - cur_pos[1]

            if cur_dir == next_dir:
                inst = 'F'
            elif inverse(cur_dir) == next_dir:
                inst = 'BF'
            else:
                if swap(cur_dir) == next_dir:
                    inst = 'RF'
                else:
                    inst = 'LF'
                if cur_dir[0] != 0:
                    inst = 'RF'if inst == 'LF' else 'LF'

            return (inst, next_dir)

        if start_face == '>': cur_dir = (0, 1)
        elif start_face == '<': cur_dir = (0, -1)
        elif start_face == '^': cur_dir = (-1, 0)
        else: cur_dir = (1, 0)
        
        res = []
        for cur_pos, next_pos in zip(path, path[1:]):
            x = f(cur_dir, cur_pos, next_pos)
            res += x[0]
            cur_dir = x[1]

        return list(res)

    path = dijkstra()

    if len(path):
        return path2instruction(path, maze[start[0]][start[1]]) 
    else:
        return []

a = [  "#########################################",
  "#<    #       #     #         # #   #   #",
  "##### # ##### # ### # # ##### # # # ### #",
  "# #   #   #   #   #   # #     #   #   # #",
  "# # # ### # ########### # ####### # # # #",
  "#   #   # # #       #   # #   #   # #   #",
  "####### # # # ##### # ### # # # #########",
  "#   #     # #     # #   #   # # #       #",
  "# # ####### ### ### ##### ### # ####### #",
  "# #             #   #     #   #   #   # #",
  "# ############### ### ##### ##### # # # #",
  "#               #     #   #   #   # #   #",
  "##### ####### # ######### # # # ### #####",
  "#   # #   #   # #         # # # #       #",
  "# # # # # # ### # # ####### # # ### ### #",
  "# # #   # # #     #   #     # #     #   #",
  "# # ##### # # ####### # ##### ####### # #",
  "# #     # # # #   # # #     # #       # #",
  "# ##### ### # ### # # ##### # # ### ### #",
  "#     #     #     #   #     #   #   #    ",
  "#########################################"]

# print(escape(a))
print('\n'.join(map(str, list(zip(escape(a), range(1, 999))))))