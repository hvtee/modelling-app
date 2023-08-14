import sqlite3
from model.sql import SQL


class Matrix:
    matrix_data = []

    def __init__(self, name, mu_1, sigma_1, d):
        try:
            self.name = name
            self.mu_1 = mu_1
            self.sigma_1 = sigma_1
            self.d = d

            Matrix.matrix_data.append(self)
        except ValueError as ve:
            print(f"Invalid value! {ve}")
        except IOError as ioe:
            print(f"IO error! {ioe}")

    @classmethod
    def create_matrix_data(cls):
        try:
            name = input("\nName of environment_data set: ")
            mu_1 = complex(input("mu1(a-bj): "))
            sigma_1 = int(input("sigma1: "))
            d = float(input("d(m): "))

            return cls(name, mu_1, sigma_1, d)
        except ValueError as ve:
            print(f"Invalid value! {ve}")
        except IOError as ioe:
            print(f"IO error! {ioe}")
        except AttributeError as ae:
            print(f"AE: {ae}")

    @classmethod
    def show_matrix_data(cls):
        if len(Matrix.matrix_data) == 0:
            return print("environment_data is empty!")

        try:
            counter = 0
            for obj in cls.matrix_data:
                print("\nEnvironment:")
                print(f"SET No: {counter}")
                print(f"name: {obj.name}")
                print(f"mu1: {obj.mu_1}")
                print(f"sigma1: {obj.sigma_1}")
                print(f"d: {obj.d}")
                counter += 1
        except AttributeError:
            print("AE")

    def save_to_db(self):
        try:
            Matrix.show_matrix_data()
            conn = sqlite3.connect('data/environment_data.db')
            cur = conn.cursor()
            cur.execute(SQL.sql_envir_create)
            values = (None, self.name, str(self.mu_1), self.sigma_1, self.d)
            cur.execute('INSERT INTO environment_data VALUES (?,?,?,?,?)', values)
            conn.commit()
            cur.close()
            conn.close()
            print("Saved with no errors.")
        except sqlite3.Error as e:
            print(f"Error saving to database: {e}")

    @classmethod
    def load_from_db(cls):
        try:
            conn = sqlite3.connect('data/environment_data.db')
            cur = conn.cursor()
            cur.execute(SQL.sql_envir_all)
            rows = cur.fetchall()

            if len(rows) == 0:
                print("No data found in database!")
                return

            counter = 0
            for row in rows:
                print(f"\nSET № {counter}")
                print(f"name: {row[0]}")
                print(f"mu_1: {row[1]}")
                print(f"sigma_1: {row[2]}")
                print(f"d: {row[3]}")
                counter += 1

            cur.execute(SQL.sql_envir_all)
            rows = cur.fetchall()
            try:
                choice = int(input("Choose SET № "))
                if choice >= len(rows) or choice < 0:
                    print("Wrong SET №!")
                    print("SET № is 0")
                    choice = 0
            except ValueError or IOError:
                print("Wrong data!")
                return
            try:
                row = rows[choice]
                Matrix(row[0], complex(row[1]), row[2], row[3])
            except ValueError:
                print("Error occurred in values of SET")

            cur.close()
            conn.close()
            print("Success")
        except sqlite3.Error as e:
            print(f"Error loading from database: {e}")
        except ValueError as ve:
            print(f"Invalid value! {ve}")

    @classmethod
    def load_examples(cls):
        try:
            conn = sqlite3.connect('data/environment_data.db')
            cur = conn.cursor()
            cur.execute("SELECT * FROM environment_examples")
            rows = cur.fetchall()

            if len(rows) == 0:
                print("No data found in database(environment_examples)!")
                return

            for row in rows:
                try:
                    Matrix(row[0], complex(row[1]), row[2], row[3])
                except ValueError:
                    print("Error occurred in values of SET")
        except sqlite3.Error as e:
            print(f"Error loading from database: {e}")
