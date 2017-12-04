#해당 월까지 누적 날짜
Dic_365 = {0 : 0, 1 : 31, 2 : 59, 3 : 90, 4 : 120, 5 : 151, 6 : 181, 7 : 212, 8 : 243, 9 : 273, 10 : 304, 11 : 334, 12 : 365}
#만약 2월이 29일인 해인 경우,
Dic_366 = {0 : 0, 1 : 31, 2 : 60, 3 : 91, 4 : 121, 5 : 152, 6 : 182, 7 : 213, 8 : 244, 9 : 274, 10 : 305, 11 : 335, 12 : 366}

## 한자리수가 input으로 들어오면 앞에 0을 붙여서 두자리로 만든다. return은 string형식으로 만든다.
def i2s(intval):
    if intval < 10:
        strval = '0'+str(intval)
    else:
        strval = str(intval)
    return strval

def date_calculate(date, days, operation = 0): #operation은 연산종류, 지금은 +밖에 안쓰니 항상 +라고 간주한다.
    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:8]) # 2015 03 13
    
    #윤년 -> 2016년만
    if year % 4 == 0:
        before_sum_day = Dic_366[month-1]
        sum_day = Dic_366[month]
        all_sum = before_sum_day + day + days - 1
        if all_sum > 366:
            after_date = str(year+1)+i2s(month-11)+i2s(all_sum-366)
        else:
            if all_sum <= sum_day:
                after_date = str(year)+i2s(month)+i2s(day+days-1)
            elif all_sum > sum_day:
                month_change = 0
                run_bool = True
                while run_bool:
                    if (all_sum > Dic_366[month+month_change]) and (all_sum <= Dic_366[month+month_change+1]) :
                        after_date = str(year)+i2s(month+month_change+1)+i2s(all_sum- Dic_366[month+month_change])
                        run_bool = False
                    else:
                        month_change +=1
                
    #2014, 2015년      
    
    else:
        before_sum_day = Dic_365[month-1]
        sum_day = Dic_365[month]
        all_sum = before_sum_day + day + days - 1 # 올해 며칠까지 지났나 + 지금 요일 + 더하려는 요일 수 -1
        if all_sum <= sum_day:
            after_date = str(year)+i2s(month)+i2s(day+days-1)

        elif all_sum > sum_day: 
            month_change = 0
            run_bool = True
            while run_bool:
                if (all_sum > Dic_365[month+month_change]) and (all_sum <= Dic_365[month+month_change+1]) :
                    after_date = str(year)+i2s(month+month_change+1)+i2s(all_sum- Dic_365[month+month_change])
                    run_bool = False
                else:
                    month_change +=1
                    
    return after_date
        