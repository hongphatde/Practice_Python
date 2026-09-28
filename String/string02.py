# Exercise 1:
def smart_log_formatter(logs):
    if not logs:
        return []
    
    result = []
    current = logs[0]
    count = 1
    
    for index in logs[1:]:
        if index == current:
            count += 1
        else:
            if count > 1:
               result.append(f"{current} (x{count})")
            else:
                result.append(current)
            current = index
            count = 1
    
    if count > 1:
        result.append(f"{current} (x{count})")
    else:
        result.append(current)
    
    return result

print(smart_log_formatter(
                [
                    "INFO Connected",
                    "WARNING Low battery",
                    "INFO Connected"
                ]
            ))

print(smart_log_formatter(
                [
                    "INFO Start",
                    "INFO Start"
                ]
            ))