import mysql.connector


class Db:
    def __init__(self):
        self.cnx = mysql.connector.connect(host="localhost",user="root",password="",database="uniqueid")
        self.cur = self.cnx.cursor(dictionary=True)


    def select(self, q):
        self.cur.execute(q)
        return self.cur.fetchall()

    def selectOne(self, q):
        self.cur.execute(q)
        return self.cur.fetchone()


    def insert(self, q):
        self.cur.execute(q)
        self.cnx.commit()
        return self.cur.lastrowid

    def update(self, q):
        a=self.cur.execute(q)
        self.cnx.commit()
        return a

    def delete(self, q):
        self.cur.execute(q)
        self.cnx.commit()
        return self.cur.rowcount

    def jsonsel(self,a):
        self.cur.execute(a)
        self.res = self.cur.fetchall()
        row_headers = [x[0] for x in self.cur.description]
        json_data = []
        for result in self.res:
            json_data.append(dict(zip(row_headers, result)));
            print(self.res, json_data)
        return json_data




