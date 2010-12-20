# -*- coding: utf-8 -*-
#
# Copyright (c) 2010 Cidadanía Coop.
# Written by: Oscar Carballal Prego <info@oscarcp.com>
#
# This file is part of e-cidadania.
#
# e-cidadania is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# e-cidadania is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with e-cidadania. If not, see <http://www.gnu.org/licenses/>.

import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from userprofile.models import BaseProfile

PHONE_TYPE = (

    ('MO', _('Mobile')),
    ('FI', _('Fixed')),

)

GENDER = (

    ('M', _('Male')),
    ('F', _('Female')),

)

class UserProfile(BaseProfile):


    """
    Extends the default User profiles of Django.
    """
    #user = models.ForeignKey(User, unique=True)
    
    firstname = models.CharField(max_length=50, blank=True)
    surname = models.CharField(max_length=200, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER, blank=True)
    
    birthdate = models.DateField(default=datetime.date.today(), blank=True)
    
    # Maybe one day this will be replaced by a list of choices.
    province = models.CharField(_('Province'), max_length=50)
    municipality = models.CharField(_('Municipality'), max_length=50)
    
    # Detailed overview of the address
    address = models.CharField(_('Address'), max_length=100)
    address_number = models.CharField(_('Number'), max_length=3, blank=True,
                                      null=True)
    address_floor = models.CharField(_('Floor'), max_length=3)
    address_letter = models.CharField(_('Letter'), max_length=2, null=True,
                                      blank=True)
    
    nid = models.CharField(_('Identification document'), max_length=200,
                           null=True, blank=True)
    
    website = models.URLField(_('Website'), verify_exists=True, max_length=200,
                              null=True, blank=True,
                              help_text=_('The URL will be checked'))
    
    # Not required since User module automatically sets the register time.
    #registered = models.DateTimeField('Registered', auto_now_add=True)
    
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


class Phone(models.Model):


    """
    This model allows to put more than one phone in the user profile.
    """
    profile = models.ForeignKey(UserProfile)
    phone_type = models.CharField(_('Type'), choices=PHONE_TYPE,
                                  max_length=9)
    phone = models.CharField(_('Phone number'), max_length=9, null=True,
                             blank=True, help_text=_('9 digits maximum'))
