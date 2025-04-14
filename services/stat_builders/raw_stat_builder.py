from models import user_inputs
    
def build_raw_player_stats(user_inputs: user_inputs.UserInputs, raw_player_stats: list) -> dict:
    '''
    Calculate the raw player stats from the raw player stats file.
    The raw player stats file is a list of strings in the format "<player_number> <action> <quality>".
    e.g. "12 a 34"
    Returns a dictionary with the player number as the key and a dictionary of actions and qualities as the value.
    The dictionary will be in the format:
    {
        <player.number>: {
            "actions": {
                <action.value>: {
                    "qualities": {11
                        <quality.value>: count
                    }
                } 
            }
        }
    }
    '''
    # Initialize player stat dict with all actions and qualities at count 0
    calculated_player_stats = {
        player.number: {
            "actions": {
                action.value: {
                    "qualities": {
                        quality.value: 0
                        for quality in user_inputs.action_qualities
                    }
                }
                for action in user_inputs.actions
            }
        }
        for player in user_inputs.players
    }

    # Loop through each line in the raw player stats list and then add to the count for the action and quality
    for raw_player_stat in raw_player_stats:
        # Split each line into format "<play_number> <action> <quality>"
        player_number, action, quality = raw_player_stat.strip().split()
        player_number = int(player_number)
        quality = int(quality)

        # Increase count by one if action and quality performed for player
        calculated_player_stats[player_number]["actions"][action]["qualities"][quality] += 1
        
    return calculated_player_stats    