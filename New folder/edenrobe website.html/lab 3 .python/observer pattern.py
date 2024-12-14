class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)


class Observer:
    def update(self, message):
        raise NotImplementedError("This method should be overridden by subclasses.")


class EmailObserver(Observer):
    def update(self, message):
        print(f"Email Notification: {message}")


class SMSObserver(Observer):
    def update(self, message):
        print(f"SMS Notification: {message}")


class PushNotificationObserver(Observer):
    def update(self, message):
        print(f"Push Notification: {message}")


class TaskManager(Subject):
    def __init__(self):
        super().__init__()
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        self.notify(f"Task added: {task}")

    def complete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            self.notify(f"Task completed: {task}")
        else:
            print(f"Task not found: {task}")


# Example usage
if __name__ == "__main__":
    task_manager = TaskManager()

    email_observer = EmailObserver()
    sms_observer = SMSObserver()
    push_observer = PushNotificationObserver()

    task_manager.attach(email_observer)
    task_manager.attach(sms_observer)
    task_manager.attach(push_observer)

    task_manager.add_task("Finish project report")
    task_manager.add_task("Attend team meeting")
    task_manager.complete_task("Finish project report")
