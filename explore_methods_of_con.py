import SAP_HANA_connection as con

sap_con = con.sap_hana_connect( );
print(sap_con.conn.getaddress())


# ins_cur = sap_con.conn.cursor();
# sql = 'INSERT INTO "KIRAN_SCHEME"."ZBWMM"( WMNGR, WMTYP, STATUS ) VALUES(?,?,?)'
### Execute Many Example
# try:
#     ins_cur.executemany(sql, (('one', 'XGEN',True), ('TWO', 'XGEN',False )), batcherrors = True);
# except BaseException as err:
#     print(ins_cur.getrowsaffectedcounts())
# finally:
#     ins_cur.close();

### prepare and execute example
# cursor2 = ins_cur.prepare(sql, newcursor=True)
# cursor2.executemanyprepared([('three', 'XGEN',True), ('four', 'XGEN',False )])
# cursor2.close()
# ins_cur.close()

# cursor = sap_con.conn.cursor()
# sql_command = "select TITLE, FIRSTNAME, NAME from KIRAN_SCHEME.CUSTOMER;"
# cursor.execute(sql_command)
# print(cursor.fetchall())

# sql_create = "CREATE COLUMN TABLE KIRAN_SCHEME.SAMPLE_TABLE (" \
#             "ID INTEGER PRIMARY KEY, VALUE INTEGER , NAME CHAR (30) NOT NULL);"
#
# ary = []
# sql_insert = 'INSERT INTO "KIRAN_SCHEME"."SAMPLE_TABLE"( ID, VALUE, NAME ) VALUES(?,?,?)'
# for number in range(10):
#     ary.append((number,number,'Value '+str(number)))
#
# ins_cur = sap_con.conn.cursor();
# ins_cur.execute(sql_create);
# cursor2 = ins_cur.prepare(sql_insert, newcursor=True)
# cursor2.executemanyprepared(ary)
# cursor2.close()
# ins_cur.close()

cursor = sap_con.conn.cursor();
sql_command = "select ID, VALUE, NAME from KIRAN_SCHEME.SAMPLE_TABLE;"
cursor.execute(sql_command)
print(cursor.fetchall())
cursor.close()




