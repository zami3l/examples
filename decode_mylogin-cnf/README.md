Récupération login mysql 
===

L'utilisation de **mysql_config_editor** permet de créer un fichier (mylogin.cnf) chiffré contenant les paramètres de connexion à la base.

Cependant, nous pouvons très simplement déchiffrer pour récupérer ces informations.

Utilisation
---

Utilisation du fichier [config.py](https://github.com/dbcli/mycli/blob/master/mycli/config.py) de l'outil **[mycli](https://github.com/dbcli/mycli)**

```python
#!/usr/bin/python3
# coding : utf-8

#file : decode.py

import mycli, sys

output = mycli.open_mylogin_cnf(sys.argv[1])

print(output.readlines())
```

```bash
$ py decode.py [PATH:mylogin.cnf]
```