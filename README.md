# Indigenous State Library Collection

## Highlights:
* Admin has full system access with ability to create, edit and delete collection items
* Community Reviewer / Elder engagement to review and update cultural metadata (including approving or rejecting public access to items)
* Library staff can create and edit collection items, include uploading new images and reviewing access requests
* Public users are able to browse all publicly available items and submit access requests
* Current database has over 15 collection items across multiple categories (historical photographs, audio recordings of oral histories, archival manuscripts and documents, artwork created by Indigenous artists, cultural artefact records and language preservation materials)

## Overview:

The Library of Indigenous Knowledge and History was created for a prominent academic library in Australia who have begun digitising their Indigenous collections.  Given the nature of the collections, the library have chosen to handle their data in an ethical way with appropriate respect to the Indigenous owners of the items, in adherence with the CARE principles.

The library has engaged with local community elders to assess the collection and receive community input on how the data is to be managed.  

## Authors:
* Joshua Beck
* Kate Freedman
* Kathleen O'Donnell
* Kayla Horniblow
* Lucy Keeling

## Installation:

### Prerequisites
* Python 3.10+
* MySQL (running locally)
* A local database instance

### Setup Instructions

#### 1. Extract the Project
Extract the contents of the submitted `.zip` archive into your chosen local working directory.

#### 2. Database Configuration
Create a new MySQL database locally. Execute the schema saved in database.sql to load the database and associated assignment data.


#### 3. Configure Environment Variables
Create a file named either `.env` or `env.txt` in the project root directory and configure it with your local MySQL credentials:

```env
MYSQL_HOST=localhost
MYSQL_USER=your_database_username
MYSQL_PASSWORD=your_database_password
MYSQL_DB=your_database_name
```

#### 4. Run the app

```
python run.py 

```


## How to use:

#### Admin:
##### Login details:
Username/email: libraryadmin@qut.edu.au
Password: libraryadmin

* The admin role has full system access
* Navigate to ...

#### Community Reviewer / Elder:
##### Login details:
Username/email: elder@qut.edu.au
Password: communityelder

* Navigate to the 'Reviewer Assessment' page to add comments to items and approve or reject public access to items
* Navigate to 'My Account' to update contact details or change password

#### Library Staff:
##### Login details:
Username/email: librarystaff@qut.edu.au
Password: librarystaff

* Navigate to
* Navigate to 'My Account' to update contact details or change password

#### Public User:
##### Login details:
Username/email: publicuser@qut.edu.au
Password: publicuser 

* Search and browse publicly available items from the home page
* Select an item to view item details
* Submit an access request to view an item at the library
* Navigate to 'My Account' to update contact details or change password
