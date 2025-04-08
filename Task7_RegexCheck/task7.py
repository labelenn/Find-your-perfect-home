import re


class RegexHandler:
    """
    A class to handle regex operations for validating email and phone numbers.
    
    Class Attributes:
        valid_email_regex (str): Regex pattern for validating email addresses.
        valid_phone_regex (str): Regex pattern for validating phone numbers.
    """
    valid_email_regex = r"^[a-zA-Z_.+-]+@([a-zA-Z-]+\.)+[a-zA-Z]+$"
    valid_phone_regex = r"^\(61\)0\d{9}$|^610\d{9}$"

    def __init__(self) -> None:
        """
        Initializes the RegexHandler class.
        """
        pass

    def validate_email(self, str2check: str) -> bool:
        """
        Validates an email address using regex.

        Arguments:
            str2check (str): The email address to validate.

        Returns:
            bool: True if the email address is valid, False otherwise.
        """
        if re.match(self.valid_email_regex, str2check):
            return True
        else:
            return False
    
    def validate_phone(self, str2check: str) -> bool:
        """
        Validates a phone number using regex.

        Arguments:
            str2check (str): The phone number to validate.

        Returns:
            bool: True if the phone number is valid, False otherwise.
        """
        if re.match(self.valid_phone_regex, str2check):
            return True
        else:
            return False

def prop_email_matcher(prop_fpath: str, email_fpath: str) -> str:
    """
    Matches property records with email addresses.

    Arguments:
        prop_fpath (str): Path to the properties CSV file.
        email_fpath (str): Path to the email addresses CSV file.

    Returns:
        str: A CSV-like string containing the property ID, full address, and matching email address (if there's any).
    """
    header = "prop_id,full_address,email"
    data = [header]
    regex_handler = RegexHandler()

    # If property file is empty, (no contents) but has header line, return the header
    with open(prop_fpath, 'r') as prop_file:
        prop_file = prop_file.readlines()
        if len(prop_file) == 1 and set(prop_file[0].strip().split(",")) == set(["prop_id","full_address"]):
            return header
        elif len(prop_file) == 0:
            return ""

    # Get the index of the columns in the files
    prop_id_index_1 = 0
    prop_id_index_2 = 0
    full_address_index = 1
    email_index = 1
    with open(prop_fpath, 'r') as prop_file:
        prop_file = prop_file.readlines()[0]
        prop_id_index_1 = prop_file.strip().split(",").index("prop_id")
        full_address_index = prop_file.strip().split(",").index("full_address")
    with open(email_fpath, 'r') as email_file:
        email_file = email_file.readlines()[0]
        prop_id_index_2 = email_file.strip().split(",").index("prop_id")
        email_index = email_file.strip().split(",").index("email")

    # Read the property file and get the property IDs
    prop_ids = []
    with open(prop_fpath, 'r') as prop_file:
        prop_file = prop_file.readlines()[1:]
        for line in prop_file:
            prop_ids.append(line.strip().split(",")[prop_id_index_1])

    # Read the email file and keep the valid emails and their corresponding property IDs if the property ID is in the property file
    valid_emails = {}
    with open(email_fpath, 'r') as email_file:
        email_file = email_file.readlines()[1:]
        for line in email_file:
            prop_id = line.strip().split(",")[prop_id_index_2]
            email = line.strip().split(",")[email_index]
            if regex_handler.validate_email(email) and prop_id in prop_ids:
                valid_emails[prop_id] = email

    # Read the property file and match with valid emails.
    with open(prop_fpath, 'r') as prop_file:
        prop_file = prop_file.readlines()[1:]
        for line in prop_file:
            prop_id = line.strip().split(",")[prop_id_index_1]
            full_address = line.strip().split(",")[full_address_index]
            if prop_id in valid_emails:
                data.append(f"{prop_id},{full_address},{valid_emails[prop_id]}")
            else:
                data.append(f"{prop_id},{full_address},")

    return "\n".join(data)

