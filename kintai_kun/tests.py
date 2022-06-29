from django.test import TestCase
from django.contrib.auth.models import User
from kintai_kun.models import *
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase


APIS = {
  "worktimestamps":"/api/worktimestamps/?format=json",
  "user_worktimestamps":"/api/user_worktimestamps/?format=json",
  "shifts":"/api/shifts/?format=json",
  "user_shifts":"/api/user_shifts/?format=json",
  "employees":"/api/employees/?format=json"
}

# Create your tests here.
class RestQuery(APITestCase):
  def setUp(self):
    self.root = User.objects.create_superuser(username="root", password="1234")
    self.c = self.client
    self.c.force_login(self.root)

  def test_worktimestamp(self):
    with self.assertNumQueries(3):
      self.c.get(APIS['worktimestamps'])

  def test_user_worktimestamp(self):
    with self.assertNumQueries(3):
      self.c.get(APIS['user_worktimestamps'])

  def test_shift(self):
    with self.assertNumQueries(3):
      self.c.get(APIS['shifts'])

  def test_user_shift(self):
    with self.assertNumQueries(3):
      self.c.get(APIS['user_shifts'])

  def test_employee(self):
    with self.assertNumQueries(3):
      self.c.get(APIS['employees'])

class RestAuth(APITestCase):
  def setUp(self):
    self.root = User.objects.create_superuser(username="root", password="1234", )
    self.user = User.objects.create_user(username="user", password="1234")

  def test_user_permissions(self):
    c = self.client
    c.force_login(self.user)
    self.assertEqual(c.get(APIS['worktimestamps']).status_code, 403) 
    self.assertEqual(c.get(APIS['user_worktimestamps']).status_code, 200) 
    self.assertEqual(c.get(APIS['shifts']).status_code, 403) 
    self.assertEqual(c.get(APIS['user_shifts']).status_code, 200) 
    self.assertEqual(c.get(APIS['employees']).status_code, 403)
   
  def test_anon_permissions(self):
    c = self.client
    self.assertEqual(c.get('/api/').status_code, 403)
    for k in APIS.values():
      self.assertEqual(c.get(k).status_code, 403)

  def test_root_permissions(self):
    c = self.client
    c.force_login(self.root)
    for k in APIS.values():
      self.assertEqual(c.get(k).status_code, 200)