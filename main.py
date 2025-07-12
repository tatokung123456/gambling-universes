from logic import load_choices, random_choice

if __name__ == "__main__":
    choices = load_choices("data/choices.txt")
    print("รายการที่สามารถสุ่มได้:")
    for i, item in enumerate(choices, 1):
        print(f"{i}. {item}")

    input("\nกด Enter เพื่อสุ่ม...")
    result = random_choice(choices)
    print(f"\n🎯 คุณได้: {result}")
