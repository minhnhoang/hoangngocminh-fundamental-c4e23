def remove_dollar_sign(s):
    original = s
    removed = original.replace("$","")
    return removed

print(remove_dollar_sign("Ain't no $money for you"))