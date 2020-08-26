import datetime as dt


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(
                            date, "%d.%m.%Y").date()


class Calculator:

    def __init__(self, limit):
        self.limit = limit
        self.records = []
        self.today = dt.date.today()

    def add_record(self, record):
        self.records.append(record)

    def sum_amounts(self, date_begin, date_end):
        return sum(record_i.amount
                   for record_i in self.records if
                   date_begin >= record_i.date >= date_end)

    def get_today_stats(self):
        date_end = self.today - dt.timedelta(days=0)
        return self.sum_amounts(self.today, date_end)

    def get_week_stats(self):
        date_week = self.today - dt.timedelta(days=6)
        return self.sum_amounts(self.today, date_week)

    def remainder_on(self):
        return self.limit - self.get_today_stats()


class CashCalculator(Calculator):
    EURO_RATE = float(70)
    USD_RATE = float(60)

    def get_today_cash_remained(self, currency):
        remainder = self.remainder_on()
        rates = {
            "rub": (1, "руб"),
            "eur": (self.EURO_RATE, "Euro"),
            "usd": (self.USD_RATE, "USD")
            }
        money, rate = (rates[currency][0], rates[currency][1])
        foreign_rate = remainder/money
        if remainder > 0:
            remainder = foreign_rate
            return f"На сегодня осталось {remainder:.2f} {rate}"
        if remainder == 0:
            return "Денег нет, держись"
        remainder = abs(foreign_rate)
        return ("Денег нет, держись: твой долг -"
                f" {remainder:.2f} {rate}")


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        remainder_cal = self.remainder_on()
        if remainder_cal > 0:
            return ("Сегодня можно съесть что-нибудь ещё, "
                    f"но с общей калорийностью не более {remainder_cal} кКал")
        return "Хватит есть!"


if __name__ == "__main__":
    pass
