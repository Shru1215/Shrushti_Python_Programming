# differnce btw two datetime (time) values

from datetime import datetime
start = datetime(2026,7,6,9,0,0)
end = datetime(2026,7,6,17,30,0)
dif = end - start

print(dif)
print(dif.seconds)

