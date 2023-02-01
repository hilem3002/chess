# function for empty playground creating as a 2D list
def play_ground_creating():
    play_ground = []
    
    # used nested loops to create a 2D list
    for line in range(8):
        line_list = []
        play_ground.append(line_list)
        for column in range(8):
            line_list.append(" ")

    return play_ground

# function for character placement to empty playground
def character_placement(play_ground):
    # placed the P as white powns
    for big_pown in range(8):
        play_ground[6][big_pown] = "P"
        
    # these are other white characters; K:castle, A:knight, F:bishop, V:queen, Ş:king
    other_characters_big = ["K", "A", "F", "V", "Ş", "F", "A", "K"]
    
    # placed the other white characters
    for character_index in range(8):
        play_ground[7][character_index] = other_characters_buyuk[character_index]
    
    # placed the p as black powns
    for small_pown in range(8):
        play_ground[1][small_pown] = "p"
    
    # these are other black characters; k:castle, a:knight, f:bishop, v:queen, ş:king
    other_characters_small = ["k", "a", "f", "v", "ş", "f", "a", "k"]
    
    # placed the other black characters
    for character_index_2 in range(8):
        play_ground[0][character_index_2] = other_characters_small[character_index_2]

# function for printing the playground that is actually seems like a chess playground
def play_ground_printing(play_ground):
    print("    A", "  B", "  C", "  D", "  E", "  F", "  G", "  H")

    for line_index in range(8):
        print("  ---------------------------------")

        for column_index in range(8):
            if column_index == 0:
                print(f"{8 - line_index}", end="")
            if sutun_index == 7:
                print(f" |", play_ground[line_index][column_index], f"| {8 - line_index}")
            else:
                print(" |", play_ground[line_index][column_index], end="")

    print("  ---------------------------------")
    print("    A", "  B", "  C", "  D", "  E", "  F", "  G", "  H")

# function for getting the direction of motion
def taking_direction_of_motion():
    current_location = input("current location: ")
    target_location = input("target location: ")

    return current_location, target_location

# function for motion and eating algorithm
def motion_eating_algorithm(play_ground, current_location, target_location, location_dict):
    # understand the current location as indexes
    current_line_index = 8 - int(current_location[0])
    current_column_index = location_dict[current_location[1]]
    
    # understand the target location as indexes
    target_line_index = 8 - int(target_location[0])
    target_column_index = location_dict[target_location[1]]
    
    # control if there is a character that you want to go and eat
    if play_ground[target_line_index][target_column_index] != " ":
        play_ground[target_line_index][target_column_index] = " "

    character = play_ground[current_line_index][current_column_index]
    play_ground[current_line_index][current_column_index] = " "
    play_ground[target_line_index][target_column_index] = character


def main():
    # dictionary for letters as indexes
    location_dict = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
    a = play_ground_creating()
    character_placement(a)
    c = True
    while c == True:
        play_ground_printing(a)
        print()
        b = list(taking_direction_of_motion())
        motion_eating_algorithm(a, b[0], b[1], location_dict)


main()
