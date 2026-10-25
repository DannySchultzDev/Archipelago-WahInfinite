from collections.abc import Mapping
from typing import Any, TextIO

from worlds.AutoWorld import World

from . import items, locations, regions, rules#, web_world
from . import options as yaml_options

class FantasticFistWorld(World):
    """
    Fantastic Fist is a 2D platformer which uses both keyboard and mouse controls.
    """

    game = "Fantastic Fist"

    #web = web_world.FantasticFistWebWorld()

    options_dataclass = yaml_options.FantasticFistOptions
    options: yaml_options.FantasticFistOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Menu"

    randomized_entrances: list[regions.Edge] = []
    randomized_doors: list[regions.Edge] = []
    secret_exit_room_order: list[int] = []
    true_coin_amount: int = 0
    secret_coin_requirements: list[int] = []
    boss_coin_requirements: list[int] = []

    ut_can_gen_without_yaml = True

    def generate_early(self) -> None:
        re_gen_passthrough = getattr(self.multiworld, "re_gen_passthrough", {})
        if re_gen_passthrough and self.game in re_gen_passthrough:
            slot_data: dict[str, Any] = re_gen_passthrough[self.game]

            for i in range(0, len(slot_data["entrances"]), 2):
               self.randomized_entrances.append(regions.Edge(regions.Node(slot_data["entrances"][i], "Level", -1), regions.Node(slot_data["entrances"][i + 1], "Pregen", -1), False))

            for j in range(0, len(slot_data["doors"]), 2):
               self.randomized_doors.append(regions.Edge(regions.Node(slot_data["doors"][j], "Pregen", -1), regions.Node(slot_data["doors"][j + 1], "Pregen", -1), False))

            setattr(self.options, "deathlink", slot_data["deathlink"])
            setattr(self.options, "deathlink_amnesty", slot_data["deathlink_amnesty"])
            setattr(self.options, "goal", slot_data["goal"])
            setattr(self.options, "difficulty", slot_data["difficulty"])
            setattr(self.options, "open_world", slot_data["open_world"])
            setattr(self.options, "paths", slot_data["paths"])
            setattr(self.options, "entrance_rando", slot_data["entrance_rando"])
            setattr(self.options, "door_rando", slot_data["door_rando"])
            setattr(self.options, "roomsanity", slot_data["roomsanity"])
            setattr(self.options, "checkpointsanity", slot_data["checkpointsanity"])
            self.options.max_coin_amount.value = slot_data["max_coin_amount"]
            setattr(self.options, "first_secret_exit_coin_requirement", slot_data["first_secret_exit_coin_requirement"])
            setattr(self.options, "second_secret_exit_coin_requirement", slot_data["second_secret_exit_coin_requirement"])
            setattr(self.options, "third_secret_exit_coin_requirement", slot_data["third_secret_exit_coin_requirement"])
            setattr(self.options, "fourth_secret_exit_coin_requirement", slot_data["fourth_secret_exit_coin_requirement"])
            setattr(self.options, "fifth_secret_exit_coin_requirement", slot_data["fifth_secret_exit_coin_requirement"])
            setattr(self.options, "sixth_secret_exit_coin_requirement", slot_data["sixth_secret_exit_coin_requirement"])
            setattr(self.options, "seventh_secret_exit_coin_requirement", slot_data["seventh_secret_exit_coin_requirement"])
            setattr(self.options, "first_boss_coin_requirement", slot_data["first_boss_coin_requirement"])
            setattr(self.options, "second_boss_coin_requirement", slot_data["second_boss_coin_requirement"])
            setattr(self.options, "third_boss_coin_requirement", slot_data["third_boss_coin_requirement"])
            setattr(self.options, "fourth_boss_coin_requirement", slot_data["fourth_boss_coin_requirement"])
            setattr(self.options, "fifth_boss_coin_requirement", slot_data["fifth_boss_coin_requirement"])
            setattr(self.options, "default_item_groups", slot_data["default_item_groups"])
            setattr(self.options, "default_extra_items", slot_data["default_extra_items"])
            self.options.destructible_blocks.value = slot_data["destructible_blocks"]
            self.options.physics_blocks.value = slot_data["physics_blocks"]
            self.options.sliding_blocks.value = slot_data["sliding_blocks"]
            self.options.boss_blocks.value = slot_data["boss_blocks"]
            self.options.pop_blocks.value = slot_data["pop_blocks"]
            self.options.bumpers.value = slot_data["bumpers"]
            self.options.switches.value = slot_data["switches"]
            self.options.punchappear_blocks.value = slot_data["punchappear_blocks"]
            self.options.skull_blocks.value = slot_data["skull_blocks"]
            self.options.extra_skull_blocks.value = slot_data["extra_skull_blocks"]
            self.options.skull_rings.value = slot_data["skull_rings"]
            self.options.extra_skull_rings.value = slot_data["extra_skull_rings"]
            self.options.enemies.value = slot_data["enemies"]
            self.options.extra_enemies.value = slot_data["extra_enemies"]
            self.options.vivi_blocks.value = slot_data["vivi_blocks"]
            self.options.block_launchers.value = slot_data["block_launchers"]
            self.options.launchers.value = slot_data["launchers"]
            self.options.hazards.value = slot_data["hazards"]
            self.options.bubbles.value = slot_data["bubbles"]
            self.options.balloons.value = slot_data["balloons"]
            self.options.bombs.value = slot_data["bombs"]
            self.options.hive_blocks.value = slot_data["hive_blocks"]
            self.options.keys.value = slot_data["keys"]
            self.options.gravity_items.value = slot_data["gravity_items"]
            self.options.lifts.value = slot_data["lifts"]
            self.options.semisolids.value = slot_data["semisolids"]
            self.options.vivis_flashlight.value = slot_data["vivis_flashlight"]

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.FantasticFistItem:
        return items.create_item_with_correct_classification(self, name)
    
    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)
    
    def fill_slot_data(self) -> Mapping[str, Any]:
        options = self.options.as_dict(
            "deathlink",
            "deathlink_amnesty",
            "goal",
            "difficulty",
            "open_world",
            "paths",
            "entrance_rando",
            "door_rando",
            "roomsanity",
            "checkpointsanity",
            "max_coin_amount",
            "first_secret_exit_coin_requirement",
            "second_secret_exit_coin_requirement",
            "third_secret_exit_coin_requirement",
            "fourth_secret_exit_coin_requirement",
            "fifth_secret_exit_coin_requirement",
            "sixth_secret_exit_coin_requirement",
            "seventh_secret_exit_coin_requirement",
            "first_boss_coin_requirement",
            "second_boss_coin_requirement",
            "third_boss_coin_requirement",
            "fourth_boss_coin_requirement",
            "fifth_boss_coin_requirement",
            "default_item_groups",
            "default_extra_items",
            "destructible_blocks",
            "physics_blocks",
            "sliding_blocks",
            "boss_blocks",
            "pop_blocks",
            "bumpers",
            "switches",
            "punchappear_blocks",
            "skull_blocks",
            "extra_skull_blocks",
            "skull_rings",
            "extra_skull_rings",
            "enemies",
            "extra_enemies",
            "vivi_blocks",
            "block_launchers",
            "launchers",
            "hazards",
            "extra_hazards",
            "bubbles",
            "balloons",
            "bombs",
            "hive_blocks",
            "keys",
            "gravity_items",
            "lifts",
            "semisolids",
            "vivis_flashlight"
        )
        for i in range(7):
            options["secret_coin_req_" + str(i)] = self.secret_coin_requirements[i]
        for i in range(5):
            options["boss_coin_req_" + str(i)] = self.boss_coin_requirements[i]

        options["secret_exit_order"] = self.secret_exit_room_order

        entrances: list[str] = []
        for entrance in self.randomized_entrances:
            entrances.append(entrance.start_node.node_name)
            entrances.append(entrance.end_node.node_name)

        options["entrances"] = entrances

        doors: list[str] = []
        for door in self.randomized_doors:
            doors.append(door.start_node.node_name)
            doors.append(door.end_node.node_name)

        options["doors"] = doors
        return options

    def write_spoiler(self, spoiler_handle: TextIO) -> None:
        spoiler_handle.write("True Coin Amount: " + str(self.true_coin_amount) + "\n")
        spoiler_handle.write("Secret Exit Coin Amount Requirments: [")
        for req in range(len(self.secret_coin_requirements)):
            spoiler_handle.write(str(self.secret_coin_requirements[req]))
            if req == 6:
                spoiler_handle.write("]\n")
            else:
                spoiler_handle.write(", ")

        spoiler_handle.write("Boss Level Coin Amount Requirments: [")
        for req in range(len(self.boss_coin_requirements)):
            spoiler_handle.write(str(self.boss_coin_requirements[req]))
            if req == 4:
                spoiler_handle.write("]\n")
            else:
                spoiler_handle.write(", ")

        spoiler_handle.write("----------MAP----------\n")
        for level_id in regions.ID_TO_LEVEL:
            level: regions.Level = regions.ID_TO_LEVEL[level_id]
            edges: list[regions.Edge] = regions.get_edge_from_start_node_name(self.randomized_entrances, level.level_id)
            spoiler_handle.write(edges[0].start_node.node_name)
            while len(edges) > 0:
                spoiler_handle.write(" -> " + edges[0].end_node.node_name)
                skipped_initial: bool = False
                for edge in edges:
                    if not skipped_initial:
                        skipped_initial = True
                        continue
                    spoiler_handle.write(" & " + edge.end_node.node_name)
                next_node_name: str = edges[0].end_node.node_name
                if next_node_name == "Verticality Room 2B" or next_node_name == "The Five Mile Spire Room 7B":
                    #Side rooms don't have additional pathing
                    next_node_name = edges[1].end_node.node_name
                edges = regions.get_edge_from_start_node_name(self.randomized_doors, next_node_name)
            spoiler_handle.write("\n")