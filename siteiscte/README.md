# Django commands

Iniciar o servidor para poder aceder ao website
```shell
python3 manage.py runserver
```

Iniciar a consola do python com o django e correr o script 'test_db.pt'
```shell
python3 manage.py shell
exec(open('test_db.py', encoding='utf-8').read())
```

Para o django criar os ficheiros com as modificações dos modelos
```shell
python3 manage.py makemigrations
```

Para o django aplicar as migrações à base de dados
```shell
python3 manage.py migrate
```

Para ver o query que a migração vai executar
```shell
python3 manage.py sqlmigrate  <app_name> <migration_file_name>
```

