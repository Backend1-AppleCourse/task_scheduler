
class Task:
    def __init__(self):
        task_name = input('Enter task name: ')
        while not task_name:
            task_name = input('Please enter a task name: ')
        task_duration = input('Enter task duration: ')
        while not task_duration.isdigit() or int(task_duration) > 8 or int(task_duration) < 1:
            task_duration = input('Task duration cannot exceed 8 hours. Please enter a valid duration: ')
        task_duration = int(task_duration)
        day = input('Enter day (0-4) or leave empty: ')
        while day and (not day.isdigit() or int(day) > 4 or int(day) < 0):
            day = input('Please enter a valid day (0-4) or leave empty: ')
        if day:
            day = int(day) if day else None
        start_hour = input('Enter start hour (0-7) or leave empty: ')
        while start_hour and (not start_hour.isdigit() or int(start_hour) > 7 or int(start_hour) < 0):
            start_hour = input('Please enter a valid start hour (0-7) or leave empty: ')
        if start_hour:
            start_hour = int(start_hour)


        self.name = task_name
        self.duration = task_duration
        self.day = day
        self.start_hour = start_hour

    def __str__(self):
        return f'{self.name} - {self.duration} hours'

class Schedule:
    def __init__(self):
        self.schedule = [[None for _ in range(8)] for _ in range(5)]

    def add_task(self, task):
        if task.day and task.start_hour:
            if self.schedule[task.day][task.start_hour]:
                print(f'Task {self.schedule[task.day][task.start_hour]} is already scheduled at {task.start_hour}:00 on day {task.day}')
                overwrite = input('Would you like to overwrite it? (y/n): ')
                if overwrite == 'y':
                    for hour in range(task.duration):
                        self.schedule[task.day][task.start_hour+hour] = task.name
                    print(f'Task {task.name} has been scheduled at {task.start_hour}:00 on day {task.day}')
                else:
                    print('Please provide a new time for the task')
            else:
                for hour in range(task.duration):
                    self.schedule[task.day][task.start_hour+hour] = task.name
                print(f'Task {task.name} has been scheduled at {task.start_hour}:00 on day {task.day}')
        else:
            for day in range(5):
                for hour in range(8):
                    if not self.schedule[day][hour]:
                        if hour + task.duration <= 8:
                            for i in range(task.duration):
                                self.schedule[day][hour + i] = task.name
                            print(f'Task {task.name} has been scheduled on day {day} from {hour}:00 to {hour + task.duration}:00')
                            break
                else:
                    continue
                break

    def print_schedule(self):
        for i, day in enumerate(self.schedule):
            print(f'Day {i}')
            for hour, task in enumerate(day):
                print(f'{hour}:00 - {task}')
            print('\n')

def task_scheduler():
    schedule = Schedule()
    while True:
        new_task = Task()

        schedule.add_task(new_task)

        print('Would you like to add another task?')
        if input('y/n: ') == 'n':
            break

    schedule.print_schedule()
    
task_scheduler()




