from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation\n"
          "========================================")

    print("Valid station created:")
    ss = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime(2050, 3, 12, 6, 20, 0)
    )
    print(f"ID: {ss.station_id}\nName: {ss.name}\nCrew: {ss.crew_size}\n"
          f"Power: {ss.power_level}%\nOxygen: {ss.oxygen_level}%\n"
          f"Status: ", end='')
    if ss.is_operational:
        print("Operational")
    else:
        print("Out of commission")

    print("\n========================================")
    print("Expected validation error:")
    try:
        SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=30,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2050, 3, 12, 6, 20, 0)
        )
    except ValidationError as e:
        print(e.errors()[0]["msg"])
    print()


if __name__ == "__main__":
    main()
