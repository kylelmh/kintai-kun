from django.test import TestCase
from django.contrib.auth.models import User
from kintai_kun.models import *
from django.utils import timezone

# Create your tests here.
class WorkTimestampFetch(TestCase):
  def test_query_count(self):
    User.objects.create(first_name="K", last_name="L", email="a@a.com")  
    Employee.objects.create(contract=1, user_id=1)
    for i in range(1,5):
      WorkTimestamp.objects.create(employee_id=1, stamp_type=1)
    with self.assertNumQueries(3):
      q = WorkTimestamp.objects.all().prefetch_related('employee__user')
      q.filter(employee__user__first_name="K", created_on__month=timezone.now().month).order_by('-created_on')
      print(q)

    self.assertEqual(len(q), 4)