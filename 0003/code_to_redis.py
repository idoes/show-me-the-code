"""promotion code to Redis
no duplicate promotion code => use Redis set data type
record added date and time
report how many has been add
"""
import redis
r = redis.Redis("localhost")

def add_pc_to_redis(r, item):
    if r.sismember("pCode", item):
        return False
    else:
        r.sadd("pCode", item)
        return True

def show_record_in_redis():
    print r.smembers("pCode")

def program_start():
    # 1 retrieve values from OS file to Python list
    pc_file = open("promotion_code.txt", "r")
    pc_list = pc_file.read().split("\n")
    #print pc_list  # test

    # 2 have a redis on localhost
    for item in pc_list:
        add_pc_to_redis(r, item)

    show_record_in_redis()

program_start()