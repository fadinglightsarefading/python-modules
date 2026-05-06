import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    names = ["Ananda", "Julius", "Thomas", "Donald", "Santiago", "Karl", "Leo",
             "Michel", "Diane", "Gordon", "Pete", "Sarah", "Gregory", "Gustave"]
    actions = ["inquire", "arrest", "approve", "desire", "investigate", "lead",
               "prevent", "mislead", "supply", "turn", "defend", "pour libation"]
    while True:
        yield (random.choice(names), random.choice(actions))


def consume_event(events: list) -> typing.Generator[tuple[str, str], None, None]:
    while len(events):
        event_index = random.randrange(len(events))
        event = events[event_index]
        del events[event_index]
        yield event


def ft_data_streams() -> None:
    print("=== Game Data Stream Processor ===")
    events = gen_event()
    for i in range(0, 1000):
        event = next(events)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    ten_events = []
    for i in range(0, 10):
        ten_events += [next(events)]
    print(f"Built list of 10 events: {ten_events}")
    for event in consume_event(ten_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events}")


def main() -> None:
    ft_data_streams()


if __name__ == "__main__":
    main()
