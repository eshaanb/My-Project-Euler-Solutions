def doWork():
    firstDate = Date(1, 19010101)
    sundayCount = 0
    while int(firstDate.date) <= 20001231:
        if firstDate.day == 6 and firstDate.date[6:8] == '01':
            sundayCount += 1
        if firstDate.day == 6:
            firstDate.day = 0
        else:
            firstDate.day += 1
        strDate = str(firstDate.date)
        year = int(strDate[0:4])
        month = int(strDate[4:6])
        day = int(strDate[6:8])

        if day > 27:
            reset = False
            if month == 2:
                # check for leap year
                if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) and day == 29:
                    reset = True
                    day = 1
                    month += 1
                elif day == 28:
                    reset = True
                    day = 1
                    month += 1
            elif month == 4 or month == 6 or month == 9 or month == 11:
                if day == 30:
                    reset = True
                    day = 1
                    month += 1
            elif day == 31:
                    if month != 12:
                        reset = True
                        day = 1
                        month += 1
                    else:
                        reset = True
                        year += 1
                        day = 1
                        month = 1
            if not reset:
                firstDate.date = str(int(firstDate.date)+1)
            else:
                firstDate.date = formatToString(day, month, year)
            #print('day: '+str(firstDate.day)+'date: '+firstDate.date)
        else:
            firstDate.date = str(int(firstDate.date)+1)
    print(str(sundayCount))

def formatToString(day, month, year):
	strDay = str(day)
	strMonth = str(month)
	if len(strDay) == 1:
		strDay = '0'+strDay
	if len(strMonth) == 1:
		strMonth = '0'+strMonth
	return str(year)+strMonth+strDay