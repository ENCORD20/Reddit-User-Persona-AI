import praw
import requests

REDDIT_CLIENT_ID = "mjgcCpvBmAexNMcCNOrwoA"
REDDIT_SECRET = "a8J9MLrVQafA7H551467QxhtUfvAwg"
USER_AGENT = "UserPersona"

def init_praw():
    return praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_SECRET,
        user_agent=USER_AGENT
    )

def get_user_content(username, limit=100):
    reddit = init_praw()
    user = reddit.redditor(username)

    posts = []
    comments = []

    try:
        for submission in user.submissions.new(limit=limit):
            posts.append({
                'title': submission.title,
                'body': submission.selftext,
                'url': submission.url,
                'permalink': f"https://reddit.com{submission.permalink}"
            })

        for comment in user.comments.new(limit=limit):
            comments.append({
                'body': comment.body,
                'permalink': f"https://reddit.com{comment.permalink}"
            })
    except Exception as e:
        print(f"Error scraping user: {e}")

    return posts, comments
