from abc import ABC, abstractmethod


class Employee(ABC):
    @staticmethod
    @abstractmethod
    def work():
        pass


class Worker(Employee):
    @staticmethod
    def work():
        print("I'm working!!")


class SuperWorker(Employee):
    @staticmethod
    def work():
        print("I work very hard!!!")


class SlowWorker(Employee):
    @staticmethod
    def work():
        print("I work very slowly...")


class Manager:
    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, Employee), '`worker` must be of type {}'.format(Worker)
        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


manager = Manager()

worker = Worker()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
try:
    manager.set_worker(super_worker)
except AssertionError:
    print("manager fails to support super_worker....")
manager.manage()

slow_worker = SlowWorker()
manager.set_worker(slow_worker)
manager.manage()
