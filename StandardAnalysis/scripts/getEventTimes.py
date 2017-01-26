#!/usr/bin/env python

import subprocess
import sys
import re
import numpy

from ROOT import TFile, TH1D

if len (sys.argv) < 2:
  print "Usage: " + sys.argv[0] + " CONDOR_DIR [OUTPUT_FILE]"
  sys.exit (1)
condorDir = sys.argv[1]
outputFile = "eventTimes.root"
if len (sys.argv) > 2:
  outputFile = sys.argv[2]

nBins = 200

cpuTimePerEvent = []
realTimePerEvent = []

################################################################################
# Extract times from output files
################################################################################
print "extracting times from output files..."
command = ["find", condorDir, "-type", "f", "-regex", ".*\/condor_[^/]*\.err$"]
logFiles = subprocess.check_output (command).split ()
for logFile in logFiles:
  f = open (logFile, "r")
  for line in f:
    if not re.match (r".*CPU time.*", line) and not re.match (r".*real time.*", line):
      continue
    timePerEvent = float (re.sub (r".*\(([^ ]*) seconds per event\)$", r"\1", line))
    if re.match (r".*CPU time.*", line):
      cpuTimePerEvent.append (timePerEvent)
    if re.match (r".*real time.*", line):
      realTimePerEvent.append (timePerEvent)
  f.close ()
cpuTimePerEvent = sorted (cpuTimePerEvent)
realTimePerEvent = sorted (realTimePerEvent)
################################################################################

################################################################################
# Fill histograms with times
################################################################################
print "filling histograms with times..."
cpuTime = []
realTime = []
cpuTime.append (TH1D ("cpuTime10p0", ";CPU time per event [s/evt]", nBins, 0.0, 10.0))
cpuTime.append (TH1D ("cpuTime1p0", ";CPU time per event [s/evt]", nBins, 0.0, 1.0))
cpuTime.append (TH1D ("cpuTime0p1", ";CPU time per event [s/evt]", nBins, 0.0, 0.1))
cpuTime.append (TH1D ("cpuTime0p01", ";CPU time per event [s/evt]", nBins, 0.0, 0.01))
cpuTime.append (TH1D ("cpuTime0p001", ";CPU time per event [s/evt]", nBins, 0.0, 0.001))
cpuTime.append (TH1D ("cpuTime0p0001", ";CPU time per event [s/evt]", nBins, 0.0, 0.0001))
cpuTime.append (TH1D ("cpuTime0p00001", ";CPU time per event [s/evt]", nBins, 0.0, 0.00001))
cpuTime.append (TH1D ("cpuTime_log", ";CPU time per event [s/evt]", nBins, numpy.logspace (-5, 1, nBins + 1)))
realTime.append (TH1D ("realTime10p0", ";real time per event [s/evt]", nBins, 0.0, 10.0))
realTime.append (TH1D ("realTime1p0", ";real time per event [s/evt]", nBins, 0.0, 1.0))
realTime.append (TH1D ("realTime0p1", ";real time per event [s/evt]", nBins, 0.0, 0.1))
realTime.append (TH1D ("realTime0p01", ";real time per event [s/evt]", nBins, 0.0, 0.01))
realTime.append (TH1D ("realTime0p001", ";real time per event [s/evt]", nBins, 0.0, 0.001))
realTime.append (TH1D ("realTime0p0001", ";real time per event [s/evt]", nBins, 0.0, 0.0001))
realTime.append (TH1D ("realTime0p00001", ";real time per event [s/evt]", nBins, 0.0, 0.00001))
realTime.append (TH1D ("realTime_log", ";real time per event [s/evt]", nBins, numpy.logspace (-5, 1, nBins + 1)))
for time in cpuTimePerEvent:
  for hist in cpuTime:
    hist.Fill (time)
for time in realTimePerEvent:
  for hist in realTime:
    hist.Fill (time)
################################################################################

################################################################################
# Write the histograms to a file
################################################################################
f = TFile.Open (outputFile, "recreate")
for hist in cpuTime:
  hist.Write ()
for hist in realTime:
  hist.Write ()
f.Close ()
print "wrote times to " + outputFile
################################################################################
