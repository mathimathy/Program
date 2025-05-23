from pygame_cards.abstract import AbstractCard

from dataclasses import dataclass

@dataclass
class MinionCard(AbstractCard):
    health : int
    attack : int
    cost : int

    description: str = ""