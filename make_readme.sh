#!/usr/bin/env bash
##############################################################################
# Genera la documentacion de los modulos, requiere la instalacion de oca
# maintainers tools
# https://github.com/OCA/maintainer-tools
#
source /opt/maintainer-tools/env/bin/activate
oca-gen-addon-readme \
	--org-name jobiols \
	--repo-name odoo-etl \
	--branch 12.0 \
	--addons-dir "$PWD" \
	--gen-html

# pylint {} --load-plugins=pylint_odoo -d C0114,C0115,C0116
# ejecutar pylint en cada repositorio
#find ./* -type d -exec pylint {} --load-plugins=pylint_odoo -d C8101 \;
