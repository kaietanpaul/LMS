import pytest


# @pytest.fixture(scope='function' ) #scope='session' przed i po  sesji w tym wypadku sa dwie funkcje wiec dwie kropkiu
# def fixture_example():
#     # setup
#     print('\n', "-" * 20)
#     print("fixture")
#     yield 42
#     # teardown
#     print('\npo')


@pytest.mark.slow
def test_create_user(user, django_user_model):
    users = django_user_model.objects.all()
    assert len(users) == 2


@pytest.mark.slow
@pytest.mark.smoke
def test_change_password(user, django_user_model):
    # Arrange
    user_db = django_user_model.objects.get(email='test@user.pl')
    # Act
    user_db.set_password('secret')

    # Assert
    assert user_db.check_password('secret') is True
