from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def business_rules(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with \"AC\""
                             " (Alien Contact)")
        if (
                self.contact_type == ContactType.PHYSICAL
                and not self.is_verified
        ):
            raise ValueError("Physical contact must be verified")
        if (
                self.contact_type == ContactType.TELEPATHIC and
                self.witness_count < 3
        ):
            raise ValueError("Telepathic contact must have at least"
                             " 3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong singals (> 7.0) should include "
                             "received messages")
        return self


def main() -> None:
    print("Alient Contact Log Validation\n"
          "=======================================")

    alcon = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2024, 1, 1, 14, 30, 0),
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Raxacoricofalapatorious"
    )
    print(f"Valid contact report:\n"
          f"ID: {alcon.contact_id}\n"
          f"Type: {alcon.contact_type.value}\n"
          f"Location: {alcon.location}\n"
          f"Signal: {alcon.signal_strength}/10\n"
          f"Duration: {alcon.duration_minutes} minutes\n"
          f"Witnesses: {alcon.witness_count}\n"
          f"Message: {alcon.message_received}")

    print("\n======================================="
          "\nExpected validation errors:")
    try:
        AlienContact(
            contact_id="2024_001",
            timestamp=datetime(2024, 1, 1, 14, 30, 0),
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=5.0,
            duration_minutes=45,
            witness_count=5,
        )
    except ValidationError as e:
        print(e.errors()[0]["msg"])

    try:
        AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2024, 1, 1, 14, 30, 0),
            location="Area 51, Nevada",
            contact_type=ContactType.PHYSICAL,
            signal_strength=5.0,
            duration_minutes=45,
            witness_count=5,
        )
    except ValidationError as e:
        print(e.errors()[0]["msg"])

    try:
        AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2024, 1, 1, 14, 30, 0),
            location="Area 51, Nevada",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=5.0,
            duration_minutes=45,
            witness_count=1,
        )
    except ValidationError as e:
        print(e.errors()[0]["msg"])

    try:
        AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2024, 1, 1, 14, 30, 0),
            location="Area 51, Nevada",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=3,
        )
    except ValidationError as e:
        print(e.errors()[0]["msg"])
    print()


if __name__ == "__main__":
    main()
