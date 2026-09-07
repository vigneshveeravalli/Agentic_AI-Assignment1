import json

from policy import evaluate_expense


# Load synthetic data
with open(
    "data.json",
    "r",
    encoding="utf-8"
) as file:

    expenses = json.load(file)


print("=" * 60)
print("POLICY COMPLIANCE AGENT")
print("=" * 60)


for expense in expenses:

    result = evaluate_expense(expense)

    print("\nExpense ID:", result["id"])
    print("Employee:", result["employee"])
    print("Status:", result["status"])

    if result["violations"]:

        print("Violations:")

        for violation in result["violations"]:

            print("-", violation)

    else:

        print("Violations: None")