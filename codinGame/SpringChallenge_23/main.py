import sys

# BFS algorithm
def _BFS_(graph, start, goal):
    explored = []
    queue = [[start]]
    if start == goal:
        # print("Same Node")
        print("Same Node", file=sys.stderr, flush=True)
        return
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored and node != -1:
            neighbours = graph[node]
            # print("***BFS for cystal: ", goal, file=sys.stderr, flush=True)
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    return new_path
            explored.append(node)
            # print("BFS explored", explored, file=sys.stderr, flush=True)
    return []

def lemme_cook_paths( bfs_list, cooked_paths ):
    print("lemme cook paths for: " , bfs_list, cooked_paths, file=sys.stderr, flush=True)

def get_pathGoals( bfs_list, cooked_paths ):
    # print("we cooking here" , bfs_list[len(bfs_list)-1:], file=sys.stderr, flush=True)
    cooked_paths.append(int(bfs_list[len(bfs_list)-1:][0]))

def check_neighbors_of_theGoal( bfs_list, cooked_paths ):
    _is_lefty = 0
    new_cooked_path = []
    commun_paths = []
    for i in range(len(cooked_paths)):
        print("test test: " , cooked_paths, " ----- " , cells[cooked_paths[i]].neighbors, file=sys.stderr, flush=True)
        if any(x in cooked_paths for x in cells[cooked_paths[i]].neighbors):
            commun_paths.append(bfs_list[i])
            # print("we got some cooked paths to seeee: " , cooked_paths[i], file=sys.stderr, flush=True)
            # print("suuuuuuuuiiii: " , cooked_paths[len(cooked_paths)-1], cells[cooked_paths[i]].neighbors[2:5], file=sys.stderr, flush=True)
            # if cooked_paths[len(cooked_paths)-1] in cells[cooked_paths[i]].neighbors[2:5]:
            #     print("we got some lefty cooked paths: " , cooked_paths[i], file=sys.stderr, flush=True)
            #     _is_lefty = 1
            # else:
            #     print("we got some righty cooked paths: " , cooked_paths[i], file=sys.stderr, flush=True)
            #     _is_lefty = 0
    print("commun shit: " , commun_paths, file=sys.stderr, flush=True)

        # print("the goal for:" , bfs_list[i], " is ", bfs_list[i][:len(str(bfs_list[i]))-1], file=sys.stderr, flush=True)

def is_neighbore_crystal(bfs_list, li_fihom):
    # for i in range(len(bfs_list)):
    # commun_stuff = []
    for x in range(6):
        # print("debuggg li fihom: " , cells[cells[bfs_list[len(bfs_list)-1]].neighbors[x]].cell_type, file=sys.stderr, flush=True)
        if cells[cells[bfs_list[len(bfs_list)-1]].neighbors[x]].cell_type == 2:
            li_fihom.append(bfs_list)
            print("the case for: " , bfs_list, " with: ",  cells[bfs_list[len(bfs_list)-1]].neighbors[x], file=sys.stderr, flush=True)
            if bfs_list not in commun_stuff:
                commun_stuff.append(bfs_list)
    print("commun stuff: " , commun_stuff, file=sys.stderr, flush=True)


def _are_eggs_around_base(cells, cell, close_eggs):
    print("jiran: ", cell.neighbors, file=sys.stderr, flush=True)
    for i in range(len(cell.neighbors)):
        print("neighghghghghgh", cells[cell.neighbors[i]].cell_type, file=sys.stderr, flush=True)
        if cells[cell.neighbors[i]].cell_type == 1 and cells[cell.neighbors[i]].resources:
            close_eggs.append(cell.neighbors[i])
    # print("jiran 0: ", cell.neighbors[0], file=sys.stderr, flush=True)
    # print("jiran 1: ", cell.neighbors[1], file=sys.stderr, flush=True)
    # print("jiran 2: ", cell.neighbors[2], file=sys.stderr, flush=True)
    # print("jiran 3: ", cell.neighbors[3], file=sys.stderr, flush=True)
    # print("jiran 4: ", cell.neighbors[4], file=sys.stderr, flush=True)
    # print("jiran 5: ", cell.neighbors[5], file=sys.stderr, flush=True)
    # print('gg')
    if len(close_eggs):
        return 1
    print("eggs are here", close_eggs, file=sys.stderr, flush=True)
    return 0

def get_eggs_around_base(cells, cell, egg_pos, close_eggs, ma_base):
    for i in range(len(egg_pos)):
        if len(_BFS_(map_graph,ma_base, egg_pos[i])) <= 3 and cells[egg_pos[i]].resources > 5:
            close_eggs.append(egg_pos[i])
    if len(close_eggs)>1:
        return 1
    print("eggs are here", close_eggs, file=sys.stderr, flush=True)
    return 0

