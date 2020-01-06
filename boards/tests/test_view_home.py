from django.test import TestCase
from django.urls import reverse, resolve
from boards.views import home, board_topics,new_topic
from boards.models import Board,Topic,Post
from django.contrib.auth.models import User
from boards.forms import NewTopicForm


class HomeTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name="Django", description="A basic django discussion forum")
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolve_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_home_view_conatins_link_to_topic_page(self):
        board_topics_url = reverse('board_topics', kwargs={'id': self.board.id})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))