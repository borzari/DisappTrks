from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.Color import *
from DisappTrks.StandardAnalysis.utilities import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
import copy
import os
import re

# Change this to False if you want to use IsolatedTracks instead of CandidateTracks in ntuples
# This is perhaps a weird place to put this switch, but this is the first DisappTrks module imported in protoConfig
UseCandidateTracks = True

# If this is true (76X and 80X) then prunedGenParticlePlusGeant will be used for hardInteractionMcparticles
# instead of prunedGenParticles
UseGeantDecays = (not os.environ['CMSSW_VERSION'].startswith('CMSSW_9_4_') and not os.environ['CMSSW_VERSION'].startswith('CMSSW_10_2_'))

print "########################################################################"
print "# Switching the following since the release is " + A_BRIGHT_BLUE + os.environ["CMSSW_VERSION"] + A_RESET + ":"
print "#"

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    print "# Datasets from: " + A_BRIGHT_CYAN + "miniAOD_80X_Samples" + A_RESET
    from DisappTrks.StandardAnalysis.miniAOD_80X_Samples import *
    print "# Backgorund samples from: " + A_BRIGHT_CYAN + "miniAODV2Samples" + A_RESET
    from DisappTrks.StandardAnalysis.miniAODV2Samples import dataset_names_bkgd
    dataset_names.update (dataset_names_bkgd)
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    if UseCandidateTracks:
        print "# Datasets from: " + A_BRIGHT_CYAN + "miniAOD_94X_Ntuples" + A_RESET
        print "# Background samples from: " + A_BRIGHT_CYAN + "miniAOD_94X_Ntuples" + A_RESET
        from DisappTrks.StandardAnalysis.miniAOD_94X_Ntuples import *
    else:
        print "# Datasets from: " + A_BRIGHT_CYAN + "miniAOD_94X_Samples" + A_RESET
        print "# Background samples from: " + A_BRIGHT_CYAN + "miniAOD_94X_Samples" + A_RESET + " (" + A_BRIGHT_YELLOW + "check for updated with MiniAODv2!" + A_RESET + ")"
        from DisappTrks.StandardAnalysis.miniAOD_94X_Samples import *
        lumi.update (CreateCompositeLumis (lumi_2017, '2017', 'BCDEF'))
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    print "# Datasets from: " + A_BRIGHT_CYAN + "miniAOD_102X_NTuples" + A_RESET
    print "# Background samples from: " + A_BRIGHT_CYAN + "miniAOD_102X_NTuples" + A_RESET + " (" + A_BRIGHT_YELLOW + "empty!" + A_RESET + ")"
    from DisappTrks.StandardAnalysis.miniAOD_102X_NTuples import *
else:
    print "# Datasets and background samples from: " + A_BRIGHT_CYAN + "miniAODV2Samples" + A_RESET
    from DisappTrks.StandardAnalysis.miniAODV2Samples import *

config_file = "config_cfg.py"

InputCondorArguments = {
    'request_memory': '2048MB',
    'request_cpus': '1',
}

datasetsBkgd = [
    'QCD',
    'DYJetsToLL',
    'ZJetsToNuNu',
    'VV',
    'SingleTop',
]
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    datasetsBkgd.append('TTJetsComposite')
else:
    datasetsBkgd.append('TTJets')

datasetsBkgdForMET = copy.deepcopy(datasetsBkgd)

datasetsBkgd.append ('WJetsToLNu')
datasetsBkgdForMET.append ('WJetsToLNu_HT')

