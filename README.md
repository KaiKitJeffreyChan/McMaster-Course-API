# McMaster Course Scrape

Returns CSV of McMaster course information.
Scraped data using Selenium library.

If you want to use this script, make sure you install selenium's chrome driver and have it in the correct location.

## Usage

### List all Courses

**_ Definitions _**

`GET /courses`

**Response**

- `200 OK` on success

```json
[
    {
        "identifier": "1XC3",
        "name": "Computer Science Practice and Expirience: Development Basics 1XC3",
        "units": 4,
        "description": "this course blah blah blah",
        "other": "prerequisites : blah blah, Antirequisites: ",
    }
    {
        "identifier": "1XD3",
        "name": "Introduction to Design Thinking",
        "units": 3,
        "description": "this course blah blah blah",
        "other": "prerequisites : blah blah, Antirequisites: ",
    }
]

```

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
  "identifier": "1XC3",
  "name": "Computer Science Practice and Expirience: Development Basics 1XC3",
  "units": 4,
  "description": "this course blah blah blah",
  "other": "prerequisites : blah blah, Antirequisites: "
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
  "identifier": "1XC3",
  "name": "Computer Science Practice and Expirience: Development Basics 1XC3",
  "units": 4,
  "description": "this course blah blah blah",
  "other": "prerequisites : blah blah, Antirequisites: "
}
```

### Delete a Course

**Definitions**

`DELETE /devices/<identifier>`

**Response**

--`404 Not Found` if device doesnt exist
--`204 No Content` happened successfully but no content to return
