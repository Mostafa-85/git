import time


def zarb(adad_aval,adad_dovom):
    a=adad_aval
    b=adad_dovom
    if not isinstance(adad_aval, (int, float)) or not isinstance(adad_dovom, (int, float)):
        return 'Error: لطفاً عدد صحیح یا اعشاری وارد کنید!'

    else:
        c = a*b
        return c

z = zarb(55555515, 's')  # ورودی نامعتبر
print(z,{time.time()})

z_valid = zarb(123499999999999999999999999999999999, 22222)  # ورودی معتبر
print(f"نتیجه ضرب: {z_valid},,,,,,,,{time.time()}")

# def taghsim(adad_aval,adad_dovom):
#     a=adad_aval
#     b=adad_dovom
#     if not isinstance(adad_aval, (int, float)) or not isinstance(adad_dovom, (int, float)):
#         return 'Error: لطفاً عدد صحیح یا اعشاری وارد کنید!'
#
#     else:
#         c = a/b
#         return c
#
# print(taghsim(55555515, 2))

#
# def menha(adad_aval,adad_dovom):
#     a=adad_aval
#     b=adad_dovom
#     if not isinstance(adad_aval, (int, float)) or not isinstance(adad_dovom, (int, float)):
#         return 'Error: لطفاً عدد صحیح یا اعشاری وارد کنید!'
#
#     else:
#         c = a-b
#         return c
#
# print(menha(5, 2))


def alave(adad_aval,adad_dovom):
    a=adad_aval
    b=adad_dovom
    if not isinstance(adad_aval, (int, float)) or not isinstance(adad_dovom, (int, float)):
        return 'Error: لطفاً عدد صحیح یا اعشاری وارد کنید!'

    else:
        c = a+b
        return c

print(alave(5, 2))


