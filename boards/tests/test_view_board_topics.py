from django.test import TestCase
from django.urls import reverse, resolve
from boards.views import home,TopicListView
from boards.models import Board,Topic,Post
from django.contrib.auth.models import User
from boards.forms import NewTopicForm


class BoardTopicTests(TestCase):
    def setUp(self):
        Board.objects.create(name="Python", description="A test Board for Django")

    def test_board_topics_view_status_code(self):
        url = reverse('board_topics', kwargs={'id': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics', kwargs={'id': 5})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_topics_resolve_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func.view_class, TopicListView)

    def test_board_topics_view_contains_link_back_home_page(self):
        board_topics_url = reverse('board_topics',kwargs={'id':1})
        response = self.client.get(board_topics_url)
        home_page_url = reverse('home')
        self.assertContains(response,'href="{0}"'.format(home_page_url))