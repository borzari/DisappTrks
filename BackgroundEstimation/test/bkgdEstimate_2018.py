#!/usr/bin/env python

import math, os, sys
from OSUT3Analysis.Configuration.Measurement import Measurement
from DisappTrks.BackgroundEstimation.bkgdEstimate import LeptonBkgdEstimate, FakeTrackBkgdEstimate
from DisappTrks.StandardAnalysis.plotUtilities import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
from ROOT import gROOT, TCanvas, TFile, TGraphErrors

gROOT.SetBatch() # I am Groot.

dirs = getUser()
canvas = TCanvas("c1", "c1",800,800)
setCanvasStyle(canvas)

background = "all"
if len(sys.argv) > 1:
    background = sys.argv[1]
background = background.upper()

nLayersWords = ["NLayers4", "NLayers5", "NLayers6plus"]
combineLayers = True
if len(sys.argv) > 2:
    nLayersWords = [sys.argv[2]]
    combineLayers = False

# '' will gives you Dataset_2018.root for the whole year
#runPeriods = ['A', B', 'C', 'D']
runPeriods = ['C']

nEstFake = {}
nEstElectron = {}
nEstMuon = {}
nEstTau = {}

nLeptons = {}
nTotal = {}

fakeSidebands = [(x * 0.05, (x + 1) * 0.05) for x in range(1, 10)]

stdout = sys.stdout
nullout = open("/dev/null", "w")

