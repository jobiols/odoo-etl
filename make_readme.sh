#!/usr/bin/env bash
##############################################################################
# Genera la documentacion de los modulos, requiere la instalacion de oca
# maintainers tools
# https://github.com/OCA/maintainer-tools
#
source /home/jobiols/.virtualenvs/oca/bin/activate
oca-gen-addon-readme \
	--org-name jobiols \
	--repo-name odoo-etl \
	--branch 12.0 \
	--addons-dir "$PWD" \
	--gen-html
