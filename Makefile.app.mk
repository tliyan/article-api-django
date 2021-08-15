#############################################################################
#
# App Management
#
# Author:  Taruka Liyanagamage <liyanagamage.t@gmail.com>
# Date:    Aug 2021 (version 1.0)
#
# Description:
# ------------
#
# Django App Lifecycle Management Macros
#
#
#
#===========================================================================

.PHONY:
configure-app: migrations admin

.PHONY:
migrations:
	docker exec -it ${APP_CONTAINER} bash -c "python ./app/manage.py makemigrations"
	docker exec -it ${APP_CONTAINER} bash -c "python ./app/manage.py migrate"

.PHONY:
admin:
	docker exec -it ${APP_CONTAINER} bash -c "python ./app/manage.py createsuperuser --noinput"