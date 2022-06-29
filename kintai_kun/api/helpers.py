from django.utils import timezone
from django.db.models import Q

def parse_month(params):
  month = timezone.now().month
  if 'month' in params:
    month = params['month']
 
  return month

def search_employee_obj_by_name(self, obj, name):
  obj = obj.filter( Q(employee__user__first_name__icontains=name) |
                    Q(employee__user__last_name__icontains=name))
  return obj