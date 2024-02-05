import pandas as pd
from lxml import etree
import os

# Extracts data from downloaded NSF files
def extract_data_from_file(file_path):
    tree = etree.parse(file_path)
    root = tree.getroot()

    extracted_data = {
        "first_name": "",
        "middle_name": "",
        "last_name": "",
        "email": "",
        "institution": "",
        "directorate": "",
        "division": "",
        "effective_date": "",
        "expiration_date": "",
        "award_amount": "",
        "award_title": "",
        "abstract": ""
    }

    award = root.find('Award')

    extracted_data["institution"] = award.findtext('Institution/Name') or ''
    extracted_data["award_title"] = award.findtext('AwardTitle') or ''
    extracted_data["effective_date"] = award.findtext('AwardEffectiveDate') or ''
    extracted_data["expiration_date"] = award.findtext('AwardExpirationDate') or ''
    extracted_data["award_amount"] = award.findtext('AwardTotalIntnAmount') or ''
    extracted_data["abstract"] = award.findtext('AbstractNarration') or ''
    extracted_data["directorate"] = award.findtext('Organization/Directorate/LongName') or ''
    extracted_data["division"] = award.findtext('Organization/Division/LongName') or ''
    # Iterate through Investigators to find the Principal Investigator
    for investigator in award.findall('Investigator'):
        role_code = investigator.findtext('RoleCode')
        if role_code == 'Principal Investigator':
            extracted_data["first_name"] = investigator.findtext('FirstName') or ''
            extracted_data["middle_name"] = investigator.findtext('PI_MID_INIT') or ''
            extracted_data["last_name"] = investigator.findtext('LastName') or ''
            extracted_data["email"] = investigator.findtext('EmailAddress').strip() if investigator.findtext(
                'EmailAddress') else ''
            break  # Stop after finding the principal investigator

    return extracted_data


# Processes all folders from 1981 to 2023
def process_all_folders(base_path, filter_directorate=None):
    all_data = []
    for year in range(1981, 2024):  # Loop through each year
        print(year)
        folder_path = os.path.join(base_path, str(year))
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            for filename in os.listdir(folder_path):
                if filename.endswith('.xml'):
                    file_path = os.path.join(folder_path, filename)
                    try:
                        data = extract_data_from_file(file_path)
                    except:
                        pass
                    if filter_directorate is None or data["directorate"] == filter_directorate:
                        all_data.append(data)
    return pd.DataFrame(all_data)

# Example usage
base_path = "../nsf_data"  # Adjust this path as needed
df = process_all_folders(base_path)
df.to_csv('nsf_data.csv', index=False)