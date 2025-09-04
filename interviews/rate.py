import time
class RateLimiter:
    def __init__(self):

        self.users = {}
        self.limit = 6000


    def add_user(self, user_id):

        user = {
            'user_id':user_id,
            'tokens':10,
            'current_timestamp': round(time.time() *1000)
        }
        self.users[user_id] = user
        # print(self.users)


    def can_serve(self,user_id):

        i = self.users[user_id]
        if i['user_id'] == user_id:
            if round(time.time() *1000) - i['current_timestamp'] < self.limit:
                if i['tokens'] == 0:
                    return False
                else:
                    i['tokens'] = i['tokens'] - 1
                    # print(self.users)
                    return True
            else:
                # max_cap = 100
                # if i['tokens'] + 10 > max_cap:
                #     i['tokens'] = max_cap
                # else:
                i['tokens'] = i['tokens'] + 10  #*factor
                # print(self.users)
                return True


if __name__ == '__main__':
    rl = RateLimiter()
    rl.add_user("savio")
    # print(rl.can_serve("savio"))

    for i in range(0,12):
        print(rl.can_serve("savio"))