for runPeriod in runPeriods:

    if background == "FAKE" or background == "ALL":

        for nLayersWord in nLayersWords:

            print "********************************************************************************"
            print "performing fake track background estimate in search region(2018", runPeriod, "--", nLayersWord, ")"
            print "--------------------------------------------------------------------------------"

            fout = TFile.Open("fakeTrackBkgdEstimate_zToMuMu_2018" + runPeriod + "_" + nLayersWord + ".root", "recreate")

            fakeTrackBkgdEstimate = FakeTrackBkgdEstimate ()
            fakeTrackBkgdEstimate.addTFile (fout)
            fakeTrackBkgdEstimate.addLuminosityInInvPb (lumi["MET_2018" + runPeriod])
            #fakeTrackBkgdEstimate.addChannel  ("Basic3hits",      "ZtoMuMuDisTrkNoD0Cut3LayersVeryClean",          "SingleMu_2018"  +  runPeriod,  dirs['Brian']+"2018/fakeTrackBackgroundVeryClean_v2")
            fakeTrackBkgdEstimate.addChannel  ("Basic3hits",      "ZtoMuMuDisTrkNoD0CutNLayers4",          "SingleMu_2018"  +  runPeriod,  dirs['Andrew']+"2018/fakeTrackBackground_noD0")
            fakeTrackBkgdEstimate.addChannel  ("DisTrkInvertD0",  "ZtoMuMuDisTrkNoD0Cut"+nLayersWord,  "SingleMu_2018"  +  runPeriod,  dirs['Andrew']+"2018/fakeTrackBackground_noD0")
            fakeTrackBkgdEstimate.addChannel  ("Basic",           "BasicSelection",                       "MET_2018_directcopy"       +  runPeriod,  dirs['Brian']+"2018/fromRutgers/basicSelection_noDuplicates/")
            fakeTrackBkgdEstimate.addChannel  ("ZtoLL",           "ZtoMuMu",                              "SingleMu_2018"  +  runPeriod,  dirs['Andrew']+"2018/zToMuMu")

            print "********************************************************************************"
            print "Baseline sideband result ({:.2f}, {:.2f}) cm: ".format(fakeSidebands[0][0], fakeSidebands[0][1])
            fakeTrackBkgdEstimate.addMinD0 (fakeSidebands[0][0])
            fakeTrackBkgdEstimate.addMaxD0 (fakeSidebands[0][1])
            nEstFake[(nLayersWord, runPeriod)] = fakeTrackBkgdEstimate.printNest ()[0]
            fout.Close ()

            print "********************************************************************************"
            print "Mean result over sidebands: "
            nEstAllSidebands = Measurement(0, 0)
            pFakeAllSidebands = Measurement(0, 0)
            for sb in fakeSidebands:
                fakeTrackBkgdEstimate.addMinD0 (sb[0])
                fakeTrackBkgdEstimate.addMaxD0 (sb[1])
                sbResults = fakeTrackBkgdEstimate.printNest (verbose = False)
                nEstAllSidebands += sbResults[0]
                pFakeAllSidebands += sbResults[1]
                print '\t({:.2f}, {:.2f}: N_est = '.format(sb[0], sb[1]) + str(sbResults[0]) + ' ; P_fake = ' + str(sbResults[1])
            nEstAllSidebands /= len(fakeSidebands)
            pFakeAllSidebands /= len(fakeSidebands)
            print "N_est (mean): ", nEstAllSidebands
            print "P_fake (mean): ", pFakeAllSidebands
            print "********************************************************************************"
            print "\n\n"

            print "********************************************************************************"
            print "performing fake track background estimate with Z->ee selection in search region(2018", runPeriod, "--", nLayersWord, ")"
            print "--------------------------------------------------------------------------------"

            fout = TFile.Open("fakeTrackBkgdEstimate_zToEE_2018" + runPeriod + "_" + nLayersWord + ".root", "recreate")

            fakeTrackBkgdEstimate = FakeTrackBkgdEstimate ()
            fakeTrackBkgdEstimate.addTFile (fout)
            fakeTrackBkgdEstimate.addLuminosityInInvPb (lumi["MET_2018" + runPeriod])
            #fakeTrackBkgdEstimate.addChannel  ("Basic3hits",      "ZtoEEDisTrkNoD0Cut3LayersVeryClean",          "SingleEle_2018"  +  runPeriod,  dirs['Andrew']+"2018/fakeTrackSystematic_zToEE_superCleanTransferFactor")
            fakeTrackBkgdEstimate.addChannel  ("Basic3hits",      "ZtoEEDisTrkNoD0CutNLayers4",          "SingleEle_2018"  +  runPeriod,  dirs['Andrew']+"2018/fakeTrackSystematic_zToEE")
            fakeTrackBkgdEstimate.addChannel  ("DisTrkInvertD0",  "ZtoEEDisTrkNoD0Cut"+nLayersWord,  "SingleEle_2018"  +  runPeriod,  dirs['Andrew']+"2018/fakeTrackSystematic_zToEE")
            fakeTrackBkgdEstimate.addChannel  ("Basic",           "BasicSelection",                       "MET_2018_directcopy"       +  runPeriod,  dirs['Brian']+"2018/fromRutgers/basicSelection_noDuplicates/")
            fakeTrackBkgdEstimate.addChannel  ("ZtoLL",           "ZtoEE",                              "SingleEle_2018"  +  runPeriod,  dirs['Andrew']+"2018/zToEE")

            print "********************************************************************************"
            print "Baseline sideband result ({:.2f}, {:.2f}) cm: ".format(fakeSidebands[0][0], fakeSidebands[0][1])
            fakeTrackBkgdEstimate.addMinD0 (fakeSidebands[0][0])
            fakeTrackBkgdEstimate.addMaxD0 (fakeSidebands[0][1])
            fakeTrackBkgdEstimate.printNest ()
            fout.Close ()

            print "********************************************************************************"
            print "Mean result over sidebands: "
            nEstAllSidebands = Measurement(0, 0)
            pFakeAllSidebands = Measurement(0, 0)
            for sb in fakeSidebands:
                fakeTrackBkgdEstimate.addMinD0 (sb[0])
                fakeTrackBkgdEstimate.addMaxD0 (sb[1])
                sbResults = fakeTrackBkgdEstimate.printNest (verbose = False)
                nEstAllSidebands += sbResults[0]
                pFakeAllSidebands += sbResults[1]
                print '\t({:.2f}, {:.2f}: N_est = '.format(sb[0], sb[1]) + str(sbResults[0]) + ' ; P_fake = ' + str(sbResults[1])
            nEstAllSidebands /= len(fakeSidebands)
            pFakeAllSidebands /= len(fakeSidebands)
            print "N_est: ", nEstAllSidebands
            print "P_fake: ", pFakeAllSidebands
            print "********************************************************************************"
            print "\n\n"

    if background == "ELECTRON" or background == "LEPTON" or background == "ALL":

        if combineLayers:

            print "********************************************************************************"
            print "performing electron background estimate in search region(2018", runPeriod, "-- combined layers bins)"
            print "--------------------------------------------------------------------------------"

            fout = TFile.Open("electronBkgdEstimate_2018" + runPeriod + "_combinedBins.root", "recreate")

            electronBkgdEstimate = LeptonBkgdEstimate("electron")
            electronBkgdEstimate.addMetCut(120.0)
            electronBkgdEstimate.addTFile(fout)
            electronBkgdEstimate.addTCanvas(canvas)
            electronBkgdEstimate.addPrescaleFactor(lumi["MET_2018" + runPeriod] / lumi["EGamma_2018" + runPeriod])
            electronBkgdEstimate.addLuminosityInInvPb(lumi["MET_2018" + runPeriod])
            electronBkgdEstimate.addLuminosityLabel(str(round(lumi["EGamma_2018" + runPeriod] / 1000.0, 2)) + " fb^{-1}(13 TeV)")
            electronBkgdEstimate.addPlotLabel("EGamma 2018" + runPeriod)

            electronBkgdEstimate.addChannel("TagProbe",       "ZtoEleProbeTrk"             + nLayersWords[0], "EGamma_2018"        + runPeriod, dirs['Kai']+"2018/fromLPC/eleBkgdNoFilterBinnedLayers")
            electronBkgdEstimate.addChannel("TagProbePass",   "ZtoEleProbeTrkWithFilter"   + nLayersWords[0], "EGamma_rereco_2018" + runPeriod, dirs['Kai']+"2018/fromLPC/eleBkgdWithFilterBinnedLayers")
            electronBkgdEstimate.addChannel("TagProbePassSS", "ZtoEleProbeTrkWithSSFilter" + nLayersWords[0], "EGamma_rereco_2018" + runPeriod, dirs['Kai']+"2018/fromLPC/eleBkgdWithFilterBinnedLayers")
            electronBkgdEstimate.addChannel("TagPt35",        "ElectronTagPt55"            + nLayersWords[0], "EGamma_2018"        + runPeriod, dirs['Kai']+"2018/fromLPC/electronControlRegionBinnedLayers")
            electronBkgdEstimate.addChannel("TagPt35MetTrig", "ElectronTagPt55MetTrig"     + nLayersWords[0], "EGamma_2018"        + runPeriod, dirs['Kai']+"2018/fromLPC/electronControlRegionBinnedLayers")
        
            for iBin in range(1, len(nLayersWords)):
            	electronBkgdEstimate.addChannel("TagProbe",       "ZtoEleProbeTrk"             + nLayersWords[iBin], "EGamma_2018"        + runPeriod, dirs['Kai']+"2018/fromLPC/eleBkgdNoFilterBinnedLayers")
            	electronBkgdEstimate.addChannel("TagProbePass",   "ZtoEleProbeTrkWithFilter"   + nLayersWords[iBin], "EGamma_rereco_2018" + runPeriod, dirs['Kai']+"2018/fromLPC/eleBkgdWithFilterBinnedLayers")
            	electronBkgdEstimate.addChannel("TagProbePassSS", "ZtoEleProbeTrkWithSSFilter" + nLayersWords[iBin], "EGamma_rereco_2018" + runPeriod, dirs['Kai']+"2018/fromLPC/eleBkgdWithFilterBinnedLayers")
            	electronBkgdEstimate.addChannel("TagPt35",        "ElectronTagPt55"            + nLayersWords[iBin], "EGamma_2018"        + runPeriod, dirs['Kai']+"2018/fromLPC/electronControlRegionBinnedLayers")
            	electronBkgdEstimate.addChannel("TagPt35MetTrig", "ElectronTagPt55MetTrig"     + nLayersWords[iBin], "EGamma_2018"        + runPeriod, dirs['Kai']+"2018/fromLPC/electronControlRegionBinnedLayers")

            electronBkgdEstimate.addUseHistogramsForPpassMetTriggers(False) # use offline quantities instead of online
            electronBkgdEstimate.addRebinFactor(4)

            print "********************************************************************************"

            nEstElectron[("combinedBins", runPeriod)] = electronBkgdEstimate.printNest()
            electronBkgdEstimate.printPpassVetoTagProbe()

            print "********************************************************************************"

            fout.Close()

            print "\n\n"

        for nLayersWord in nLayersWords:

            print "********************************************************************************"
            print "performing electron background estimate in search region(2018", runPeriod, "--", nLayersWord, ")"
            print "--------------------------------------------------------------------------------"

            fout = TFile.Open("electronBkgdEstimate_2018" + runPeriod + "_" + nLayersWord + ".root", "recreate")

            electronBkgdEstimate = LeptonBkgdEstimate("electron")
            electronBkgdEstimate.addMetCut(120.0)
            electronBkgdEstimate.addTFile(fout)
            electronBkgdEstimate.addTCanvas(canvas)
            electronBkgdEstimate.addPrescaleFactor(lumi["MET_2018" + runPeriod] / lumi["EGamma_2018" + runPeriod])
            electronBkgdEstimate.addLuminosityInInvPb(lumi["MET_2018" + runPeriod])
            electronBkgdEstimate.addLuminosityLabel(str(round(lumi["EGamma_2018" + runPeriod] / 1000.0, 2)) + " fb^{-1}(13 TeV)")
            electronBkgdEstimate.addPlotLabel("EGamma 2018" + runPeriod)

            electronBkgdEstimate.addChannel("TagProbe",       "ZtoEleProbeTrk"             + nLayersWord, "EGamma_2018"        + runPeriod, dirs['Kai']+"2018/fromLPC/eleBkgdNoFilterBinnedLayers")
            electronBkgdEstimate.addChannel("TagProbePass",   "ZtoEleProbeTrkWithFilter"   + nLayersWord, "EGamma_rereco_2018" + runPeriod, dirs['Kai']+"2018/fromLPC/eleBkgdWithFilterBinnedLayers")
            electronBkgdEstimate.addChannel("TagProbePassSS", "ZtoEleProbeTrkWithSSFilter" + nLayersWord, "EGamma_rereco_2018" + runPeriod, dirs['Kai']+"2018/fromLPC/eleBkgdWithFilterBinnedLayers")
            electronBkgdEstimate.addChannel("TagPt35",        "ElectronTagPt55"            + nLayersWord, "EGamma_2018"        + runPeriod, dirs['Kai']+"2018/fromLPC/electronControlRegionBinnedLayers")
            electronBkgdEstimate.addChannel("TagPt35MetTrig", "ElectronTagPt55MetTrig"     + nLayersWord, "EGamma_2018"        + runPeriod, dirs['Kai']+"2018/fromLPC/electronControlRegionBinnedLayers")
        
            electronBkgdEstimate.addUseHistogramsForPpassMetTriggers(False) # use offline quantities instead of online
            electronBkgdEstimate.addRebinFactor(4)

            print "********************************************************************************"

            nEstElectron[(nLayersWord, runPeriod)] = electronBkgdEstimate.printNest()
            electronBkgdEstimate.printPpassVetoTagProbe()

            print "********************************************************************************"

            fout.Close()

            print "\n\n"

    if background == "MUON" or background == "LEPTON" or background == "ALL":

        if combineLayers:

            print "********************************************************************************"
            print "performing muon background estimate in search region(2018", runPeriod, "-- combined layer bins)"
            print "--------------------------------------------------------------------------------"

            fout = TFile.Open("muonBkgdEstimate_2018" + runPeriod + "_combinedBins.root", "recreate")

            muonBkgdEstimate = LeptonBkgdEstimate("muon")
            muonBkgdEstimate.addMetCut(120.0)
            muonBkgdEstimate.addTFile(fout)
            muonBkgdEstimate.addTCanvas(canvas)
            muonBkgdEstimate.addPrescaleFactor(lumi["MET_2018" + runPeriod] / lumi["SingleMuon_2018" + runPeriod])
            muonBkgdEstimate.addLuminosityInInvPb(lumi["MET_2018" + runPeriod])
            muonBkgdEstimate.addLuminosityLabel(str(round(lumi["SingleMuon_2018" + runPeriod] / 1000.0, 2)) + " fb^{-1}(13 TeV)")
            muonBkgdEstimate.addPlotLabel("SingleMuon 2018" + runPeriod)

            muonBkgdEstimate.addChannel("TagProbe",       "ZtoMuProbeTrk"             + nLayersWords[0], "SingleMu_2018"        + runPeriod, dirs['Brian'] + "2018/muonBackground_" + nLayersWords[0])
            muonBkgdEstimate.addChannel("TagProbePass",   "ZtoMuProbeTrkWithFilter"   + nLayersWords[0], "SingleMu_rereco_2018" + runPeriod, dirs['Brian'] + "2018/muonBackground_" + nLayersWords[0])
            muonBkgdEstimate.addChannel("TagProbePassSS", "ZtoMuProbeTrkWithSSFilter" + nLayersWords[0], "SingleMu_rereco_2018" + runPeriod, dirs['Brian'] + "2018/muonBackground_" + nLayersWords[0])
            muonBkgdEstimate.addChannel("TagPt35",        "MuonTagPt55"               + nLayersWords[0], "SingleMu_2018"        + runPeriod, dirs['Brian'] + "2018/fromLPC/muonControlRegion")
            muonBkgdEstimate.addChannel("TagPt35MetTrig", "MuonTagPt55MetTrig"        + nLayersWords[0], "SingleMu_2018"        + runPeriod, dirs['Brian'] + "2018/fromLPC/muonControlRegion")

            for iBin in range(1, len(nLayersWords)):
                muonBkgdEstimate.appendChannel("TagProbe",       "ZtoMuProbeTrk"             + nLayersWords[iBin], "SingleMu_2018"        + runPeriod, dirs['Brian'] + "2018/muonBackground_" + nLayersWords[iBin])
                muonBkgdEstimate.appendChannel("TagProbePass",   "ZtoMuProbeTrkWithFilter"   + nLayersWords[iBin], "SingleMu_rereco_2018" + runPeriod, dirs['Brian'] + "2018/muonBackground_" + nLayersWords[iBin])
                muonBkgdEstimate.appendChannel("TagProbePassSS", "ZtoMuProbeTrkWithSSFilter" + nLayersWords[iBin], "SingleMu_rereco_2018" + runPeriod, dirs['Brian'] + "2018/muonBackground_" + nLayersWords[iBin])
                muonBkgdEstimate.appendChannel("TagPt35",        "MuonTagPt55"               + nLayersWords[iBin], "SingleMu_2018"        + runPeriod, dirs['Brian'] + "2018/fromLPC/muonControlRegion")
                muonBkgdEstimate.appendChannel("TagPt35MetTrig", "MuonTagPt55MetTrig"        + nLayersWords[iBin], "SingleMu_2018"        + runPeriod, dirs['Brian'] + "2018/fromLPC/muonControlRegion")

            muonBkgdEstimate.addUseHistogramsForPpassMetTriggers(False) # use offline quantities instead of online
            muonBkgdEstimate.addRebinFactor(4)

            print "********************************************************************************"

            nEstMuon[("combinedBins", runPeriod)] = muonBkgdEstimate.printNest()
            muonBkgdEstimate.printPpassVetoTagProbe()

            combinedPpassMetCut = muonBkgdEstimate.getPpassMetCut()
            combinedPpassMetTriggers, combinedTriggerEfficiency = muonBkgdEstimate.getPpassMetTriggers()

            print "********************************************************************************"

            fout.Close()

            print "\n\n"

        for nLayersWord in nLayersWords:

            print "********************************************************************************"
            print "performing muon background estimate in search region(2018", runPeriod, "--", nLayersWord, ")"
            print "--------------------------------------------------------------------------------"

            fout = TFile.Open("muonBkgdEstimate_2018" + runPeriod + "_" + nLayersWord + ".root", "recreate")

            muonBkgdEstimate = LeptonBkgdEstimate("muon")
            muonBkgdEstimate.addMetCut(120.0)
            muonBkgdEstimate.addTFile(fout)
            muonBkgdEstimate.addTCanvas(canvas)
            muonBkgdEstimate.addPrescaleFactor(lumi["MET_2018" + runPeriod] / lumi["SingleMuon_2018" + runPeriod])
            muonBkgdEstimate.addLuminosityInInvPb(lumi["MET_2018" + runPeriod])
            muonBkgdEstimate.addLuminosityLabel(str(round(lumi["SingleMuon_2018" + runPeriod] / 1000.0, 2)) + " fb^{-1}(13 TeV)")
            muonBkgdEstimate.addPlotLabel("SingleMuon 2018" + runPeriod)

            muonBkgdEstimate.addChannel("TagProbe",       "ZtoMuProbeTrk"             + nLayersWord, "SingleMu_2018"        + runPeriod, dirs['Brian'] + "2018/muonBackground_" + nLayersWord)
            muonBkgdEstimate.addChannel("TagProbePass",   "ZtoMuProbeTrkWithFilter"   + nLayersWord, "SingleMu_rereco_2018" + runPeriod, dirs['Brian'] + "2018/muonBackground_" + nLayersWord)
            muonBkgdEstimate.addChannel("TagProbePassSS", "ZtoMuProbeTrkWithSSFilter" + nLayersWord, "SingleMu_rereco_2018" + runPeriod, dirs['Brian'] + "2018/muonBackground_" + nLayersWord)
            muonBkgdEstimate.addChannel("TagPt35",        "MuonTagPt55"               + nLayersWord, "SingleMu_2018"        + runPeriod, dirs['Brian'] + "2018/fromLPC/muonControlRegion")
            muonBkgdEstimate.addChannel("TagPt35MetTrig", "MuonTagPt55MetTrig"        + nLayersWord, "SingleMu_2018"        + runPeriod, dirs['Brian'] + "2018/fromLPC/muonControlRegion")

            muonBkgdEstimate.addUseHistogramsForPpassMetTriggers(False) # use offline quantities instead of online
            muonBkgdEstimate.addRebinFactor(4)

            print "********************************************************************************"

            nEstMuon[(nLayersWord, runPeriod)] = muonBkgdEstimate.printNest()
            muonBkgdEstimate.printPpassVetoTagProbe()

            print "********************************************************************************"

            if nLayersWord == "NLayers4" or nLayersWord == "NLayers5":
                print "using the combined 4/5/6+ layers sample for Poffline and Ptrigger:"
                muonBkgdEstimate.printNestCombinedMet(combinedPpassMetCut, combinedPpassMetTriggers)

            print "********************************************************************************"

            fout.Close()

            print "\n\n"

    if background == "TAU" or background == "LEPTON" or background == "ALL":

        if combineLayers:

            print "********************************************************************************"
            print "performing tau background estimate in search region(2018", runPeriod, "-- combined layer bins)"
            print "--------------------------------------------------------------------------------"

            fout = TFile.Open("tauBkgdEstimate_2018" + runPeriod + "_combinedBins.root", "recreate")

            tauBkgdEstimate = LeptonBkgdEstimate("tau")
            tauBkgdEstimate.addMetCut(120.0)
            tauBkgdEstimate.addTFile(fout)
            tauBkgdEstimate.addTCanvas(canvas)
            tauBkgdEstimate.addPrescaleFactor(lumi["MET_2018" + runPeriod] / lumi["HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_v*"]["Tau_2018" + runPeriod])
            tauBkgdEstimate.addLuminosityInInvPb(lumi["MET_2018" + runPeriod])
            tauBkgdEstimate.addLuminosityLabel(str(round(lumi["HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_v*"]["Tau_2018" + runPeriod] / 1000.0, 2)) + " fb^{-1}(13 TeV)")
            tauBkgdEstimate.addPlotLabel("Tau 2018" + runPeriod)
            
            tauBkgdEstimate.addChannel("TagProbe",         "ZtoTauToMuProbeTrk"              + nLayersWords[0], "SingleMu_2018"         + runPeriod, dirs['Brian']+"2018/fromLPC/zToTauToMuBkgd"  + nLayersWords[0])
            tauBkgdEstimate.addChannel("TagProbePass",     "ZtoTauToMuProbeTrkWithFilter"    + nLayersWords[0], "SingleMu_rereco_2018"  + runPeriod, dirs['Brian']+"2018/fromLPC/zToTauToMuBkgd"  + nLayersWords[0])
            tauBkgdEstimate.addChannel("TagProbePassSS",   "ZtoTauToMuProbeTrkWithSSFilter"  + nLayersWords[0], "SingleMu_rereco_2018"  + runPeriod, dirs['Brian']+"2018/fromLPC/zToTauToMuBkgd"  + nLayersWords[0])
            tauBkgdEstimate.addChannel("TagProbe1",        "ZtoTauToEleProbeTrk"             + nLayersWords[0], "SingleEle_2018"        + runPeriod, dirs['Brian']+"2018/fromLPC/zToTauToEleBkgd" + nLayersWords[0])
            tauBkgdEstimate.addChannel("TagProbePass1",    "ZtoTauToEleProbeTrkWithFilter"   + nLayersWords[0], "SingleEle_rereco_2018" + runPeriod, dirs['Brian']+"2018/fromLPC/zToTauToEleBkgd" + nLayersWords[0])
            tauBkgdEstimate.addChannel("TagProbePassSS1",  "ZtoTauToEleProbeTrkWithSSFilter" + nLayersWords[0], "SingleEle_rereco_2018" + runPeriod, dirs['Brian']+"2018/fromLPC/zToTauToEleBkgd" + nLayersWords[0])
            tauBkgdEstimate.addChannel("TagPt35",          "TauTagPt55"                      + nLayersWords[0], "Tau_2018"              + runPeriod, dirs['Brian']+"2018/fromLPC/tauControlRegionBinnedHits_v2")
            tauBkgdEstimate.addChannel("TagPt35MetTrig",   "TauTagPt55MetTrig"               + nLayersWords[0], "Tau_2018"              + runPeriod, dirs['Brian']+"2018/fromLPC/tauControlRegionBinnedHits_v2")
            tauBkgdEstimate.addChannel("TrigEffDenom",     "ElectronTagPt55"                 + nLayersWords[0], "SingleEle_2018"        + runPeriod, dirs['Brian']+"2018/fromLPC/electronControlRegionBinnedLayers")
            tauBkgdEstimate.addChannel("TrigEffNumer",     "ElectronTagPt55MetTrig"          + nLayersWords[0], "SingleEle_2018"        + runPeriod, dirs['Brian']+"2018/fromLPC/electronControlRegionBinnedLayers")
            tauBkgdEstimate.addChannel("TagPt35MetL1Trig", "TauTagPt55"                      + nLayersWords[0], "Tau_2018"              + runPeriod, dirs['Brian']+"2018/fromLPC/tauControlRegionBinnedHits")

            for iBin in range(1, len(nLayersWords)):
                tauBkgdEstimate.appendChannel("TagProbe",         "ZtoTauToMuProbeTrk"              + nLayersWords[iBin], "SingleMu_2018"         + runPeriod, dirs['Brian']+"2018/fromLPC/zToTauToMuBkgd"  + nLayersWords[iBin])
                tauBkgdEstimate.appendChannel("TagProbePass",     "ZtoTauToMuProbeTrkWithFilter"    + nLayersWords[iBin], "SingleMu_rereco_2018"  + runPeriod, dirs['Brian']+"2018/fromLPC/zToTauToMuBkgd"  + nLayersWords[iBin])
                tauBkgdEstimate.appendChannel("TagProbePassSS",   "ZtoTauToMuProbeTrkWithSSFilter"  + nLayersWords[iBin], "SingleMu_rereco_2018"  + runPeriod, dirs['Brian']+"2018/fromLPC/zToTauToMuBkgd"  + nLayersWords[iBin])
                tauBkgdEstimate.appendChannel("TagProbe1",        "ZtoTauToEleProbeTrk"             + nLayersWords[iBin], "SingleEle_2018"        + runPeriod, dirs['Brian']+"2018/fromLPC/zToTauToEleBkgd" + nLayersWords[iBin])
                tauBkgdEstimate.appendChannel("TagProbePass1",    "ZtoTauToEleProbeTrkWithFilter"   + nLayersWords[iBin], "SingleEle_rereco_2018" + runPeriod, dirs['Brian']+"2018/fromLPC/zToTauToEleBkgd" + nLayersWords[iBin])
                tauBkgdEstimate.appendChannel("TagProbePassSS1",  "ZtoTauToEleProbeTrkWithSSFilter" + nLayersWords[iBin], "SingleEle_rereco_2018" + runPeriod, dirs['Brian']+"2018/fromLPC/zToTauToEleBkgd" + nLayersWords[iBin])
                tauBkgdEstimate.appendChannel("TagPt35",          "TauTagPt55"                      + nLayersWords[iBin], "Tau_2018"              + runPeriod, dirs['Brian']+"2018/fromLPC/tauControlRegionBinnedHits_v2")
                tauBkgdEstimate.appendChannel("TagPt35MetTrig",   "TauTagPt55MetTrig"               + nLayersWords[iBin], "Tau_2018"              + runPeriod, dirs['Brian']+"2018/fromLPC/tauControlRegionBinnedHits_v2")
                tauBkgdEstimate.appendChannel("TrigEffDenom",     "ElectronTagPt55"                 + nLayersWords[iBin], "SingleEle_2018"        + runPeriod, dirs['Brian']+"2018/fromLPC/electronControlRegionBinnedLayers")
                tauBkgdEstimate.appendChannel("TrigEffNumer",     "ElectronTagPt55MetTrig"          + nLayersWords[iBin], "SingleEle_2018"        + runPeriod, dirs['Brian']+"2018/fromLPC/electronControlRegionBinnedLayers")
                tauBkgdEstimate.appendChannel("TagPt35MetL1Trig", "TauTagPt55"                      + nLayersWords[iBin], "Tau_2018"              + runPeriod, dirs['Brian']+"2018/fromLPC/tauControlRegionBinnedHits")

            tauBkgdEstimate.addUseHistogramsForPpassMetTriggers(False) # temporary measure
            tauBkgdEstimate.addRebinFactor(8)

            print "********************************************************************************"

            nEstTau[("combinedBins", runPeriod)] = tauBkgdEstimate.printNest()
            tauBkgdEstimate.printPpassVetoTagProbe()

            combinedPpassMetCut = tauBkgdEstimate.getPpassMetCut()
            combinedPpassMetTriggers, combinedTriggerEfficiency = tauBkgdEstimate.getPpassMetTriggers()

            print "********************************************************************************"

            if nLayersWord == "NLayers4" or nLayersWord == "NLayers5":
                print "using the combined 4/5/6+ layers sample for Poffline and Ptrigger:"
                tauBkgdEstimate.printNestCombinedMet(combinedPpassMetCut, combinedPpassMetTriggers)

            print "********************************************************************************"
            
            fout.Close()

            print "\n\n"

        for nLayersWord in nLayersWords:

            print "********************************************************************************"
            print "performing tau background estimate in search region(2018", runPeriod, "--", nLayersWord, ")"
            print "--------------------------------------------------------------------------------"

            fout = TFile.Open("tauBkgdEstimate_2018" + runPeriod + "_" + nLayersWord + ".root", "recreate")

            tauBkgdEstimate = LeptonBkgdEstimate("tau")
            tauBkgdEstimate.addMetCut(120.0)
            tauBkgdEstimate.addTFile(fout)
            tauBkgdEstimate.addTCanvas(canvas)
            tauBkgdEstimate.addPrescaleFactor(lumi["MET_2018" + runPeriod] / lumi["HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_v*"]["Tau_2018" + runPeriod])
            tauBkgdEstimate.addLuminosityInInvPb(lumi["MET_2018" + runPeriod])
            tauBkgdEstimate.addLuminosityLabel(str(round(lumi["HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_v*"]["Tau_2018" + runPeriod] / 1000.0, 2)) + " fb^{-1}(13 TeV)")
            tauBkgdEstimate.addPlotLabel("Tau 2018" + runPeriod)
            
            tauBkgdEstimate.addChannel("TagProbe",         "ZtoTauToMuProbeTrk"              + nLayersWord, "SingleMu_2018"         + runPeriod, dirs['Brian']+"2018/fromLPC/zToTauToMuBkgd"  + nLayersWord)
            tauBkgdEstimate.addChannel("TagProbePass",     "ZtoTauToMuProbeTrkWithFilter"    + nLayersWord, "SingleMu_rereco_2018"  + runPeriod, dirs['Brian']+"2018/fromLPC/zToTauToMuBkgd"  + nLayersWord)
            tauBkgdEstimate.addChannel("TagProbePassSS",   "ZtoTauToMuProbeTrkWithSSFilter"  + nLayersWord, "SingleMu_rereco_2018"  + runPeriod, dirs['Brian']+"2018/fromLPC/zToTauToMuBkgd"  + nLayersWord)
            tauBkgdEstimate.addChannel("TagProbe1",        "ZtoTauToEleProbeTrk"             + nLayersWord, "SingleEle_2018"        + runPeriod, dirs['Brian']+"2018/fromLPC/zToTauToEleBkgd" + nLayersWord)
            tauBkgdEstimate.addChannel("TagProbePass1",    "ZtoTauToEleProbeTrkWithFilter"   + nLayersWord, "SingleEle_rereco_2018" + runPeriod, dirs['Brian']+"2018/fromLPC/zToTauToEleBkgd" + nLayersWord)
            tauBkgdEstimate.addChannel("TagProbePassSS1",  "ZtoTauToEleProbeTrkWithSSFilter" + nLayersWord, "SingleEle_rereco_2018" + runPeriod, dirs['Brian']+"2018/fromLPC/zToTauToEleBkgd" + nLayersWord)
            tauBkgdEstimate.addChannel("TagPt35",          "TauTagPt55"                      + nLayersWord, "Tau_2018"              + runPeriod, dirs['Brian']+"2018/fromLPC/tauControlRegionBinnedHits_v2")
            tauBkgdEstimate.addChannel("TagPt35MetTrig",   "TauTagPt55MetTrig"               + nLayersWord, "Tau_2018"              + runPeriod, dirs['Brian']+"2018/fromLPC/tauControlRegionBinnedHits_v2")
            tauBkgdEstimate.addChannel("TrigEffDenom",     "ElectronTagPt55"                 + nLayersWord, "SingleEle_2018"        + runPeriod, dirs['Brian']+"2018/fromLPC/electronControlRegionBinnedLayers")
            tauBkgdEstimate.addChannel("TrigEffNumer",     "ElectronTagPt55MetTrig"          + nLayersWord, "SingleEle_2018"        + runPeriod, dirs['Brian']+"2018/fromLPC/electronControlRegionBinnedLayers")
            tauBkgdEstimate.addChannel("TagPt35MetL1Trig", "TauTagPt55"                      + nLayersWord, "Tau_2018"              + runPeriod, dirs['Brian']+"2018/fromLPC/tauControlRegionBinnedHits")

            tauBkgdEstimate.addUseHistogramsForPpassMetTriggers(False) # temporary measure
            tauBkgdEstimate.addRebinFactor(8)

            print "********************************************************************************"

            nEstTau[(nLayersWord, runPeriod)] = tauBkgdEstimate.printNest()
            tauBkgdEstimate.printPpassVetoTagProbe()

            print "********************************************************************************"

            fout.Close()

            print "\n\n"

