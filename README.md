# sparkify-etl
An ETL pipeline to analyze song and user activity data collected by Sparkify

## Description
TBD.

## Source data

### Song data
```javascript
{
  "num_songs": 1,
  "artist_id": "ARJIE2Y1187B994AB7",
  "artist_latitude": null,
  "artist_longitude": null,
  "artist_location": "",
  "artist_name": "Line Renaud",
  "song_id": "SOUPIRU12A6D4FA1E1",
  "title": "Der Kleine Dompfaff",
  "duration": 152.92036,
  "year": 0
}
```

### Log data
```javascript
{
  "index": 2,
  "artist": "Des'ree",
  "auth": "Logged In",
  "firstName": "Kaylee",
  "gender": "F",
  "itemInSession": 1,
  "lastName": "Summers",
  "length": 246.30812,
  "level": "free",
  "location": "Phoenix-Mesa-Scottsdale, AZ",
  "method": "PUT",
  "page": "NextSong",
  "registration": 1540344794796,
  "sessionId": 139,
  "song": "You Gotta Be",
  "status": 200,
  "ts": 1541106106796,
  "userAgent": "\"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36\"",
  "userId": 8
}
```

## Local setup
You can work with this project locally by having an environment with the following (or equivalent):

- macOS 10.14.6.
- Homebrew 2.2.11. [Installation](https://brew.sh/).
- Python 3.7.7 and pip 20.0.2. Install both with Homebrew: `brew install python`.
- psycopg2 2-2.8.4. Install with pip3: `pip3 install psycopg2`.
- PostgreSQL 9.5.4. [Installation](https://www.codementor.io/@engineerapart/getting-started-with-postgresql-on-mac-osx-are8jcopb).

**The above could not be tested, as there were problems installing the psycopg2 library with pip3. I will be using Udacity's project workspace to develop the project and use this git project solely to track the development.**