def get_eggs_around_base_v2(cells, cell, egg_pos, close_eggs, ma_base):
    for i in range(len(egg_pos)):
        if len(_BFS_(map_graph, ma_base, egg_pos[i])) <= 3:
            close_eggs.append(egg_pos[i])
    if len(close_eggs):
        return 1
    print("eggs are here v2", close_eggs, file=sys.stderr, flush=True)
    return 0



# def _are_crystals_around_base(cells, cell, close_crystals):
#     print("jiran: ", cell.neighbors, file=sys.stderr, flush=True)
#     for i in range(len(cell.neighbors)):
#         print("neighghghghghgh", cells[cell.neighbors[i]].cell_type, file=sys.stderr, flush=True)
#         if cells[cell.neighbors[i]].cell_type == 2 and cells[cell.neighbors[i]].resources:
#             close_crystals.append(cell.neighbors[i])
#     # print("jiran 0: ", cell.neighbors[0], file=sys.stderr, flush=True)
#     # print("jiran 1: ", cell.neighbors[1], file=sys.stderr, flush=True)
#     # print("jiran 2: ", cell.neighbors[2], file=sys.stderr, flush=True)
#     # print("jiran 3: ", cell.neighbors[3], file=sys.stderr, flush=True)
#     # print("jiran 4: ", cell.neighbors[4], file=sys.stderr, flush=True)
#     # print("jiran 5: ", cell.neighbors[5], file=sys.stderr, flush=True)
#     # print('gg')
#     if len(close_crystals):
#         return 1
#     print("crystals are here", close_crystals, file=sys.stderr, flush=True)
#     return 0

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

####
# crystal_pos = []
# egg_pos = []
crystal_qty = []
map_graph = {}
commun_stuff = []
# close_eggs = []
####
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

print("my bases: ", my_bases, file=sys.stderr, flush=True)
print("op bases: ", opp_bases, file=sys.stderr, flush=True)
# game loop

cooked_paths = []
li_fihom = []

