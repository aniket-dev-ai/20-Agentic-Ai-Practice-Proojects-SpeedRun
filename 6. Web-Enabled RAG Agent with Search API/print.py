from rich import print_json


def inspect_agent_response(response):
    for index, message in enumerate(response["messages"], start=1):
        print(f"\n{'=' * 80}")
        print(f"MESSAGE #{index} | {message.__class__.__name__}")
        print('=' * 80)

        print_json(data=message.model_dump())