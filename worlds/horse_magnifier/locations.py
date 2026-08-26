from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location, Region

from . import items, regions

if TYPE_CHECKING:
    from .world import HorseMagnifierWorld

LOCATION_NAME_TO_ID = {
    "Level 01 Cleared": 1,
    "Level 02 Cleared": 2,
    "Level 03 Cleared": 3,
    "Level 04 Cleared": 4,
    "Level 05 Cleared": 5,
    "Level 06 Cleared": 6,
    "Level 07 Cleared": 7,
    "Level 08 Cleared": 8,
    "Level 09 Cleared": 9,
    "Level 10 Cleared": 10,
    "Level 11 Cleared": 11,
    "Level 12 Cleared": 12,
    "Level 13 Cleared": 13,
    "Level 14 Cleared": 14,
    "Level 15 Cleared": 15,
    "Level 16 Cleared": 16,
    "Level 17 Cleared": 17,
    "Level 18 Cleared": 18,
    "Level 19 Cleared": 19,
    "Level 20 Cleared": 20,
    "Level 21 Cleared": 21,
    "Level 22 Cleared": 22,
    "Level 23 Cleared": 23,
    "Level 24 Cleared": 24,
    "Level 25 Cleared": 25,
    "Level 26 Cleared": 26,
    "Level 27 Cleared": 27,
    "Level 28 Cleared": 28,
    "Level 29 Cleared": 29,
    "Level 30 Cleared": 30,
    "Level 31 Cleared": 31,
    "Level 32 Cleared": 32,
    "Level 33 Cleared": 33,
    "Level 34 Cleared": 34,
    "Level 35 Cleared": 35,
    "Level 36 Cleared": 36,
    "Level 37 Cleared": 37,
    "Level 38 Cleared": 38,
    "Level 39 Cleared": 39,
    "Level 40 Cleared": 40,
    "Level 41 Cleared": 41,
    "Level 42 Cleared": 42,
    "Level 43 Cleared": 43,
    "Level 44 Cleared": 44,
    "Level 45 Cleared": 45,
    "Level 46 Cleared": 46,
    "Level 47 Cleared": 47,
    "Level 48 Cleared": 48,
    "Level 49 Cleared": 49,
    "Level 50 Cleared": 50,
    "Level 51 Cleared": 51,
    "Level 52 Cleared": 52,
    "Level 53 Cleared": 53,

    "Level 01 Perfected": 101,
    "Level 02 Perfected": 102,
    "Level 03 Perfected": 103,
    "Level 04 Perfected": 104,
    "Level 05 Perfected": 105,
    "Level 06 Perfected": 106,
    "Level 07 Perfected": 107,
    "Level 08 Perfected": 108,
    "Level 09 Perfected": 109,
    "Level 10 Perfected": 110,
    "Level 11 Perfected": 111,
    "Level 12 Perfected": 112,
    "Level 14 Perfected": 113,
    "Level 15 Perfected": 114,
    "Level 16 Perfected": 115,
    "Level 17 Perfected": 116,
    "Level 18 Perfected": 117,
    "Level 20 Perfected": 118,
    "Level 21 Perfected": 119,
    "Level 22 Perfected": 120,
    "Level 23 Perfected": 121,
    "Level 24 Perfected": 122,
    "Level 25 Perfected": 123,
    "Level 26 Perfected": 124,
    "Level 27 Perfected": 125,
    "Level 28 Perfected": 126,
    "Level 29 Perfected": 127,
    "Level 30 Perfected": 128,
    "Level 31 Perfected": 129,
    "Level 32 Perfected": 130,
    "Level 33 Perfected": 131,
    "Level 34 Perfected": 132,
    "Level 35 Perfected": 133,
    "Level 36 Perfected": 134,
    "Level 37 Perfected": 135,
    "Level 39 Perfected": 136,
    "Level 40 Perfected": 137,
    "Level 41 Perfected": 138,
    "Level 42 Perfected": 139,
    "Level 43 Perfected": 140,
    "Level 44 Perfected": 141,
    "Level 45 Perfected": 142,
    "Level 46 Perfected": 143,
    "Level 47 Perfected": 144,
    "Level 49 Perfected": 145,
    "Level 50 Perfected": 146,
    "Level 51 Perfected": 147,
    "Level 52 Perfected": 148,
    "Level 53 Perfected": 149,
}

ID_TO_LOCATION_NAME = {v: k for k, v in LOCATION_NAME_TO_ID.items()}

class HorseMagnifierLocation(Location):
    game = "Horse Magnifier"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_names] for location_name in location_names}

def create_all_locations(world: HorseMagnifierWorld) -> None:
    region = world.get_region("Menu")
    for location_id in range(1, 54):
        location_name: str = ID_TO_LOCATION_NAME[location_id]
        location = HorseMagnifierLocation(world.player, location_name, location_id, region)
        region.locations.append(location)

    if world.options.perfect_accuracy:
        for location_id in range(101, 150):
            location_name: str = ID_TO_LOCATION_NAME[location_id]
            location = HorseMagnifierLocation(world.player, location_name, location_id, region)
            region.locations.append(location)

    region.add_event("Victory", location_type=HorseMagnifierLocation, item_type=items.HorseMagnifierItem)