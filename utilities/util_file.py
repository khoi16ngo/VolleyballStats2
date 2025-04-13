import mimetypes
import os
from services.stats.assist_stat_collector import get_assist_stats_headers
from services.stats.attack_stat_collector import get_attack_stats_headers
from services.stats.block_stat_collector import get_block_stats_headers
from services.stats.dig_stat_collector import get_dig_stats_headers
from services.stats.free_ball_stats import get_free_ball_stats_headers
from services.stats.serve_receive_stat_collector import get_serve_receive_stats_headers
from services.stats.serve_stat_collector import get_serve_stats_headers

def get_file_extension(file_name: str) -> str:
    '''
    Returns the file extension of the file name.
    For example, if the file name is "file.txt", the function will return "txt".
    '''
    mime_type, _ = mimetypes.guess_type(file_name)
    return mime_type

def remove_file_extension(file_name: str) -> str:
    '''
    Removes the file extension from the file name.
    For example, if the file name is "file.txt", the function will return "file".'''
    base, _ = os.path.splitext(file_name)
    return base

def get_last_n_file_path(file_path: str, number_path: int) -> str:
    '''
    Returns the last n file path from the file path.
    For example, if the file path is "/home/user/file.txt" and number_path is 2,
    the function will return "user/file.txt".
    '''
    file_path_list = file_path.split("/")
    return_file_path = []
    for i in range(0, number_path):
        return_file_path.append(file_path_list[-1-i])
    return '/'.join(reversed(return_file_path))

def get_file_headers() -> list:
    '''
    Headers will outline all types of actions and action stats for each player.
    Returns a list of headers for the players stats file.
    '''
    headers = ['Player Name']
    headers += get_attack_stats_headers()
    headers += get_block_stats_headers()
    headers += get_assist_stats_headers()
    headers += get_free_ball_stats_headers()
    headers += get_dig_stats_headers()
    headers += get_serve_receive_stats_headers()
    headers += get_serve_stats_headers()
    return headers