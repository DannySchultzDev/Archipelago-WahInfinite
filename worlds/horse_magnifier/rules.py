from __future__ import annotations

from typing import TYPE_CHECKING

from . import regions

from BaseClasses import Location, Entrance
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule

if TYPE_CHECKING:
    from .world import HorseMagnifierWorld

FISHEYE = Has("Fisheye Lens")
ANTI_FISHEYE = Has("Anti-Fisheye Lens")
FLIP = Has("Flip Lens")
STRETCH = Has("Stretch Lens")
COMPRESS = Has("Compress Lens")
SWIRL = Has("Swirl Lens")
PORTAL = Has("Portal Lens")
REPLICATOR = Has("Replicator Lens")
XRAY = Has("X-Ray Lens")
COLOR = Has("Color Lens")
APPLE = Has("Apple")
SWATTER = Has("Horsefly Swatter")

ITEM_REQUIREMENTS = {
    "Level 01 Cleared": FISHEYE,
    "Level 02 Cleared": FISHEYE,
    "Level 03 Cleared": FISHEYE,
    "Level 04 Cleared": FISHEYE & ANTI_FISHEYE,
    "Level 05 Cleared": FISHEYE,
    "Level 06 Cleared": FISHEYE & ANTI_FISHEYE,
    "Level 07 Cleared": FISHEYE & ANTI_FISHEYE,
    "Level 08 Cleared": FISHEYE & ANTI_FISHEYE,
    "Level 09 Cleared": FISHEYE & ANTI_FISHEYE,
    "Level 10 Cleared": FISHEYE & ANTI_FISHEYE,
    "Level 11 Cleared": FISHEYE & ANTI_FISHEYE,
    "Level 12 Cleared": FISHEYE,
    "Level 13 Cleared": FISHEYE,
    "Level 14 Cleared": FLIP,
    "Level 15 Cleared": FISHEYE & ANTI_FISHEYE & FLIP,
    "Level 16 Cleared": FISHEYE & FLIP,
    "Level 17 Cleared": ANTI_FISHEYE & FLIP,
    "Level 18 Cleared": FISHEYE & FLIP,
    "Level 19 Cleared": XRAY & APPLE,
    "Level 20 Cleared": STRETCH & COMPRESS,
    "Level 21 Cleared": FISHEYE & ANTI_FISHEYE & STRETCH,
    "Level 22 Cleared": STRETCH & COMPRESS,
    "Level 23 Cleared": FISHEYE & FLIP & COMPRESS,
    "Level 24 Cleared": ANTI_FISHEYE & COMPRESS,
    "Level 25 Cleared": SWIRL,
    "Level 26 Cleared": SWIRL,
    "Level 27 Cleared": FLIP & SWIRL,
    "Level 28 Cleared": ANTI_FISHEYE & SWIRL,
    "Level 29 Cleared": COLOR,
    "Level 30 Cleared": FISHEYE & COMPRESS & SWIRL,
    "Level 31 Cleared": SWIRL,
    "Level 32 Cleared": FLIP & SWIRL,
    "Level 33 Cleared": COLOR,
    "Level 34 Cleared": FISHEYE & SWIRL & COMPRESS,
    "Level 35 Cleared": COMPRESS & SWIRL,
    "Level 36 Cleared": ANTI_FISHEYE & SWIRL,
    "Level 37 Cleared": COLOR,
    "Level 38 Cleared": APPLE,
    "Level 39 Cleared": PORTAL,
    "Level 40 Cleared": PORTAL,
    "Level 41 Cleared": FISHEYE & SWIRL & PORTAL,
    "Level 42 Cleared": PORTAL,
    "Level 43 Cleared": PORTAL,
    "Level 44 Cleared": FISHEYE & FLIP & REPLICATOR,
    "Level 45 Cleared": REPLICATOR,
    "Level 46 Cleared": REPLICATOR,
    "Level 47 Cleared": COMPRESS & REPLICATOR,
    "Level 48 Cleared": FISHEYE & SWATTER,
    "Level 49 Cleared": FLIP & SWIRL & REPLICATOR,
    "Level 50 Cleared": FLIP & SWIRL & REPLICATOR,
    "Level 51 Cleared": FISHEYE & FLIP & REPLICATOR,
    "Level 52 Cleared": ANTI_FISHEYE & FLIP & SWIRL & REPLICATOR,
    "Level 53 Cleared": ANTI_FISHEYE & FLIP & REPLICATOR,

    "Level 01 Perfected": FISHEYE,
    "Level 02 Perfected": FISHEYE,
    "Level 03 Perfected": FISHEYE,
    "Level 04 Perfected": FISHEYE & ANTI_FISHEYE,
    "Level 05 Perfected": FISHEYE,
    "Level 06 Perfected": FISHEYE & ANTI_FISHEYE,
    "Level 07 Perfected": FISHEYE & ANTI_FISHEYE,
    "Level 08 Perfected": FISHEYE & ANTI_FISHEYE,
    "Level 09 Perfected": FISHEYE & ANTI_FISHEYE,
    "Level 10 Perfected": FISHEYE & ANTI_FISHEYE,
    "Level 11 Perfected": FISHEYE & ANTI_FISHEYE,
    "Level 12 Perfected": FISHEYE,
    "Level 14 Perfected": FLIP,
    "Level 15 Perfected": FISHEYE & ANTI_FISHEYE & FLIP,
    "Level 16 Perfected": FISHEYE & FLIP,
    "Level 17 Perfected": ANTI_FISHEYE & FLIP,
    "Level 18 Perfected": FISHEYE & FLIP,
    "Level 20 Perfected": STRETCH & COMPRESS,
    "Level 21 Perfected": FISHEYE & ANTI_FISHEYE & STRETCH,
    "Level 22 Perfected": STRETCH & COMPRESS,
    "Level 23 Perfected": FISHEYE & FLIP & COMPRESS,
    "Level 24 Perfected": ANTI_FISHEYE & COMPRESS,
    "Level 25 Perfected": SWIRL,
    "Level 26 Perfected": SWIRL,
    "Level 27 Perfected": FLIP & SWIRL,
    "Level 28 Perfected": ANTI_FISHEYE & SWIRL,
    "Level 29 Perfected": COLOR,
    "Level 30 Perfected": FISHEYE & COMPRESS & SWIRL,
    "Level 31 Perfected": SWIRL,
    "Level 32 Perfected": FLIP & SWIRL,
    "Level 33 Perfected": COLOR,
    "Level 34 Perfected": FISHEYE & SWIRL & COMPRESS,
    "Level 35 Perfected": COMPRESS & SWIRL,
    "Level 36 Perfected": ANTI_FISHEYE & SWIRL,
    "Level 37 Perfected": COLOR,
    "Level 39 Perfected": PORTAL,
    "Level 40 Perfected": PORTAL,
    "Level 41 Perfected": FISHEYE & SWIRL & PORTAL,
    "Level 42 Perfected": PORTAL,
    "Level 43 Perfected": PORTAL,
    "Level 44 Perfected": FISHEYE & FLIP & REPLICATOR,
    "Level 45 Perfected": REPLICATOR,
    "Level 46 Perfected": REPLICATOR,
    "Level 47 Perfected": COMPRESS & REPLICATOR,
    "Level 49 Perfected": FLIP & SWIRL & REPLICATOR,
    "Level 50 Perfected": FLIP & SWIRL & REPLICATOR,
    "Level 51 Perfected": FISHEYE & FLIP & REPLICATOR,
    "Level 52 Perfected": ANTI_FISHEYE & FLIP & SWIRL & REPLICATOR,
    "Level 53 Perfected": ANTI_FISHEYE & FLIP & REPLICATOR,
}

def set_all_rules(world: HorseMagnifierWorld):
    for item_requirement in ITEM_REQUIREMENTS:
        rule: Rule = ITEM_REQUIREMENTS[item_requirement]

        if rule is None:
            continue

        location_id: int = world.location_name_to_id[item_requirement]
        if (not world.options.perfect_accuracy) & (location_id >= 100):
            #If perfect accuracy is off, don't add rules for checkpoints.
            continue

        location: Location = world.get_location(item_requirement)

        world.set_rule(location, rule)

    horse_req: int = int((world.options.goal_requirement / 100.0) * world.options.horse_amount)
    victory_rule: Rule = Has("Horse", count = horse_req) & FISHEYE & ANTI_FISHEYE & STRETCH & COMPRESS & SWIRL & REPLICATOR
    world.set_rule(world.get_location("Victory"), victory_rule)

    world.set_completion_rule(Has("Victory"))