def inputIntPredicate(alert, errAlert, predicate):
    while True:
      value = inputInt(alert, errAlert)
      if not predicate(value):
          print(errAlert)
      else: return value

def inputPInt(alert, errAlert):
    while True:
        try:
            num = int(input(alert))
            if num <= 0:
                raise ValueError('err')
            return num
        except ValueError:
            print(errAlert)
 
def inputInt(alert, errAlert):
    while True:
        try:
            return int(input(alert))
        except ValueError:
            print(errAlert)

def inputRange(alertFrom, alertTo, errAlert, valueFromMoreTo):
    valueFrom = inputInt(
        alertFrom,
        errAlert
    )
    valueTo = inputInt(
        alertTo,
        errAlert
    )
    while valueFrom > valueTo:
        print(valueFromMoreTo)
        valueFrom = inputInt(
            alertFrom,
            errAlert
        )
        valueTo = inputInt(
            alertTo,
            errAlert
        )
    return (valueFrom, valueTo)