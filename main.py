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
else:
    print("[OK] Resuming url text extraction")

data_size = dbArch.get_length()
scReq.scrp_loop(data_size)
print("ended")
