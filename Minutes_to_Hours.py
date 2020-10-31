#Convert Minutes to Hours
def MintoHours(Minutes):
    Hours = Minutes // 60
    Remaining_min = Minutes % 60
    return "Hours: {}, Minutes: {}".format(Hours, Remaining_min)
