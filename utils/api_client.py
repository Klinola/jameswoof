from utils.utils import get_request, post_request

api_endpoints = {
    "getTwitterUrl": ("get", "/login/app/twitter_url"),
    "login": ("post", "/login/app/sign_in"),
    "tempLogin": ("post", "/app/login/temp_login"),
    "checkFreePet": ("get", "/pet/free_exist"),
    "petClaim": ("post", "/pet/claim"),
    "checkPetAward": ("get", "/pet/activity_award"),
    "awardPetClaim": ("post", "/pet/receive_activity_award"),
    "myPetList": ("get", "/pet/mine"),
    "shopList": ("get", "/pet_store/list"),
    "buyPet": ("post", "/pet_store/buy"),
    "renewalPet": ("post", "/pet/renewal"),
    "renamePet": ("post", "/pet/rename"),
    "getFriendList": ("get", "/user/friend_list"),
    "userInfo": ("get", "/user"),
    "accountTotal": ("get", "/account/total"),
    "taskData": ("get", "/login/task"),
    "uptaskData": ("post", "/task"),
    "getAward": ("post", "/task/receive_award"),
    "getFollowAuthURL": ("get", "/task/app/follow_twitter_auth_url"),
    "followTwitter": ("post", "/task/app/follow_twitter"),
    "petDetail": ("get", "/pet"),
    "addInviteCode": ("post", "/user/add_invite_code"),
    "wakeup": ("post", "/pet/wakeup"),
    "rankingList": ("get", "/user/ranking_list"),
    "friendList": ("get", "/user/friend_list"),
    "friendStatistics": ("get", "/user/friend_statistics"),
    "friendAwardList": ("get", "/user/friend_award_list"),
    "getDailyTotal": ("get", "/daily_reward/total"),
    "getDailyList": ("get", "/daily_reward"),
    "getDailyReward": ("post", "/daily_reward"),
    "getEvent": ("get", "/task/events"),
    "getSeedList": ("get", "/seed/list"),
    "migrateAuth": ("get", "/user/migrate"),
    "migrate": ("post", "/user/migrate"),
    "create": ("post", "/g/create"),
    "getGroup": ("get", "/g")
}

class APIMeta(type):
    def __new__(cls, name, bases, dct):
        for func_name, (method, endpoint) in api_endpoints.items():
            if method == "get":
                dct[func_name] = cls.create_get_function(endpoint)
            elif method == "post":
                dct[func_name] = cls.create_post_function(endpoint)
        return super().__new__(cls, name, bases, dct)

    @staticmethod
    def create_get_function(endpoint):
        def get_function(self, data=None):
            return get_request(self.token, endpoint, custom_data=data)
        return get_function

    @staticmethod
    def create_post_function(endpoint):
        def post_function(self, data=None):
            return post_request(self.token, endpoint, custom_data=data)
        return post_function

class APIClient(metaclass=APIMeta):
    def __init__(self, token):
        self.token = token

# example

if __name__ == "__main__":
    token = ""
    client = APIClient(token)

    client.getTwitterUrl()
    client.login()
    client.tempLogin()