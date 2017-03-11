import praw

bot = praw.Reddit(user_agent='Smiley Reply Bot',
                  client_id='',
                  client_secret='',
                  username='',
                  password='')

subreddit = bot.subreddit('all')
comments = subreddit.stream.comments()
list = ['test']
counter = 0

for comment in comments:
        text = comment.body
        author = comment.author

        if ':)' in text.lower() and author not in list:
                list.append(author)
                counter += 1
                if counter % 2 == 0:
                        comment.reply(":)")
                else:
                        comment.reply(":D")

                print "Replied"
