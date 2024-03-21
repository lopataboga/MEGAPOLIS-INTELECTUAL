import csv
c = 0
product_promo = open("product_promo.csv", "w")
ans = csv.writer(product_promo)
ans.writerow(['Category','product','Date','Price per unit','Count', 'promocode']) # записываем заголовок таблицы
with open("products.csv", "r") as f: #открытие файлика
    for i in csv.reader(f):
        if c > 0: #вытаскиваем переменные из строк таблицы
            line = "".join(i).split(";")
            promo = line[1][:2].upper() + line[2].split(".")[0] + line[1][-2].upper() + line[1][-3].upper() + line[2].split(".")[1][::-1]
            ans.writerow([line[0],line[1],line[2], line[3],line[4], promo])
        c += 1