from . import jalali
from django.utils import timezone


def jalali_converter(time):
    time = timezone.localtime(time)
    time_to_str = "{}-{}-{}".format(time.year,time.month, time.day)
    output = "{} ساعت {}:{}  ".format(jalali.Gregorian(time_to_str).persian(),time.hour, time.minute)
    return (output)

def jalalis(time):
    time = timezone.localtime(time)
    time_to_str = "{}-{}-{}".format(time.year,time.month, time.day)
    output = "{}".format(jalali.Gregorian(time_to_str).persian())
    return (output)
# 1400/01/01
def jalalif(time):
    time= timezone.localtime(time)
    time_to_str = "{}-{}-{}".format(time.year, time.month, time.day)
    output = jalali.Gregorian(time_to_str).persian_string
    return output