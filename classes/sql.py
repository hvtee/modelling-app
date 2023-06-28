class SQL:
    sql_npart_create = """CREATE TABLE IF NOT EXISTS nanoparticles_data (
                        name TEXT UNIQUE,
                        mu_2 TEXT,
                        sigma_2 REAL,
                        c REAL,
                        a REAL
                    )
                    """

    sql_npart_all = "SELECT name, mu_2, sigma_2, c, a FROM nanoparticles_data"

    sql_nstruct_create = """
                    CREATE TABLE IF NOT EXISTS nanostructures_data (
                        name TEXT UNIQUE,
                        ro REAL,
                        C REAL,
                        L REAL
                        )
                    """

    sql_nstruct_all = "SELECT name, ro, C, L FROM nanostructures_data"

    sql_envir_create = """CREATE TABLE IF NOT EXISTS environment_data (
                        name TEXT UNIQUE,
                        mu_1 TEXT,
                        sigma_1 REAL,
                        d REAL
                        )
                    """

    sql_envir_all = "SELECT name, mu_1, sigma_1, d FROM environment_data"
