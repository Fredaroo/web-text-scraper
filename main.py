import dbModule.dataArch as dbArch
import dbModule.dataSource as dbSrc
import scrpModule.scrpRequest as scReq


dbArch.initiate_connection()
print("[OK] Connection initiated")

# Querying for new data source:
query = input("Would you like to import a new data source? [yes/no]:")
if query == "yes":
    file_name = dbSrc.import_source()
    dbArch.import_data(file_name)
    data_size = dbArch.get_length()
    scReq.scrp_loop(data_size)
else:
    query = input("Would you like to continue where you left off? [yes/no]:")
    if query == "yes":
        query = input("Would you like to skip  a url? (advised on crash) [yes/no]: \n")
        if query == "yes":
            # Skip code +1
            fetched_length = dbArch.get_last_range()
            fetched_length = int(fetched_length) + 2
            scReq.set_initial_loc(fetched_length)
            print("[OK] Resuming url text extraction")
            data_size = dbArch.get_length()
            scReq.scrp_loop(data_size)
        elif query == "no":
            # Continue but do not skip
            fetched_length = dbArch.get_last_range()
            fetched_length = int(fetched_length) + 1
            scReq.set_initial_loc(fetched_length)
            print("[OK] Resuming url text extraction")
            data_size = dbArch.get_length()
            scReq.scrp_loop(data_size)
    else:
        print("[OK] Resuming url text extraction")
        data_size = dbArch.get_length()
        scReq.scrp_loop(data_size)

print("ended")
