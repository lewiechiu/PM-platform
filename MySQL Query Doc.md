# Usage of MySQL Query Document

## QueryALL
This function will return all of the results you sent into the api via *cmd* argument.

```{code}
q = MySQL_Query()
q.queryALL("SELECT * FROM db2019FP.Bugs;") # Returns "Bugs" table.
```

## Query1
This function will return only **one** result you sent into the api via *cmd* argument.

```{code}
q = MySQL_Query()
q.query1("SELECT * FROM db2019FP.Bugs;") 
# [('1', '2018-05-26 00:00:00', '2017-05-01 00:00:00', 'the different font size for monospace characters (the read window and beyond the edit window)', '164')]

```