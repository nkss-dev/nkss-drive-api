# import db
from Google import connect_to_drive
import pandas as pd
import json


def get_folder_contents(service, id):

    query = f"parents = '{id}'"
    if not service:
        print("Connection failed")
        return []

    response = service.files().list(q=query).execute()
    files = response.get('files', [])
    nextPageToken = response.get('nextPageToken')
    
    while nextPageToken:
        response = service.files().list(q=query, pageToken=nextPageToken).execute()
        files.extend(response.get('files'))
        nextPageToken = response.get('nextPageToken')

    return files


def list_drive(service, folder_id, result, parentName='', grandParentName=''):
    files = get_folder_contents(service, folder_id)
    
    for item in files:
        if item['mimeType'] != 'application/vnd.google-apps.folder':
            try:
                id = item['id']
                link = (service.files().get(fileId=id, fields='webViewLink').execute())[
                    'webViewLink']
                item['tags'] = [parentName, grandParentName]
                item['drive_url'] = link
                result.append(item)
            except Exception as error:
                print("Error: ", error)

    for item in files:
        # parentName = 'General'
        if item['mimeType'] == 'application/vnd.google-apps.folder':
            if parentName != 'General':
                grandParentName = parentName
            parentName = item['name']
            folder_id = item['id']
            # contents = get_folder_contents(service, folder_id)
            try:
                list_drive(service, folder_id, result,
                           parentName, grandParentName)
            except Exception as error:
                print("Error: ", error)


def main():
    # TODO: query the drive and add files to the database
    # call db.add_files() to add files to the database

    folder_id = '1U2taK5kEhOiUJi70ZkU2aBWY83uVuMmD'
    CLIENT_SECRET_FILE = '../credentials.json'
    SCOPES = ['https://www.googleapis.com/auth/drive']
    service = connect_to_drive(CLIENT_SECRET_FILE, SCOPES)
    if not service:
        print("Connection failed")
        exit()

    print("Drive Connected!")
    result = []
    list_drive(service, folder_id, result, 'General', '')
    files = pd.DataFrame(result)
    print(files)
    files.to_excel("links.xlsx")

    pass


if __name__ == '__main__':
    main()
