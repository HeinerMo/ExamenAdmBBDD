def isValidDate(date:str):
    year = date[0:4]
    firstHyphen = date[4:5]
    month = date[5:7]
    secondHyphen = date[7:8]
    day = date[8:10]

    isYear = False
    isFHyphen = False
    isMonth = False
    isSHyphen = False
    isDay = False
    if (year.isdigit() and int(year) >= 1970):
        isYear = True
    if (firstHyphen == "-"):
        isFHyphen = True
    if (month.isdigit() and int(month) >= 1 and int(month) <= 12):
        isMonth = True
    if (secondHyphen == "-"):
        isSHyphen = True
    if (day.isdigit() and int(day) >= 1 and int(day) <= 31):
        isDay = True

    if (isYear and isFHyphen and isMonth and isSHyphen and isDay):
        return True
    
    return False