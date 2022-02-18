"""
Module use API and return information about user friend
"""
import tweepy


def friend_info(name):
    """
    Return usernames and locations of friends of inputted user
    """
    auth = tweepy.OAuthHandler("TM3E73Zu6QgpoY9xctnNNmVtb",
                               "O41Hsxoo2hpwTo84ODzTE0HtP8JdqRNN76Ehs9LL4UJmH7ko5i")
    auth.set_access_token("1492029335435419654-o8ExDUpguupbc34NX8G7QZ9R9Z8UJw",
                          "FXxWfUSATRUgbsUMeuVeckOxu0TuMtxUVuWQxtCUea1eM")
    api = tweepy.API(auth)
    try:
        user = api.get_user(screen_name=name)
    except tweepy.errors.NotFound:
        return None
    f_info = []
    for friend in user.friends():
        location = friend.location
        if len(location) > 0:
            f_info.append([friend.screen_name, friend.location])
    return f_info
