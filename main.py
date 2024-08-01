import requests

def get_top_hacker_news_stories():
    top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    story_url_template = "https://hacker-news.firebaseio.com/v0/item/{}.json"

    response = requests.get(top_stories_url)

    if response.status_code == 200:
        top_story_ids = response.json()

        top_stories = []
        for story_id in top_story_ids[:30]:
            story_response = requests.get(story_url_template.format(story_id))
            if story_response.status_code == 200:
                story_data = story_response.json()
                top_stories.append(story_data)

        for idx, story in enumerate(top_stories, start=1):
            print(f"{idx}. {story.get('title')} (ID: {story.get('id')})")
    else:
        print(f"Failed to retrieve top stories. Error code: {response.status_code}")


get_top_hacker_news_stories()
