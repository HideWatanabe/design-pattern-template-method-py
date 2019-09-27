import sys
from abc import ABC, abstractmethod

class Repository(ABC):
    def template_method(self):
        self.__audit()
        self.config_repository()
        self.call_action()
        self.after_request()

    def __audit(self):
        action = sys._getframe().f_code.co_name
        print(f"Logging action {action}")

    @abstractmethod
    def config_repository(self):
        pass

    @abstractmethod
    def call_action(self):
        pass

    def after_request(self):
        print("Request to the repository done!")

class DatabaseRepository(Repository):
    def config_repository(self):
        print("Getting database credentials")
        print("Credentials ok!")

    def call_action(self):
        print("Calling database with query sended")
        print("Data ok!")

    def after_request(self):
        print("Resultset ok!")

class RestRepository(Repository):
    def config_repository(self):
        print("Getting request data! Host, port...")
        print("Variables ok!")

    def call_action(self):
        print("Calling rest API")
        print("Request ok! HTTP status code 200")


if __name__ == "__main__":
    database = DatabaseRepository()
    rest = RestRepository()
    database.template_method()
    rest.template_method()