try:
        value = int("abc")
except ValueError as err:
        print("bad number:", err)
else:
        print("parsed",value)
finally:
        print("Always runs")