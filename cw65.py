import random
import datetime

start_date=datetime.date(2014,3,26)
end_date=datetime.date(2026,5,16)

diff=(end_date - start_date).days
print(diff)

random_day=random.randint(0,diff)
random_date= start_date + datetime.timedelta(days=random_day)
print(random_date)
