# Real-Time Tweet Retrieval Project

This project aims to retrieve the text of tweets from one or more specific Twitter accounts as soon as they are published, using the X API. The script is designed to run continuously without manual restarts and handles API rate limits.

## Features

- **Tweet Text Extraction**: Retrieves the text of a tweet as soon as it is posted.
- **API Cooldown Management**: The script automatically waits for the necessary time when the API request limit is reached.
- **Real-Time Retrieval**: Uses the X Streaming API to capture new tweets as soon as they are published.
- **Data Storage**: Allows storing extracted tweets in a file (or database as needed).

## Prerequisites

- Python 3.x
- `tweepy` library to interact with the X API
- X API keys for authentication

## Project Steps

### Step 1: Extract Tweet Text
- **Objective**: Retrieve the text of a tweet when it is posted.
- **Method**: Use the X API to access tweets from a specific account.

### Step 2: Manage API Cooldown
- **Objective**: Manage the request limit imposed by the X API to avoid having to manually restart the script when this limit is reached.
- **Method**: Implement logic that automatically waits for the cooldown to end before resuming extraction.

### Step 3: Retrieve Tweets in Real-Time (Streaming)
- **Objective**: Use the X Streaming API to listen for real-time tweets and retrieve those published without manually restarting the script.
- **Method**: Configure real-time tweet listening via the X Streaming API.

### Step 4: Handle Errors and Exceptions
- **Objective**: Ensure the script does not crash in case of errors (e.g., lost connection, API error).
- **Method**: Implement error handling that restarts the process in case of issues.

### Step 5: Store Retrieved Tweets
- **Objective**: Save retrieved tweets for later analysis or use.
- **Method**: Save extracted tweets to a file or database.

### Step 6: Data Processing
- **Objective**: Add processing for retrieved tweets to extract additional information (e.g., sentiment analysis, hashtag extraction).
- **Method**: Process extracted tweets according to project needs.


