import csv
c = 0
file = open("products_new.csv", "w")
ans = 0
product_new = csv.writer(file)
product_new.writerow(['Category','product','Date','Price per unit','Count','total']) # записываем заголовок таблицы
with open("products.csv", "r") as f: #открытие файлика
    for i in csv.reader(f):
        if c > 0: #вытаскиваем переменные из строк таблицы
            line = "".join(i).split(";")
            if line[0] == "Закуски":
                ans += int(float(line[3]))*int(float(line[4]))
            product_new.writerow([line[0], line[1], line[2], line[3], line[4], int(float(line[3]))*int(float(line[4]))])
        c += 1
print(ans)