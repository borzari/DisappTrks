#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake' : {
        'N' : '1',
        'alpha' : '0.423370525738',
    },
    'Elec' : {
        'N' : '33',
        'alpha' : '0.142867612755',
    },
    'Muon' : {
        'N' : '12', # 8 (BCDE) * 1.4823110077656325 fixme
        'alpha' : '0.0353387365143',
    },
    'Tau' : {
        'N' : '7',
        'alpha' : '0.0522894893596',
    },
}

background_systematics = {
    'Fake_alpha_NLayers6plus' : { # error on alpha
        'value' : '1.01698139546',
        'background' : 'Fake',
    },
    'Elec_alpha_NLayers6plus' : { # error on alpha
        'value' : '1.01047519123',
        'background' : 'Elec',
    },
    'Muon_alpha_NLayers6plus' : { # error on alpha
        'value' : '1.00452879753',
        'background' : 'Muon',
    },
    'Tau_alpha_NLayers6plus' : { # error on alpha
        'value' : '1.17342348494',
        'background' : 'Tau',
    },



    'Fake_syst_NLayers6plus' : { # error on fake track rate assumption
        'value' : str (max (1.0 - 100.0 / 100.0, 1.0e-3)) + "/" + str (1.0 + 99.3 / 100.0),
        'background' : 'Fake',
    },
    'Elec_energy_NLayers6plus' : { # error on energy assumption
        'value' : str (1.0 + 11.7113892531 / 100.0),
        'background' : 'Elec',
    },
    'Tau_energy_NLayers6plus' : { # error on energy assumption
        'value' : str (1.0 + 16.8609344527 / 100.0),
        'background' : 'Tau',
    },
}
