import sys

def convert_hours_to_seconds(hours):
    return hours * 3600

if __name__ == "__main__":
    hours = float(sys.argv[1])
    seconds = convert_hours_to_seconds(hours)
    print(f"{hours} hours is equal to {seconds} seconds.")
