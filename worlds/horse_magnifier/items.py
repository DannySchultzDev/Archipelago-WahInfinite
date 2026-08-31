from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification
from ..ladx.LADXR import itempool

if TYPE_CHECKING:
    from .world import HorseMagnifierWorld

ITEM_NAME_TO_ID = {
    "Fisheye Lens": 1,
    "Anti-Fisheye Lens": 2,
    "Flip Lens": 3,
    "Stretch Lens": 4,
    "Compress Lens": 5,
    "Swirl Lens": 6,
    "Portal Lens": 7,
    "Replicator Lens": 8,
    "X-Ray Lens": 9,
    "Color Lens": 10,
    "Apple": 11,
    "Horsefly Swatter": 12,

    "Horse": 20,

    "Donkey": 30,
    "Mule": 31,
    "Camel": 32,
    "Unicorn": 33,
    "Seahorse": 34,
    "Deer": 35,
    "Pony": 36,
    "Zebra": 37,
    "Centaur": 38,
    "Kelpie": 39,

    "Grenade Trap": 50,
    "Jumpscare Trap": 51,
}

ID_TO_ITEM_NAME = {v: k for k, v in ITEM_NAME_TO_ID.items()}


class HorseMagnifierItem(Item):
    game = "Horse Magnifier"

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Fisheye Lens": ItemClassification.progression,
    "Anti-Fisheye Lens": ItemClassification.progression,
    "Flip Lens": ItemClassification.progression,
    "Stretch Lens": ItemClassification.progression,
    "Compress Lens": ItemClassification.progression,
    "Swirl Lens": ItemClassification.progression,
    "Portal Lens": ItemClassification.progression,
    "Replicator Lens": ItemClassification.progression,
    "X-Ray Lens": ItemClassification.progression,
    "Color Lens": ItemClassification.progression,
    "Apple": ItemClassification.progression,
    "Horsefly Swatter": ItemClassification.progression,

    "Horse": ItemClassification.progression_deprioritized_skip_balancing,

    "Donkey": ItemClassification.filler,
    "Mule": ItemClassification.filler,
    "Camel": ItemClassification.filler,
    "Unicorn": ItemClassification.filler,
    "Seahorse": ItemClassification.filler,
    "Deer": ItemClassification.filler,
    "Pony": ItemClassification.filler,
    "Zebra": ItemClassification.filler,
    "Centaur": ItemClassification.filler,
    "Kelpie": ItemClassification.filler,

    "Grenade Trap": ItemClassification.trap,
    "Jumpscare Trap": ItemClassification.trap,
}

def get_random_filler_item_name(world: HorseMagnifierWorld) -> str:
    if world.random.randint(0, 100) < world.options.trap_percentage:
        if world.random.randint(0, 100) < world.options.grenade_percentage:
            return "Grenade Trap"
        else:
            return "Jumpscare Trap"
    return ID_TO_ITEM_NAME[world.random.randint(30, 39)]

def create_item_with_correct_classification(world: HorseMagnifierWorld, name: str) -> HorseMagnifierItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    return HorseMagnifierItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: HorseMagnifierWorld) -> None:

    itempool: list[Item] = [
        world.create_item("Anti-Fisheye Lens"),
        world.create_item("Stretch Lens"),
        world.create_item("Compress Lens"),
        world.create_item("X-Ray Lens"),
        world.create_item("Apple"),
        world.create_item("Horsefly Swatter")
    ]

    if world.options.starting_lens == 0:
        world.push_precollected(world.create_item("Fisheye Lens"))
    else:
        itempool.append(world.create_item("Fisheye Lens"))

    if world.options.starting_lens == 1:
        world.push_precollected(world.create_item("Flip Lens"))
    else:
        itempool.append(world.create_item("Flip Lens"))

    if world.options.starting_lens == 2:
        world.push_precollected(world.create_item("Swirl Lens"))
    else:
        itempool.append(world.create_item("Swirl Lens"))

    if world.options.starting_lens == 3:
        world.push_precollected(world.create_item("Color Lens"))
    else:
        itempool.append(world.create_item("Color Lens"))

    if world.options.starting_lens == 4:
        world.push_precollected(world.create_item("Portal Lens"))
    else:
        itempool.append(world.create_item("Portal Lens"))

    if world.options.starting_lens == 5:
        world.push_precollected(world.create_item("Replicator Lens"))
    else:
        itempool.append(world.create_item("Replicator Lens"))

    itempool += [world.create_item("Horse") for _ in range(world.options.horse_amount)]

    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool