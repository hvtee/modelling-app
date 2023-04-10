import os
import pickle
import sqlite3

import numpy
from numpy import ndarray


class ImpedanceData:
    impedance_data = []

    def __init__(self, name, omega, ro, C, L, Z, Z_type):
        self.name = name
        self.omega = omega
        self.ro = ro
        self.C = C
        self.L = L
        self.Z = Z
        self.Z_type = Z_type

        ImpedanceData.impedance_data.append(self)

    @classmethod
    def create_impedance_data(cls):
        try:
            name = input("\nName of impedance data set: ")
            omega = numpy.linspace(6 * pow(10, 9), 6 * pow(10, 10), 540)
            ro = float(input("\nro: "))
            C = float(input("C(pF): ")) * pow(10, -12)
            L = float(input("L(pHn): ")) * pow(10, -12)

            user_choice = 0
            while user_choice not in ["1", "2", "3", "4"]:
                user_choice = str(input("""Choose impedance:
                           1 - consistent
                           2 - part_parallel
                           3 - consistent_parallel
                           4 - parallel
                           Input: """))
                print()

                if user_choice == "1":
                    Z = ro + 1j * (omega * L - (1 / (omega * C)))
                    Z_type = "consistent"
                elif user_choice == "2":
                    Z = (ro + 1j * omega * L) / (1j * omega * C * (
                            ro + 1j * (omega * L - (1 / (omega * C)))))
                    Z_type = "part_parallel"
                elif user_choice == "3":
                    Z = ro + (1 / (1j * omega * C + (1 / (1j * omega * L))))
                    Z_type = "consistent_parallel"
                elif user_choice == "4":
                    Z = 1 / (1 / ro + 1j * (omega * C - (1 / (omega * L))))
                    Z_type = "parallel"
                else:
                    print("Wrong choice!")
                    print("Z type set to consistent")
                    Z = ro + 1j * (omega * L - (1 / (omega * C)))
                    Z_type = "consistent"

                return cls(name, omega, ro, C, L, Z, Z_type)
        except ValueError as ve:
            print(f"Invalid value! {ve}")
        except IOError as ioe:
            print(f"IO error! {ioe}")

    @classmethod
    def show_impedance_data(cls):
        if len(ImpedanceData.impedance_data) == 0:
            return print("Impedance data is empty!")
        counter = 0
        for obj in cls.impedance_data:
            print("\nIMPEDANCE: ")
            print(f"Set No: {counter}")
            print(f"Name of impedance data set: {obj.name}")
            print(f"ro: {obj.ro}")
            print(f"C: {obj.C}")
            print(f"L: {obj.L}")
            print(f"Z: {obj.Z[0]} - {obj.Z[-1]}, {obj.Z_type}\n")
            counter += 1

    def save_to_db(self):
        try:
            ImpedanceData.show_impedance_data()
            conn = sqlite3.connect('impedance_data.db')
            cur = conn.cursor()
            cur.execute("""
                    CREATE TABLE IF NOT EXISTS impedance_data (
                        name TEXT UNIQUE,
                        omega BLOB,
                        ro REAL,
                        C REAL,
                        L REAL,
                        Z BLOB,
                        Z_type TEXT
                    )
                    """)
            values = (self.name, ndarray.tobytes(self.omega), self.ro, self.C,
                      self.L, ndarray.tobytes(numpy.asarray(self.Z)), self.Z_type)
            cur.execute('INSERT INTO impedance_data VALUES (?,?,?,?,?,?,?)', values)
            conn.commit()
            cur.close()
            conn.close()
            print("Saved with no errors.")
        except sqlite3.Error as e:
            print(f"Error saving to database: {e}")

    @classmethod
    def load_from_db(cls):
        try:
            conn = sqlite3.connect('impedance_data.db')
            cur = conn.cursor()
            cur.execute("""SELECT
                        name,
                        ro,
                        C,
                        L,
                        Z,
                        Z_type
                        FROM impedance_data""")
            rows = cur.fetchall()

            if len(rows) == 0:
                print("No data found in database!")
                return

            counter = 0
            for row in rows:
                print(f"\nSET № {counter}")
                print(f"name: {row[0]}")
                print(f"ro: {row[1]}")
                print(f"C: {row[2]}")
                print(f"L: {row[3]}")
                Z = numpy.frombuffer(row[4]).reshape(-1, 2)
                # print(f"Z: {Z[:, 0] + 1j * Z[:, 1]}")
                print(f"Z_type: {row[5]}")
                counter += 1

            cur.execute("""SELECT * FROM impedance_data""")
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
                Z = numpy.frombuffer(row[5]).reshape(-1, 2)
                ImpedanceData(row[0], numpy.frombuffer(row[1]), row[2], row[3], row[4],
                              Z[:, 0] + 1j * Z[:, 1], row[6])
            except ValueError:
                print("Error occurred in values of SET")

            cur.close()
            conn.close()
            print("Success")
        except sqlite3.Error as e:
            print(f"Error loading from database: {e}")
        except ValueError as ve:
            print(f"Invalid value! {ve}")

# Z_from_mu_consistent = ro + 1j * (ImpedanceData.impedance_data * L - (1 / (CommonData.omega * C)))
# Z_from_mu_part_parallel = (ro + 1j * CommonData.omega * L) / (
#         1j * CommonData.omega * C * (ro + 1j * (CommonData.omega * L - (1 / (CommonData.omega * C)))))
# Z_from_mu_consistent_parallel = ro + (1 / (1j * CommonData.omega * C + (1 / (1j * CommonData.omega * L))))
# Z_from_mu_parallel = 1 / (1 / ro + 1j * (CommonData.omega * C - (1 / (CommonData.omega * L))))
