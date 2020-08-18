import datetime as dt

class Record:
    def __init__(self, amount, comment, date = None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
              
class Calculator:                       
    def __init__(self, limit):
        self.limit = limit
        self.records = []
    
    def add_record(self, record):
        self.records.append(record)
        return self.records
    
    def get_today_stats(self):
        sum_records = 0
        for record in self.records:
            if record.date == dt.date.today():
                sum_records += record.amount
        return sum_records
    
    def get_week_stats(self):
        date_week = dt.date.today() - dt.timedelta(days=6)
        sum_records = 0
        for record in self.records: 
            if (record.date >= date_week) and (record.date <= dt.date.today()):
                sum_records += record.amount
        return sum_records

class CashCalculator(Calculator):
    EURO_RATE = float(80)
    USD_RATE = float(70)
    
    def get_today_cash_remained(self, currency):
        remainder = self.limit - self.get_today_stats()
        rates = {
            "rub" : "руб",
            "eur" : "Euro",
            "usd" : "USD"
        }
        if currency == "rub":
            if remainder > 0:
                return ("На сегодня осталось "
                f"{round(remainder, 2)} {rates[currency]}")
            elif remainder == 0:
                return ("Денег нет, держись")
            elif remainder < 0:
                return ("Денег нет, держись: твой долг - "
                f"{round(abs(remainder), 2)} {rates[currency]}")
        elif currency == "eur":
            if remainder > 0:
                return ("На сегодня осталось " 
                f"{round(remainder/self.EURO_RATE, 2)} {rates[currency]}")
            elif remainder == 0:
                return ("Денег нет, держись")
            elif remainder < 0:
                return ("Денег нет, держись: твой долг - "
                f"{round(abs(remainder/self.EURO_RATE,), 2)} {rates[currency]}")
        elif currency == "usd":
            if remainder > 0:
                return ("На сегодня осталось "
                f"{round(remainder/self.USD_RATE, 2)} {rates[currency]}")
            elif remainder == 0:
                return ("Денег нет, держись")
            elif remainder < 0:
                return ("Денег нет, держись: твой долг - "
                f"{round(abs(remainder/self.USD_RATE), 2)} {rates[currency]}")
           
class CaloriesCalculator(Calculator):
      
    def get_calories_remained(self):
        remainder_cal = self.limit - self.get_today_stats()
        if remainder_cal > 0:
            return (f"Сегодня можно съесть что-нибудь ещё, "
            f"но с общей калорийностью не более {remainder_cal} кКал")
        else:
            return ("Хватит есть!")

        