while True:
    crystal_pos = []
    egg_pos = []
    print("graph", map_graph, file=sys.stderr, flush=True)
    # _BFS_(map_graph, 3, 23)
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
                # if cells[i].resources > 20:
                egg_pos.append(i)
            elif cells[i].cell_type == 2:
                # check if the neighbors of the crystal cell is some other crystal
                # if _is_neighbor_of_crystal_crystal():
                crystal_pos.append(i)
            crystal_qty.append(resources)
    print("howwww", file=sys.stderr, flush=True)
    
    
    for base in range(len(my_bases)):    
        print("~~~~~~~~~ base num: ", my_bases[base], file=sys.stderr, flush=True)
        # check if some eggs are around the base
        close_eggs = []
        close_crystals = []
        printed_cells = []
        # sorted(crystal_pos)
        # if _are_eggs_around_base(cells, cells[my_bases[0]], close_eggs):
        if get_eggs_around_base(cells, cells[my_bases[base]], egg_pos, close_eggs, my_bases[base]):
            # go for eggs only first
            print("eggs around", close_eggs, file=sys.stderr, flush=True)
            for i in range(len(close_eggs)):
                # print('LINE ' + str(my_bases[0]) + ' ' + str(close_eggs[i]) + ' ' + str(5) , end=';')
                # print('LINE ' + str(close_eggs[i]) + ' ' + str(my_bases[0]) + ' ' + str(5) , end=';')
                bfs_list = _BFS_(map_graph, my_bases[base], close_eggs[i])
                # print("bfs path for close egg: ", len(bfs_list), file=sys.stderr, flush=True)
                for x in range(len(bfs_list)):
                    # print("bfs dyal i: ", bfs_list[x], file=sys.stderr, flush=True)
                    if bfs_list[x] not in printed_cells:
                        print('BEACON ' + str(bfs_list[x]) + ' ' + str(1) , end=';')
                        printed_cells.append(bfs_list[x])
            
            # for i in range(len(crystal_pos)):
            #     print('LINE ' + str( my_bases[0]) + ' ' + str(crystal_pos[i]) + ' ' + str(1) , end=';')
            # if _are_crystals_around_base(cells, cells[my_bases[0]], close_crystals):
            #     # go for crystals around base with BEACON commande
            #     for i in range(len(close_crystals)):
            #         # print("eggs around", close_eggs[i], file=sys.stderr, flush=True)
            #         print('BEACON ' + str(close_crystals[i]) + ' ' + str(1) , end=';')
        else:
            # the normal routine
        # if cells.neighbors[neigh_0].cell_type == 1:

            print("noo eggs", file=sys.stderr, flush=True)
        # sorted(crystal_pos)
        # for i in range(len(crystal_pos)):
        #     print("poses: ", crystal_pos[i], " qty: ", crystal_qty[i], file=sys.stderr, flush=True)

            close_crystals = []
            fare_ones = []
                
            get_eggs_around_base_v2(cells, cells[my_bases[base]], egg_pos, close_eggs, my_bases[base])
            if not len(close_eggs):
                # lines
                for i in range(len(crystal_pos)):
                    bfs_list = _BFS_(map_graph, my_bases[base], crystal_pos[i])
                    # cooked_paths = []
                    # get_pathGoals(bfs_list, cooked_paths)
                    # check_neighbors_of_theGoal(bfs_list, cooked_paths)
                    is_neighbore_crystal(bfs_list, li_fihom)
                    # print("bfs path for close egg: ", len(bfs_list), file=sys.stderr, flush=True)
                    for x in range(len(bfs_list)):
                        if bfs_list[x] not in printed_cells:
                            print('BEACON ' + str(bfs_list[x]) + ' ' + str(1) , end=';')
                            printed_cells.append(bfs_list[x])
            else:
                print("no eggs around!! goo for crystal!!!!!!", close_eggs, file=sys.stderr, flush=True)
                # we print the close ones first
                for i in range(len(crystal_pos)):
                    bfs_list = _BFS_(map_graph, my_bases[base], crystal_pos[i])
                    # print("bfs path for close egg: ", len(bfs_list), file=sys.stderr, flush=True)
                    # cooked_paths = []
                    # get_pathGoals(bfs_list, cooked_paths)
                    # check_neighbors_of_theGoal(bfs_list, cooked_paths)
                    is_neighbore_crystal(bfs_list, li_fihom)
                    for x in range(len(bfs_list)):
                        if bfs_list[x] not in printed_cells:
                            print('BEACON ' + str(bfs_list[x]) + ' ' + str(1) , end=';')
                            printed_cells.append(bfs_list[x])
                # print("bfs path for close egg: ", len(eggs_bfs_list), file=sys.stderr, flush=True)
                # mn b33d
                for i in range(len(close_eggs)):
                    eggs_bfs_list = _BFS_(map_graph, my_bases[base], close_eggs[i])
                    for x in range(len(eggs_bfs_list)):
                        # print("bfs dyal i: ", eggs_bfs_list[x], file=sys.stderr, flush=True)
                        if eggs_bfs_list[x] not in printed_cells:
                            print('BEACON ' + str(eggs_bfs_list[x]) + ' ' + str(1) , end=';')
                            printed_cells.append(eggs_bfs_list[x])
                        # print('BEACON ' + str(eggs_bfs_list[x]) + ' ' + str(1) , end=';')
                        # print('LINE ' + str(my_bases[0]) + ' ' + str(crystal_pos[i]) + ' ' + str(1) , end=';')
                    # print('LINE ' + str(crystal_pos[i]) + ' ' + str(my_bases[0]) + ' ' + str(1) , end=';')
            
            # for i in range(len(egg_pos)):
            #     print('LINE ' + str(my_bases[0]) + ' ' + str(egg_pos[i]) + ' ' + str(5) , end=';')
            
                # if crystal_pos[i] in cells[my_bases[0]].neighbors:
                #     close_crystals.append(crystal_pos[i])
                #     print("close crystal",crystal_pos[i], file=sys.stderr, flush=True)
                # else:
                #     fare_ones.append(crystal_pos[i])
                #     print("fare crystal", crystal_pos[i], file=sys.stderr, flush=True)

            # for i in range(len(close_crystals)):
            #     print('BEACON ' + str(close_crystals[i]) + ' ' + str(1) , end=';')
            
            # for i in range(len(fare_ones)):
            #     # get the short path from base or its neighbors
            #     temp_start_point = BFS(map_graph, cells[my_bases[0]], fare_ones[i])
            #     for i in cells[my_bases[0]].neighbors:
            #         if temp_start_point < BFS(map_graph, cells[my_bases[0]].neighbors[i], fare_ones[i]):
            #             temp_start_point = BFS(map_graph, cells[my_bases[0]].neighbors[i], fare_ones[i])

            #     print('LINE ' + str(temp_start_point) + ' ' + str(fare_ones[i]) + ' ' + str(1) , end=';')
        print('WAIT' , end=';')
            
    print()

    # for i in range(len(cells)):
    #     if cells[i].resources:
    #         print('BEACON', i, 2)
    #         print('BEACON', i, 4)
            


    # WAIT | LINE <sourceIdx> <targetIdx> <strength> | BEACON <cellIdx> <strength> | MESSAGE <text>
    # actions = []
    # print("base pos: ", my_bases[0])
    
    # for now
    # _pos = my_bases[0]
    # for i in range(len(cells)):
    #     if cells[i].resources:
    #         actions.append('BEACON '+str(i)+' '+str(2))

    # TODO: choose actions to perform and push them into actions
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    # if len(actions) == 0:
    #     print('WAIT')
    # else:
    #     print(';'.join(actions))

