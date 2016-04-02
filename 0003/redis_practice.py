"""practice redis """
import redis
from hashlib import md5

# redis namespace | relation representation
# [key] ~ [datatype] ~ [values]
# [user

redis_server = redis.Redis("localhost")

# assuming no duplicate account_name
def add_user(account_name, user_full_name, user_pass):
    if redis_server.sadd("account_name_set", account_name):
        redis_server.set("user:{0}:fullName".format(account_name),
                         user_full_name )
        redis_server.set("user:{0}:pass".format(account_name),
                         md5(user_pass).hexdigest())
        return True
    else:
        return False


def authenticate_user(account_name, user_pass):
    if redis_server.sismember("account_name_set", account_name):
        pass_hash = md5(user_pass).hexdigest()
        if pass_hash == redis_server.get("user:{0}:pass".format(account_name))\
            or user_pass == redis_server.get("user:{0}:pass".format(account_name)):
            return True
        else:
            return False
    else:
        return False


def delete_account(account_name):
    if redis_server.sismember("account_name_set", account_name):
        redis_server.srem("account_name_set", account_name)
        redis_server.delete("user:{0}:fullName".format(account_name))
        redis_server.delete("user:{0}:pass".format(account_name))
        return True
    else:
        return False
