from dataclasses import dataclass
from functools import cached_property
from pathlib import Path
import sys
from time import sleep
import pygame
from minion_card import MinionCard

from pygame_emojis import load_emoji

from pygame_cards.abstract import AbstractCardGraphics

from minion_set import MY_COMMUNITY_OF_THE_RING
from pygame_cards.utils import position_for_centering

@dataclass
class MinionCardGraphics(AbstractCardGraphics):

    card: MinionCard

    filepath: Path = None

    @cached_property
    def surface(self) -> pygame.Surface:
        x, y = self.size

        surf = pygame.Surface(self.size)

        if self.filepath is not None:
            picture = pygame.image.load(self.filepath)
            surf.blit(pygame.transform.scale(picture, self.size), (0,0))

        font = pygame.font.SysFont("urwgothic", 48)
        name = font.render(self.card.name, True, pygame.color(163, 146, 139))

        surf.blit(name, (position_for_centering(name, surf)[0], 10))

        emoji_size = (100, 100)
        attack_emoji = load_emoji("⚔️", emoji_size)
        life_emoji = load_emoji("♥️", emoji_size)

        emoji_border_offset = 5
        surf.blit(
            attack_emoji,
            (
                emoji_border_offset,
                self.size[1] - emoji_border_offset - emoji_size[1],
            ),
        )
        surf.blit(
            life_emoji,
            (
                self.size[0] - emoji_border_offset - emoji_size[0],
                self.size[1] - emoji_border_offset - emoji_size[1],
            ),
        )

        return surf