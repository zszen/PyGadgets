
# n = 730
n=1105
print(int(n/60), n%60)

sectionTime_m = int(n / 60)
sectionTime_s = "0" + n % 60 if n % 60 < 10 else n % 60
print(sectionTime_m, sectionTime_s)