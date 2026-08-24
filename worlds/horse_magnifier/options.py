from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

class Deathlink(Toggle):
    """
    When someone dies with deathlink, the current level gets reset.
    """
    display_name = "Deathlink"

class PerfectAccuracy(Toggle):
    """
    Should getting perfect accuracy in a level send a check.
    """

    display_name = "Perfect Accuracy"

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


@dataclass
class HorseMagnifierOptions(PerGameCommonOptions):
    deathlink: Deathlink
    perfect_accuracy: PerfectAccuracy
    horse_amount: HorseAmount
    goal_requirement: GoalRequirement
    starting_lens: StartingLens