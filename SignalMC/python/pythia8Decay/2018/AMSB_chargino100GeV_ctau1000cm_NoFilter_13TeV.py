COM_ENERGY = 13000.
CROSS_SECTION = 1.0
MCHI = 100  # GeV
CTAU = 10000  # mm
SLHA_TABLE="""
#  ISAJET SUSY parameters in SUSY Les Houches Accord 2 format
#  Created by ISALHA 2.0 Last revision: C. Balazs 21 Apr 2009
Block SPINFO   # Program information
     1   ISASUGRA from ISAJET          # Spectrum Calculator
     2   7.80   29-OCT-2009 12:50:36   # Version number
Block MODSEL   # Model selection
     1     3   # Minimal anomaly mediated (AMSB) model
Block SMINPUTS   # Standard Model inputs
     1     1.27843697E+02   # alpha_em^(-1)
     2     1.16570000E-05   # G_Fermi
     3     1.17200002E-01   # alpha_s(M_Z)
     4     9.11699982E+01   # m_{Z}(pole)
     5     4.19999981E+00   # m_{b}(m_{b})
     6     1.73070007E+02   # m_{top}(pole)
     7     1.77699995E+00   # m_{tau}(pole)
Block MINPAR   # SUSY breaking input parameters
     1     1.50000000E+03   # m_0
     2     3.50800000E+04   # m_{3/2}
     3     5.00000000E+00   # tan(beta)
     4     1.00000000E+00   # sign(mu)
Block EXTPAR   # Non-universal SUSY breaking parameters
     0     1.26820216E+16   # Input scale
Block MASS   # Scalar and gaugino mass spectrum
#  PDG code   mass                 particle
        24     8.04229965E+01   #  W^+
        25     1.09165016E+02   #  h^0
        35     1.69811304E+03   #  H^0
        36     1.68658362E+03   #  A^0
        37     1.69844373E+03   #  H^+
   1000001     1.64875269E+03   #  dnl
   1000002     1.64692371E+03   #  upl
   1000003     1.64875269E+03   #  stl
   1000004     1.64692432E+03   #  chl
   1000005     1.36096313E+03   #  b1
   1000006     1.00422571E+03   #  t1
   1000011     1.49030664E+03   #  el-
   1000012     1.48858191E+03   #  nuel
   1000013     1.49030664E+03   #  mul-
   1000014     1.48858191E+03   #  numl
   1000015     1.48539880E+03   #  tau1
   1000016     1.48676428E+03   #  nutl
   1000021     8.64298706E+02   #  glss
   1000022     9.98443985E+01   #  z1ss
   1000023     3.20083069E+02   #  z2ss
   1000024     1.00132974E+02   #  w1ss
   1000025    -7.42030518E+02   #  z3ss
   1000035     7.49072571E+02   #  z4ss
   1000037     7.49086609E+02   #  w2ss
   2000001     1.65904858E+03   #  dnr
   2000002     1.65516052E+03   #  upr
   2000003     1.65904858E+03   #  str
   2000004     1.65516113E+03   #  chr
   2000005     1.65050024E+03   #  b2
   2000006     1.37387744E+03   #  t2
   2000011     1.49084143E+03   #  er-
   2000013     1.49084143E+03   #  mur-
   2000015     1.48991235E+03   #  tau2
Block ALPHA   # Effective Higgs mixing parameter
         -1.98805586E-01   # alpha
Block STOPMIX   # stop mixing matrix
  1  1     6.12325780E-02   # O_{11}
  1  2    -9.98123527E-01   # O_{12}
  2  1     9.98123527E-01   # O_{21}
  2  2     6.12325780E-02   # O_{22}
Block SBOTMIX   # sbottom mixing matrix
  1  1     9.99970913E-01   # O_{11}
  1  2     7.62549881E-03   # O_{12}
  2  1    -7.62549881E-03   # O_{21}
  2  2     9.99970913E-01   # O_{22}
Block STAUMIX   # stau mixing matrix
  1  1     5.97260058E-01   # O_{11}
  1  2     8.02047670E-01   # O_{12}
  2  1    -8.02047670E-01   # O_{21}
  2  2     5.97260058E-01   # O_{22}
Block NMIX   # neutralino mixing matrix
  1  1     1.02890544E-02   #
  1  2    -9.93297398E-01   #
  1  3     1.09105095E-01   #
  1  4    -3.67495306E-02   #
  2  1    -9.96177256E-01   #
  2  2    -1.99755784E-02   #
  2  3    -7.35215694E-02   #
  2  4     4.27322201E-02   #
  3  1     2.25971118E-02   #
  3  2    -5.08868955E-02   #
  3  3    -7.03913569E-01   #
  3  4    -7.08099306E-01   #
  4  1     8.37496892E-02   #
  4  2    -1.01842113E-01   #
  4  3    -6.97993875E-01   #
  4  4     7.03859687E-01   #
Block UMIX   # chargino U mixing matrix
  1  1    -9.88591433E-01   # U_{11}
  1  2     1.50621936E-01   # U_{12}
  2  1    -1.50621936E-01   # U_{21}
  2  2    -9.88591433E-01   # U_{22}
Block VMIX   # chargino V mixing matrix
  1  1    -9.98679578E-01   # V_{11}
  1  2     5.13723604E-02   # V_{12}
  2  1    -5.13723604E-02   # V_{21}
  2  2    -9.98679578E-01   # V_{22}
Block GAUGE Q=  1.13725037E+03   #
     1     3.57492119E-01   # g`
     2     6.52496159E-01   # g_2
     3     1.22099471E+00   # g_3
Block YU Q=  1.13725037E+03   #
  3  3     8.78648043E-01   # y_t
Block YD Q=  1.13725037E+03   #
  3  3     6.93556666E-02   # y_b
Block YE Q=  1.13725037E+03   #
  3  3     5.13891652E-02   # y_tau
Block HMIX Q=  1.13725037E+03   # Higgs mixing parameters
     1     7.33976440E+02   # mu(Q)
     2     5.00000000E+00   # tan(beta)(M_GUT)
     3     2.51144409E+02   # Higgs vev at Q
     4     2.84456425E+06   # m_A^2(Q)
Block MSOFT Q=  1.13725037E+03   # DRbar SUSY breaking parameters
     1     3.23079498E+02   # M_1(Q)
     2     9.78689346E+01   # M_2(Q)
     3    -7.54845886E+02   # M_3(Q)
    31     1.48517932E+03   # MeL(Q)
    32     1.48517932E+03   # MmuL(Q)
    33     1.48340161E+03   # MtauL(Q)
    34     1.48875891E+03   # MeR(Q)
    35     1.48875891E+03   # MmuR(Q)
    36     1.48529724E+03   # MtauR(Q)
    41     1.61164856E+03   # MqL1(Q)
    42     1.61164856E+03   # MqL2(Q)
    43     1.33004492E+03   # MqL3(Q)
    44     1.61942517E+03   # MuR(Q)
    45     1.61942517E+03   # McR(Q)
    46     9.72402039E+02   # MtR(Q)
    47     1.62276147E+03   # MdR(Q)
    48     1.62276147E+03   # MsR(Q)
    49     1.62246484E+03   # MbR(Q)
Block AU Q=  1.13725037E+03   #
  1  1     6.08556396E+02   # A_u
  2  2     6.08556396E+02   # A_c
  3  3     6.08556396E+02   # A_t
Block AD Q=  1.13725037E+03   #
  1  1     1.45460706E+03   # A_d
  2  2     1.45460706E+03   # A_s
  3  3     1.45460706E+03   # A_b
Block AE Q=  1.13725037E+03   #
  1  1     3.71930389E+02   # A_e
  2  2     3.71930389E+02   # A_mu
  3  3     3.71930389E+02   # A_tau
#
#
#
#                             =================
#                             |The decay table|
#                             =================
#
#         PDG            Width
DECAY   1000024     %.9g # chargino decay
#
#
""" % (1.97326979e-13 / CTAU)

