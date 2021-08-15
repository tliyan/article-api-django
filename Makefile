#############################################################################
#
# Global Makefile
#
# Author:  Taruka Liyanagamage <liyanagamage.t@gmail.com>
# Date:    Aug 2021 (version 1.0)
#
# Description:
# ------------
#
# Global makefile to run all sub-makefile macro files
#
#
#
#===========================================================================

## Imports
##==========================================================================

include Makefile.build.mk
include Makefile.app.mk
include Makefile.cq.mk
include Makefile.test.mk


#===========================================================================

## Global Variables
##==========================================================================
APP_CONTAINER := article_api
DB_CONTAINER := article_db
