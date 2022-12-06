import datetime




def vaqt_uzgartirish(vaqt):
    vaqt = vaqt.split("+")[0]
    vaqt = datetime.datetime.strptime(vaqt, "%y/%m/%d,%H:%M:%S")
    vaqt = vaqt + datetime.timedelta(hours=5)
    return vaqt.strftime("%y/%m/%d,%H:%M:%S")

