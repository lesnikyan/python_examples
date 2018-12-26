 
from pprint import p
import pymysql.cursors
import traceback

connDict = { 'host' : '127.0.0.1', 'user': 'root', 'password' : '',\
    'db' : 'test_odbc', 'cursorclass': pymysql.cursors.DictCursor, 'charset':'utf8' }
 
conn = pymysql.connect(**connDict)
try:
    with conn.cursor() as cursor:
        p('Block 1')
        cursor.execute('select count(id) as curcount from test1')
        #resCount = cursor.fetchone()
        #p(resCount)
        #count = resCount['curcount']
        count = cursor.fetchone()['curcount']
        p('count = {}'.format(count))
        sqlInsert = 'insert into test1(name, amount, is_active) values (%s, %s, %s);'
        params = ('Jack'+str(count), (count+0.5), True)
        cursor.execute(sqlInsert, params)
    conn.commit()
    
    with conn.cursor() as cursor:
        p('Block 2')
        sql = 'select * from test1'
        cursor.execute(sql)
        res = cursor.fetchall()
        for row in res:
            p(row)
        
    

except Exception as err:
    p('!!! Error:')
    p(err)
    traceback.print_exc()
finally:
    conn.close()
