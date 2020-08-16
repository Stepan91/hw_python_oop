import datetime as dt

class Record:
    def __init__(self, amount, comment, date = None):
        self.amount = amount
        if date is None:
            date = dt.datetime.now().strftime('%d.%m.%Y')
        else:
            date = dt.datetime().strftime('%d.%m.%Y')
        self.comment = comment
        

class Calculator:                       
    def __init__(self, limit):
        self.limit = limit
        self.records = []
    
    def add_record(self, record):
        self.records.append(record)
    
    def get_today_stats(self):
        date_now = dt.datetime.now().date()
        sum_records = 0
        for i in self.records:
            if i.date == date_now:
                sum_records += i.amount
        return sum_records
    
    def get_week_stats(self):
        date_now = dt.datetime.now().date()
        date_week = date_now - dt.timedelta(6)
        sum_records = 0
        for i in self.records: 
            if i.date >= date_week:
                sum_records += i.amount
        return sum_records

class CashCalculator(Calculator):
    EUR_RATE = 80
    USD_RATE = 70
    
    def get_today_cash_remained(self, currency):
        if currency == "rub" and self.records == dt.datetime.now().date():
            remainder = self.limit - super().get_week_stats()
            if remainder < self.limit:
                return f"На сегодня осталось {remainder} руб"
            elif remainder == self.limit:
                return ("Денег нет, держись")
            elif remainder > self.limit:
                return f"Денег нет, держись: твой долг - {remainder} руб"
        
        elif currency == "eur" and self.records == dt.datetime.now().date():
            remainder = (self.limit - super().get_week_stats())/self.EUR_RATE
            if remainder < self.limit:
                return f"На сегодня осталось {remainder} Euro"
            elif remainder == self.limit:
                return ("Денег нет, держись")
            elif remainder > self.limit:
                return f"Денег нет, держись: твой долг - {remainder} Euro"
        
        elif currency == "usd" and self.records == dt.datetime.now().date():
            remainder = (self.limit - super().get_week_stats())/self.USD_RATE
            if remainder < self.limit:
                return f"На сегодня осталось {remainder} USD"
            elif remainder == self.limit:
                return ("Денег нет, держись")
            elif remainder > self.limit:
                return f"Денег нет, держись: твой долг - {remainder} USD"
           
class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        remainder = self.limit - super().get_week_stats()
        if remainder < self.limit:
            return (f"Сегодня можно съесть что-нибудь еще,"
            f"но с общей калорийностью не более {remainder} кКал")
        if remainder >= self.limit:
            return ("Хватит есть!")
        

    
