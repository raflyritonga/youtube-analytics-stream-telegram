# YouTube Analytics Streamed to Telegram Real-Time

This project utilizes Python to fetch real-time YouTube metrics such as likes, views, comments, and favorites. The data is streamed via Kafka, processed using ksqlDB, and subsequently sent to a Telegram bot for real-time notifications.

## Tech Stack

- Python 3.10 (minimum)
- Kafka
- Telegram API
- Docker
- Confluent Containers (Zookeeper, Kafka, Schema Registry, Connect, ksqlDB, Control Center)

## Getting Started

1. Clone the repository.
   ```bash
   git clone https://github.com/airscholar/YoutubeAnalytics.git
   ```

2. Install dependencies.
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure the Docker and Confluent containers set up.

## Configuration

1. Make a `config` folder with `config.local` in it and set the following:
    - `[youtube]` : Section
    - `API_KEY`: Your YouTube API Key
    - `PLAYLIST_ID`: The YouTube playlist ID you want to track

2. Set up your Kafka server address in the main script, by default, it's set to `localhost:9092`.

## Running the Code

1. Start your Kafka and other Confluent services on Docker with
   ```bash
   docker compose up -d
   ``` 
2. Run the Python script.
    ```bash
    python youtube_analytics.py
    ```