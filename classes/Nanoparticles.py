import sqlite3
from classes.sql import SQL


class Nanoparticles:
    nanoparticles_data = []

    def __init__(self, name, mu_2, sigma_2, c, a):
        try:
            self.name = name
            self.mu_2 = mu_2
            self.sigma_2 = sigma_2
            self.c = c
            self.a = a

            Nanoparticles.nanoparticles_data.append(self)
        except ValueError as ve:
            print(f"Invalid value! {ve}")
        except IOError as ioe:
            print(f"IO error! {ioe}")

    @classmethod
    def create_nanoparticles_data(cls):
        try:
            name = input("\nName of nanoparticles data set: ")
            mu_2 = complex(input("mu2(a-bj): "))
            sigma_2 = int(input("sigma2: "))
            c = float(input("c: "))
            a = int(input("a(nm): ")) * pow(10, -9)

            return cls(name, mu_2, sigma_2, c, a)
        except ValueError as ve:
            print(f"Invalid value! {ve}")
        except IOError as ioe:
            print(f"IO error! {ioe}")
        except AttributeError as ae:
            print(f"AE: {ae}")

    @classmethod
    def show_nanoparticles_data(cls):
        if len(Nanoparticles.nanoparticles_data) == 0:
            return print("Nanoparticles data is empty!")

        try:
            counter = 0
            for obj in cls.nanoparticles_data:
                print("\nNANOPARTICLES:")
                print(f"SET No: {counter}")
                print(f"name: {obj.name}")
                print(f"mu2: {obj.mu_2}")
                print(f"sigma2: {obj.sigma_2}")
                print(f"c: {obj.c}")
                print(f"a: {obj.a}")
                counter += 1
        except AttributeError:
            print("AE")

    def save_to_db(self):
        try:
            Nanoparticles.show_nanoparticles_data()
            conn = sqlite3.connect('data/nanoparticles_data.db')
            cur = conn.cursor()
            cur.execute(SQL.sql_npart_create)
            values = (None, self.name, str(self.mu_2), self.sigma_2, self.c, self.a)
            cur.execute('INSERT INTO nanoparticles_data VALUES (?,?,?,?,?,?)', values)
            conn.commit()
            cur.close()
            conn.close()
            print("Saved with no errors.")
        except sqlite3.Error as e:
            print(f"Error saving to database: {e}")

    @classmethod
    def load_from_db(cls):
        try:
            conn = sqlite3.connect('data/nanoparticles_data.db')
            cur = conn.cursor()
            cur.execute(SQL.sql_npart_all)
            rows = cur.fetchall()

            if len(rows) == 0:
                print("No data found in database!")
                return

            counter = 0
            for row in rows:
                print(f"\nSET № {counter}")
                print(f"name: {row[0]}")
                print(f"mu_2: {row[1]}")
                print(f"sigma_2: {row[2]}")
                print(f"c: {row[3]}")
                print(f"a: {row[4]}")
                counter += 1

            cur.execute(SQL.sql_npart_all)
            rows = cur.fetchall()
            try:
                choice = int(input("Choose SET № "))
                if choice >= len(rows) or choice < 0:
                    print("Wrong SET №!")
                    print("SET № is 0")
                    choice = 0
            except ValueError or IOError:
                print("Wrong data!")
                print("SET № is 0")
                choice = 0
                print("Success")

            try:
                row = rows[choice]
                Nanoparticles(row[0], complex(row[1]), row[2], row[3], row[4])
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
            conn = sqlite3.connect('data/nanoparticles_data.db')
            cur = conn.cursor()
            cur.execute("SELECT * FROM nanoparticles_examples")
            rows = cur.fetchall()

            if len(rows) == 0:
                print("No data found in database!(nanoparticles_examples)")
                return

            for row in rows:
                try:
                    Nanoparticles(row[0], complex(row[1]), row[2], row[3], row[4])
                except ValueError as ve:
                    print(f"Invalid value! {ve}")
        except sqlite3.Error as e:
            print(f"Error loading from database(npart): {e}")
