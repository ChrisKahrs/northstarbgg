from flask import Flask, render_template, url_for
from forms import usernamesform
import http.client, urllib.request, urllib.parse, urllib.error, base64, json, urllib

app = Flask(__name__)

app.config['SECRET_KEY'] ='1029384756a;sldkfjgh'

posts = []

def getPostData(users):
    result = None
    for user in users:
        urlString = "https://bgg-json.azurewebsites.net/collection/" + str(user)
        headers = {
            'Content-Type': 'application/json',
        }
        try:
            # Execute the REST API call and get the response.
            conn = http.client.HTTPSConnection("bgg-json.azurewebsites.net")
            request_path = "/collection/"  + str(user)
            conn.request("GET", request_path, None, headers)
            response = conn.getresponse()

            data = response.read().decode("UTF-8")
            
            if len(data) > 0:
                if result:
                    intermeidate_result = json.loads(data)
                    for item in intermeidate_result:
                        item.update( {"bggusername": str(user)})
                    result = result + intermeidate_result
                else: 
                    result = json.loads(data)
                    for item in result:
                        item.update( {"bggusername": str(user)})
            

        except Exception as ex:
            raise ex
    res = [i for i in result if not (i['rank'] == -1)] 
    return sorted(res, key = lambda i: (i['rank'])) 

posts = [
    {
        "username": "ckahrs",
        "gameId": 207830,
        "name": "5-Minute Dungeon",
        "image": "https://cf.geekdo-images.com/original/img/qmIKAcdaUMX4skrH8pX0qBMxijg=/0x0/pic3370214.jpg",
        "thumbnail": "https://cf.geekdo-images.com/thumb/img/ARZr8-iwv0GPlRiJHbseSwvXtKk=/fit-in/200x150/pic3370214.jpg",
        "minPlayers": 2,
        "maxPlayers": 5,
        "playingTime": 30,
        "isExpansion": False,
        "yearPublished": 2017,
        "bggRating": 0.0,
        "averageRating": 7.15569,
        "rank": 675,
        "numPlays": 0,
        "rating": -1.0,
        "owned": True,
        "preOrdered": False,
        "forTrade": True,
        "previousOwned": False,
        "want": False,
        "wantToPlay": False,
        "wantToBuy": False,
        "wishList": False,
        "userComment": ""
    },
    {
        "username": "jkahrs",
        "gameId": 173346,
        "name": "7 Wonders Duel",
        "image": "https://cf.geekdo-images.com/original/img/M6wL1YFgW-PsdtJ328m2QiJf1K8=/0x0/pic3376065.jpg",
        "thumbnail": "https://cf.geekdo-images.com/thumb/img/cwWMq5feF7O4O82HJOK3WE5IZ6o=/fit-in/200x150/pic3376065.jpg",
        "minPlayers": 2,
        "maxPlayers": 2,
        "playingTime": 30,
        "isExpansion": False,
        "yearPublished": 2015,
        "bggRating": 0.0,
        "averageRating": 8.11154,
        "rank": 17,
        "numPlays": 0,
        "rating": -1.0,
        "owned": True,
        "preOrdered": False,
        "forTrade": False,
        "previousOwned": False,
        "want": False,
        "wantToPlay": False,
        "wantToBuy": False,
        "wishList": False,
        "userComment": "Test Comment"
    }
]


@app.route("/", methods=['GET','POST'])
@app.route("/home", methods=['GET','POST'])
def home():
    form = usernamesform()
    if form.validate_on_submit():
        userList = str(form.usernames.data).split(",")
        posts = getPostData(userList)
        return render_template("finalResult.html", posts=posts, users=userList)
    else:
        posts = [""]
    return render_template("table.html", posts=posts, form=form)

@app.route("/table")
def table():
    return render_template("table.html", posts=posts)

if __name__ == '__main__':
    app.run(debug=True)


  


