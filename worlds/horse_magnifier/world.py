from collections.abc import Mapping
from typing import Any, TextIO

from worlds.AutoWorld import World

from . import items, locations, regions, rules
from . import options as yaml_options

class HorseMagnifierWorld(World):
    """
    Horse Magnifier is a game where you lenses on horses to magnify them.
    """

    game = "Horse Magnifier"

    options_dataclass = yaml_options.HorseMagnifierOptions
    options: yaml_options.HorseMagnifierOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Menu"

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.HorseMagnifierItem:
        return items.create_item_with_correct_classification(self, name)
    
    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)
    
    def fill_slot_data(self) -> Mapping[str, Any]:
        options = self.options.as_dict(
            "deathlink",
            "perfect_accuracy",
            "leniency",
            "horse_amount",
            "goal_requirement",
        )

        return options