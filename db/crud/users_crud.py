from db.crud.interface_crud import CrudABC


class UsersDb(CrudABC):

    def create(self):
        pass

    def read(self, email):
        sql_query = """
        SELECT * FROM Users
        WHERE email=?;
        """
        cursor = self.connection.cursor()
        cursor.execute(sql_query, (email,))

        users = cursor.fetchall()  # return a list with a list

        # return a list with dict
        users_json = []
        for user in users:
            users_json.append({
                "id": user[0],
                "email": user[1]
            }
            )
        return users_json

    def update(self):
        pass

    def delete(self):
        pass
