from flask import Flask,render_template, request
from database import find_story_by_id, get_all_users, get_all_stories,add_story
import random
app = Flask(__name__)
 

quotes=[' “Nobody has ever measured, not even poets, how much the heart can hold.” – Zelda Fitzgerald' , '  “We loved with a love that was more than love.”– Edgar Allan Poe ', '  “Who, being loved, is poor?” – Oscar Wilde ']



@app.route('/')
def hello_world():
    return render_template("home.html")

@app.route('/newsfeed', methods=["POST", "GET"])
def news_feed():
    quote_day = random.choice(quotes)
    all_stories = get_all_stories()
    print(all_stories,"stories",request.method)
    if request.method=="POST":
        content= request.form['story']
        picture= request.form['picture']
        spouse1 = request.form['name1']
        spouse2 = request.form['name2']
        title= spouse1 + " & " + spouse2 
        add_story(content, picture, spouse1, spouse2, title)
        all_stories = get_all_stories()

    return render_template("newsfeed.html", stories = all_stories,quote = quote_day) 



@app.route('/storypage/<int:story_id>')
def storyyy(story_id):
    story= find_story_by_id(story_id)
    return render_template("storypage.html",story = story)

if __name__ == '__main__':
    app.run(debug=True)