# flask_app.py

The main module that creates a web page to generate a map with a user's friends on Twitter.

# tweep.py

Module use Twitter API. After receiving username, it return list with friends' usernames and locations.

# map_make.py

Module receive the list with friends' usernames and locations and return HTML file with map with markers that contain friends' username.

# templates

Directory that contain HTML and CSS file of web page where user pirnt necessary username.

## Usage

Run flusk_app.py and use link http://127.0.0.1:8082/ in browser.

![image](https://user-images.githubusercontent.com/92572643/154812633-69c2b962-454b-4bf7-b44e-5092e50496cd.png)

Result:
![image](https://user-images.githubusercontent.com/92572643/154812608-86d41ae3-7dee-40dd-aefb-4869a2866b4b.png)
