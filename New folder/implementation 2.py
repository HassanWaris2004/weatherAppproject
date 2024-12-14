from abc import ABC, abstractmethod

# Step 1: Define the Task interface
class Task(ABC):
    @abstractmethod
    def execute(self):
        pass

# Step 2: Implement different task classes
class EmailTask(Task):
    def __init__(self, recipient: str, subject: str, body: str):
        self.recipient = recipient
        self.subject = subject
        self.body = body

    def execute(self):
        print(f"Sending email to {self.recipient} with subject '{self.subject}' and body:\n{self.body}\n")

class ReportGenerationTask(Task):
    def __init__(self, report_name: str):
        self.report_name = report_name

    def execute(self):
        print(f"Generating report: {self.report_name}\n")

# Step 3: Create the Task Processor
class TaskProcessor:
    def process_task(self, task: Task):
        print("Processing task...")
        task.execute()

# Test program
if __name__ == "__main__":
    # Create instances of different tasks
    email_task = EmailTask("eg@example.com", "Meeting Reminder", "Don't forget our meeting at 10 AM.")
    report_task = ReportGenerationTask("Annual Financial Report")
    
    # Create a TaskProcessor
    task_processor = TaskProcessor()
    
    # Process the tasks
    print("Processing Email Task:")
    task_processor.process_task(email_task)
    
    print("Processing Report Generation Task:")
    task_processor.process_task(report_task)
