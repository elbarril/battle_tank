from models.player.Bot import Bot

from models.map.MapObject import MapObject
from models.map.MapObjectType import MapObjectType

from models.map.objects.BrickCompound import BrickCompound
from models.map.objects.PlayerTank import PlayerTank
from models.map.objects.BotTank import BotTank

from constants.game import FIRST_PLAYER, SECOND_PLAYER

STATIC_OBJECT_TYPES = {
    MapObjectType.BRICK: BrickCompound
}

BOT_TANK_TYPES = {
    MapObjectType.BOT_TANK: BotTank
}

PLAYER_TANK_TYPES = {
    MapObjectType.PLAYER_ONE: PlayerTank,
    MapObjectType.PLAYER_TWO: PlayerTank
}

MAP_OBJECT_TYPES = STATIC_OBJECT_TYPES | BOT_TANK_TYPES | PLAYER_TANK_TYPES


class MapObjectCreator:
    __bots:set[Bot] = set()
    __statics:set[MapObject] = set()
    __player_tanks:dict[int, PlayerTank] = {
        FIRST_PLAYER: None,
        SECOND_PLAYER: None
    }

    def _create_map_object(self, object_type, position, size):
        if not object_type in MAP_OBJECT_TYPES: return
        object_class = MAP_OBJECT_TYPES[object_type]
        map_object = object_class(position, size)
        if object_type in STATIC_OBJECT_TYPES:
            self.__statics.add(map_object)
        elif object_type in PLAYER_TANK_TYPES:
            player_number = FIRST_PLAYER if object_type is MapObjectType.PLAYER_ONE else SECOND_PLAYER
            self.__player_tanks[player_number] = map_object
        elif object_type in BOT_TANK_TYPES:
            bot = Bot(map_object)
            self.__bots.add(bot)

    @property
    def _bots(self):
        return self.__bots

    @property
    def _statics(self):
        return self.__statics

    @property
    def _player_tanks(self):
        return self.__player_tanks
