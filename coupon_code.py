from datetime import datetime

def coupon_validity(given_code, actual_code, current_date, expiration_date):

    current_date = datetime.strptime(current_date, "%B %d %Y")
    expiration_date = datetime.strptime(expiration_date, "%B %d %Y")

    if given_code != actual_code:
        return False

    if current_date <= expiration_date:
        return True

    return False

given_code, actual_code, current_date, expiration_date = input().split(",")

result = coupon_validity(given_code, actual_code, current_date, expiration_date)
print(result) 