sys.stdout = stdout

# print sums
if background == "ALL":
    nElectrons = {}
    nMuons = {}
    nTaus = {}
    nFakes = {}

    nLeptons = copy.deepcopy(nEstElectron)
    nTotal = copy.deepcopy(nEstElectron)

    for runPeriod in runPeriods:
        for nLayersWord in nLayersWords:
            nLeptons[(nLayersWord, runPeriod)] += nEstMuon[(nLayersWord, runPeriod)] + nEstTau[(nLayersWord, runPeriod)]
            nTotal[(nLayersWord, runPeriod)] = nLeptons[(nLayersWord, runPeriod)] + nEstFake[(nLayersWord, runPeriod)]
            print "********************************************************************************"
            print "Total background from leptons (2018" + runPeriod + ", " + nLayersWord + "): " + nLayersWord[(nLayersWord, runPeriod)]
            print "Total background from fake tracks (2018" + runPeriod + ", " + nLayersWord + "): " + nEstFake[(nLayersWord, runPeriod)]
            print "********************************************************************************"
            print "Total background (2018" + runPeriod + ", " + nLayersWord + "): " + nTotal[(nLayersWord, runPeriod)]
            print "********************************************************************************"
            print "\n\n"

    fout = TFile.Open("backgroundCrossSections_2018.root", "recreate")

    for nLayersWord in nLayersWords:

        x = array("d"); ex = array("d")
        electron   =  array ("d");  muon   =  array ("d");  tau   =  array ("d");  fake   =  array ("d")
        eElectron  =  array ("d");  eMuon  =  array ("d");  eTau  =  array ("d");  eFake  =  array ("d")

        #runPeriodsToPlot = ["B", "C", "D", "E", "F"]
        runPeriodsToPlot = [""]
        i = 0.0

        for runPeriod in runPeriodsToPlot:
            x.append(i)
            ex.append(0.0)
            i += 1.0

            electron.append( nEstElectron[(nLayersWord, runPeriod)] / lumi["MET_2018" + runPeriod] ).centralValue()
            muon.append    ( nEstMuon    [(nLayersWord, runPeriod)] / lumi["MET_2018" + runPeriod] ).centralValue()
            tau.append     ( nEstTau     [(nLayersWord, runPeriod)] / lumi["MET_2018" + runPeriod] ).centralValue()
            fake.append    ( nEstFake    [(nLayersWord, runPeriod)] / lumi["MET_2018" + runPeriod] ).centralValue()

            eElectron.append( nEstElectron[(nLayersWord, runPeriod)] / lumi["MET_2018" + runPeriod] ).maxUncertainty()
            eMuon.append    ( nEstMuon    [(nLayersWord, runPeriod)] / lumi["MET_2018" + runPeriod] ).maxUncertainty()
            eTau.append     ( nEstTau     [(nLayersWord, runPeriod)] / lumi["MET_2018" + runPeriod] ).maxUncertainty()
            eFake.append    ( nEstFake    [(nLayersWord, runPeriod)] / lumi["MET_2018" + runPeriod] ).maxUncertainty()

        gElectron = TGraphErrors(len(x), x, electron, ex, eElectron)
        gMuon     = TGraphErrors(len(x), x, muon,     ex, eMuon)
        gTau      = TGraphErrors(len(x), x, tau,      ex, eTau)
        gFake     = TGraphErrors(len(x), x, fake,     ex, eFake)

        fout.mkdir(nLayersWord)
        fout.cd(nLayersWord)

        gElectron.Write("electron")
        gMuon.Write("muon")
        gTau.Write("tau")
        gFake.Write("fake")

        fout.cd()

    fout.Close()