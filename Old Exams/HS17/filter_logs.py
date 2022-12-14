def filter_logs(text):
    error_list = get_logs()
    lines = []
    for i in error_list:
        if text.upper() in i.upper():
            lines.append(i)

    return lines