def prop_phone_matcher(prop_fpath: str, phone_fpath: str) -> str:
    """
    Matches property records with phone numbers.

    Arguments:
        prop_fpath (str): Path to the properties CSV file.
        phone_fpath (str): Path to the phone numbers CSV file.

    Returns:
        str: A CSV-like string containing the property ID, full address, and matching phone number (if there's any).
    """
    header = "prop_id,full_address,phone"
    data = [header]
    regex_handler = RegexHandler()

    # If property file is empty, (no contents) but has header line, return the header
    with open(prop_fpath, 'r') as prop_file:
        prop_file = prop_file.readlines()
        if len(prop_file) == 1 and set(prop_file[0].strip().split(",")) == set(["prop_id","full_address"]):
            return header
        elif len(prop_file) == 0:
            return ""

    # Get the index of the columns in the files
    prop_id_index_1 = 0
    prop_id_index_2 = 0
    full_address_index = 1
    phone_index = 2
    with open(prop_fpath, 'r') as prop_file:
        prop_file = prop_file.readlines()[0]
        prop_id_index_1 = prop_file.strip().split(",").index("prop_id")
        full_address_index = prop_file.strip().split(",").index("full_address")
    with open(phone_fpath, 'r') as phone_file:
        phone_file = phone_file.readlines()[0]
        prop_id_index_2 = phone_file.strip().split(",").index("prop_id")
        phone_index = phone_file.strip().split(",").index("phone")

    # Read the phone file and keep the valid phones and their corresponding property IDs
    valid_phones = {}
    with open(phone_fpath, 'r') as phone_file:
        phone_file = phone_file.readlines()[1:]
        for line in phone_file:
            prop_id = line.strip().split(",")[prop_id_index_2]
            phone = line.strip().split(",")[phone_index]
            if regex_handler.validate_phone(phone):
                valid_phones[prop_id] = phone

    # Read the property file and match with valid phones
    with open(prop_fpath, 'r') as prop_file:
        prop_file = prop_file.readlines()[1:]
        for line in prop_file:
            prop_id = line.strip().split(",")[prop_id_index_1]
            full_address = line.strip().split(",")[full_address_index]
            if prop_id in valid_phones:
                data.append(f"{prop_id},{full_address},{valid_phones[prop_id]}")

    return "\n".join(data)


def merge_prop_email_phone(prop_fpath: str, email_phone_fpath: str) -> str:
    """
    Merges property records with email and phone numbers.

    Arguments:
        prop_fpath (str): Path to the properties CSV file.
        email_phone_fpath (str): Path to the email and phone numbers CSV file.

    Returns:
        str: A CSV-like string containing the property ID, full address, email, and phone number.
    """

    header = "prop_id,full_address,email,phone"
    data = [header]
    regex_handler = RegexHandler()

    # If property file is empty, (no contents) but has header line, return the header
    with open(prop_fpath, 'r') as prop_file:
        prop_file = prop_file.readlines()
        if len(prop_file) == 1 and set(prop_file[0].strip().split(",")) == set(["prop_id","full_address"]):
            return header
        elif len(prop_file) == 0:
            return ""

    # Get the index of the columns in the files
    prop_id_index_1 = 0
    prop_id_index_2 = 0
    full_address_index = 1
    email_index = 1
    phone_index = 2
    with open(prop_fpath, 'r') as prop_file:
        prop_file = prop_file.readlines()[0]
        prop_id_index_1 = prop_file.strip().split(",").index("prop_id")
        full_address_index = prop_file.strip().split(",").index("full_address")
    with open(email_phone_fpath, 'r') as email_phone_file:
        email_phone_file = email_phone_file.readlines()[0]
        prop_id_index_2 = email_phone_file.strip().split(",").index("prop_id")
        email_index = email_phone_file.strip().split(",").index("email")
        phone_index = email_phone_file.strip().split(",").index("phone")

    # Read the email and phone file and keep the entries where at least one of the contact information is valid
    valid_emails_phones = {}
    with open(email_phone_fpath, 'r') as email_phone_file:
        email_phone_file = email_phone_file.readlines()[1:]
        for line in email_phone_file:
            prop_id = line.strip().split(",")[prop_id_index_2]
            email = line.strip().split(",")[email_index]
            phone = line.strip().split(",")[phone_index]
            if regex_handler.validate_email(email) and regex_handler.validate_phone(phone):
                valid_emails_phones[prop_id] = (email, phone)
            elif regex_handler.validate_email(email) and not regex_handler.validate_phone(phone):
                valid_emails_phones[prop_id] = (email, False)
            elif not regex_handler.validate_email(email) and regex_handler.validate_phone(phone):
                valid_emails_phones[prop_id] = (False, phone)

    # Read the property file and match with the valid emails and phones
    with open(prop_fpath, 'r') as prop_file:
        prop_file = prop_file.readlines()[1:]
        for line in prop_file:
            prop_id = line.strip().split(",")[prop_id_index_1]
            full_address = line.strip().split(",")[full_address_index]
            if prop_id in valid_emails_phones:
                if valid_emails_phones[prop_id][0] and valid_emails_phones[prop_id][1]:
                    data.append(f"{prop_id},{full_address},{valid_emails_phones[prop_id][0]},{valid_emails_phones[prop_id][1]}")
                elif valid_emails_phones[prop_id][0] and not valid_emails_phones[prop_id][1]:
                    data.append(f"{prop_id},{full_address},{valid_emails_phones[prop_id][0]},")
                elif not valid_emails_phones[prop_id][0] and valid_emails_phones[prop_id][1]:
                    data.append(f"{prop_id},{full_address},,{valid_emails_phones[prop_id][1]}")

    if len(data) == 1:
        return header
    return "\n".join(data)
    

if __name__ == "__main__":
    print("Task 1 results: ")
    print(prop_email_matcher("sample_properties.csv", "sample_properties_email_phone.csv"))
    print("="*50)
    print("Task 2 results: ")
    print(prop_phone_matcher("sample_properties.csv", "sample_properties_email_phone.csv"))
    print("="*50)
    print("Task 3 results: ")
    print(merge_prop_email_phone("sample_properties.csv", "sample_properties_email_phone.csv"))

