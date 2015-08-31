import sqlite3 as lite

# Create database

conn = lite.connect('canadian_election.db')
cur = conn.cursor()
conn.text_factory = str

df.to_sql('fed_census', conn, index=False, index_label=None)

sql = "SELECT * FROM fed_census"

df2 = psql.read_sql(sql, conn)

sql = "SELECT Prov_Name, FED_Name, Characteristic, Total  \
        FROM fed_census \
        where Characteristic = 'Population in 2011' \
        group by Prov_Name, FED_Name, Characteristic, Total"

psql.read_sql(sql, conn)