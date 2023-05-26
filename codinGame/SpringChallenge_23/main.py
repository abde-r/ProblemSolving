import sys

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
egg_pos = []
crystal_qty = []
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
        neighbors = list(filter(lambda id: id > -1,[neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5])),
        my_ants = 0,
        opp_ants = 0
    )
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

# game loop
while True:
    crystal_pos = []
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
                egg_pos.append(i)
            elif cells[i].cell_type == 2:
                # check if the neighbors of the crystal cell is some other crystal
                # if _is_neighbor_of_crystal_crystal():
                crystal_pos.append(i)
            crystal_qty.append(resources)

    # check if some eggs are around the base
    close_eggs = []
    # sorted(crystal_pos)
    if _are_eggs_around_base(cells, cells[my_bases[0]], close_eggs):
        # go for eggs only first
        for i in range(len(close_eggs)):
            print("eggs around", close_eggs[i], file=sys.stderr, flush=True)
            print('LINE ' + str(my_bases[0]) + ' ' + str(close_eggs[i]) + ' ' + str(1) , end=';')
            # print('BEACON ' + str(close_eggs[i]) + ' ' + str(1) , end=';')
    else:
        # the normal routine
    # if cells.neighbors[neigh_0].cell_type == 1:

    # print("resources type: ", cells[i].cell_type, file=sys.stderr, flush=True)
    # sorted(crystal_pos)
    # for i in range(len(crystal_pos)):
    #     print("poses: ", crystal_pos[i], " qty: ", crystal_qty[i], file=sys.stderr, flush=True)
        for i in range(len(crystal_pos)):
                # print('BEACON 2 1;BEACON 6 1;BEACON 23 1;BEACON 16 1;BEACON 28 1;BEACON 21 1')
            # print("distance", my_bases[0] - crystal_pos[i], file=sys.stderr, flush=True)
            # if my_bases[0] - crystal_qty[i] < 50:


            print('LINE ' + str( my_bases[0]) + ' ' + str(crystal_pos[i]) + ' ' + str(1) , end=';')
            # else:
            #     print('LINE ' + str( my_bases[0]) + ' ' + str(crystal_pos[i]) + ' ' + str(1) , end=';')
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

