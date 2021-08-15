#############################################################################
#
# Code Quality
#
# Author:  Taruka Liyanagamage <liyanagamage.t@gmail.com>
# Date:    Aug 2021 (version 1.0)
#
# Description:
# ------------
#
# Python App Code Quality Management Macros
#
#
#
#
#===========================================================================

.PHONY:
format:
	docker exec -it ${APP_CONTAINER} bash -c "python -m black app"