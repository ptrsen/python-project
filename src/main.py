import argparse

def greet(name):
    return f"Hello, {name}!"

def cli():
    parser = argparse.ArgumentParser(description="Greet someone by name.")
    parser.add_argument("name", help="Name of the person to greet")
    args = parser.parse_args()

    # Call the `greet` function with the provided name
    print(greet(args.name))

if __name__ == "__main__":
    cli()