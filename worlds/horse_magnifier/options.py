from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

class Deathlink(Choice):
    """
    When someone dies with deathlink, send either a grenade or jumpscare trap.
    """
    display_name = "Deathlink"

    option_disabled = 0
    option_grenade_trap = 1
    option_jumpscare_trap = 2

    default = option_disabled

class PerfectAccuracy(Toggle):
    """
    Should getting perfect accuracy in a level send a check.
    """

    display_name = "Perfect Accuracy"


class Leniency(Range):
    """
    If Perfect Accuracy is enabled, how many pixels you can be away to still receive the check.
    """

    display_name = "Leniency"

    range_start = 0
    range_end = 20

    default = 5

class HorseAmount(Range):
    """
    How many Horse macguffins are added to the world.
    """

    display_name = "Horse Amount"

    range_start = 0
    range_end = 40

    default = 40

class GoalRequirement(Range):
    """
    What percentage of horses are required to unlock the final level.
    """

    display_name = "Goal Requirement"

    range_start = 0
    range_end = 100

    default = 70


class StartingLens(Choice):
    """
    Which Lens you start with.
    """

    display_name = "Starting Lens"

    option_fisheye = 0
    option_flip = 1
    option_swirl = 2
    option_color = 3
    option_portal = 4
    option_replicator = 5

    default = option_fisheye

class TrapPercentage(Range):
    """
    What percentage of filler items are replaced with traps.
    """

    display_name = "Trap Percentage"

    range_start = 0
    range_end = 100

    default = 0


class GrenadePercentage(Range):
    """
    What percentage of traps are grenade traps.
    The rest of the traps will be jumpscare traps.

    Grenade Traps reset the current level (they do not send a deathlink).
    Jumpscare Traps are self-explanatory (they will occur even if the setting is off).
    """

    display_name = "Grenade Trap Percentage"

    range_start = 0
    range_end = 100

    default = 0

@dataclass
class HorseMagnifierOptions(PerGameCommonOptions):
    deathlink: Deathlink
    perfect_accuracy: PerfectAccuracy
    leniency: Leniency
    horse_amount: HorseAmount
    goal_requirement: GoalRequirement
    starting_lens: StartingLens
    trap_percentage: TrapPercentage
    grenade_percentage: GrenadePercentage