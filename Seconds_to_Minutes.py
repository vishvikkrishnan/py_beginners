def SectoMin(Seconds):
    Min = Seconds // 60
    Remaining_sec = Seconds % 60
    return "Minutes: {}, Seconds: {}".format(Min, Remaining_sec)
