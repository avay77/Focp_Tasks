print("Park Run Timer\n~~~~~~~~~~~~~~")
print("\nLet's go!\n")

total_runners = 0
total_time = 0
fastest_time = float("inf")
slowest_time = 0
fastest_runner = None 

def get_time_string(minutes, seconds):
    time_string = ""
    if minutes >= 0:
        time_string += f"{minutes} minute"
        if minutes > 1:
            time_string += "s"
        if seconds >= 0:
            time_string += ", "
    if seconds >= 0:
        time_string += f"{seconds} second"
        if seconds > 1:
            time_string += "s"
    return time_string

while True:
    try:
        line = input(">")
        if line == 'END':
            break
        else:
            if "::" not in line:
                print("Error in data stream. Ignorning. Carry on.")
                continue
            runner, time= line.split("::")
            if not runner or not time:
                print("Error in data stream. Ignorning. Carry on.")
                continue
            try:
                time=int(time)
                runner=int(runner)
            except ValueError:
                print("Error in data stream. Ignorning. Carry on.")
                continue
    except ValueError:
                print("Error in data stream. Ignorning. Carry on.")
                continue
      
    total_runners += 1
    total_time += time
    if time < fastest_time:
            fastest_time = time
            fastest_runner = runner
    if time > slowest_time:
            slowest_time = time

if total_runners == 0:
    print("No data found. Nothing to do. What a pity.")
else:
    avg_time = total_time / total_runners
    avg_time_minutes = int(avg_time // 60)
    avg_time_seconds = int(avg_time % 60)
    fastest_time_minutes = int(fastest_time // 60)
    fastest_time_seconds = int(fastest_time % 60)
    slowest_time_minutes = int(slowest_time // 60)
    slowest_time_seconds = int(slowest_time % 60)

    print(f"\nTotal Runners: {total_runners}")

    avg_time_string = get_time_string(avg_time_minutes, avg_time_seconds)
    fastest_time_string = get_time_string(fastest_time_minutes, fastest_time_seconds)
    slowest_time_string = get_time_string(slowest_time_minutes, slowest_time_seconds)

    print(f"Average Time: {avg_time_string}")
    print(f"Fastest Time: {fastest_time_string}")
    print(f"Slowest Time: {slowest_time_string}")


    print(f"\nBest Time Here: Runner #{fastest_runner}")