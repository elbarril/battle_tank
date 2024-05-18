from models import Game
from views import GameView, TK_KEYBOARD
from models import GameModeManager
from models import GameStateManager


def toggle_fullscreen():
    game_view.fullscreen = not game_view.fullscreen


def toggle_pause():
    if state_manager.is_level_paused:
        state_manager.level_playing()
    else:
        state_manager.level_paused()


def start():
    global game_p_bind, game_space_bind
    game_p_bind = game_view.bind(TK_KEYBOARD.P, lambda e: toggle_pause())
    game_view.unbind(TK_KEYBOARD.UP, menu_up_bind)
    game_view.unbind(TK_KEYBOARD.DOWN, menu_down_bind)
    game_view.unbind(TK_KEYBOARD.SPACE, game_space_bind)
    state_manager.players_ready()
    state_manager.level_ready()
    state_manager.level_playing()


# game_model = Game()
game_view = GameView(fullscreen=False)

state_manager = GameStateManager()
state_manager.add_observer(game_view)
state_manager.game_init()

mode_manager = GameModeManager()
menu_frame = game_view.set_menu_frame(
    mode_manager.all_modes, mode_manager.mode)
mode_manager.add_observer(menu_frame)

game_escape_bind = game_view.bind(TK_KEYBOARD.ESC, lambda e: quit())
game_f_bind = game_view.bind(TK_KEYBOARD.F, lambda e: toggle_fullscreen())

menu_down_bind = game_view.bind(
    TK_KEYBOARD.DOWN, lambda e: mode_manager.set_two_players())
menu_up_bind = game_view.bind(
    TK_KEYBOARD.UP, lambda e: mode_manager.set_one_player())

game_space_bind = game_view.bind(TK_KEYBOARD.SPACE, lambda e: start())

game_view.mainloop()
