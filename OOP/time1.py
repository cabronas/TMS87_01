class MyTime:

    # def __init__(self, hours, minutes, seconds):
    #     self.__hours = hours
    #     self.__minutes = minutes
    #     self.__seconds = seconds
    def __init__(self, *args):
        if args[0].__class__ == MyTime:
            self.__hours = args[0].hours
            self.__minutes = args[0].minutes
            self.__seconds = args[0].seconds
        elif len(args) == 3:
            self.__hours = int(args[0])
            self.__minutes = int(args[1])
            self.__seconds = int(args[2])
        elif len(args) == 1:
            possible_time = args[0].split("-")
            if len(possible_time) == 3:
                self.__hours = int(possible_time[0])
                self.__minutes = int(possible_time[1])
                self.__seconds = int(possible_time[2])
        else:
            self.__hours = 0
            self.__minutes = 0
            self.__seconds = 0


    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, hours):
        self.__hours = hours

    @property
    def minutes(self):
        return self.__minutes

    @minutes.setter
    def minutes(self, minutes):
        self.__minutes = minutes

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self, seconds):
        self.__seconds = seconds

    def __str__(self):
        return f"{self.hours}-{self.minutes}-{self.seconds}"

    def __add__(self, other):
        # seconds
        spilsecond = False
        temp = MyTime(0, 0, 0)
        seconds = other.seconds
        if self.seconds + seconds < 60:
            temp.seconds = self.seconds + seconds
        else:
            spilsecond = True
            temp.seconds = self.seconds + seconds - 60
        # minutes
        spilminute = False
        minutes = other.minutes
        if spilsecond:
            minutes += 1
        if self.minutes + minutes < 60:
            temp.minutes = self.minutes + minutes
        else:
            spilminute = True
            temp.minutes = self.minutes + minutes - 60
        # hours
        hours = other.hours
        if spilminute:
            hours += 1
        if self.hours + hours < 24:
            temp.hours = self.hours + hours
        else:
            temp.hours = self.hours + hours - 24
        return temp

    def __sub__(self, other):
        # seconds
        spilsecond = False
        temp = MyTime(0, 0, 0)
        seconds = other.seconds
        if self.seconds - seconds >= 0:
            temp.seconds = self.seconds - seconds
        else:
            spilsecond = True
            temp.seconds = self.seconds - seconds + 60
        # minutes
        spilminute = False
        minutes = other.minutes
        if spilsecond:
            minutes += 1
        if self.minutes - minutes >= 0:
            temp.minutes = self.minutes - minutes
        else:
            spilminute = True
            temp.minutes = self.minutes - minutes + 60
        # hours
        hours = other.hours
        if spilminute:
            hours += 1
        if self.hours - hours >= 0:
            temp.hours = self.hours - hours
        else:
            temp.hours = self.hours - hours + 24
        return temp

    def __eq__(self, other):
        return self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds

    def __ne__(self, other):
        return not (self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds)