import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(-1),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    SLHATableForPythia8 = cms.string('%s' % SLHA_TABLE),
    comEnergy = cms.double(COM_ENERGY),
    crossSection = cms.untracked.double(CROSS_SECTION),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
				pythia8PSweightsSettingsBlock,
        processParameters = cms.vstring(
            'SUSY:all = off',
            'SUSY:qqbar2chi+chi- = on',
            'SUSY:qqbar2chi+-chi0 = on',
            '1000024:isResonance = false',
            '1000024:oneChannel = 1 1.0 100 1000022 211',
            '1000024:tau0 = %.1f' % CTAU,
            'ParticleDecays:tau0Max = %.1f' % (CTAU * 10),
       ),
        parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'pythia8CP5Settings',
            'pythia8PSweightsSettings',
            'processParameters')
    ),
    # The following parameters are required by Exotica_HSCP_SIM_cfi:
    slhaFile = cms.untracked.string(''),   # value not used
    processFile = cms.untracked.string('SimG4Core/CustomPhysics/data/RhadronProcessList.txt'),
    useregge = cms.bool(False),
    hscpFlavor = cms.untracked.string('stau'),
    massPoint = cms.untracked.int32(MCHI),  # value not used
    particleFile = cms.untracked.string('DisappTrks/SignalMC/data/geant4/geant4_AMSB_chargino_%sGeV_ctau%scm.slha' % (MCHI, CTAU/10))
)

ProductionFilterSequence = cms.Sequence(generator)
