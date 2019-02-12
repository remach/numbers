"C:\Program Files\PostgreSQL\10\bin\pg_dump.exe" -Fc --no-acl --no-owner -h localhost -U postgres Numbers >  Numbers.dump
aws s3 cp Numbers.dump s3://f.noosferabank.obr.space --acl public-read
heroku pg:backups:restore --app space-obr-api-stage https://s3-eu-west-1.amazonaws.com/f.noosferabank.obr.space/Numbers.dump postgresql-silhouetted-77301 --confirm space-obr-api-stage