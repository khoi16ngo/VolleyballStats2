from models.player import Player

def askForPlayers() -> list:    
    """
    Prompt the user for the number of players and their names.
    Returns list of Player objects.
    """

    players = []
    print("Please enter the names and numbers of the players on the team.")
    while True:
        # Get player name
        playerName = input("Enter player name: ").strip().title()
        if playerName == "":
            print("No player name entered. Please try again.")
            continue

        # Get player number
        playerNumber = input("Enter player number: ").strip()
        if playerNumber == "":
            print("No player number entered. Please try again.")
            continue
        elif not playerNumber.isnumeric():
            print("Invalid player number entered. Please try again.")
            continue
        elif int(playerNumber) >= 100 or int(playerNumber) < 0:
            print("Invalid player number entered. Must be between 0 and 100. Please try again.")
            continue
        
        # Add player to list
        print(f"Adding player ... {playerName} ({playerNumber})")
        players.append(Player(playerName, int(playerNumber)))

        # Ask if there are more players
        while True:
            exit = input("Are there more players? (y/n): ").strip().lower()
            if exit == "y":
                break
            elif exit == "n":
                return players
            else:
                print("Invalid input. Please enter 'y' or 'n'.")