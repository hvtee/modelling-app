import os
import pickle
import sqlite3
import numpy
from numpy import ndarray


class CommonData:
    common_data = []

    def __init__(self, name, omega, mu_0, epsilon_0, mu_1, mu_2, sigma_1, sigma_2, c, a, d):
        try:
            # self.omega: float = 6 * pow(10, 9)
            self.name = name
            self.omega = omega
            self.mu_0 = mu_0
            self.epsilon_0 = epsilon_0
            self.mu_1 = mu_1
            self.mu_2 = mu_2
            self.sigma_1 = sigma_1
            self.sigma_2 = sigma_2
            self.c = c
            self.a = a
            self.d = d

            CommonData.common_data.append(self)
        except ValueError as ve:
            print(f"Invalid value! {ve}")
        except IOError as ioe:
            print(f"IO error! {ioe}")

    @classmethod
    def create_common_data(cls):
        try:
            name = input("\nName of common data set: ")
            omega = numpy.linspace(6 * pow(10, 9), 6 * pow(10, 10), 540)
            mu_0: float = 4 * 3.14 * pow(10, -7)
            epsilon_0 = 8.85 * pow(10, -12)
            mu_1 = complex(input("mu1(a-bj): "))
            mu_2 = complex(input("mu2(a-bj): "))
            sigma_1 = int(input("sigma1: "))
            sigma_2 = int(input("sigma2: "))
            c = float(input("c: "))
            a = int(input("a(nm): ")) * pow(10, -9)
            d = float(input("d(m): "))

            return cls(name, omega, mu_0, epsilon_0, mu_1, mu_2, sigma_1, sigma_2, c, a, d)
        except ValueError as ve:
            print(f"Invalid value! {ve}")
        except IOError as ioe:
            print(f"IO error! {ioe}")
        except AttributeError as ae:
            print(f"AE: {ae}")

    @classmethod
    def show_common_data(cls):
        if len(CommonData.common_data) == 0:
            return print("Common data is empty!")

        try:
            counter = 0
            for obj in cls.common_data:
                print("\nCOMMON:")
                print(f"SET No: {counter}")
                print(f"name: {obj.name}")
                print(f"omega: {obj.omega[0]} - {obj.omega[-1]}")
                print(f"mu0: {obj.mu_0}")
                print(f"mu1: {obj.mu_1}")
                print(f"mu2: {obj.mu_2}")
                print(f"c: {obj.c}")
                print(f"a: {obj.a}")
                print(f"d: {obj.d}")
                print(f"sigma1: {obj.sigma_1}")
                print(f"sigma2: {obj.sigma_2}")
                print(f"epsilon0: {obj.epsilon_0}")
                counter += 1
        except AttributeError as ae:
            print("AE")

    def save_to_db(self):
        try:
            CommonData.show_common_data()
            conn = sqlite3.connect('common_data.db')
            cur = conn.cursor()
            cur.execute("""
                    CREATE TABLE IF NOT EXISTS common_data (
                        name TEXT UNIQUE,
                        omega BLOB,
                        mu_0 REAL,
                        epsilon_0 REAL,
                         mu_1 TEXT,
                        mu_2 TEXT,
                        sigma_1 REAL,
                        sigma_2 REAL,
                        c REAL,
                        a REAL,
                        d REAL
                    )
                    """)
            values = (self.name, ndarray.tobytes(self.omega), self.mu_0, self.epsilon_0,
                      str(self.mu_1), str(self.mu_2), self.sigma_1, self.sigma_2,
                      self.c, self.a, self.d)
            cur.execute('INSERT INTO common_data VALUES (?,?,?,?,?,?,?,?,?,?,?)', values)
            conn.commit()
            cur.close()
            conn.close()
            print("Saved with no errors.")
        except sqlite3.Error as e:
            print(f"Error saving to database: {e}")

    @classmethod
    def load_from_db(cls):
        try:
            conn = sqlite3.connect('common_data.db')
            cur = conn.cursor()
            cur.execute("""SELECT 
                        name,
                        mu_0,
                        epsilon_0,
                        mu_1,
                        mu_2,
                        sigma_1,
                        sigma_2,
                        c,
                        a,
                        d  
                        FROM common_data""")
            rows = cur.fetchall()

            if len(rows) == 0:
                print("No data found in database!")
                return

            counter = 0
            for row in rows:
                print(f"\nSET № {counter}")
                print(f"name: {row[0]}")
                print(f"mu_0: {row[1]}")
                print(f"epsilon_0: {row[2]}")
                print(f"mu_1: {row[3]}")
                print(f"mu_2: {row[4]}")
                print(f"sigma_1: {row[5]}")
                print(f"sigma_2: {row[6]}")
                print(f"c: {row[7]}")
                print(f"a: {row[8]}")
                print(f"d: {row[9]}")
                counter += 1

            cur.execute("""SELECT * FROM common_data""")
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
                CommonData(row[0], numpy.frombuffer(row[1]), row[2], row[3], complex(row[4]),
                           complex(row[5]), row[6], row[7], row[8], row[9], row[10])
            except ValueError:
                print("Error occurred in values of SET")

            cur.close()
            conn.close()
            print("Success")
        except sqlite3.Error as e:
            print(f"Error loading from database: {e}")
        except ValueError as ve:
            print(f"Invalid value! {ve}")
