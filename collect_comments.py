import api
from csv_writer import write
import sentiment

N = 100

def main():
    topstories = api.get_topstories()[0:N]
    print("checking first " + str(N) + " top stories")

    comments = api.all_items(topstories)
    comments = [get_sentiment(comment) for comment in comments if 'text' in comment]
    print("found " + str(len(comments)) + " comments")

    headers = ['id', 'type', 'sentiment']
    write(comments, "test1.csv", headers)
    print("done")


def get_sentiment(comment):
    if 'text' in comment:
        comment['sentiment'] = sentiment.comparative(comment['text'])
    else:
        comment['sentiment'] = 0

    return comment


if __name__ == "__main__":
    main()
