# task 10
class Event:
    def __init__(self, name, date, time, description):
        self.name = name
        self.date = date
        self.time = time
        self.description = description
    def __str__(self):
        return f"{self.name}({self.date} o {self.time}) - {self.description}"    
    
class Calendar:
    def __init__(self):
        self.events = []
    def add_event(self, event):
        self.events.append(event)
    def get_events_by_date(self, date):
        result = []
        for e in self.events:
            if e.date == date:
                result.append(e)
            return result                
    def show_all(self):
        for e in self.events:
            print(e)    
            
cal = Calendar()
cal.add_event(Event("Meeting", "2025-10-20", "10:00", "Project discussion"))  
cal.add_event(Event("Lunch", "2025-10-20", "13:00", "With client"))   
cal.add_event(Event("Movie", "2025-10-21", "19:00", "Cinema night"))

print("All events: ")
cal.show_all()

print("\n Events on 2025-10-20:")
for e in cal.get_events_by_date("2025-10-20"):
    print(e)       