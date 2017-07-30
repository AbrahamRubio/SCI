#    Copyright (C) 2015 Alexandre Teyar

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
#    limitations under the License.


def get_valid_regs(returned_reg, regs):
    """
    Return the valid registers that can be used to store data.
    """
    valid_regs = []

    for reg in regs:
        if ((reg[0] == 'v') and (reg != returned_reg) and (int(reg[1:]) < 16)):
            valid_regs.append(reg)

    return valid_regs


def clean_reg_name(reg, list):
    """
    Clean the name of the registers by removing any characters contained in
    the inputted list.
    """
    for char in list:
        reg = reg.replace(char, '')

    return reg
