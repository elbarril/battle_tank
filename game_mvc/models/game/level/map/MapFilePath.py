from os import PathLike
from utils.functions import files_from_path, extract_sub_string
from exceptions.map import NonExistentMapLevelNumber

from constants.map import MAPS_PATH, MAPS_FILENAME_PREFIX, MAPS_FILE_EXTENSION

class MapFilePath(PathLike):
    __LEVEL_MAP_NUMBERS = [extract_sub_string(level_map_file_path, MAPS_FILENAME_PREFIX, MAPS_FILE_EXTENSION) for level_map_file_path in files_from_path(MAPS_PATH)]

    def __init__(self, level_number, level_maps_path=MAPS_PATH, level_maps_filename_prefix=MAPS_FILENAME_PREFIX, level_maps_file_extension=MAPS_FILE_EXTENSION):
        if not str(level_number) in self.__LEVEL_MAP_NUMBERS:
            raise NonExistentMapLevelNumber()
        self.__file_path = level_maps_path + ((level_maps_filename_prefix + "%s" + level_maps_file_extension) % level_number)

    @classmethod
    def extract_level_number(self, file_path):
        return str.removeprefix(file_path, MAPS_FILENAME_PREFIX).removesuffix(MAPS_FILE_EXTENSION)

    def __fspath__(self):
        return self.__file_path