import datetime
class Project:
    def __init__(self,name,start_date,priority,cost_estimate,completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"{self.name}, start: {self.start_date},  priority {self.priority}, estimate: ${self.cost_estimate}, completion: {self.completion_percentage}%"

    def is_complete(self):
        return self.completion_percentage == 100

    def get_new_completion(self,new_percentage):
        self.completion_percentage = new_percentage

    def date_filter(self,user_date):
        date_condition = datetime.datetime.strptime(user_date, "%d/%m/%Y").date()
        start_date = datetime.datetime.strptime(self.start_date, "%d/%m/%Y").date()
        return start_date >= date_condition

