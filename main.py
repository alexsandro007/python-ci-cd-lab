from abc import ABC, abstractmethod

# Абстрактный класс Product
class Watch(ABC):
    @abstractmethod
    def display_time(self):
        pass

# Конкретные классы продуктов
class SmartWatch(Watch):
    def display_time(self):
        return "Displaying time on a smart watch with additional features"

class AnalogWatch(Watch):
    def display_time(self):
        return "Displaying time on an analog watch"

# Фабрика для создания продуктов
class WatchFactory:
    @staticmethod
    def create_watch(watch_type):
        if watch_type == "smart":
            return SmartWatch()
        elif watch_type == "analog":
            return AnalogWatch()
        else:
            raise ValueError("Unknown watch type")

# Пример использования фабрики
if __name__ == "__main__":
    watch_type = input("Enter watch type (smart/analog): ")
    watch = WatchFactory.create_watch(watch_type)
    print(watch.display_time())