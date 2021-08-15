#############################################################################
#
# Test
#
# Author:  Taruka Liyanagamage <liyanagamage.t@gmail.com>
# Date:    Aug 2021 (version 1.0)
#
# Description:
# ------------
# 
# Testing macros 
#
#
#
#
#===========================================================================

test:
	docker exec -it ${APP_CONTAINER} bash -c "pytest"