datasetsSig = [
    'AMSB_chargino_100GeV_100cm_76X',
    'AMSB_chargino_100GeV_1000cm_76X',
    'AMSB_chargino_100GeV_10000cm_76X',

    'AMSB_chargino_200GeV_10cm_76X',
    'AMSB_chargino_200GeV_100cm_76X',
    'AMSB_chargino_200GeV_1000cm_76X',
    'AMSB_chargino_200GeV_10000cm_76X',

    'AMSB_chargino_300GeV_10cm_76X',
    'AMSB_chargino_300GeV_100cm_76X',
    'AMSB_chargino_300GeV_1000cm_76X',
    'AMSB_chargino_300GeV_10000cm_76X',

    'AMSB_chargino_400GeV_10cm_76X',
    'AMSB_chargino_400GeV_100cm_76X',
    'AMSB_chargino_400GeV_1000cm_76X',
    'AMSB_chargino_400GeV_10000cm_76X',

    'AMSB_chargino_500GeV_10cm_76X',
    'AMSB_chargino_500GeV_100cm_76X',
    'AMSB_chargino_500GeV_1000cm_76X',
    'AMSB_chargino_500GeV_10000cm_76X',

    'AMSB_chargino_600GeV_10cm_76X',
    'AMSB_chargino_600GeV_100cm_76X',
    'AMSB_chargino_600GeV_1000cm_76X',
    'AMSB_chargino_600GeV_10000cm_76X',

    'AMSB_chargino_700GeV_10cm_76X',
    'AMSB_chargino_700GeV_100cm_76X',
    'AMSB_chargino_700GeV_1000cm_76X',
    'AMSB_chargino_700GeV_10000cm_76X',

    'AMSB_chargino_800GeV_10cm_76X',
    'AMSB_chargino_800GeV_100cm_76X',
    'AMSB_chargino_800GeV_1000cm_76X',
    'AMSB_chargino_800GeV_10000cm_76X',

    'AMSB_chargino_900GeV_10cm_76X',
    'AMSB_chargino_900GeV_100cm_76X',
    'AMSB_chargino_900GeV_1000cm_76X',
    'AMSB_chargino_900GeV_10000cm_76X',
]

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    print "# Signal samples: " + A_BRIGHT_CYAN + "80X samples" + A_RESET
    for i in range (0, len (datasetsSig)):
        datasetsSig[i] = re.sub (r"(.*)_76X$", r"\1_80X", datasetsSig[i])
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    print "# Signal samples: " + A_BRIGHT_CYAN + "94X samples" + A_RESET
    for i in range (0, len (datasetsSig)):
        datasetsSig[i] = re.sub (r"(.*)_76X$", r"\1_94X", datasetsSig[i])
    for i in [100, 200, 300, 400, 500, 600, 700, 800, 900]:
        datasetsSig.append('AMSB_chargino_' + str(i) + 'GeV_1cm_94X')
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    print "# Signal samples: " + A_BRIGHT_CYAN + "102X samples" + A_RESET
    for i in range (0, len (datasetsSig)):
        datasetsSig[i] = re.sub (r"(.*)_76X$", r"\1_102X", datasetsSig[i])
    for i in [100, 200, 300, 400, 500, 600, 700, 800, 900]:
        datasetsSig.append('AMSB_chargino_' + str(i) + 'GeV_1cm_102X')
else:
    print "# Signal samples: " + A_BRIGHT_CYAN + "76X samples" + A_RESET

datasetsSigShort = copy.deepcopy(datasetsSig)

datasetsSigShort100 = datasetsSig[0:3]
datasetsSigShort200 = datasetsSig[3:7]
datasetsSigShort300 = datasetsSig[7:11]
datasetsSigShort400 = datasetsSig[11:15]
datasetsSigShort500 = datasetsSig[15:19]
datasetsSigShort600 = datasetsSig[19:23]
datasetsSigShort700 = datasetsSig[23:27]
datasetsSigShort800 = datasetsSig[27:31]
datasetsSigShort900 = datasetsSig[31:35]

addLifetimeReweighting (datasetsSig)

composite_dataset_definitions["allBkgd"] = datasetsBkgd

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    composite_dataset_definitions['DYJetsToLL'] = [
        'DYJetsToLL_50',
        'DYJetsToLL_5to50',
    ]
    composite_dataset_definitions['SingleTop'] = [
        'SingleTop_s_channel',
        'SingleTop_t_channel_top',
        'SingleTop_t_channel_antitop',
        'SingleTop_tW',
        'SingleTop_tbarW',
    ]
    composite_dataset_definitions['TTJetsComposite'] = [
        'TTJets_2L2Nu',
        'TTJets_SemiLeptonic',
        'TTJets_Hadronic',
    ]
    # no 5-10, 10-15 samples in 94X
    composite_dataset_definitions['QCD'] = [
        'QCD_15to30',
        'QCD_30to50',
        'QCD_50to80',
        'QCD_80to120',
        'QCD_120to170',
        'QCD_170to300',
        'QCD_300to470',
        'QCD_470to600',
        'QCD_600to800',
        'QCD_800to1000',
        'QCD_1000to1400',
        'QCD_1400to1800',
        'QCD_1800to2400',
        'QCD_2400to3200',
        'QCD_3200toInf',
    ]
    composite_dataset_definitions['ZJetsToNuNu'] = [
        'ZJetsToNuNu_HT100to200',
        'ZJetsToNuNu_HT200to400',
        'ZJetsToNuNu_HT400to600',
        'ZJetsToNuNu_HT600to800',
        'ZJetsToNuNu_HT800to1200',
        'ZJetsToNuNu_HT1200to2500',
        'ZJetsToNuNu_HT2500toInf',
    ]
    composite_dataset_definitions["VV"] = [
        #'WWToLNuQQ',
        #'WWToLNuLNu',
        'WW',
        'WZ',
        'ZZ',
        #'WG',
        #'ZG',
    ]
    composite_dataset_definitions["VG"] = [
        'WG',
        #'ZG',
    ]
    composite_dataset_definitions['WJetsToLNu_HT'] = [
        'WJetsToLNu_HT100to200',
        'WJetsToLNu_HT200to400',
        'WJetsToLNu_HT400to600',
        'WJetsToLNu_HT600to800',
        'WJetsToLNu_HT800to1200',
        #'WJetsToLNu_HT1200to2500',
        'WJetsToLNu_HT2500toInf',
    ]
