"""
PS 58 - Fitness Data Tracker
Rungta International Skills University
Language: Python 3
Concepts: Lists, Functions, Calculations, Visualization
"""

try:
    import matplotlib.pyplot as plt  # type: ignore
except ModuleNotFoundError:
    plt = None

DAILY_GOAL = 10000

# Records are kept in Python lists (index 0 = Day 1)
steps_list = []
calories_list = []


# ---------- Input validation ----------
def read_whole_number(text):
    """Return int if text is a non-negative whole number, else None."""
    text = text.strip()
    if text.isdigit():
        return int(text)
    return None


def read_positive_float(text):
    """Return float if text is a positive number, else None."""
    try:
        value = float(text.strip())
    except ValueError:
        return None
    return value if value > 0 else None


def read_non_negative_float(text):
    """Return float if text is a non-negative number, else None."""
    try:
        value = float(text.strip())
    except ValueError:
        return None
    return value if value >= 0 else None


# ---------- Core features ----------
def add_record():
    steps = read_whole_number(input("Steps: "))
    if steps is None:
        print("Invalid steps. Enter a non-negative whole number. Record not saved.")
        return

    calories = read_non_negative_float(input("Calories: "))
    if calories is None:
        print("Invalid calories. Enter a non-negative number. Record not saved.")
        return

    steps_list.append(steps)
    calories_list.append(calories)

    day = len(steps_list)
    percent = steps / DAILY_GOAL * 100
    achieved = "Yes" if steps >= DAILY_GOAL else "No"
    print(f"Record saved for Day {day}. Goal achieved: {achieved} ({percent:.2f}% of goal)")


def calculate_average(values):
    return sum(values) / len(values)


def calculate_total(values):
    return sum(values)


def find_best_day(steps):
    """Return (day_number, steps) for the day with the most steps."""
    best_index = steps.index(max(steps))
    return best_index + 1, steps[best_index]


def count_goal_days(steps):
    return sum(1 for s in steps if s >= DAILY_GOAL)


def show_summary():
    if not steps_list:
        print("No records yet. Add a record first (option 1).")
        return

    avg_steps = calculate_average(steps_list)
    total_cal = calculate_total(calories_list)
    best_day, best_steps = find_best_day(steps_list)
    goal_days = count_goal_days(steps_list)

    print(
        f"Average steps: {avg_steps:.2f} | Total calories: {total_cal:g} | "
        f"Goal days: {goal_days}/{len(steps_list)}"
    )
    print(f"Best day: Day {best_day} ({best_steps} steps)")


def calculate_bmi(weight, height):
    return weight / (height ** 2)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    return "Obese"


def show_bmi():
    weight = read_positive_float(input("Weight (kg): "))
    if weight is None:
        print("Invalid weight. Enter a positive number.")
        return

    height = read_positive_float(input("Height (m): "))
    if height is None:
        print("Invalid height. Enter a positive number.")
        return

    bmi = calculate_bmi(weight, height)
    print(f"BMI: {bmi:.2f} | Category: {bmi_category(bmi)}")


def show_chart():
    if not steps_list:
        print("No records yet. Add a record first (option 1).")
        return

    days = [f"Day {i}" for i in range(1, len(steps_list) + 1)]

    plt.figure(figsize=(8, 5))
    plt.bar(days, steps_list, color="steelblue", label="Daily steps")
    plt.axhline(DAILY_GOAL, color="red", linestyle="--", label=f"Goal ({DAILY_GOAL} steps)")
    plt.title("Daily Steps")
    plt.xlabel("Day")
    plt.ylabel("Steps")
    plt.legend()
    plt.tight_layout()
    plt.show()


# ---------- Main menu ----------
def main():
    while True:
        print("\n===== Fitness Data Tracker =====")
        print("1. Add record")
        print("2. Summary")
        print("3. BMI")
        print("4. Chart")
        print("5. Exit")
        choice = input("Menu option: ").strip()

        if choice == "1":
            add_record()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            show_bmi()
        elif choice == "4":
            show_chart()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Choose 1-5.")


if __name__ == "__main__":
    main()
