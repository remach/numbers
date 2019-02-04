pg_dump -Fc --no-acl --no-owner -h localhost -U postgres Numbers >  Numbers.dump
:aws upload
heroku pg:backups:restore  https://s3-eu-west-1.amazonaws.com/f.noosferabank.obr.space/Numbers.dump DATABASE_URL