# import db
from Google import connect_to_drive
import pandas as pd
import db


def get_folder_contents(service, id):

    query = f"'{id}' in parents"
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
                item['tags'] = [parentName, grandParentName]
                result.append(item)
            except Exception as error:
                print("Error: ", error)

    for item in files:

        if item['mimeType'] == 'application/vnd.google-apps.folder':
            if parentName != 'General':
                grandParentName = parentName
            parentName = item['name']
            folder_id = item['id']
            try:
                list_drive(service, folder_id, result,
                           parentName, grandParentName)
            except Exception as error:
                print("Error: ", error)


def main():

    folder_id = '1U2taK5kEhOiUJi70ZkU2aBWY83uVuMmD'
    CLIENT_SECRET_FILE = './data/credentials.json'
    SCOPES = ['https://www.googleapis.com/auth/drive']
    service = connect_to_drive(CLIENT_SECRET_FILE, SCOPES)
    if not service:
        print("Connection failed")
        exit()

    print("Drive Connected!")

    result = []

    list_drive(service, folder_id, result, 'General', '')

    files = pd.DataFrame(result)
    files.to_excel("data/links.xlsx")
    pass


if __name__ == '__main__':
    main()
