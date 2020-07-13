from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event,Invite


class Calendar(HTMLCalendar):
  def __init__(self, user,year=None, month=None):
    self.year = year
    self.month = month
    self.user = user
    super(Calendar, self).__init__()

  def formatday(self, day, events):
    events_per_day = Event.objects.filter(date_of_happening__day=day).filter(user=self.user)
    invites_per_day = Invite.objects.filter(invited_to__date_of_happening__day=day).filter(user=self.user)
    d = ''
    # print(events_per_day)
    for event in events_per_day:
      d += f'<li class="calendar_list"> <a href="{event.get_absolute_url()}"> {event.title} </a>  </li>'
    for event in invites_per_day:
      d += f'<li class="calendar_list invites"> <a href="{event.invited_to.get_absolute_url()}"> {event.invited_to.title} </a>  </li>'
    if day != 0:
     return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
    return '<td></td>'
  
  def formatweek(self, theweek, events):
    week = ''
    for d, weekday in theweek:
      week += self.formatday(d, events)
    return f'<tr> {week} </tr>'
  
  def formatmonth(self, withyear=True):
    events = Event.objects.filter(date_of_happening__year=self.year, date_of_happening__month=self.month).filter(user=self.user)
    cal = f'<table border="0" cellpadding="0" cellspacing="0"     class="calendar">\n'  
    cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
    cal += f'{self.formatweekheader()}\n'
    for week in self.monthdays2calendar(self.year, self.month):
      cal += f'{self.formatweek(week, events)}\n'
    cal+= f'</table>'  
    return cal