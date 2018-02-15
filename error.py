def error(argv):
    if len(argv) is 2:
        if argv[0].isnumeric() is False:
            return 84
        try:
            if float(argv[1]) < 1 or float(argv[1]) >= 4:
                return 84
        except:
            return 84
        return 0
    elif len(argv) is 3:
        for i in argv:
            if i.isnumeric() is False:
                return 84
        if int(argv[1]) > int(argv[2]):
            return 84
        return 0
    else:
        return 84
