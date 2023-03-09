import pytest
from django.contrib.auth.models import Permission


@pytest.fixture
def user(db, django_user_model):
    """User instance from default django user model."""
    return django_user_model.objects.create_user(
        email='test@user.pl',
        fullname='Test User',
        password='testPass123'
    )


@pytest.fixture
def user_instructor(db, django_user_model):
    """User instance from default django user model with instructor permissions."""
    user = django_user_model.objects.create_user(
        email='instructor@user.pl',
        fullname='Instructor User',
        password='testPass123',
        is_instructor=True,
    )
    permission = Permission.objects.get(name='Can add course')
    user.user_permissions.add(permission)

    yield user
