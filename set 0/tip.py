def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    d_sign = d.replace("$", "")
    return float(d_sign)



def percent_to_float(p):
    p_sign = p.replace("%", "")
    p_con = float(p_sign) / 100
    return p_con



main()