from sqlalchemy import text
from app.database.connection import engine


def get_employee(employee_id):
    query = text("""
        select
            e.employee_id,
            e.name,
            e.department,
            e.designation,
            e.location,
            lb.casual_leave,
            lb.earned_leave,
            lb.sick_leave
        from Employee e
        join LeaveBalance lb
            on e.employee_id = lb.employee_id
        where e.employee_id = :employee_id
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {"employee_id": employee_id}
        ).mappings().first()

    if not result:
        return None

    return dict(result)