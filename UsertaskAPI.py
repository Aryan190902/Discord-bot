from sqlite3 import connect
from dataclasses import dataclass
from datetime import datetime,timedelta

@dataclass
class UserTask:
    id: str #discord id
    name: str #username
    description : str #description of task
    tim : str #hh:mm 24 hr format
    date : str #dd/mm/yyyy format

    def remaining(self):
        now=datetime.now()
        day,month,year=map(int,self.date.split('/'))
        hour,min=map(int,self.tim.split(':'))
        tasktime=datetime(year,month,day,hour,min)
        return str(timedelta(tasktime-now)).split('.')[0]





