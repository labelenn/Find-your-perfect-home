with open("sample_properties.csv", 'r') as prop_file:
        prop_file = prop_file.readlines()
        print(prop_file)
        if len(prop_file) == 1 and set(prop_file[0].strip().split(",")) == set(["prop_id","full_address"]):
            print("Header is correct")
        elif len(prop_file) == 0:
            print("File is empty")