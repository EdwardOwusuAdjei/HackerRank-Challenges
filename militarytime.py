
import os

#
# Complete the timeConversion function below.
#


def timeConversion(s):
    am_or_pm = s[-2:].upper()
    if am_or_pm == "AM":
        hour = int(s[:2])
        if hour == 12:
            twelve_time = f"00{s[2:-2]}"
            return twelve_time
        new_time = f"{s[:-2]}"
        return new_time

    if am_or_pm == "PM":
        hour = int(s[:2])
        if hour == 12:
            twelve_time = f"12{s[2:-2]}"
            return twelve_time
        new_time = f"{str(hour + 12)}{s[2:-2]}"
        return new_time



if __name__ == '__main__':
    #f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    print(result)
    #f.write(result + '\n')

    #f.close()