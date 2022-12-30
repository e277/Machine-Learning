from time import sleep


def import_file(filename):
    with open(filename) as f:
        return f.read()


# check if date is between two dates
def is_between(date, start_date, end_date):
    if date >= start_date and date <= end_date:
        return True
    else:
        return False


# get the date from the file
def get_date(contents):
    date = contents.split(" ")[0]
    return date


# count the distinct for FLOW and the distinct count for Digicel in data.csv
def count_distinct(contents):
    flow_count = 0
    digicel_count = 0
    cw_pstn_count = 0
    miphone_count = 0

    for line in contents.split("\n"):
        if "FLOW Jamaica" in line:
            flow_count += 1
        elif "Digicel Jamaica" in line:
            digicel_count += 1
        elif "C&W PSTN Jamaica" in line:
            cw_pstn_count += 1
        elif "Miphone Cellular Jamaica" in line:
            miphone_count += 1

    return flow_count, digicel_count, cw_pstn_count, miphone_count


# filter the data.csv file for the string 'COVID-19 Vaccination appointment booking'
def filter_data(contents):
    with open("moh_data.csv", "w") as moh_data, open("no_moh_data.csv", "w") as no_moh_data:
        for line in contents.split("\n"):
            if "COVID-19 Vaccination appointment booking" in line or "dose" in line:
                moh_data.write(line + "\n")
            else:
                no_moh_data.write(line + "\n")


def main():
    filename = input("Enter the filename: ")
    contents = import_file(filename)
    # print(contents)
    date_input = input("Enter a date (YYYY-MM-DD): ")
    
    # check if user date_input is present in data.csv, check if date_input is bewteen '2022-01-01' and '2022-03-24'
    if is_between(date_input, "2022-01-01", "2022-03-24"):
        print("Date is between 2022-01-01 and 2022-03-24")
    
    # count the distinct FLOW and Digicel in data.csv
    flow_count, digicel_count, cw_pstn_count, miphone_count = count_distinct(contents)
    print("FLOW count: ", flow_count)
    print("Digicel count: ", digicel_count)
    print("C&W PSTN count: ", cw_pstn_count)
    print("Miphone Cellular count: ", miphone_count)

    # search for a specific string in data.csv
    filter_data(contents)

    print("Writing to dump_data.csv and no_dump_data.csv")
    sleep(2)
    print("Done")


if __name__ == "__main__":
    main()