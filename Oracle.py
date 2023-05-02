import cx_racle


def initialize_oracle_client(lib_dir):
    try:
        cx_Oracle.init_oracle_client(lib_dir=lib_dir)
        print("Successfully initialized Oracle client")
    except cx_Oracle.InterfaceError as e:
        if 'has already been initialized' in str(e):
            print("Oracle Client already initialized")
        else:
            print('Please check connection string or database status')
    except Exception as e:
        print('An error occurred while initializing the Oracle client:', e)


initialize_oracle_client('sds')
