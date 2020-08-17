import datetime as dt

class Record:
    def __init__(self, amount, comment, date = None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y')
        
        

class Calculator:                       
    def __init__(self, limit):
        self.limit = limit
        self.records = []
    
    def add_record(self, record):
        self.records.append(record)
        return self.records
    
    def get_today_stats(self):
        date_now = dt.datetime.now().date()
        sum_records = 0
        for record in self.records:
            if record.date == date_now:
                sum_records += record.amount
        return sum_records
    
    def get_week_stats(self):
        date_now = dt.datetime.now().date()
        date_week = date_now - dt.timedelta(6)
        sum_records = 0
        for record in self.records: 
            if record.date >= date_week:
                sum_records += record.amount
        return sum_records

class CashCalculator(Calculator):
    EURO_RATE = 80
    USD_RATE = 70
    
    def get_today_cash_remained(self, currency):
        if currency == "rub":
            remainder = round((self.limit - super().get_today_stats()), 2)
            if remainder < self.limit:
                return f"На сегодня осталось {remainder} руб"
            elif remainder == self.limit:
                return ("Денег нет, держись")
            elif remainder > self.limit:
                return f"Денег нет, держись: твой долг - {remainder} руб"
        
        elif currency == "eur":
            remainder = round((self.limit - super().get_today_stats()/self.EURO_RATE), 2)
            if remainder < self.limit:
                return f"На сегодня осталось {remainder} Euro"
            elif remainder == self.limit:
                return ("Денег нет, держись")
            elif remainder > self.limit:
                return f"Денег нет, держись: твой долг - {remainder} Euro"
        
        elif currency == "usd":
            remainder = round(((self.limit - super().get_today_stats())/self.USD_RATE), 2)
            if remainder < self.limit:
                return f"На сегодня осталось {remainder} USD"
            elif remainder == self.limit:
                return ("Денег нет, держись")
            elif remainder > self.limit:
                return f"Денег нет, держись: твой долг - {remainder} USD"
           
class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        sum_today = super().get_today_stats()
        remainder = self.limit - sum_today
        if remainder < self.limit:
            return (f"Сегодня можно съесть что-нибудь еще,"
            f"но с общей калорийностью не более {remainder} кКал")
        if remainder >= self.limit:
            return ("Хватит есть!")
        

    
