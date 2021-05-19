from . import jalali
from django.utils import timezone


def jalali_converter(time):
 
    # jmonth = {
    # 'far','ord','khor','tir','mor','shah','mehr','aban','azar','dey','bahman','esfand'}
    time = timezone.localtime(time)
    time_to_str = "{}-{}-{}".format(time.year,time.month, time.day)
    # time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()
    # time_to_list = list(time_to_tuple)
    # for index , month in enumerate(jmonth):
        # if time_to_list[1]== index+1:
            # time_to_list[1]= month
            # break

    # o
    # utput = "{} {} {},saat{}:{}".format(
     
        # time_to_list[2],
     
        # time_to_list[1],
     
        # time_to_list[0],
     
        # time.hour,
     
        # time.minute
    # )
    output = "{} ساعت {}:{}  ".format(jalali.Gregorian(time_to_str).persian(),time.hour, time.minute)
    return (output)