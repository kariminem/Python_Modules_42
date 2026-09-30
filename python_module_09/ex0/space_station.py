"""Exercise 0: basic Pydantic model with Field constraints."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    """Vital statistics reported by a space station."""

    # min_length / max_length constrain string length
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    # ge / le mean "greater or equal" / "less or equal"
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    # Pydantic converts ISO strings like "2024-01-15T10:30:00" to datetime
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def display_station(station: SpaceStation) -> None:
    """Print the main information of a station."""
    status = "Operational" if station.is_operational else "Offline"
    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print(f"Status: {status}")


def main() -> None:
    """Demonstrate a valid and an invalid space station."""
    separator = "=" * 40
    print("Space Station Data Validation")
    print(separator)

    # model_validate takes raw data (e.g. parsed JSON): the timestamp
    # string is automatically converted into a datetime object
    try:
        station = SpaceStation.model_validate({
            "station_id": "ISS001",
            "name": "International Space Station",
            "crew_size": 6,
            "power_level": 85.5,
            "oxygen_level": 92.3,
            "last_maintenance": "2024-01-15T10:30:00",
        })
        display_station(station)
    except ValidationError as error:
        print(f"Unexpected error: {error}")

    print()
    print(separator)

    # crew_size above 20 must be rejected
    try:
        SpaceStation(
            station_id="BAD001",
            name="Overcrowded Station",
            crew_size=25,
            power_level=50.0,
            oxygen_level=50.0,
            last_maintenance=datetime.now(),
        )
    except ValidationError as error:
        print("Expected validation error:")
        for detail in error.errors():
            print(detail["msg"])


if __name__ == "__main__":
    main()
