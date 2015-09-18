"""
game_core.py contains core game mechanic for dungeon game
(DOC incomplete)
"""
import random, sys
import game_grid


def game_status(pieces):
    """Check win status.
    Returns False if nothing happened.
    Returns win/loss message str if something happened.
    """
    player_loc = get_last_loc('player', pieces)
    monster_loc = get_last_loc('monster', pieces)
    door_loc = get_last_loc('door', pieces)

    if player_loc == door_loc:
        return '\nPlayer found exit!'
    elif monster_loc == player_loc:
        return '\nMonster ate player'
    else:
        return False


def get_last_loc(name, pieces):
    """Retrieve most recent trace of piece.
    """
    if name in pieces:
        return pieces[name]['trace'][-1] #Doing [-1:] return as list


def move_manual(trace, dirs, grid):
    """Return new (x,y) that belongs to grid by user picked direction."""
    dest = None
    last_loc = trace[-1]
  
    while(dest not in grid):
        new_dir = input('Choose direction: ').lower()

        # Note: Pretty messy upto return satement. Can I refactor this?
        if new_dir == 'quit':
            print("\nBye\n")
            sys.exit()

        if new_dir in dirs:
            dest = game_grid.add_vector(last_loc, dirs[new_dir])
            if dest not in grid:
                print("\nYou hit a wall but warewolf is keep looking for you.\n")
                return last_loc #Adds penalty for hitting wall.
        else:
            print("""\nYou try to move but it appears that your anxiety has lost sense of direction.
                \rYou take a breath and try to move again.\n""")

    return dest


def move_random(trace, dirs, grid):
    """Returns new (x,y) that belongs to grid by randomly picked direction.
    """
    dest = None
    last_loc = trace[-1]
    dirs = list(dirs.values())
    
    while(dest not in grid):
        rand_dir = random.choice(dirs)
        dest = game_grid.add_vector(last_loc, rand_dir)

    return dest


def nchoices(choices, n = 1):
    """Randomly choose unique n..items from iterable and return it as a list."""
    result = []
    
    while (len(result) < n):
        loc = random.choice(choices)
        if loc not in result:
            result.append(loc)

    return result


def set_pieces(pieces, grid):
    """Assign random starting co-ordinates to each pieces."""
    locations = nchoices(grid, len(pieces))

    try:
        for key in pieces:
            piece = pieces[key]
            piece['trace'].append(locations.pop())
   
        return True

    except BaseException as E:
        print(E)
        return False


def start_game(pieces, dirs, grid):
    """Start game
    """
    info = """
Contorls (quit to exit)           Map

  nw  n  ne               (0, 2) (1, 2) (2, 2)
  w       e               (0, 1) (1, 1) (2, 1)
  sw  s  se               (0, 0) (1, 0) (2, 0)
    """ 
    # Initialize start location
    set_pieces(pieces, grid)

    # Examine current status <- this should always be false
    status = game_status(pieces)
    
    print(info)
    print('\nNight has fall, you hear footsteps of a warewolf vigorously looking for you. ' + 
          'You must find exit through this darkness.\n')
    print("You can't see anything in this dark but you know that you were standing at {}.\n".
            format(get_last_loc('player', pieces)))

    while (status == False):
        print("Nothing has happened so far....\n")
        take_turn(pieces, dirs, grid)

        #Examine game status
        status = game_status(pieces)

        # If status returned something meaningful
        if (status):
            print(status)
            break


def take_turn(pieces, dirs, grid):
    """Update moves of movable game pieces.
    """
    # Get trace
    player_loc = pieces['player']['trace']
    monster_loc = pieces['monster']['trace']
    
    # Make move
    player_move = move_manual(player_loc, dirs, grid)
    monster_move = move_random(monster_loc, dirs, grid)

    # Update move
    player_loc.append(player_move)
    monster_loc.append(monster_move)
