import pytest
from employee.models import Employee


@pytest.mark.django_db
def test_employee_empty_model():
    count = Employee.objects.count()
    print(count, "Employee(s)")
    assert count == 0


@pytest.mark.django_db
def test_employee_model():
    Employee.objects.create_user(
        username="test_user",
        password="pass1234",
        email="test@test.com",
        address="Dhaka",
        contact_no="+8801234567",
        emergency_contact="+880986544323",
        is_verified=True
    )

    count = Employee.objects.all().count()
    print(count, "Employee(s)")
    assert Employee.objects.count() == count
