#!/bin/bash

echo HOST_ENV=$HOST_ENV >> api.env
echo SECRET_KEY=$SECRET_KEY >> api.env
echo DATABASE_URL=$DATABASE_URL >> api.env
echo SENTRY_INGEST=$SENTRY_INGEST >> api.env

echo POSTGRES_USER=$POSTGRES_USER >> db.env
echo POSTGRES_PASSWORD=$POSTGRES_PASSWORD >> db.env
echo POSTGRES_DB=$POSTGRES_DB >> db.env
