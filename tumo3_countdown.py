import time


def timetable_to_seconds(hrs: int, mins: int, secs: int) -> int:
    """
    Function returns seconds from hours & minutes & seconds
    :param hrs:
    :param mins:
    :param secs:
    :return:
    """
    return secs + 60 * mins + 3600 * hrs


def seconds_to_timetable(secs: int) -> str:
    """
    Function returns string h:m:s which is got from seconds
    :param secs:
    :return:
    """
    return str(f'{secs//3600} : {(secs%3600)//60} : {secs%60}')


def check(hrs: int, mins: int, secs: int) -> bool:
    """
    Checking if input is correct: 0<=hours<=23, 0<=min, sec<=59
    :param hrs:
    :param mins:
    :param secs:
    :return:
    """
    if hrs not in range(0, 24) or mins not in range(0, 60) or secs not in range(0, 60):
        print("Incorrect time format. Try again.")
        return False
    return True


def countdown() -> None:
    """
    Main function here. Takes user formatted input and gives the countdown
    :return:
    """
    correct_time: bool = False
    hours, minutes, seconds = 0, 0, 0

    # repeat unless input is incorrect
    while not correct_time:
        # getting input
        user_input: str = input("Input time for countdown in format 'hours:minutes:seconds', or 'q' to quit : ")

        # if 'q' then quit program
        if user_input == 'q':
            print("Ok, let's quit, bye!")
            return None

        # splitting the input by ':' and checking if the format is correct
        try:
            hours_str, minutes_str, seconds_str = user_input.split(':')
            hours, minutes, seconds = int(hours_str), int(minutes_str), int(seconds_str)
            correct_time = check(hours, minutes, seconds)

        # otherwise repeat input, back to the beginning of cycle
        except Exception:
            print("Incorrect time format. Try again.")
            continue

    # getting the duration is seconds for initial point of countdown
    full_time_sec = timetable_to_seconds(hours, minutes, seconds)

    # countdown
    while full_time_sec >= 0:
        print(seconds_to_timetable(full_time_sec))
        full_time_sec -= 1
        time.sleep(1)

    # ending function, final print
    print("The countdown is finished! Bye! ")


if __name__ == '__main__':
    countdown()
