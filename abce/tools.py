# Copyright 2012 Davoud Taghawi-Nejad
#
# Module Author: Davoud Taghawi-Nejad
#
# ABCE is open-source software. If you are using ABCE for your research you are
# requested the quote the use of this software.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License and quotation of the
# author. You may obtain a copy of the License at
#       http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
""" This file contains functions to compare floating point variables to 0. All
variables in this simulation as in every computer programm are floating
point variables. Floating point variables are not exact. Therefore var_a == var_b
has no meaning. Further a variable that is var_c = 9.999999999999966e-30 is for our
purpose equal to zero, but var_c == 0 would lead to False.
:meth:`is_zero`, :meth:`is_positive` and :meth:`is_negative` work
around this problem by defining float epsilon and determine whether the variable is
sufficiently close to zero or not.

This file also defines the :exc:`tools.NotEnoughGoods`
"""
from sys import float_info
epsilon = 10000 * float_info.epsilon


def agent_name(group_name, idn):
    """
    Given a group name and a id-number it returns the
    agent_name of the individual agent with the number idn. A message sent to
    the agent_name, will be received by this individual agent
    """
    return '%s_%i:' % (group_name, idn)


def group_address(group_name):
    # given a group_name it returns a group address with which you can send a message
    # to a group. (group addresses are group names with a trailing ':'.)
    return '%s:' % group_name


def is_zero(x):
    """ checks whether a number is sufficiently close to zero. All variables
    in ABCE are floating point numbers. Due to the workings of floating point
    arithmetic. If x is 1.0*e^-100 so really close to 0, x == 0 will be false;
    is_zero will be true.
    """
    if - epsilon < x < epsilon:
        return True
    else:
        return False


def is_positive(x):
    """ checks whether a number is positive and sufficiently different from
    zero. All variables in ABCE are floating point numbers. Due to the workings
    of floating point arithmetic. If x is 1.0*e^-100 so really close to 0,
    x > 0 will be true, eventhough it is very very small;
    is_zero will be true.
    """
    if epsilon <= x:
        return True
    else:
        return False


def is_negative(x):
    """ see is positive """
    if x <= - epsilon:
        return True
    else:
        return False


class NotEnoughGoods(Exception):
    """ Methods raise this exception when the agent has less goods than needed

    These functions (self.produce, self.offer, self.sell, self.buy)
    should be encapsulated by a try except block::

     try:
        self.produce(...)
     except NotEnoughGoods:
        alternative_statements()

    """
    def __init__(self, _agent_name, good, amount_missing):
        self.good = good
        self.amount_missing = amount_missing
        self.name = _agent_name
        Exception.__init__(self)

    def __str__(self):
        return repr(self.name + " '" + str(self.amount_missing) + " of good '" + self.good + "' missing")
