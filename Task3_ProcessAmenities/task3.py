import csv
import json

def process_schools(file_name: str) -> dict:
    """
    Reads the schools" information from the given file name.

    Arguments:
        file_name (str): the name of the file containing the schools' information

    Returns:
        dict: a dictionary containing the schools' information. The dictionary will have the school_no as the key, and the value is a dictionary containing the school's information.
    """

    schools = {}

    with open(file_name, mode="r", newline="", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        next(reader) # Skip the header
        
        for row in reader:
            school = {}

            # If latitutude and longitude are not provided, skip the row
            if row[-1] == "" or row[-2] == "" or row[-1] == "NA" or row[-2] == "NA":
                continue

            # Extract the information from the row and store it in a dictionary
            school["school_no"] = row[0]
            school["school_name"] = row[1]
            school["school_type"] = row[2]
            school["school_lat"] = float(row[-1])
            school["school_lon"] = float(row[-2])

            # Add the school information to the schools dictionary
            schools[school["school_no"]] = school

    return schools

def process_medicals(file_name: str) -> dict:
    """
    Reads the all the GP"s information from the given file and returns a dictionary.

    Arguments:
        file_name (str): the name of the file containing the GP's information

    Returns:
        dict: a dictionary containing the GP's information. The dictionary will have the gp_code as the key, and the value is a dictionary containing the GP's information.
    """

    medicals = {}

    with open(file_name, mode="r", newline="", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        next(reader) # Skip the header

        for row in reader:
            medical = {}

            # If latitutude and longitude are not provided, skip the row
            if row[-1] == "" or row[-1] == "NA":
                continue

            location = json.loads(row[-1])
            if location["lat"] == "" or location["lng"] == "" or location["lat"] == "NA" or location["lng"] == "NA":
                continue

            # Extract the information from the row and store it in a dictionary
            medical["gp_code"] = row[0]
            medical["gp_name"] = row[1]

            # Extract the latitude and longitude from the JSON string provided in the last column
            medical["gp_lat"] = location["lat"]
            medical["gp_lon"] = location["lng"]

            # Add the GP information to the medicals dictionary
            medicals[medical["gp_code"]] = medical

    return medicals

def process_sport(file_name: str) -> dict:
    """
    Reads the sport facilities" information from the given file and returns a dictionary.

    Arguments:
        file_name (str): the name of the file containing the sport facilities' information

    Returns:
        dict: a dictionary containing the sport facilities' information. The dictionary will have the facility_id as the key, and the value is a dictionary containing the sport facility's information.
    """

    sports = {}

    with open(file_name, mode="r", newline="", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        next(reader) # Skip the header

        for row in reader:
            sport = {}

            # If latitude and longitude are not provided, skip the row
            if row[3] == "" or row[4] == "" or row[3] == "NA" or row[4] == "NA":
                continue

            # Extract the information from the row and store it in a dictionary
            sport["facility_id"] = row[0]
            sport["facility_name"] = row[2]
            sport["sport_lat"] = float(row[3])
            sport["sport_lon"] = float(row[4])
            sport["sport_played"] = row[5]

            # Add the sport information to the sports dictionary
            sports[sport["facility_id"]] = sport

    return sports

def main():
    school_dict = process_schools("sample_melbourne_schools.csv")
    medical_dict = process_medicals("sample_melbourne_medical.csv")
    sport_dict = process_sport("sample_sport_facilities.csv")

    sample_medical_code = "mgp0041"
    print(f"There are {len(school_dict)} schools and {len(sport_dict)} sport facilities in our dataset")
    print(f"The location for {medical_dict[sample_medical_code]["gp_name"]} is {medical_dict[sample_medical_code]["gp_lat"]}, {medical_dict[sample_medical_code]["gp_lon"]}")

if __name__ == "__main__":
    main()

