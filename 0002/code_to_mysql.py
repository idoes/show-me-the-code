"""save code to code(table) testdb(database name on localhost)"""

import MySQLdb

def connect_to_database(server_name, db_user_name, db_user_key, server_database):
    db_connection = MySQLdb.connect(server_name, db_user_name, db_user_key, server_database)
    #print db_connection  # test
    return db_connection

def create_code_table(db_mysql_connection):
    db_table_name = "code"
    query = """\
create table `promotion_code`(
`id` int(11) unsigned NOT NULL AUTO_INCREMENT,
`promotion_code` VARCHAR(50) NOT NULL,
PRIMARY KEY (`id`))
ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""
    #print query  # test
    query_execution_object = db_mysql_connection.cursor()
    query_execution_object.execute("DROP TABLE IF EXISTS promotion_code")
    query_execution_object.execute(query)

def one_code_into_table(one_code, db_connection):
    query = "insert into `promotion_code`(`promotion_code`)values('{0}')"
    query = query.format(one_code)
    print query  # test
    query_execution_object = db_connection.cursor()
    try:
        query_execution_object.execute(query)
        db_connection.commit()
    except:
        db_connection.rollback()




def program_start():
    server_name = "localhost"
    db_user_name = "root"
    db_user_key = "asd"
    server_database = "testdb"
    db_connection_object = connect_to_database(server_name,
                                               db_user_name,
                                               db_user_key,
                                               server_database)
    create_code_table(db_connection_object)
    #print db_connection_object  # test

    file_name="promotion_code.txt"
    f = open(file_name)
    file_line_list = f.read().split("\n")
    for one_code in file_line_list:
        one_code_into_table(one_code, db_connection_object)

    f.close()
    db_connection_object.close()



program_start()
