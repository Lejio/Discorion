import json
from typing import List, Dict, Set


class Type:
    def __init__(self, _type: str) -> None:
        self._type = _type

    @property
    def type_name(self) -> str:
        return self._type


class PokeObject:
    class Version:
        class PokedexData:
            class Ability:
                def __init__(self, ability: dict) -> None:
                    self._href: str = ability["href"]
                    self._effect: str = ability["effect"]
                    self._hidden: bool = ability["hidden"]

                @property
                def href(self) -> str:
                    return self.href

                @property
                def effect(self) -> str:
                    return self._effect

                @property
                def hidden(self) -> bool:
                    return self._hidden

            def __init__(self, pokedex_data: dict) -> None:
                self._national_no: int = int(pokedex_data["National No."])
                self._type: List[Type] = pokedex_data["Type"]
                self._species: str = pokedex_data["Species"]
                self._height: str = pokedex_data["Height"]
                self._weight: str = pokedex_data["Weight"]
                self._abilities: Dict[str, self.Ability] = {}

                for ability in pokedex_data["Abilities"]:
                    self._abilities[ability] = self.Ability(
                        pokedex_data["Abilities"][ability]
                    )

            @property
            def national_no(self) -> int:
                return self._national_no

            @property
            def poke_types(self) -> List[Type]:
                return self._type

            @property
            def species(self) -> str:
                return self._species

            @property
            def height(self) -> str:
                return self._height

            @property
            def weight(self) -> str:
                return self._weight

            @property
            def abilities(self) -> Dict[str, Ability]:
                return self._abilities

        class TrainingData:
            def __init__(self, training_data: dict) -> None:
                self._ev_yield: str = training_data["EV yield"]
                self._catch_rate: int = int(training_data["Catch rate"])
                self._basefriendship: int = int(training_data["BaseFriendship"])
                self._base_exp: int = int(training_data["Base Exp."])
                self._growth_rate: str = training_data["Growth Rate"]

            @property
            def ev_yield(self) -> str:
                return self._ev_yield

            @property
            def catch_rate(self) -> int:
                return self._catch_rate

            @property
            def base_friendship(self) -> int:
                return self._basefriendship

            @property
            def base_exp(self) -> int:
                return self._base_exp

            @property
            def growth_rate(self) -> str:
                return self._growth_rate

        class BreedingData:
            def __init__(self, training_data: dict) -> None:
                self._gender: str = training_data["Gender"]

            @property
            def gender(self) -> str:
                return self._gender

        class BaseStats:
            class Stat:
                def __init__(self, stat: dict) -> None:
                    self._base = int(stat["Base"])
                    self._min = int(stat["Min"])
                    self._max = int(stat["Max"])

                @property
                def base(self) -> int:
                    return self._base

                @property
                def minimum(self) -> int:
                    return self._min

                @property
                def maximum(self) -> int:
                    return self._max

            def __init__(self, base_stats: dict) -> None:
                self._hp = self.Stat(base_stats["HP"])
                self._attack = self.Stat(base_stats["Attack"])
                self._defense = self.Stat(base_stats["Defense"])
                self._sp_atk = self.Stat(base_stats["Sp. Atk"])
                self._sp_def = self.Stat(base_stats["Sp. Def"])
                self._speed = self.Stat(base_stats["Speed"])
                self._total = int(base_stats["Total"])

            @property
            def hp(self) -> Stat:
                return self._hp

            @property
            def attack(self) -> Stat:
                return self._attack

            @property
            def defense(self) -> Stat:
                return self._defense

            @property
            def sp_atk(self) -> Stat:
                return self._sp_atk

            @property
            def sp_def(self) -> Stat:
                return self._sp_def

            @property
            def speed(self) -> Stat:
                return self._speed

            @property
            def total(self) -> int:
                return self._total

        class DefenseStats:
            class DefenseStat:
                def __init__(self, _type: str, val: str) -> None:
                    self._type: str = _type
                    self._val: str = val

                @property
                def poke_type(self) -> str:
                    return self._type

                @property
                def value(self) -> str:
                    return self._val

            def __init__(self, defense_stats: dict) -> None:
                self._defense_categories: Dict[str, Set[self.DefenseStat]] = {
                    name: self.__defense_stat_processor(defense_stats[name])
                    for name in defense_stats
                }

            def __defense_stat_processor(self, defense_stats: dict) -> Set[DefenseStat]:
                return {
                    self.DefenseStat(_type, defense_stats[_type])
                    for _type in defense_stats
                }

            @property
            def defenses(self) -> Dict[str, Set[DefenseStat]]:
                return self._defense_categories

        class Images:
            def __init__(self, images: dict) -> None:
                self._discord_image: str = images["discord_image"]
                self._discord_sprite: str = images["discord_sprite"]

            @property
            def discord_image(self) -> str:
                return self._discord_image

            @property
            def discord_sprite(self) -> str:
                return self._discord_sprite

        def __init__(self, version: dict) -> None:
            self._name: str = version["name"]
            self._data: dict = version["data"]

        @property
        def name(self) -> str:
            return self._name

        @property
        def pokedex_data(self) -> PokedexData:
            return self.PokedexData(self._data["pokedex_data"])

        @property
        def training_data(self) -> TrainingData:
            return self.TrainingData(self._data["training_data"])

        @property
        def breeding(self) -> BreedingData:
            return self.BreedingData(self._data["breeding_data"])

        @property
        def base_stats(self) -> BaseStats:
            return self.BaseStats(self._data["base_stats"])

        @property
        def defense_stats(self) -> DefenseStats:
            return self.DefenseStats(self._data["defense_stats"])

        @property
        def images(self) -> Images:
            return self.Images(self._data["images"])

    class Evolution:
        class EvolutionPokemon:
            def __init__(self, pokemon: dict) -> None:
                self._name: str = pokemon["name"]
                self._national_no: int = int(pokemon["nationalNo"][1:])
                self._type: List[Type] = [
                    Type(poke_type) for poke_type in pokemon["type"]
                ]
                self._nickname: str | None = pokemon["nickname"]

            @property
            def name(self) -> str:
                return self.name

            @property
            def national_no(self) -> int:
                return self._national_no

            @property
            def poke_type(self) -> List[Type]:
                return self._type

            @property
            def nickname(self) -> str | None:
                return self._nickname

        def __init__(self, evolution) -> None:
            self._from = self.EvolutionPokemon(evolution["from"])
            self._to = self.EvolutionPokemon(evolution["to"])
            self._requirement: str = evolution["requirement"]
            self._shed: self.EvolutionPokemon | None = (
                evolution["shed"]
                if evolution["shed"] is None
                else self.EvolutionPokemon(evolution["shed"])
            )

        @property
        def evolution_from(self) -> EvolutionPokemon:
            return self._from

        @property
        def evolution_to(self) -> EvolutionPokemon:
            return self._to

        @property
        def requirement(self) -> str:
            return self._requirement

        @property
        def shed(self) -> EvolutionPokemon | None:
            return self._shed

    class AttackCategory(dict):
        class Attack:
            def __init__(self, name: str, val: str | None) -> None:
                self._name: str = name
                self._val: str | None = val

            @property
            def name(self) -> str:
                return self._name

            @property
            def val(self) -> str | None:
                return self._val

            def __str__(self) -> str:
                return self._name

        def __init__(self, category_name: str, category_moves) -> None:
            self._name: str = category_name
            self._moves: List[self.Attack] = []

            print("1", category_moves)
            for move in category_moves:
                for name in move:
                    print(name)
                    self._moves.append(self.Attack(name, move[name]))

        @property
        def name(self) -> str:
            return self._name

        @property
        def moves(self) -> List[Attack]:
            return self._moves

    class EntryVersion:
        class Entry:
            def __init__(self, entry) -> None:
                self._text: str = entry

            @property
            def text(self) -> str:
                return self._text

        def __init__(self, entries: list) -> None:
            self._entries: List[self.Entry] = [self.Entry(entry) for entry in entries]

        @property
        def entries(self) -> List[Entry]:
            return self._entries

    def __init__(self, pokemon_raw: dict) -> None:
        self._versions = self.__pokemon_version_processor(pokemon_raw["versions"])
        self._evo_stats = self.__pokemon_evolution_processor(pokemon_raw["evo_stats"])
        self._attacks_data = self.__pokemon_attacks_processor(
            pokemon_raw["attacks_data"]
        )
        self._entries = self.__pokemon_entries_processor(pokemon_raw["entries"])
        self._name = pokemon_raw["name"]

    @property
    def versions_list(self) -> List[str]:
        return [version.name for version in self._versions]

    @property
    def versions(self) -> List[Version]:
        return self._versions

    @property
    def evolutions(self) -> List[Evolution]:
        return self._evo_stats

    @property
    def attacks(self) -> List[AttackCategory]:
        return self._attacks_data

    @property
    def entries(self) -> Dict[str, EntryVersion]:
        return self._entries

    @property
    def name(self) -> str:
        return self._name

    def __pokemon_version_processor(self, pokemon_versions_raw: dict) -> List[Version]:
        return [self.Version(version) for version in pokemon_versions_raw]

    def __pokemon_evolution_processor(
        self, pokemon_evolution_raw: list
    ) -> List[Evolution]:
        return [
            [self.Evolution(evolution) for evolution in evolution_category]
            for evolution_category in pokemon_evolution_raw
        ]

    def __pokemon_attacks_processor(
        self, pokemon_attacks_raw: dict
    ) -> List[AttackCategory]:
        return [
            self.AttackCategory(category, pokemon_attacks_raw[category])
            for category in pokemon_attacks_raw
        ]

    def __pokemon_entries_processor(
        self, pokemon_entires_raw: dict
    ) -> Dict[str, EntryVersion]:
        return {
            name: self.EntryVersion(pokemon_entires_raw[name])
            for name in pokemon_entires_raw
        }


with open(
    "/Users/geneni/Developer/Workspace/Projects/Discoreon/src/poketools/pokegenerator/new_pokedex/6.json",
    "r",
) as pokemon_json:
    pokemon_raw = json.load(pokemon_json)

pikachu = PokeObject(pokemon_raw)
