import csv

def process_schools(file_name: str) -> dict:
    '''
    Reads the schools' information from the given file and returns a dictionary.
    The dictionary will have the school_no as the key, and the value is a dictionary containing five keys:
    - school_no <str>: the school's number
    - school_name <str>: the school's name
    - school_type <str>: the school's type
    - school_lat <float>: the school's latitude
    - school_lon <float>: the school's longitude
    '''

def process_medicals(file_name: str) -> dict:
    '''
    Reads the all the GP's information from the given file and returns a dictionary.
    The dictionary will have the gp_code as the key, and the value is a dictionary containing four keys:
    - gp_code <str>: the GP's code
    - gp_name <str>: the GP's name
    - gp_lat <float>: the GP's latitude
    - gp_lon <float>: the GP's longitude
    '''

def process_sport(file_name: str) -> dict:
    '''
    Reads the sport facilities' information from the given file and returns a dictionary.
    The dictionary will have the facility_id as the key, and the value is a dictionary containing five keys:
    - facility_id <str>: the facility's ID
    - facility_name <str>: the facility's name
    - sport_lat <float>: the facility's latitude
    - sport_lon <float>: the facility's longitude
    - sport_played <str>: the sport played at the facility
    '''

def main():
    school_dict = process_schools('sample_melbourne_schools.csv')
    medical_dict = process_medicals('sample_melbourne_medical.csv')
    sport_dict = process_sport('sample_sport_facilities.csv')

    sample_medical_code = 'mgp0041'
    print(f"There are {len(school_dict)} schools and {len(sport_dict)} sport facilities in our dataset")
    print(f"The location for {medical_dict[sample_medical_code]['gp_name']} is {medical_dict[sample_medical_code]['gp_lat']}, {medical_dict[sample_medical_code]['gp_lon']}")

if __name__ == '__main__':
    main()

