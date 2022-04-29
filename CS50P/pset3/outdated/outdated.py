import re


def main():
    while True:
        try:
            outdated_date = input("Date: ")
            if outdated_date_matches := re.search("^(\d+)/(\d+)/(\d+)$", outdated_date):
                month, day, year = outdated_date_matches.groups()
            elif outdated_date_matches := re.search("^(\w+) (\d+)[,]? (\d+)$", outdated_date):
                month_word, day, year = outdated_date_matches.groups()
                month = months[month_word]
            else:
                pass
            day = int(day)
            month = int(month)
            year = int(year)
            if day <= 31 and month <= 12:
                print(f"{year}-{month:02}-{day:02}")
                break
        except:
            pass


months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

if __name__ == "__main__":
    main()