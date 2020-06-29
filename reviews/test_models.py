from django.test import TestCase
from reviews.models import Post
from django.utils import timezone

# Create your tests here.
class TestModelsForReviewApp(TestCase):
    def test_add_reviews(self):
        """To test the Post model works by collecting
        review information from the user
        """
        date_now = timezone.now()
        review = Post(title="great drum", content="amazing",
                      created_date=date_now, published_date=date_now)
        self.assertEqual(review.title, "great drum")
        self.assertEqual(review.content, "amazing")
        self.assertEqual(review.created_date, date_now)
        self.assertEqual(review.published_date, date_now)
