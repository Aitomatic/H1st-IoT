from __future__ import print_function

import os
import subprocess

from arimo_pw.runtime import params

from arimo.IoT.PredMaint import __path__


cmd_args = [
    os.path.join(__path__[0], 'bin', 'arimo-iot-pm'),
    params.PROJECT,
    'profile-data-flds',
    '--gen-tp', params.EQUIPMENT_GENERAL_TYPE,
    '--unq-tp-grp', params.EQUIPMENT_UNIQUE_TYPE_GROUP,
] + (params.TO_MONTHS.split(',')
     if params.TO_MONTHS
     else [])


cmd = ' '.join(cmd_args)

print('\n*** RUNNING {}... ***\n'.format(cmd))

subprocess.check_call(cmd_args)

print('\n*** {} DONE! ***\n'.format(cmd))