class Observer:

    def __init__(self):
        self.subscribers = []

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def delete_subscriber(self, subscriber):
        self.subscribers.remove(subscriber)

    def show_subscribers(self):
        for subscriber in self.subscribers:
            print(subscriber.name)

    def __str__(self):
        return 'Observer pattern'


class Subscriber:
    def __init__(self, name):
        self.name = name


observer = Observer()

person1 = Subscriber("Mathew")
person2 = Subscriber('Bob')
person3 = Subscriber('Dylan')

observer.add_subscriber(person1)
observer.add_subscriber(person2)
observer.add_subscriber(person3)

observer.delete_subscriber(person3)


observer.__str__()
observer.show_subscribers()
