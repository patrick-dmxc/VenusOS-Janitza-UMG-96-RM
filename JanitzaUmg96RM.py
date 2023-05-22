# VenusOS module for support of Janitza UMG 96 RM-E Analyzer - and maybe others
# 
# Community contribution by Patrick Grote
# Version 0.1 - 2023-05-22

import logging
import device
import probe
from register import *

log = logging.getLogger()

class Reg_u64b(Reg_num):
    def __init__(self, base, *args, **kwargs):
        super(Reg_u64b, self).__init__(base, 4, *args, **kwargs)
        self.coding = ('>Q', '>4H')
        self.scale = float(self.scale)
        
class Reg_f32b(Reg_num):
    def __init__(self, base, *args, **kwargs):
        super(Reg_f32b, self).__init__(base, 2, *args, **kwargs)
        self.coding = ('>f', '>2H')
        self.scale = float(self.scale)

class JANITZA_UMG_96RM(device.EnergyMeter):
    productid = 0xb017
    productname = 'Janitza UMG 96 RM-E'
    min_timeout = 1

    def __init__(self, *args):
        super(JANITZA_UMG_96RM, self).__init__(*args)
        log.info('Janitza Probing') 
        self.info_regs = [
            Reg_s16(756, '/HardwareVersion'),
            Reg_s16(750, '/FirmwareVersion'),
        ]

    def phase_regs(self, n):
        s = 0x0002 * (n - 1)
        return [
            Reg_f32b(19000 + s, '/Ac/L%d/Voltage' % n,        1, '%.1f V'),
            Reg_f32b(19012 + s, '/Ac/L%d/Current' % n,        1, '%.1f A'),
            Reg_f32b(19020 + s, '/Ac/L%d/Power' % n,          1, '%.0f W'),
            Reg_f32b(19062 + s, '/Ac/L%d/Energy/Forward' % n, 1000, '%.2f kWh'),
            Reg_f32b(19068 + s, '/Ac/L%d/Energy/Reverse' % n, 1000, '%.2f kWh'),
        ]


    def device_init(self):
        self.read_info()

        phases = 3

        regs = [
            Reg_f32b(19026, '/Ac/Power',          1, '%.0f W'),
            Reg_f32b(19018, '/Ac/Current',        1, '%.1f A'),
            Reg_f32b(19050, '/Ac/Frequency',      1, '%.1f Hz'),
            Reg_f32b(19068, '/Ac/Energy/Forward', 1000, '%.2f kWh'),
            Reg_f32b(19076, '/Ac/Energy/Reverse', 1000, '%.2f kWh'),
        ]


        for n in range(1, phases + 1):
            regs += self.phase_regs(n)

        self.data_regs = regs

    def get_ident(self):
        return 'cg_%s' % self.info['/Serial']


models = {
    30518: {
        'model':    'UMG96RM-E-RCM',
        'handler':  JANITZA_UMG_96RM,
    },
}

probe.add_handler(probe.ModelRegister(756, models,
                                      methods=['rtu','tcp'],
                                      rates=[115200],
                                      units=[1]))