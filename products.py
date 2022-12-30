import os

#讀取檔案
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        products = []
        for line in f:
            if '商品,價格' in line:#跳過'商品,價格'
                continue
            name, price = line.strip().split(',')
            #分割後分別存入name 和 price 
            #strip
            #split遇到括號裡的內容做一次切割
            products.append([name, price])
        return products


#讓使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱: ')
        if name == 'q':
            break
        price = input('請輸入商品價格: ')
        price = price
        #p = []
        #p.append(name)
        #p.append(price)
        #p = [name, price]
        products.append([name, price])
    print(products)
    return products

#印出所有購買紀錄
def print_products(products):
    for p in products:
        print(p[0], '的價格為', p[1])

#寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')


def main():
    #檢查檔案在不在
    filename = 'producets.csv'
    if os.path.isfile(filename): 
        print('找到檔案')
        products = read_file(filename)
    else:
        print('找不到檔案')
        products = []

    products = user_input(products)
    print_products(products)
    write_file('producets.csv', products)

main()