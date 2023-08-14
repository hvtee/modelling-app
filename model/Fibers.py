import sqlite3
from model.sql import SQL


class Fibers:
    fibers_data = []

    def __init__(self, name, ro, C, L):
        self.name = name
        self.ro = ro
        self.C = C
        self.L = L

        Fibers.fibers_data.append(self)

    @classmethod
    def create_fibers_data(cls):
        try:
            name = input("\nName of impedance data set: ")
            ro = float(input("\nro: "))
            C = float(input("C(pF): ")) * pow(10, -12)
            L = float(input("L(pHn): ")) * pow(10, -12)

            return cls(name, ro, C, L)
        except ValueError as ve:
            print(f"Invalid value! {ve}")
        except IOError as ioe:
            print(f"IO error! {ioe}")

    @classmethod
    def show_fibers_data(cls):
        if len(Fibers.fibers_data) == 0:
            return print("Nanostructures data is empty!")
        counter = 0
        for obj in cls.fibers_data:
            print("\nNANOSTRUCTURES DATA: ")
            print(f"Set No: {counter}")
            print(f"Name of nanostructures data set: {obj.name}")
            print(f"ro: {obj.ro}")
            print(f"C: {obj.C}")
            print(f"L: {obj.L}")
            counter += 1

    def save_to_db(self):
        try:
            Fibers.show_fibers_data()
            conn = sqlite3.connect('data/nanostructures_data.db')
            cur = conn.cursor()
            cur.execute(SQL.sql_nstruct_create)
            values = (self.name, self.ro, self.C, self.L)
            cur.execute('INSERT INTO nanostructures_data VALUES (?,?,?,?)', values)
            conn.commit()
            cur.close()
            conn.close()
            print("Saved with no errors.")
        except sqlite3.Error as e:
            print(f"Error saving to database: {e}")

    @classmethod
    def load_from_db(cls):
        try:
            conn = sqlite3.connect('data/nanostructures_data.db')
            cur = conn.cursor()
            cur.execute(SQL.sql_nstruct_all)
            rows = cur.fetchall()

            if len(rows) == 0:
                print("No data found in database!(nanostructures_data)")
                return
            try:
                cur.execute(SQL.sql_nstruct_all)
                rows = cur.fetchall()
                for row in rows:
                    Fibers(row[0], row[1], row[2], row[3])
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
