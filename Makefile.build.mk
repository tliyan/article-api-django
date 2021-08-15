#############################################################################
#
# Build
#
# Author:  Taruka Liyanagamage <liyanagamage.t@gmail.com>
# Date:    Aug 2021 (version 1.0)
#
# Description:
# ------------
#
# Macros to build and lifecycle manage docker containers
#
#
#
#===========================================================================


.PHONY:
build:
	docker-compose build

.PHONY:
start-db:
	docker-compose up -d db

.PHONY:
start-app:
	docker-compose up article_api

.PHONY:
exec-app:
	docker exec -it ${APP_CONTAINER} bash

.PHONY:
exec-db:
	docker exec -it ${DB_CONTAINER} bash

.PHONY:
clean:
	docker-compose down
