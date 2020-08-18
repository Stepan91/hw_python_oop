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
            if (record.date >= date_week) and (record.date <= date_week):
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
                return f"На сегодня осталось {round(remainder, 2)} {rates[currency]}"
            elif remainder == 0:
                return ("Денег нет, держись")
            elif remainder < 0:
                return f"Денег нет, держись: твой долг - {round(abs(remainder), 2)} {rates[currency]}"
        elif currency == "eur":
            if remainder > 0:
                return f"На сегодня осталось {round(remainder/self.EURO_RATE, 2)} {rates[currency]}"
            elif remainder == 0:
                return ("Денег нет, держись")
            elif remainder < 0:
                return f"Денег нет, держись: твой долг - {round(abs(remainder), 2)} {rates[currency]}"
        elif currency == "usd":
            if remainder > 0:
                return f"На сегодня осталось {round(remainder/self.USD_RATE, 2)} {rates[currency]}"
            elif remainder == 0:
                return ("Денег нет, держись")
            elif remainder < 0:
                return f"Денег нет, держись: твой долг - {round(abs(remainder), 2)} {rates[currency]}"
           
class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        remainder = self.get_today_stats()
        diff = self.limit - remainder
        if remainder < self.limit:
            return (f"Сегодня можно съесть что-нибудь еще,"
            f"но с общей калорийностью не более {diff} кКал")
        if remainder >= self.limit:
            return ("Хватит есть!")


cash_calculator = CashCalculator(100)
        
# дата в параметрах не указана, 
# так что по умолчанию к записи должна автоматически добавиться сегодняшняя дата
cash_calculator.add_record(Record(amount=145, comment="кофе")) 
# и к этой записи тоже дата должна добавиться автоматически
cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
# а тут пользователь указал дату, сохраняем её
cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))
                
print(cash_calculator.get_today_cash_remained("rub"))
