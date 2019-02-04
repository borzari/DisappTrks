COM_ENERGY = 13000.
MGLU = 1600  # GeV
MCHI = 700  # GeV
CTAU = 1000  # mm
CROSS_SECTION = 0.00887 # pb
SLHA_TABLE="""
#  ISAJET SUSY parameters in SUSY Les Houches Accord 2 format
#  Created by ISALHA 2.0 Last revision: C. Balazs 21 Apr 2009
Block SPINFO   # Program information
     1   ISASUGRA from ISAJET          # Spectrum Calculator
     2   7.80   29-OCT-2009 12:50:36   # Version number
Block MODSEL   # Model selection
     1     3   # Minimal anomaly mediated (AMSB) model
Block SMINPUTS   # Standard Model inputs
     1     1.27842453E+02   # alpha_em^(-1)
     2     1.16570000E-05   # G_Fermi
     3     1.17200002E-01   # alpha_s(M_Z)
     4     9.11699982E+01   # m_{Z}(pole)
     5     4.19999981E+00   # m_{b}(m_{b})
     6     1.73070007E+02   # m_{top}(pole)
     7     1.77699995E+00   # m_{tau}(pole)
Block MINPAR   # SUSY breaking input parameters
     1     1.50000000E+03   # m_0
     2     2.46440000E+05   # m_{3/2}
     3     5.00000000E+00   # tan(beta)
     4     1.00000000E+00   # sign(mu)
Block EXTPAR   # Non-universal SUSY breaking parameters
     0     1.04228903E+16   # Input scale
Block MASS   # Scalar and gaugino mass spectrum
#  PDG code   mass                 particle
        24     8.04229965E+01   #  W^+
        25     1.16918777E+02   #  h^0
        35     4.13995459E+03   #  H^0
        36     4.11271240E+03   #  A^0
        37     4.12772119E+03   #  H^+
   1000001     4.68634814E+03   #  dnl
   1000002     4.68567432E+03   #  upl
   1000003     4.68634814E+03   #  stl
   1000004     4.68567480E+03   #  chl
   1000005     4.09400562E+03   #  b1
   1000006     3.40991528E+03   #  t1
   1000011     1.14678894E+03   #  el-
   1000012     1.12562231E+03   #  nuel
   1000013     1.14678894E+03   #  mul-
   1000014     1.12562231E+03   #  numl
   1000015     1.02227649E+03   #  tau1
   1000016     1.11225781E+03   #  nutl
   1000021     %.9g   #  glss
   1000022     6.99874146E+02   #  z1ss
   1000023     2.26904956E+03   #  z2ss
   1000024     7.00047607E+02   #  w1ss
   1000025    -3.87153369E+03   #  z3ss
   1000035     3.87282349E+03   #  z4ss
   1000037     3.87772314E+03   #  w2ss
   2000001     4.76078076E+03   #  dnr
   2000002     4.71648975E+03   #  upr
   2000003     4.76078076E+03   #  str
   2000004     4.71649023E+03   #  chr
   2000005     4.72474414E+03   #  b2
   2000006     4.13260303E+03   #  t2
   2000011     1.02800623E+03   #  er-
   2000013     1.02800623E+03   #  mur-
   2000015     1.12574829E+03   #  tau2
Block ALPHA   # Effective Higgs mixing parameter
         -1.97664991E-01   # alpha
Block STOPMIX   # stop mixing matrix
  1  1     8.36024433E-02   # O_{11}
  1  2    -9.96499181E-01   # O_{12}
  2  1     9.96499181E-01   # O_{21}
  2  2     8.36024433E-02   # O_{22}
Block SBOTMIX   # sbottom mixing matrix
  1  1     9.99983907E-01   # O_{11}
  1  2     5.66892792E-03   # O_{12}
  2  1    -5.66892792E-03   # O_{21}
  2  2     9.99983907E-01   # O_{22}
Block STAUMIX   # stau mixing matrix
  1  1     1.32659495E-01   # O_{11}
  1  2     9.91161644E-01   # O_{12}
  2  1    -9.91161644E-01   # O_{21}
  2  2     1.32659495E-01   # O_{22}
Block NMIX   # neutralino mixing matrix
  1  1    -8.25339637E-04   #
  1  2     9.99776781E-01   #
  1  3    -2.02405099E-02   #
  1  4     6.01018919E-03   #
  2  1     9.99794424E-01   #
  2  2     1.23403966E-03   #
  2  3     1.68632567E-02   #
  2  4    -1.11932158E-02   #
  3  1    -4.01982665E-03   #
  3  2     1.00584431E-02   #
  3  3     7.06979156E-01   #
  3  4     7.07151294E-01   #
  4  1     1.98580157E-02   #
  4  2    -1.85414888E-02   #
  4  3    -7.06743419E-01   #
  4  4     7.06947982E-01   #
Block UMIX   # chargino U mixing matrix
  1  1    -9.99564528E-01   # U_{11}
  1  2     2.95085218E-02   # U_{12}
  2  1    -2.95085218E-02   # U_{21}
  2  2    -9.99564528E-01   # U_{22}
Block VMIX   # chargino V mixing matrix
  1  1    -9.99936998E-01   # V_{11}
  1  2     1.12252701E-02   # V_{12}
  2  1    -1.12252701E-02   # V_{21}
  2  2    -9.99936998E-01   # V_{22}
Block GAUGE Q=  3.58269727E+03   #
     1     3.57497722E-01   # g`
     2     6.52475953E-01   # g_2
     3     1.22070026E+00   # g_3
Block YU Q=  3.58269727E+03   #
  3  3     8.38887691E-01   # y_t
Block YD Q=  3.58269727E+03   #
  3  3     6.52210116E-02   # y_b
Block YE Q=  3.58269727E+03   #
  3  3     5.15824445E-02   # y_tau
Block HMIX Q=  3.58269727E+03   # Higgs mixing parameters
     1     3.87514209E+03   # mu(Q)
     2     5.00000000E+00   # tan(beta)(M_GUT)
     3     2.51709106E+02   # Higgs vev at Q
     4     1.69144040E+07   # m_A^2(Q)
Block MSOFT Q=  3.58269727E+03   # DRbar SUSY breaking parameters
     1     2.30335156E+03   # M_1(Q)
     2     6.64254944E+02   # M_2(Q)
     3    -4.50376855E+03   # M_3(Q)
    31     1.12926123E+03   # MeL(Q)
    32     1.12926123E+03   # MmuL(Q)
    33     1.11625525E+03   # MtauL(Q)
    34     1.03541077E+03   # MeR(Q)
    35     1.03541077E+03   # MmuR(Q)
    36     9.99967957E+02   # MtauR(Q)
    41     4.45722266E+03   # MqL1(Q)
    42     4.45722266E+03   # MqL2(Q)
    43     3.91252832E+03   # MqL3(Q)
    44     4.48730469E+03   # MuR(Q)
    45     4.48730469E+03   # McR(Q)
    46     3.28067163E+03   # MtR(Q)
    47     4.53066406E+03   # MdR(Q)
    48     4.53066406E+03   # MsR(Q)
    49     4.55108252E+03   # MbR(Q)
Block AU Q=  3.58269727E+03   #
  1  1     3.86256177E+03   # A_u
  2  2     3.86256177E+03   # A_c
  3  3     3.86256177E+03   # A_t
Block AD Q=  3.58269727E+03   #
  1  1     9.22079785E+03   # A_d
  2  2     9.22079785E+03   # A_s
  3  3     9.22079785E+03   # A_b
Block AE Q=  3.58269727E+03   #
  1  1     2.57661255E+03   # A_e
  2  2     2.57661255E+03   # A_mu
  3  3     2.57661255E+03   # A_tau
#
#
#
#                             =================
#                             |The decay table|
#                             =================
#
#         PDG            Width
DECAY   1000021     5.50675438E+00 # gluino decay
#  BR              NDA  ID1  ID2  ID3
   2.50000000E-01  3    1    -1   1000022
   2.50000000E-01  3    2    -2   1000022
   2.50000000E-01  3    1    -2   1000024
   2.50000000E-01  3    -1   2    -1000024
#
#         PDG            Width
DECAY   1000024     %.9g # chargino decay
#
""" % (MGLU, (1.97326979e-13 / CTAU))

import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *

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
        processParameters = cms.vstring(
            'SUSY:all = off',
            'SUSY:gg2gluinogluino = on',
            'SUSY:qqbar2gluinogluino = on',
            '1000024:isResonance = false',
            '1000024:oneChannel = 1 1.0 100 1000022 211',
            '1000024:tau0 = %.1f' % CTAU,
            'ParticleDecays:tau0Max = %.1f' % (CTAU * 10),
       ),
        parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'pythia8CP5Settings',
            'processParameters')
    ),
    # The following parameters are required by Exotica_HSCP_SIM_cfi:
    slhaFile = cms.untracked.string(''),   # value not used
    processFile = cms.untracked.string('SimG4Core/CustomPhysics/data/RhadronProcessList.txt'),
    useregge = cms.bool(False),
    hscpFlavor = cms.untracked.string('stau'),
    massPoint = cms.untracked.int32(MCHI),  # value not used
    particleFile = cms.untracked.string('Configuration/GenProduction/python/ThirteenTeV/DisappTrksAMSBCascade/test/geant4_AMSB_chargino_%sGeV_ctau%scm.slha' % (MCHI, CTAU/10))
)

ProductionFilterSequence = cms.Sequence(generator)
