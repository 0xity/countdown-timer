import time
import datetime


class Counter:
    def count(self):
        h, m, s = 0, 0, 0
        try:
            h = int(input("Enter time in hours: "))
            m = int(input("Enter time in minutes: "))
            s = int(input("Enter time in seconds: "))
        except ValueError:
            print("Invalid input!")
            self.count()

        total_seconds = h * 3600 + m * 60 + s

        while total_seconds > 0:
            timer = datetime.timedelta(seconds=total_seconds)
            print(timer, end="\r\n")
            time.sleep(1)
            total_seconds -= 1

        print("Timer is up!")


if __name__ == "__main__":
    counter = Counter()
    counter.count()