else:
    composite_dataset_definitions['SingleTop'] = [
        'SingleTop_s_channel',
        'SingleTop_t_channel',
        'SingleTop_tW',
        'SingleTop_tbarW',
    ]
    composite_dataset_definitions["VV"] = [
        'WWToLNuQQ',
        'WWToLNuLNu',
        'WZ',
        'ZZ',
        'WG',
        'ZG',
    ]
    composite_dataset_definitions["VG"] = [
        'WG',
        'ZG',
    ]
    composite_dataset_definitions['WJetsToLNu_HT'] = [
        'WJetsToLNu_HT100to200',
        'WJetsToLNu_HT200to400',
        'WJetsToLNu_HT400to600',
        'WJetsToLNu_HT600toInf',
    ]

types["WW"] = "bgMC"
types["WZ"] = "bgMC"
types["ZZ"] = "bgMC"
types["VG"] = "bgMC"
types["VV"] = "bgMC"
types["allBkgd"] = "bkMC"

colors["WW"] = 390
colors["WZ"] = 393
colors["ZZ"] = 397
colors["VG"] = 400
colors["VV"] = 800
colors["allBkgd"] = 601

labels["DYJetsToLL_50"] = "Z#rightarrowll"
labels["DYJetsToLL"] = "Z#rightarrowll"
labels["DYJetsToNuNu"] = "Z#rightarrow#nu#bar{#nu}"
labels["WJetsToLNu"] = "W#rightarrowl#nu"
labels["WJetsToLNu_HT"] = "W#rightarrowl#nu"
labels["WW"] = "WW"
labels["WZ"] = "WZ"
labels["ZZ"] = "ZZ"
labels["VG"] = "V#gamma"
labels["VV"] = "Diboson"
labels["allBkgd"] = "Total bkgd"

# add dataset attributes for 2016BC and 2016DEFGH
for attribute in list (locals ()):
    if not isinstance (locals ()[attribute], dict) or attribute.startswith ("lumi"):
        continue
    newKeys = {}
    for a in locals ()[attribute]:
        if re.match (r".*2016B.*", a):
            b = re.sub (r"(.*)2016B(.*)", r"\g<1>2016BC\2", a)
            newKeys[b] = copy.deepcopy (locals ()[attribute][a])
            if isinstance (newKeys[b], str) and re.match (r".*2016B.*", newKeys[b]):
                newKeys[b] = re.sub (r"(.*)2016B(.*)", r"\g<1>2016B+C\2", newKeys[b])
        if re.match (r".*2016D.*", a):
            b = re.sub (r"(.*)2016D(.*)", r"\g<1>2016DEFGH\2", a)
            newKeys[b] = copy.deepcopy (locals ()[attribute][a])
            if isinstance (newKeys[b], str) and re.match (r".*2016D.*", newKeys[b]):
                newKeys[b] = re.sub (r"(.*)2016D(.*)", r"\g<1>2016D-H\2", newKeys[b])
    locals ()[attribute].update (newKeys)

# add dataset attributes for 2016 MC
for attribute in list (locals ()):
    if not isinstance (locals ()[attribute], dict) or attribute.startswith ("lumi") or attribute == "dataset_names":
        continue
    newKeys = {}
    for a in locals ()[attribute]:
        if re.match (r"DYJetsToLL_50", a) or re.match (r"WZ", a) or re.match (r"WZToLNuNuNu", a):
            b = re.sub (r"(.*)", r"\1_2016MC", a)
            newKeys[b] = copy.deepcopy (locals ()[attribute][a])
            if isinstance (newKeys[b], str) and attribute == "labels":
                newKeys[b] = re.sub (r"(.*)", r"\1 (2016 MC)", newKeys[b])
    locals ()[attribute].update (newKeys)
