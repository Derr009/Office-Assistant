def route_question(question):
    question = question.lower()

    policy_keywords = [
        "policy",
        "leave policy",
        "travel policy",
        "expense policy",
        "work from home",
        "security policy",
        "it policy",
        "handbook"
    ]

    employee_keywords = [
        "my leave",
        "my leave balance",
        "leave balance",
        "how many leaves",
        "my expenses",
        "my laptop",
        "my asset",
        "my details",
        "my information",
        "employee details"
    ]

    has_policy = any(
        keyword in question
        for keyword in policy_keywords
    )

    has_employee = any(
        keyword in question
        for keyword in employee_keywords
    )

    if has_policy and has_employee:
        return "combined"

    if has_policy:
        return "policy"

    if has_employee:
        return "employee"

    return "unknown"