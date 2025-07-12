from logic import load_choices, random_choice

def main():
    print("🎲 โปรแกรมสุ่มรายการ 🎲")
    print("==========================")

    # โหลดรายการจากไฟล์
    choices = load_choices("data/choices.txt")

    if not choices:
        print("⚠️ ไม่พบรายการในไฟล์หรือไฟล์หาย กรุณาตรวจสอบ data/choices.txt")
        return

    # แสดงรายการทั้งหมด
    print("\nรายการที่สามารถสุ่มได้:")
    for i, item in enumerate(choices, 1):
        print(f"{i}. {item}")

    input("\nกด Enter เพื่อทำการสุ่ม...")

    # แสดงผลลัพธ์การสุ่ม
    result = random_choice(choices)
    print(f"\n🎯 ผลลัพธ์: {result}")

if __name__ == "__main__":
    main()
