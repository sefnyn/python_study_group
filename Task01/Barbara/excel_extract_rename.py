import win32com.client
import os
import re
import pandas as pd

def extract_excel_attachments(input_folder, output_folder):
    counter = 0

    for file in os.listdir(input_folder):
        if file.endswith(".msg"):
            # Create instance of the Outlook application
            outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
            file_path = os.path.join(input_folder, file)

            # Open Outlook message file
            msg = outlook.OpenSharedItem(file_path)
            print(file_path)

            # Get attachments from Outlook message
            att = msg.Attachments
            for attachment in att:

                # Check if attachment is Excel file
                if re.search(r".*\.xls|.*\.xlsx", attachment.Filename):
                    counter += 1

                    save_path = os.path.join(output_folder, f"{counter}_{attachment.Filename}")
                    attachment.SaveAsFile(save_path)

                    # Read Excel file to get institution name
                    excel_file_path = save_path
                    df = pd.read_excel(excel_file_path, header=None)

                    # Get institution name
                    institution_name = find_institution_name(df)

                    # Remove invalid characters from institution name
                    invalid_chars = r'[:/\\?*|"<>,/\r?\n|\r/]'
                    institution_name = re.sub(invalid_chars, '_', str(institution_name))

                    # Rename the file with institution name
                    if institution_name is not None:
                        new_file_name = f"{institution_name}.xlsx"
                        new_file_path = os.path.join(output_folder, new_file_name)

                        while os.path.exists(new_file_path):
                            counter += 1
                            new_file_name = f'{institution_name}_{counter}.xlsx'
                            new_file_path = os.path.join(output_folder, new_file_name)
                        os.rename(save_path, new_file_path)
                        print(f"File renamed to: {new_file_name}")
                    else:
                        print('Institution name not found. File renamed as counter')

    return counter


def find_institution_name(df):
    institution_name_5 = get_cell_value(df, 5)
    if not pd.isna(institution_name_5):
        return institution_name_5
    institution_name_6 = get_cell_value(df, 6)
    if not pd.isna(institution_name_6):
        return institution_name_6
    return None


def get_cell_value(df, row_number):
    try:
        # Concatenate values from columns A and B of the specified row
        value = str(df.iloc[row_number, 0]) + "_" + str(df.iloc[row_number, 1])
        # print(f'value at {row_number}: {value}')
        return value

    except IndexError:
        # Return none if the row is out of index
        return None

# Specify input and output folders
input_folder = r"C:\Users\bpackard\OneDrive - The National Archives\Documents\Accessions_2023_emails"
output_folder = r"C:\Users\bpackard\OneDrive - The National Archives\Documents\Accessions_2023files"

# Call the function
attachments_count = extract_excel_attachments(input_folder, output_folder)
print(f"Number of Excel attachments saved: {attachments_count}")