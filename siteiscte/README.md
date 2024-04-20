# Django commands

Iniciar o servidor para poder aceder ao website
```shell
python manage.py runserver
```

Iniciar a consola do python com o django e correr o script 'test_db.pt'
```shell
python manage.py shell

exec(open('test_db.py', encoding='utf-8').read())
exit()
```

Para o django criar os ficheiros com as modificações dos modelos
```shell
python manage.py makemigrations
```

Para o django aplicar as migrações à base de dados
```shell
python manage.py migrate
```

Para ver o query que a migração vai executar
```shell
python manage.py sqlmigrate  <app_name> <migration_file_name>
```

Criação de um administrador (superuser) na linha de comandos
```shell
python manage.py createsuperuser --username=tony --email=antonio@iscte.pt
```

Página de admin
http://127.0.0.1:8000/admin