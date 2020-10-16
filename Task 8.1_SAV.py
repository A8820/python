
class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 2025:
                    return f'Correct'
                else:
                    return f'Unknown year'
            else:
                return f'Unknown month'
        else:
            return f'Unknown day'

    def __str__(self):
        return f'Current date {Data.extract(self.day_month_year)}'


today = Data('15 - 10 - 2020')
print(today)
print(Data.valid(33, 11, 2022))
print(Data.valid(11, 31, 2000))
print(Data.extract('11 - 11 - 2011'))
print(today.extract('15 - 10 - 2020'))
