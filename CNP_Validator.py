import calendar


def sex_validator(s: int) -> bool:
    return 0 < s < 10


def month_of_birth(ll: int) -> bool:
    return 0 < ll < 13


def day_of_birth(zz: int, s: int, aa: int, ll: int) -> bool:
    if 1 <= s <= 2:
        year = 19
    elif 3 <= s <= 4:
        year = 18
    else:
        year = 20

    year = year * 100 + aa

    valid_days = {1: 31,
                  2: 28,
                  3: 31,
                  4: 30,
                  5: 31,
                  6: 30,
                  7: 31,
                  8: 31,
                  9: 30,
                  10: 31,
                  11: 30,
                  12: 31}
    if calendar.isleap(year) and ll == 2:
        return 0 < zz < 29
    else:
        return 0 < zz < valid_days.get(ll)


def country_code(jj: int) -> bool:
    return 0 < jj < 47 or 50 < jj < 53


def control_digit(cnp: str) -> bool:
    cnp_const = "279146358279"
    sum = 0

    for i in range(0, len(cnp_const)):
        sum += int(cnp[i]) * int(cnp_const[i])
    
    div = sum % 11
    
    return (div == 10 and cnp[12] == '1') or (div == int(cnp[12]))


if __name__ == '__main__':

    cnp = input("Insert CNP for validation:").strip()
    if cnp.isdigit() is False:
        print("Invalid input. Please try again")
    else:

        if sex_validator(int(cnp[0])) is False:
            print("Sex of CNP is not valid")
        elif month_of_birth(int(cnp[3:5])) is False:
            print("Month of CNP is not valid")
        elif country_code(int(cnp[7:9])) is False:
            print("Contry code of CNP is not valid")
        elif day_of_birth(int(cnp[5:7]), int(cnp[0]), int(cnp[1:3]), int(cnp[3:5])) is False:
            print("Day of birth is not valid")
        elif control_digit(cnp) is False:
            print("Control digit of CNP is not valid")
        else:
            print("Valid CNP")
