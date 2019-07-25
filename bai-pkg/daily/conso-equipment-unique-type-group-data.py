from __future__ import print_function

from datetime import date, timedelta
import os
import subprocess

from arimo_pw.runtime import params

from arimo.IoT.PredMaint import __path__


today = date.today()

cmd_args = [
    os.path.join(__path__[0], 'bin', 'arimo-iot-pm'),
    params.PROJECT,
    'conso-data',
    params.EQUIPMENT_GENERAL_TYPE, params.EQUIPMENT_UNIQUE_TYPE_GROUP,
    str(today - timedelta(days=1)), '--to', str(today)
]


cmd = ' '.join(cmd_args)

print('\n*** RUNNING {}... ***\n'.format(cmd))

subprocess.check_call(cmd_args)

print('\n*** {} DONE! ***\n'.format(cmd))