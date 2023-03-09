import pytest
from django.urls import reverse


@pytest.mark.smoke
def test_add_course_page_with_instructor(client, user_instructor):
    url = reverse('courses:course-create')

    client.login(email=user_instructor.email, password='testPass123')
    response = client.get(url)

    assert response.status_code == 200
    assert '<h1>Create course</h1>' in response.content.decode('UTF-8')


def test_add_course_page_without_logged_in_user(client):
    url = reverse('courses:course-create')

    response = client.get(url)

    assert response.status_code == 302
    assert '/users/login/' in response.url

    next_response = client.get(response.url)
    assert next_response.status_code == 200
    assert '<h1>Login</h1>' in next_response.content.decode('UTF-8')


# @pytest.mark.skip(reason='WIP')
# @pytest.mark.skipif(reason='WIP') i dodać CONDITION
def test_add_course_page_with_logged_in_user_not_instructor(client, user):
    url = reverse('courses:course-create')

    client.login(email=user.email, password='testPass123')
    response = client.get(url)

    assert response.status_code == 403
