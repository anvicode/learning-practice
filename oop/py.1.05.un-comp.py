# py.1.04 -> py.1.05
# understanding composition


class Wheel:
    def __init__(self, dia: float, brand: str) -> None:
        self._dia = dia
        self._brand = brand

    def get_dia(self) -> float:
        return self._dia

    def get_brand(self) -> str:
        return self._brand


class Engine:
    def __init__(self, fuel: str, power: int) -> None:
        self._fuel = fuel
        self._power = power
        self._is_on = False

    def get_fuel(self) -> str:
        return self._fuel

    def get_power(self) -> int:
        return self._power

    def get_is_on(self) -> bool:
        return self._is_on

    def on_off(self) -> None:
        if not self._is_on:
            self._is_on = True
        else:
            self._is_on = False


class Auto:
    def __init__(self, engine: Engine) -> None:
        self._engine = engine
        self._wheels: list[Wheel] = []

    def __str__(self) -> str:
        return f"Auto with {self._engine.get_fuel()} engine with {len(self._wheels)} wheels"

    def get_engine(self) -> str:
        ret = f"Engine: Fuel: {self._engine.get_fuel()}, Power: {self._engine.get_power()}, Is on: {self._engine.get_is_on()}"
        return ret

    def get_wheels(self) -> str:
        return (
            ", ".join([f"{i.get_dia()}, {i.get_brand()}" for i in self._wheels])
            if self._wheels
            else "No wheels!"
        )

    def add_wheels(self, wheels: list[Wheel]) -> None:
        if len(wheels) == 4:
            for i in wheels:
                self._wheels.append(i)
                print(f"Added {i.get_dia()}, {i.get_brand()}")
        else:
            print("Not enough wheels! Need 4.")


au1 = Auto(Engine("gasoline", 100))

print()
print(au1)
print(au1.get_engine())
print(au1.get_wheels())

au1.add_wheels([Wheel(15, "Michelin")])
au1.add_wheels(
    [
        Wheel(15, "Michelin"),
        Wheel(15, "Michelin"),
        Wheel(15, "Michelin"),
        Wheel(15, "Michelin"),
    ]
)

print(au1.get_wheels())
print(au1)
