from app.agents.router import route_question
from app.tools.employee_tool import get_employee
from app.rag.rag_chain import ask_policy_question


def ask_agent(question, employee_id=None):
    route = route_question(question)

    if route == "policy":
        return ask_policy_question(question)

    if route == "employee":
        if not employee_id:
            return "Please provide your employee ID."

        employee = get_employee(employee_id)

        if not employee:
            return "Employee not found."

        return (
            f"You currently have "
            f"{employee['casual_leave']} casual leaves, "
            f"{employee['earned_leave']} earned leaves, and "
            f"{employee['sick_leave']} sick leaves."
        )

    if route == "combined":
        if not employee_id:
            return "Please provide your employee ID."

        employee = get_employee(employee_id)

        if not employee:
            return "Employee not found."

        policy_answer = ask_policy_question(question)

        return (
    f"{policy_answer}\n\n"
    f"Your current leave balance is:\n"
    f"- Casual Leave: {employee['casual_leave']} days\n"
    f"- Earned Leave: {employee['earned_leave']} days\n"
    f"- Sick Leave: {employee['sick_leave']} days"
)

    return "I'm not sure whether this is a policy or employee-related question."