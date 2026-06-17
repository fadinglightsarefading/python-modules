from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialisation: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def safety_requirements(self):
        if not self.mission_id.startswith('M'):
            raise ValueError("Mission ID must start with \'M\'")
        if not (any(member.rank == Rank.CAPTAIN for member in self.crew) or
                any(member.rank == Rank.COMMANDER for member in self.crew)):
            raise ValueError("Must have at least one Commander or Captain")
        if self.duration_days > 365 and (
            sum(member.years_experience >= 5 for member in self.crew)
            < (len(self.crew) / 2)
        ):
            raise ValueError("Long missions (> 365 days) need 50% "
                             "experienced crew (5+ years)")
        if any(not member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")
        return self


def main() -> None:
    print("Space Mission Crew Validation\n"
          "=========================================")
    space_crew = [
        CrewMember(
            member_id="001",
            name="Sarah Connor",
            rank=Rank.COMMANDER,
            age=55,
            specialisation="Mission Command",
            years_experience=25),
        CrewMember(
            member_id="002",
            name="John Smith",
            rank=Rank.LIEUTENANT,
            age=39,
            specialisation="Navigation",
            years_experience=18),
        CrewMember(
            member_id="003",
            name="Alice Johnson",
            rank=Rank.OFFICER,
            age=50,
            specialisation="Engineering",
            years_experience=30)
    ]
    msn = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime(2024, 1, 1, 5, 0, 0),
        duration_days=900,
        crew=space_crew,
        budget_millions=2500.0
    )
    print(f"Valid mission created:\n"
          f"Mission: {msn.mission_name}\n"
          f"ID: {msn.mission_id}\n"
          f"Destination: {msn.destination} days\n"
          f"Duration: {msn.duration_days}\n"
          f"Budget: ${msn.budget_millions}M\n"
          f"Crew size: {len(msn.crew)}\n"
          f"Crew members:")
    for member in msn.crew:
        print(f"- {member.name} ({member.rank.value})"
              f" - {member.specialisation}")
    print("\n========================================="
          "\nExpected validation errors:")
    try:
        SpaceMission(
            mission_id="2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 1, 1, 5, 0, 0),
            duration_days=900,
            crew=space_crew,
            budget_millions=2500.0
        )
    except ValidationError as e:
        print(e.errors()[0]["msg"])
    try:
        no_capt_comm = [
            CrewMember(
                member_id=member.member_id,
                name=member.name,
                rank=Rank.CADET,
                age=member.age,
                specialisation=member.specialisation,
                years_experience=member.years_experience
            )
            for member in space_crew
        ]
        SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 1, 1, 5, 0, 0),
            duration_days=900,
            crew=no_capt_comm,
            budget_millions=2500.0
        )
    except ValidationError as e:
        print(e.errors()[0]["msg"])
    try:
        unexperienced_crew = [
            CrewMember(
                member_id=member.member_id,
                name=member.name,
                rank=member.rank,
                age=member.age,
                specialisation=member.specialisation,
                years_experience=1
            )
            for member in space_crew
        ]
        SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 1, 1, 5, 0, 0),
            duration_days=900,
            crew=unexperienced_crew,
            budget_millions=2500.0
        )
    except ValidationError as e:
        print(e.errors()[0]["msg"])
    try:
        space_crew[0].is_active = False
        SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 1, 1, 5, 0, 0),
            duration_days=900,
            crew=space_crew,
            budget_millions=2500.0
        )
    except ValidationError as e:
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
