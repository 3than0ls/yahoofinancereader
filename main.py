import csv
import os
from datetime import datetime

# working with command line is too complicated currently
# start date of data wanted
START_DATE = '2023-05-08'
# number of days after start date to stop data wanted
CUTOFF = 15


def filter_data(start_date, cutoff, datapath=os.path.join(os.path.curdir, "data")):
    data = {}

    for csvfile in os.listdir(datapath):
        if csvfile[-4:] != '.csv':
            print(csvfile, " is not a csv file, skipping.")

        try:
            with open(os.path.join(os.path.curdir, "data", csvfile), 'r') as f:
                csvfile_data = {}

                # purely for the purpose of finding the starting index
                start_index = 0
                reader = list(csv.reader(f, delimiter=','))

                for i, row in enumerate(list(reader)):
                    if row[0] == start_date:
                        start_index = i
                        break
                else:
                    print(
                        f"!! ENCOUNTERED ERROR WHILE READING {csvfile}. DATE OF {start_date} NOT FOUND. SKIPPING FILE !!")

                for i, row in enumerate(reader[start_index:start_index+cutoff]):
                    day_data = {}

                    date = datetime.strptime(row[0], "%Y-%m-%d")
                    weekday = date.strftime('%A')

                    day_data["Weekday"] = weekday
                    day_data["Closing Price"] = round(float(row[4]), 2)
                    try:
                        day_data["After Hours"] = round(
                            float(reader[start_index+i+1][1]), 2)
                    except IndexError:
                        day_data["After Hours"] = "No Data Yet"

                    csvfile_data[str(date.strftime('%m/%d/%Y'))] = day_data

                data[csvfile[:-4]] = csvfile_data

        except Exception as e:
            print(
                f"!! ENCOUNTERED ERROR (SEEN BELOW) WHILE READING {csvfile}, SKIPPING FILE !!")
            print(e)

    return data


def print_data(data, out_dir=os.path.join(os.path.curdir, "output")):
    with open(os.path.join(out_dir, "output.txt"), "w") as file:
        for name, subdata in data.items():
            file.write(f'Ticker: {name}\n')
            for date, day_data in subdata.items():
                print(date, day_data)
                file.write(
                    f"Date: {date}\tWeekday: {day_data['Weekday']}\tClosing Price: {day_data['Closing Price']}\tAfter Hours: {day_data['After Hours']}\n")
            file.write('\n\n')

    with open(os.path.join(out_dir, "output_specialized.txt"), "w") as file:
        for name, subdata in data.items():
            file.write(f'Ticker: {name}')
            file.write('\tDate\tClosing Price\tAfter Hours\n')

            cur_week = 1
            file.write(f"Week {cur_week}")

            for date, day_data in subdata.items():
                file.write(
                    f"\t{date}\t{day_data['Closing Price']}\t{day_data['After Hours']}\n")
                if day_data['Weekday'] == "Friday":
                    cur_week += 1
                    file.write(f"Week {cur_week}")
            file.write('\n\n')


def main():
    data = filter_data(START_DATE, CUTOFF)
    print_data(data)


if __name__ == '__main__':
    main()
