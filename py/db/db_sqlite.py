# -*- coding: UTF8 -*
"""
@author: Jiang
@file name: db
@create date: 2022/8/20 11:13
@description:
"""
import os.path
import sqlite3


class DB_SQLite:
    def __init__(self, db_name=r'C:\Users\Jiang\IdeaProjects\hxh\backend\db\database.db'):
        try:
            self.db_name = os.path.join(os.getcwd(), db_name)
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            print('数据库连接成功: {}'.format(os.path.basename(self.db_name)))
        except Exception as e:
            print(str(e))
            raise

    def select(self, sql):
        retLen, ret = 0, []
        try:
            self.cursor.execute(sql)
            ret = self.cursor.fetchall()
            retLen = len(ret)
            print('查询共 {} 条记录: {}'.format(retLen, str(ret)))
        except Exception as e:
            print('数据库错误: {}'.format(str(e)))
        finally:
            self.cursor.close()
            self.conn.close()
            print(f'数据库关闭成功: {os.path.basename(self.db_name)}')
            return retLen, ret

    def ex_sql(self, sql):
        count = 0
        try:
            ret = self.cursor.execute(sql)
            self.conn.commit()
            count = ret.rowcount
            print('影响行数: {}'.format(count))
        except Exception as e:
            print('数据库错误: {}'.format(str(e)))
        finally:
            self.cursor.close()
            self.conn.close()
            print(f'数据库关闭成功: {os.path.basename(self.db_name)}')
            return count

    update = ex_sql

    delete = ex_sql

    insert = ex_sql

    def create_table(self, table_name: str, field_list: list) -> bool:
        ret = False
        try:
            fields = ', '.join([field + ' TEXT' for field in field_list])
            sql = f"CREATE TABLE {table_name} ({fields});"
            self.cursor.execute(sql)
            self.conn.commit()
            ret = True
        except Exception as e:
            print(f'数据库错误, 创建 {table_name} 表失败: {str(e)}')
            ret = False
        finally:
            self.cursor.close()
            self.conn.close()
            print(f'数据库关闭成功: {os.path.basename(self.db_name)}')
            return ret


db_sqlite = DB_SQLite()
