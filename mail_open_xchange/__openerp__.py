# -*- coding: utf-8 -*-
{
    'name': 'Open-Xchange Odoo',
    'version': '1.0',
    'category': 'Social Network',
    'sequence': 2,
    'summary': 'Discussions, Mailing Lists, News',
    'description': """
Open-Xchange Integration
=========================
This module is designed to be a standard open-xchange inbox inside Odoo to allow for the use of email inside the Odoo framework as an option alongside Odoo's own mail module.
I would like to slowly add features to this to further integrate Open-Xchange inside Odoo to allow for easier migration to Odoo for those that are not interested in using Odoo's default mail module to completely replace their emails.

Main Features
-------------
* Open-Xchange webmail interface inside Odoo.
* Multi-inbox handling by Open-Xchange.
* More features to be added later to further integrate Open-Xchange with Odoo.
    """,
    'author': 'Luke Branch',
    'website': 'https://github.com/OdooCommunityWidgets/IDEAS-FOR-MODULES/mail_open_xchange',
    'depends': ['base', 'base_setup', 'mail'],
    'data': [
        '',
    ],
    'installable': False,
    'application': True,
}
