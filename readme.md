# DjangoTraining

```
docker-compose -f local.yml up --build -d --remove-orphans
```

```
docker-compose -f local.yml logs
```

### backup
```
docker-compose -f local.yml exec postgres backup
```

### backup list
```
docker-compose -f local.yml exec postgres backups
```

### restore
```
docker-compose -f local.yml exec postgres restore <backup_id>
```
```
docker-compose -f local.yml exec postgres restore backup_2023_12_19T19_47_08.sql.gz
```