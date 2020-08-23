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

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today = dt.date.today()
        sum_records = sum(int(record_i.amount)
                          for record_i in self.records if
                          record_i.date == today)
        return sum_records

    def get_week_stats(self):
        date_week = dt.date.today() - dt.timedelta(days=6)
        sum_records = sum(int(record_i.amount)
                          for record_i in self.records if
                          dt.date.today() >= record_i.date >= date_week)
        return sum_records

    def remainder_on(self):
        return self.limit - self.get_today_stats()


class CashCalculator(Calculator):
    EURO_RATE = float(80)
    USD_RATE = float(70)

    def get_today_cash_remained(self, currency):
        remainder = self.remainder_on()
        remainder_eur = remainder/self.EURO_RATE
        remainder_usd = remainder/self.USD_RATE
        abs_remainder = abs(remainder)
        abs_remainder_eur = abs(remainder_eur)
        abs_remainder_usd = abs(remainder_usd)
        rates = {
            "rub": "руб",
            "eur": "Euro",
            "usd": "USD"
            }
        rate = rates[currency]

        if remainder > 0:
            if currency == "rub":
                return f"На сегодня осталось {remainder:.2f} {rate}"
            elif currency == "eur":
                return ("На сегодня осталось"
                        f" {remainder_eur:.2f} {rate}")
            else:
                return ("На сегодня осталось"
                        f" {remainder_usd:.2f} {rate}")
        elif remainder == 0:
            return ("Денег нет, держись")
        else:
            if currency == "rub":
                return ("Денег нет, держись: твой долг -"
                        f" {abs_remainder:.2f} {rate}")
            elif currency == "eur":
                return ("Денег нет, держись: твой долг -"
                        f" {abs_remainder_eur:.2f} {rate}")
            else:
                return ("Денег нет, держись: твой долг -"
                        f" {abs_remainder_usd:.2f} {rate}")


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        remainder_cal = self.remainder_on()
        if remainder_cal > 0:
            return ("Сегодня можно съесть что-нибудь ещё, "
                    f"но с общей калорийностью не более {remainder_cal} кКал")
        else:
            return "Хватит есть!"


if __name__ == "__main__":
    pass
