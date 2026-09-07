from datetime import date


MAX_EXPENSE = 10000

ALLOWED_CATEGORIES = [
    "Travel",
    "Food",
    "Office"
]


def check_amount(expense):

    if expense["amount"] > MAX_EXPENSE:
        return False, "Expense exceeds the ₹10,000 limit."

    return True, None


def check_receipt(expense):

    if not expense["receipt"]:
        return False, "Receipt is missing."

    return True, None


def check_category(expense):

    if expense["category"] not in ALLOWED_CATEGORIES:
        return False, "Expense category is not allowed."

    return True, None


def check_date(expense):

    expense_date = date.fromisoformat(
        expense["date"]
    )

    today = date.today()

    if expense_date > today:
        return False, "Expense date is in the future."

    return True, None


def evaluate_expense(expense):

    violations = []

    rules = [
        check_amount,
        check_receipt,
        check_category,
        check_date
    ]

    for rule in rules:

        passed, message = rule(expense)

        if not passed:
            violations.append(message)

    if violations:

        status = "NON-COMPLIANT"

    else:

        status = "COMPLIANT"

    return {
        "id": expense["id"],
        "employee": expense["employee"],
        "status": status,
        "violations": violations
    }
