import datetime

def dayofyear():


    year = input("请输入年份：")

    month = input("请输入月份：")

    day = input("请输入天：")

    date1 = datetime.date(year=int(year),month = int(month),day = int(day))
    date2 = datetime.date(year=int(year),month = 1,day = 1)

    # 日期对象可以直接运算  days属性可以转化为int 类型
    return (date1 - date2 ).days +1

print(dayofyear())
