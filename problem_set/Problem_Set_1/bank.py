def main():
    greeting = input("Greeting: ").strip().lower()
    reward = determine_reward(greeting)
    print(f"${reward}")


def determine_reward(greeting):
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100
main()