import sys

# BFS algorithm
def _BFS_(graph, start, goal):
    explored = []
    queue = [[start]]
    if start == goal:
        return []
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored and node != -1:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    return new_path
            explored.append(node)
    return []

class Paths(object):
    source: int
    target: int
    distance: int

    def __init__(self, source: int, target: int, distance: int):
        self.source = source
        self.target = target
        self.distance = distance

_paths: list[Paths] = []

class Cell(object):
    index: int
    cell_type: int
    resources: int
    neighbors: list[int]
    my_ants: int
    opp_ants: int

    def __init__(self, index: int, cell_type: int, resources: int, neighbors: list[int], my_ants: int, opp_ants: int):
        self.index = index
        self.cell_type = cell_type
        self.resources = resources
        self.neighbors = neighbors
        self.my_ants = my_ants
        self.opp_ants = opp_ants


cells: list[Cell] = []

_starting_game, _mid_game, _ending_game = 0, 0, 0
map_graph = {}

number_of_cells = int(input())  # amount of hexagonal cells in this map
for i in range(number_of_cells):
    inputs = [int(j) for j in input().split()]
    cell_type = inputs[0] # 0 for empty, 1 for eggs, 2 for crystal
    initial_resources = inputs[1] # the initial amount of eggs/crystals on this cell
    neigh_0 = inputs[2] # the index of the neighbouring cell for each direction
    neigh_1 = inputs[3]
    neigh_2 = inputs[4]
    neigh_3 = inputs[5]
    neigh_4 = inputs[6]
    neigh_5 = inputs[7]
    cell: Cell = Cell(
        index = i,
        cell_type = cell_type,
        resources = initial_resources,
        neighbors = list([neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5]),
        my_ants = 0,
        opp_ants = 0,
    )
    map_graph[cell.index] = cell.neighbors
    cells.append(cell)

    
number_of_bases = int(input())
my_bases: list[int] = []
for i in input().split():
    my_base_index = int(i)
    my_bases.append(my_base_index)
opp_bases: list[int] = []
for i in input().split():
    opp_base_index = int(i)
    opp_bases.append(opp_base_index)

_flag = 0

initial_num_of_crystal_cells = 0
initial_num_of_egg_cells = 0

initial_EGG_SUM = 0
initial_CRYS_SUM = 0

while True:
    _resources = []
    
    _ANTS_SUM = 0
    _EGG_SUM = 0
    _CRYSTAL_SUM = 0

    score = input().split()
    my_score = int(score[0])
    opp_score = int(score[1])
    for i in range(number_of_cells):
        inputs = [int(j) for j in input().split()]
        resources = inputs[0] # the current amount of eggs/crystals on this cell
        my_ants = inputs[1] # the amount of your ants on this cell
        opp_ants = inputs[2] # the amount of opponent ants on this cell

        cells[i].resources = resources
        cells[i].my_ants = my_ants
        cells[i].opp_ants = opp_ants

        if resources > 0:
            if cells[i].cell_type == 1:
                _EGG_SUM += resources
                if not _ending_game:
                    _resources.append(cells[i].index)
            elif cells[i].cell_type == 2:
                _CRYSTAL_SUM += resources
                if not _starting_game:
                    _resources.append(cells[i].index)
        
        _ANTS_SUM += my_ants
    
    if not _flag:
        initial_EGG_SUM = _EGG_SUM
        initial_CRYS_SUM = _CRYSTAL_SUM
    _flag = 1

    if _EGG_SUM / initial_EGG_SUM >= 0.65: # starting phase; eggs only
        _starting_game = 1
        _mid_game = 0
        _ending_game = 0
    elif _EGG_SUM / initial_CRYS_SUM >= 0.3: # ending phase; crystals only
        _starting_game = 0
        _mid_game = 0
        _ending_game = 1
    else: # mid phase; crystals and eggs
        _starting_game = 0
        _mid_game = 1
        _ending_game = 0
    

    for base in range(len(my_bases)):
        _source = cells[my_bases[base]].index
        for x in range(len(_resources)):
            _target = _resources[x]
            _distance = len(_BFS_(map_graph, _source, _target))#_get_distance(cells, path.sorce, path.target)
            path: Paths = Paths( source = _source, target = _target, distance = _distance )
            print("path: ", path.source, file=sys.stderr, flush=True)
            _paths.append(path)
    _paths = sorted(_paths, key=lambda x: x.distance, reverse=True)
    for i in range(0, len(_paths)//2+1):
        source = _paths[i].source
        target = _paths[i].target
        distance = _paths[i].distance

        if cells[target].cell_type == 1 and _ending_game:
            continue
        elif cells[target].cell_type == 2 and _starting_game:
            continue
        
        for x in range(0, i):
            _temp = len(_BFS_(map_graph,  _paths[x].target, _paths[i].target))
            if distance > _temp:
                source = _paths[x].target
                distance = _temp
        if distance+1 <= _ANTS_SUM:
            print('LINE ' + str(source) + ' ' + str(target) + ' ' + str(1) , end=';')
            _ANTS_SUM -= distance+1
    
    print('MESSAGE' , 'DIMA KOKAB', end=';')
            
    print()

