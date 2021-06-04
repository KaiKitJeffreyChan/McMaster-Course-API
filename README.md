# McMaster Course API

## Usage

```https://mcmaster-course-api.herokuapp.com```

### List all Courses

**Definitions**

`GET /courses`

**Response**

- `200 OK` on success

```json
[
    {
        "identifier": "1A03",
        "name": "CLASSICS 1A03 - Introduction to Classical Archaeology",
        "units": "3 unit(s)",
        "description": "A study of the history and methodology of Greek and Roman archaeology illustrated with materials from excavated sites.",
        "other": "Three lectures; one term"
    },
    {
        "identifier": "1B03",
        "name": "CLASSICS 1B03 - An Introduction to Ancient Myth and Literature",
        "units": "3 unit(s)",
        "description": "A study of Greek and Roman mythology and literature. Texts such as Homer, Virgil and Greek tragedies will be read in    
        translation.",
        "other": "Two lectures, one tutorial; one term"
    }
 
]

```

### Edit existing course

**Definitions**

`PUT /courses/<identifier>`

**Arguments** 

- `"identifier" : string` unique identifier for the course
- `"name": string` friendly name for the course with course code
- `"units": int` how many units is the course
- `"description": string` description of the course if there is any
- `"other": string` anything additional to add, course requisites, semesters taught

-- `201 Created` on success
-- `404 Not Found` if the course does not exist

### Adding a New Course

**Definitions**

`POST /courses`

**Arguments**

- `"identifier" : string` unique identifier for the course
- `"name": string` friendly name for the course with course code
- `"units": int` how many units is the course
- `"description": string` description of the course if there is any
- `"other": string` anything additional to add, course requisites, semesters taught

If course with identifier already exists, overwrites it

**Response**

-- `201 Created` on success

```json
{
  "CLASSICS 1A03 - Introduction to Classical Archaeology": {
        "identifier": "1A03",
        "name": "CLASSICS 1A03 - Introduction to Classical Archaeology",
        "units": "3 unit(s)",
        "description": "A study of the history and methodology of Greek and Roman archaeology illustrated with materials from excavated sites.",
        "other": "Three lectures; one term"
  }
}
```

### Lookup Course Details

**Definitions**

`GET /courses/<identifier>`

**Response**

-- `404 Not Found` if the course does not exist
-- `200 OK` on success

```json
{
    "identifier": "1A03",
    "name": "CLASSICS 1A03 - Introduction to Classical Archaeology",
    "units": "3 unit(s)",
    "description": "A study of the history and methodology of Greek and Roman archaeology illustrated with materials from excavated sites.",
    "other": "Three lectures; one term"
}
```

### Delete a Course

**Definitions**

`DELETE /devices/<identifier>`

**Response**

--`404 Not Found` if device doesnt exist
--`204 No Content` happened successfully but no content to return


## Scraping Script

Returns CSV of McMaster course information.
Scraped data using Selenium library.

If you want to use this script, make sure you install selenium's chrome driver and have it in the correct location.

FYI, This only scrapes information from the McMaster Calender (I noticed that its not always updated, etc there are courses listed on McMaster's CAS website that are not yet on the calender)

<img width="1435" alt="Screen Shot 2021-05-14 at 6 45 27 PM" src="https://user-images.githubusercontent.com/77026758/118338607-8dd4aa80-b4e4-11eb-857e-225d90752009.png">
