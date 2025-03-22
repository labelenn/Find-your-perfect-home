def process_schools(file_name: str) -> dict:
    raise NotImplementedError

def process_medicals(file_name: str) -> dict:
    raise NotImplementedError

def process_sport(file_name: str) -> dict:
    raise NotImplementedError

def main():
    school_dict = process_schools('sample_melbourne_schools.csv')
    medical_dict = process_medicals('sample_melbourne_medical.csv')
    sport_dict = process_sport('sample_sport_facilities.csv')

    sample_medical_code = 'mgp0041'
    print(f"There are {len(school_dict)} schools and {len(sport_dict)} sport facilities in our dataset")
    print(f"The location for {medical_dict[sample_medical_code]['gp_name']} is {medical_dict[sample_medical_code]['gp_lat']}, {medical_dict[sample_medical_code]['gp_lon']}")

if __name__ == '__main__':
    main()

