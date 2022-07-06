from models.Random import Random
from models.Cautious import Cautios
from models.Demanding import Demanding
from models.Impulsive import Impulsive
from models.Player import Player
from models.Property import Property
from models.Board import Board
import random


class Monopoly:
    def __init__(self, num_simulations: int, time_out: int, num_properties: int):
        self.players = self._get_players()
        self.board: Board = Board()
        self.time_out = time_out
        self.num_simulations = num_simulations
        self.num_properties = num_properties
        self.total_match = 0
        self.total_match_finished_by_timeout = 0
        self.total_matches_with_wins = 0
        self.wins = dict()
        self.total_turns_per_match = dict()

    def _get_players(self):
        return [
            Impulsive("Impulsivo"),
            Demanding("Exigente"),
            Cautios("Cauteloso"),
            Random("Aleatório")
        ]

    def _populate_random_board(self):
        for i in range(self.num_properties):
            property = f"Property-{i}"
            self.board.add_property(
                Property(name=property, buy_price=random.choice(range(50, 220)),
                         rent_price=random.choice(range(50, 100)))
            )

    def _play_game(self):
        self._new_board()
        self._play()

    def _new_board(self):
        self.board: Board = Board()
        self.board.add_players(self.players)
        self._populate_random_board()

    def _play(self):
        while len(self.board.players) > 1 and self.board.round < self.time_out:
            for n, player in enumerate(self.board.players):
                if not player.in_game:
                    break
                else:
                    player.move()

                    property = self.board.properties[player.board_position]

                    if property.available_for_buy():
                        player.check_profile_purchase_property(property)

                    if property.owner is not None and property.owner is not player:
                        property.receive_rent(player)

                    if not player.validate_player_in_game():
                        self.board.remove_player(player)
                        self.board.return_property(player)
                        if len(self.board.players) == 1:
                            break

            self.board.round += 1

        if self.board.round >= self.time_out:
            self.total_match_finished_by_timeout += 1
            self._sort_balance_players()
        elif len(self.board.players) == 1:
            self.total_turns_per_match[self.total_match] = self.board.round
            self.total_matches_with_wins += 1
        self._add_wins()

    def _sort_balance_players(self):
        self.board.players.sort(key=lambda x: (x.balance, x.qty_played), reverse=True)
        return self.board.players

    def _add_wins(self):
        if self.board.players[0].name.upper() in self.wins.keys():
            self.wins[self.board.players[0].name.upper()] += 1
        else:
            self.wins[self.board.players[0].name.upper()] = 1

    def _match(self):
        while self.total_match < self.num_simulations:
            self._play_game()
            self.total_match += 1

    def _get_percent_wins(self, player: Player):
        if player.name.upper() in self.wins.keys():
            total_wins_player = self.wins[player.name.upper()]
            return '{:.2f}'.format((total_wins_player / self.num_simulations) * 100)
        return 0

    def _get_average_turn(self):
        return '{:.2f}'.format(sum(self.total_turns_per_match) / len(self.total_turns_per_match))

    def _get_most_winer_player(self):
        return max(self.wins, key=self.wins.get)

    def run(self):
        self._match()
        print(f" Partidas finalizadas por time out : {self.total_match_finished_by_timeout}")
        print(f" Média de turnos por partida : {self._get_average_turn()}")
        print(f" Porcentagem de vitórias jogador IMPULSIVO : {self._get_percent_wins(self.players[0])}")
        print(f" Porcentagem de vitórias jogador EXIGENTE : {self._get_percent_wins(self.players[1])}")
        print(f" Porcentagem de vitórias jogador CAUTELOSO :{self._get_percent_wins(self.players[2])}")
        print(f" Porcentagem de vitórias jogador ALEATÓRIO : {self._get_percent_wins(self.players[3])}")
        print(f" Comportamento que mais vence : {self._get_most_winer_player()}")
