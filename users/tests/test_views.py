from django.urls import reverse


def test_login_page(client):
    url = reverse('users:login')
    response = client.get(url)

    assert response.status_code == 200
    assert '<h1>Login</h1>' in response.content.decode('UTF-8')


def test_register_user(client, django_user_model):
    url = reverse('users:registration')
    user_data = {
        'email': 'haha@ha.pl',
        'fullname': 'haha',
        'is_instructor': False,
        'password': '123',
        'password_confirmation': '123'
    }

    response = client.post(url, data=user_data)
    user_queryset = django_user_model.objects.filter(email='haha@ha.pl')

    assert response.status_code == 302
    assert len(user_queryset) == 1
    assert user_queryset.first().fullname == 'haha'
