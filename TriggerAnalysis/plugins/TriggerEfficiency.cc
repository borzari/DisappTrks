#include "CommonTools/Utils/interface/TFileDirectory.h"

#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/PatCandidates/interface/Electron.h"

#include "DisappTrks/TriggerAnalysis/plugins/TriggerEfficiency.h"

template<class T>
TriggerEfficiency<T>::TriggerEfficiency (const edm::ParameterSet &cfg) :
  isMC_          (cfg.getParameter<bool>           ("isMC")),
  mets_          (cfg.getParameter<edm::InputTag>  ("mets")),
  muons_         (cfg.getParameter<edm::InputTag>  ("muons")),
  tracks_        (cfg.getParameter<edm::InputTag>  ("tracks")),
  triggerBits_   (cfg.getParameter<edm::InputTag>  ("triggerBits")),
  triggerObjs_   (cfg.getParameter<edm::InputTag>  ("triggerObjs")),
  vertices_      (cfg.getParameter<edm::InputTag>  ("vertices")),
  genParticles_  (cfg.getParameter<edm::InputTag>  ("genParticles")),
  jets_          (cfg.getParameter<edm::InputTag>  ("jets")),
  metTriggersList_ ({
    {"HLT_IsoMu20_v"},
    {"hltL1sL1ETM60ORETM70"},
    {"hltMET75"},
    {"hltMETClean75"},
    {"HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight_v"}, // in data
    {"HLT_PFMET120_PFMHT120_IDTight_v"},                      // in data
    {"HLT_PFMETNoMu120_NoiseCleaned_PFMHTNoMu120_IDTight_v"}, // in MC
    {"HLT_PFMET120_PFMHT120_IDLoose_v"},                      // in MC
    {"hltMET75", "HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight_v"},
    {"hltMET75", "HLT_PFMET120_PFMHT120_IDTight_v"},
    {"hltMET75", "HLT_PFMETNoMu120_NoiseCleaned_PFMHTNoMu120_IDTight_v"},
    {"hltMET75", "HLT_PFMET120_PFMHT120_IDLoose_v"},
    {"hltMETClean75", "HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight_v"},
    {"hltMETClean75", "HLT_PFMET120_PFMHT120_IDTight_v"},
    {"hltMETClean75", "HLT_PFMETNoMu120_NoiseCleaned_PFMHTNoMu120_IDTight_v"},
    {"hltMETClean75", "HLT_PFMET120_PFMHT120_IDLoose_v"}
  }),
  metTriggerNames_ ({})
{
  TH1::SetDefaultSumw2 ();
  TFileDirectory MuMETNoMETNoTrigger_metDir = fs_->mkdir ("MuMETNoMETNoTriggerPlotter/Met Plots"),
                 MuMETNoMETNoTrigger_muonDir = fs_->mkdir ("MuMETNoMETNoTriggerPlotter/Muon Plots");
  map<string, TFileDirectory> MuMETNoMET_metDir,
                              MuMETNoMET_muonDir,
                              MuMETNoMETL1Seed_metDir,
                              MuMETNoMETL1Seed_muonDir,
                              MuMETNoMETMuSeed_metDir,
                              MuMETNoMETMuSeed_muonDir,
                              MuMETNoMuonPt_metDir,
                              MuMETNoMuonPt_muonDir,
                              MuMETNoMuonPtNoTrigger_metDir,
                              MuMETNoMuonPtNoTrigger_muonDir;
  vector<double> bins, wideBins;
  logSpace (1000, 0.0, 3.0, bins);
  logSpace (60, 0.0, 3.0, wideBins);

  oneDHists_["NoTrigger"];
  twoDHists_["NoTrigger"];

  oneDHists_.at ("NoTrigger")["MuMETNoMETNoTrigger_metDir/metPt"] = MuMETNoMETNoTrigger_metDir.make<TH1D> ("metPt", ";E_{T}^{miss} [GeV]", bins.size () - 1, bins.data ());
  oneDHists_.at ("NoTrigger")["MuMETNoMETNoTrigger_metDir/pfMETNoMuPt"] = MuMETNoMETNoTrigger_metDir.make<TH1D> ("pfMETNoMuPt", ";calo E_{T}^{miss} [GeV]", bins.size () - 1, bins.data ());
  oneDHists_.at ("NoTrigger")["MuMETNoMETNoTrigger_muonDir/muonPt"] = MuMETNoMETNoTrigger_muonDir.make<TH1D> ("muonPt", ";muon p_{T} [GeV]", bins.size () - 1, bins.data ());

  twoDHists_.at ("NoTrigger")["MuMETNoMETNoTrigger_metDir/pfMETNoMuVsPFMET"] = MuMETNoMETNoTrigger_metDir.make<TH2D> ("pfMETNoMuVsPFMET", ";PF E_{T}^{miss} [GeV];calo E_{T}^{miss} [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
  twoDHists_.at ("NoTrigger")["MuMETNoMETNoTrigger_metDir/hltMetVsPFMET"] = MuMETNoMETNoTrigger_metDir.make<TH2D> ("hltMetVsPFMET", ";PF E_{T}^{miss} [GeV];hltMet [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
  twoDHists_.at ("NoTrigger")["MuMETNoMETNoTrigger_metDir/hltMetCleanVsPFMET"] = MuMETNoMETNoTrigger_metDir.make<TH2D> ("hltMetCleanVsPFMET", ";PF E_{T}^{miss} [GeV];hltMetClean [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
  twoDHists_.at ("NoTrigger")["MuMETNoMETNoTrigger_metDir/hltMetVsPFMETNoMu"] = MuMETNoMETNoTrigger_metDir.make<TH2D> ("hltMetVsPFMETNoMu", ";calo E_{T}^{miss} [GeV];hltMet [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
  twoDHists_.at ("NoTrigger")["MuMETNoMETNoTrigger_metDir/hltMetCleanVsPFMETNoMu"] = MuMETNoMETNoTrigger_metDir.make<TH2D> ("hltMetCleanVsPFMETNoMu", ";calo E_{T}^{miss} [GeV];hltMetClean [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());

  for (const auto &metTriggers : metTriggersList_)
    {
      string metTriggerName = "";
      for (auto metTrigger = metTriggers.cbegin (); metTrigger != metTriggers.cend (); metTrigger++)
        {
          metTriggerName += *metTrigger;
          if (metTrigger + 1 != metTriggers.cend ())
            metTriggerName += " OR ";
        }
      metTriggerNames_.push_back (metTriggerName);

      MuMETNoMET_metDir[metTriggerName] = fs_->mkdir ("MuMETNoMETPlotter/" + metTriggerName + "/Met Plots"),
      MuMETNoMET_muonDir[metTriggerName] = fs_->mkdir ("MuMETNoMETPlotter/" + metTriggerName + "/Muon Plots"),
      MuMETNoMETL1Seed_metDir[metTriggerName] = fs_->mkdir ("MuMETNoMETL1SeedPlotter/" + metTriggerName + "/Met Plots"),
      MuMETNoMETL1Seed_muonDir[metTriggerName] = fs_->mkdir ("MuMETNoMETL1SeedPlotter/" + metTriggerName + "/Muon Plots"),
      MuMETNoMETMuSeed_metDir[metTriggerName] = fs_->mkdir ("MuMETNoMETMuSeedPlotter/" + metTriggerName + "/Met Plots"),
      MuMETNoMETMuSeed_muonDir[metTriggerName] = fs_->mkdir ("MuMETNoMETMuSeedPlotter/" + metTriggerName + "/Muon Plots"),
      MuMETNoMuonPt_metDir[metTriggerName] = fs_->mkdir ("MuMETNoMuonPtPlotter/" + metTriggerName + "/Met Plots"),
      MuMETNoMuonPt_muonDir[metTriggerName] = fs_->mkdir ("MuMETNoMuonPtPlotter/" + metTriggerName + "/Muon Plots");
      MuMETNoMuonPtNoTrigger_metDir[metTriggerName] = fs_->mkdir ("MuMETNoMuonPtNoTriggerPlotter/" + metTriggerName + "/Met Plots");
      MuMETNoMuonPtNoTrigger_muonDir[metTriggerName] = fs_->mkdir ("MuMETNoMuonPtNoTriggerPlotter/" + metTriggerName + "/Muon Plots");

      oneDHists_[metTriggerName];
      twoDHists_[metTriggerName];

      oneDHists_.at (metTriggerName)["MuMETNoMET_metDir/metPt"] = MuMETNoMET_metDir.at (metTriggerName).make<TH1D> ("metPt", ";E_{T}^{miss} [GeV]", bins.size () - 1, bins.data ());
      oneDHists_.at (metTriggerName)["MuMETNoMET_metDir/pfMETNoMuPt"] = MuMETNoMET_metDir.at (metTriggerName).make<TH1D> ("pfMETNoMuPt", ";calo E_{T}^{miss} [GeV]", bins.size () - 1, bins.data ());
      oneDHists_.at (metTriggerName)["MuMETNoMET_muonDir/muonPt"] = MuMETNoMET_muonDir.at (metTriggerName).make<TH1D> ("muonPt", ";muon p_{T} [GeV]", bins.size () - 1, bins.data ());

      twoDHists_.at (metTriggerName)["MuMETNoMET_metDir/pfMETNoMuVsPFMET"] = MuMETNoMET_metDir.at (metTriggerName).make<TH2D> ("pfMETNoMuVsPFMET", ";PF E_{T}^{miss} [GeV];calo E_{T}^{miss} [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
      twoDHists_.at (metTriggerName)["MuMETNoMET_metDir/hltMetVsPFMET"] = MuMETNoMET_metDir.at (metTriggerName).make<TH2D> ("hltMetVsPFMET", ";PF E_{T}^{miss} [GeV];hltMet [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
      twoDHists_.at (metTriggerName)["MuMETNoMET_metDir/hltMetCleanVsPFMET"] = MuMETNoMET_metDir.at (metTriggerName).make<TH2D> ("hltMetCleanVsPFMET", ";PF E_{T}^{miss} [GeV];hltMetClean [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
      twoDHists_.at (metTriggerName)["MuMETNoMET_metDir/hltMetVsPFMETNoMu"] = MuMETNoMET_metDir.at (metTriggerName).make<TH2D> ("hltMetVsPFMETNoMu", ";calo E_{T}^{miss} [GeV];hltMet [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
      twoDHists_.at (metTriggerName)["MuMETNoMET_metDir/hltMetCleanVsPFMETNoMu"] = MuMETNoMET_metDir.at (metTriggerName).make<TH2D> ("hltMetCleanVsPFMETNoMu", ";calo E_{T}^{miss} [GeV];hltMetClean [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());

      oneDHists_.at (metTriggerName)["MuMETNoMETL1Seed_metDir/metPt"] = MuMETNoMETL1Seed_metDir.at (metTriggerName).make<TH1D> ("metPt", ";E_{T}^{miss} [GeV]", bins.size () - 1, bins.data ());
      oneDHists_.at (metTriggerName)["MuMETNoMETL1Seed_metDir/pfMETNoMuPt"] = MuMETNoMETL1Seed_metDir.at (metTriggerName).make<TH1D> ("pfMETNoMuPt", ";calo E_{T}^{miss} [GeV]", bins.size () - 1, bins.data ());
      oneDHists_.at (metTriggerName)["MuMETNoMETL1Seed_muonDir/muonPt"] = MuMETNoMETL1Seed_muonDir.at (metTriggerName).make<TH1D> ("muonPt", ";muon p_{T} [GeV]", bins.size () - 1, bins.data ());

      twoDHists_.at (metTriggerName)["MuMETNoMETL1Seed_metDir/pfMETNoMuVsPFMET"] = MuMETNoMETL1Seed_metDir.at (metTriggerName).make<TH2D> ("pfMETNoMuVsPFMET", ";PF E_{T}^{miss} [GeV];calo E_{T}^{miss} [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
      twoDHists_.at (metTriggerName)["MuMETNoMETL1Seed_metDir/hltMetVsPFMET"] = MuMETNoMETL1Seed_metDir.at (metTriggerName).make<TH2D> ("hltMetVsPFMET", ";PF E_{T}^{miss} [GeV];hltMet [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
      twoDHists_.at (metTriggerName)["MuMETNoMETL1Seed_metDir/hltMetCleanVsPFMET"] = MuMETNoMETL1Seed_metDir.at (metTriggerName).make<TH2D> ("hltMetCleanVsPFMET", ";PF E_{T}^{miss} [GeV];hltMetClean [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
      twoDHists_.at (metTriggerName)["MuMETNoMETL1Seed_metDir/hltMetVsPFMETNoMu"] = MuMETNoMETL1Seed_metDir.at (metTriggerName).make<TH2D> ("hltMetVsPFMETNoMu", ";calo E_{T}^{miss} [GeV];hltMet [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
      twoDHists_.at (metTriggerName)["MuMETNoMETL1Seed_metDir/hltMetCleanVsPFMETNoMu"] = MuMETNoMETL1Seed_metDir.at (metTriggerName).make<TH2D> ("hltMetCleanVsPFMETNoMu", ";calo E_{T}^{miss} [GeV];hltMetClean [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());

      oneDHists_.at (metTriggerName)["MuMETNoMETMuSeed_metDir/metPt"] = MuMETNoMETMuSeed_metDir.at (metTriggerName).make<TH1D> ("metPt", ";E_{T}^{miss} [GeV]", bins.size () - 1, bins.data ());
      oneDHists_.at (metTriggerName)["MuMETNoMETMuSeed_metDir/pfMETNoMuPt"] = MuMETNoMETMuSeed_metDir.at (metTriggerName).make<TH1D> ("pfMETNoMuPt", ";calo E_{T}^{miss} [GeV]", bins.size () - 1, bins.data ());
      oneDHists_.at (metTriggerName)["MuMETNoMETMuSeed_muonDir/muonPt"] = MuMETNoMETMuSeed_muonDir.at (metTriggerName).make<TH1D> ("muonPt", ";muon p_{T} [GeV]", bins.size () - 1, bins.data ());

      twoDHists_.at (metTriggerName)["MuMETNoMETMuSeed_metDir/pfMETNoMuVsPFMET"] = MuMETNoMETMuSeed_metDir.at (metTriggerName).make<TH2D> ("pfMETNoMuVsPFMET", ";PF E_{T}^{miss} [GeV];calo E_{T}^{miss} [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
      twoDHists_.at (metTriggerName)["MuMETNoMETMuSeed_metDir/hltMetVsPFMET"] = MuMETNoMETMuSeed_metDir.at (metTriggerName).make<TH2D> ("hltMetVsPFMET", ";PF E_{T}^{miss} [GeV];hltMet [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
      twoDHists_.at (metTriggerName)["MuMETNoMETMuSeed_metDir/hltMetCleanVsPFMET"] = MuMETNoMETMuSeed_metDir.at (metTriggerName).make<TH2D> ("hltMetCleanVsPFMET", ";PF E_{T}^{miss} [GeV];hltMetClean [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
      twoDHists_.at (metTriggerName)["MuMETNoMETMuSeed_metDir/hltMetVsPFMETNoMu"] = MuMETNoMETMuSeed_metDir.at (metTriggerName).make<TH2D> ("hltMetVsPFMETNoMu", ";calo E_{T}^{miss} [GeV];hltMet [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
      twoDHists_.at (metTriggerName)["MuMETNoMETMuSeed_metDir/hltMetCleanVsPFMETNoMu"] = MuMETNoMETMuSeed_metDir.at (metTriggerName).make<TH2D> ("hltMetCleanVsPFMETNoMu", ";calo E_{T}^{miss} [GeV];hltMetClean [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());

      oneDHists_.at (metTriggerName)["MuMETNoMuonPt_metDir/metPt"] = MuMETNoMuonPt_metDir.at (metTriggerName).make<TH1D> ("metPt", ";E_{T}^{miss} [GeV]", bins.size () - 1, bins.data ());
      oneDHists_.at (metTriggerName)["MuMETNoMuonPt_metDir/pfMETNoMuPt"] = MuMETNoMuonPt_metDir.at (metTriggerName).make<TH1D> ("pfMETNoMuPt", ";calo E_{T}^{miss} [GeV]", bins.size () - 1, bins.data ());
      oneDHists_.at (metTriggerName)["MuMETNoMuonPt_muonDir/muonPt"] = MuMETNoMuonPt_muonDir.at (metTriggerName).make<TH1D> ("muonPt", ";muon p_{T} [GeV]", bins.size () - 1, bins.data ());

      twoDHists_.at (metTriggerName)["MuMETNoMuonPt_metDir/pfMETNoMuVsPFMET"] = MuMETNoMuonPt_metDir.at (metTriggerName).make<TH2D> ("pfMETNoMuVsPFMET", ";PF E_{T}^{miss} [GeV];calo E_{T}^{miss} [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
      twoDHists_.at (metTriggerName)["MuMETNoMuonPt_metDir/hltMetVsPFMET"] = MuMETNoMuonPt_metDir.at (metTriggerName).make<TH2D> ("hltMetVsPFMET", ";PF E_{T}^{miss} [GeV];hltMet [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
      twoDHists_.at (metTriggerName)["MuMETNoMuonPt_metDir/hltMetCleanVsPFMET"] = MuMETNoMuonPt_metDir.at (metTriggerName).make<TH2D> ("hltMetCleanVsPFMET", ";PF E_{T}^{miss} [GeV];hltMetClean [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
      twoDHists_.at (metTriggerName)["MuMETNoMuonPt_metDir/hltMetVsPFMETNoMu"] = MuMETNoMuonPt_metDir.at (metTriggerName).make<TH2D> ("hltMetVsPFMETNoMu", ";calo E_{T}^{miss} [GeV];hltMet [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
      twoDHists_.at (metTriggerName)["MuMETNoMuonPt_metDir/hltMetCleanVsPFMETNoMu"] = MuMETNoMuonPt_metDir.at (metTriggerName).make<TH2D> ("hltMetCleanVsPFMETNoMu", ";calo E_{T}^{miss} [GeV];hltMetClean [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());

      oneDHists_.at (metTriggerName)["MuMETNoMuonPtNoTrigger_metDir/metPt"] = MuMETNoMuonPtNoTrigger_metDir.at (metTriggerName).make<TH1D> ("metPt", ";E_{T}^{miss} [GeV]", bins.size () - 1, bins.data ());
      oneDHists_.at (metTriggerName)["MuMETNoMuonPtNoTrigger_metDir/pfMETNoMuPt"] = MuMETNoMuonPtNoTrigger_metDir.at (metTriggerName).make<TH1D> ("pfMETNoMuPt", ";calo E_{T}^{miss} [GeV]", bins.size () - 1, bins.data ());
      oneDHists_.at (metTriggerName)["MuMETNoMuonPtNoTrigger_muonDir/muonPt"] = MuMETNoMuonPtNoTrigger_muonDir.at (metTriggerName).make<TH1D> ("muonPt", ";muon p_{T} [GeV]", bins.size () - 1, bins.data ());

      twoDHists_.at (metTriggerName)["MuMETNoMuonPtNoTrigger_metDir/pfMETNoMuVsPFMET"] = MuMETNoMuonPtNoTrigger_metDir.at (metTriggerName).make<TH2D> ("pfMETNoMuVsPFMET", ";PF E_{T}^{miss} [GeV];calo E_{T}^{miss} [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
      twoDHists_.at (metTriggerName)["MuMETNoMuonPtNoTrigger_metDir/hltMetVsPFMET"] = MuMETNoMuonPtNoTrigger_metDir.at (metTriggerName).make<TH2D> ("hltMetVsPFMET", ";PF E_{T}^{miss} [GeV];hltMet [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
      twoDHists_.at (metTriggerName)["MuMETNoMuonPtNoTrigger_metDir/hltMetCleanVsPFMET"] = MuMETNoMuonPtNoTrigger_metDir.at (metTriggerName).make<TH2D> ("hltMetCleanVsPFMET", ";PF E_{T}^{miss} [GeV];hltMetClean [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
      twoDHists_.at (metTriggerName)["MuMETNoMuonPtNoTrigger_metDir/hltMetVsPFMETNoMu"] = MuMETNoMuonPtNoTrigger_metDir.at (metTriggerName).make<TH2D> ("hltMetVsPFMETNoMu", ";calo E_{T}^{miss} [GeV];hltMet [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
      twoDHists_.at (metTriggerName)["MuMETNoMuonPtNoTrigger_metDir/hltMetCleanVsPFMETNoMu"] = MuMETNoMuonPtNoTrigger_metDir.at (metTriggerName).make<TH2D> ("hltMetCleanVsPFMETNoMu", ";calo E_{T}^{miss} [GeV];hltMetClean [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
    }
}

template<class T>
TriggerEfficiency<T>::~TriggerEfficiency ()
{
}

template<class T> bool
TriggerEfficiency<T>::filter (edm::Event &event, const edm::EventSetup &setup)
{
  edm::Handle<vector<pat::MET> > mets;
  event.getByLabel (mets_, mets);
  edm::Handle<vector<pat::Muon> > muons;
  event.getByLabel (muons_, muons);
  edm::Handle<vector<T> > tracks;
  event.getByLabel (tracks_, tracks);
  edm::Handle<edm::TriggerResults> triggerBits;
  event.getByLabel (triggerBits_, triggerBits);
  edm::Handle<vector<pat::TriggerObjectStandAlone> > triggerObjs;
  event.getByLabel (triggerObjs_, triggerObjs);
  edm::Handle<vector<reco::Vertex> > vertices;
  event.getByLabel (vertices_, vertices);
  edm::Handle<vector<reco::GenParticle> > genParticles;
  isMC_ && event.getByLabel (genParticles_, genParticles);
  edm::Handle<vector<pat::Jet> > jets;
  event.getByLabel (jets_, jets);

  const edm::TriggerNames &triggerNames = event.triggerNames (*triggerBits);
  const reco::Vertex &pv = vertices->at (0);
  const pat::TriggerObjectStandAlone &hltMet = getHLTMET (triggerNames, *triggerObjs, "hltMet");
  const pat::TriggerObjectStandAlone &hltMetClean = getHLTMET (triggerNames, *triggerObjs, "hltMetClean");
  const TVector2 * const metNoMu = getPFMETNoMu (*mets, *muons);
  bool passesL1Seed = passesTriggerFilter (triggerNames, *triggerObjs, "hltL1sL1ETM60ORETM70");
  bool passesMuSeed = hasGoodMuon (*muons, pv) && passesTrigger (triggerNames, *triggerBits, "HLT_IsoMu20_v");

  //////////////////////////////////////////////////////////////////////////////
  // Require leading jet to be central.  
  //////////////////////////////////////////////////////////////////////////////
  if (jets->size ())
    {
      // first jet is always leading jet (https://github.com/cms-sw/cmssw/blob/CMSSW_7_4_X/PhysicsTools/PatAlgos/plugins/PATJetProducer.cc#L406)
      const pat::Jet &leadingJet = jets->at (0);
      if (fabs (leadingJet.eta ()) > 2.4)
        return false; // skip these events
    }
  //////////////////////////////////////////////////////////////////////////////

  //////////////////////////////////////////////////////////////////////////////
  // MuMETNoMETNoTrigger channel
  //////////////////////////////////////////////////////////////////////////////
  fillHistograms (*mets, *metNoMu, hltMet, hltMetClean, *tracks, "MuMETNoMETNoTrigger");
  //////////////////////////////////////////////////////////////////////////////

  for (unsigned i = 0; i < metTriggersList_.size (); i++)
    {
      bool passesMETTriggers = false;
      for (const auto &metTrigger : metTriggersList_.at (i))
        {
          if (metTrigger == "HLT_IsoMu20_v")
            passesMETTriggers = passesMuSeed;
          else
            passesMETTriggers = passesMETTriggers || (metTrigger.find ("HLT") == 0 ? passesTrigger (triggerNames, *triggerBits, metTrigger) : passesTriggerFilter (triggerNames, *triggerObjs, metTrigger));
          if (passesMETTriggers)
            break;
        }

      //////////////////////////////////////////////////////////////////////////////
      // MuMETNoMET channel
      //////////////////////////////////////////////////////////////////////////////
      if (passesMETTriggers)
        fillHistograms (*mets, *metNoMu, hltMet, hltMetClean, *tracks, "MuMETNoMET", metTriggerNames_.at (i));
      //////////////////////////////////////////////////////////////////////////////

      //////////////////////////////////////////////////////////////////////////////
      // MuMETNoMETL1Seed channel
      //////////////////////////////////////////////////////////////////////////////
      if (passesL1Seed && passesMETTriggers)
        fillHistograms (*mets, *metNoMu, hltMet, hltMetClean, *tracks, "MuMETNoMETL1Seed", metTriggerNames_.at (i));
      //////////////////////////////////////////////////////////////////////////////

      //////////////////////////////////////////////////////////////////////////////
      // MuMETNoMETMuSeed channel
      //////////////////////////////////////////////////////////////////////////////
      if (passesMuSeed && passesMETTriggers)
        fillHistograms (*mets, *metNoMu, hltMet, hltMetClean, *tracks, "MuMETNoMETMuSeed", metTriggerNames_.at (i));
      //////////////////////////////////////////////////////////////////////////////

      //////////////////////////////////////////////////////////////////////////////
      // MuMETNoMuonPtNoTrigger channel
      //////////////////////////////////////////////////////////////////////////////
      vector<const T *> selectedTracks;
      selectedTracks.clear ();
      for (const auto &track : *tracks)
        {
          bool goodTrack = (isMC_ ? isGoodTrack (track, pv, *tracks, *genParticles) : isGoodTrack (track, pv, *tracks));
          if (!goodTrack)
            continue;
          selectedTracks.push_back (&track);
        }
      sort (selectedTracks.begin (), selectedTracks.end (), [](const T *a, const T *b) -> bool { return (a->pt () > b->pt ()); });
      if ((selectedTracks.size () == 1 || selectedTracks.size () == 2) && passesMETTriggers)
        fillHistograms (*mets, *metNoMu, hltMet, hltMetClean, *selectedTracks.at (0), "MuMETNoMuonPtNoTrigger", metTriggerNames_.at (i));
      //////////////////////////////////////////////////////////////////////////////

      //////////////////////////////////////////////////////////////////////////////
      // MuMETNoMuonPt channel
      //////////////////////////////////////////////////////////////////////////////
      if ((selectedTracks.size () == 1 || selectedTracks.size () == 2) && passesMETTriggers && passesTrigger (triggerNames, *triggerBits, "HLT_MET75_IsoTrk50_v"))
        fillHistograms (*mets, *metNoMu, hltMet, hltMetClean, *selectedTracks.at (0), "MuMETNoMuonPt", metTriggerNames_.at (i));
      //////////////////////////////////////////////////////////////////////////////
    }

  return false;
}

template<class T> void
TriggerEfficiency<T>::logSpace (const unsigned n, const double a, const double b, vector<double> &bins) const
{
  double step = (b - a) / ((double) n);

  bins.clear ();
  for (double i = a; i < b + 0.5 * step; i += step)
    bins.push_back (pow (10.0, i));
}

template<class T> void
TriggerEfficiency<T>::linSpace (const unsigned n, const double a, const double b, vector<double> &bins) const
{
  double step = (b - a) / ((double) n);

  bins.clear ();
  for (double i = a; i < b + 0.5 * step; i += step)
    bins.push_back (i);
}

template<class T> const TVector2 * const
TriggerEfficiency<T>::getPFMETNoMu (const vector<pat::MET> &mets, const vector<pat::Muon> &muons) const
{
  TVector2 *metNoMu = new TVector2 (0.0, 0.0);
  for (const auto &met : mets)
    {
      *metNoMu += TVector2 (met.px (), met.py ());
      for (const auto &muon : muons)
        {
          if (!muon.isLooseMuon ())
            continue;
          *metNoMu += TVector2 (muon.px (), muon.py ());
        }
    }

  return metNoMu;
}

template<class T> void
TriggerEfficiency<T>::fillHistograms (const vector<pat::MET> &mets, const TVector2 &metNoMu, const pat::TriggerObjectStandAlone &hltMet, const pat::TriggerObjectStandAlone &hltMetClean, const T &track, const string &channel, const string &trigger) const
{
  for (const auto &met : mets)
    {
      oneDHists_.at (trigger).at (channel + "_metDir/metPt")->Fill (met.pt ());

      twoDHists_.at (trigger).at (channel + "_metDir/pfMETNoMuVsPFMET")->Fill (met.pt (), metNoMu.Mod ());
      twoDHists_.at (trigger).at (channel + "_metDir/hltMetVsPFMET")->Fill (met.pt (), hltMet.pt ());
      twoDHists_.at (trigger).at (channel + "_metDir/hltMetCleanVsPFMET")->Fill (met.pt (), hltMetClean.pt ());
    }
  oneDHists_.at (trigger).at (channel + "_metDir/pfMETNoMuPt")->Fill (metNoMu.Mod ());

  twoDHists_.at (trigger).at (channel + "_metDir/hltMetVsPFMETNoMu")->Fill (metNoMu.Mod (), hltMet.pt ());
  twoDHists_.at (trigger).at (channel + "_metDir/hltMetCleanVsPFMETNoMu")->Fill (metNoMu.Mod (), hltMetClean.pt ());

  oneDHists_.at (trigger).at (channel + "_muonDir/muonPt")->Fill (track.pt ());
}

template<class T> void
TriggerEfficiency<T>::fillHistograms (const vector<pat::MET> &mets, const TVector2 &metNoMu, const pat::TriggerObjectStandAlone &hltMet, const pat::TriggerObjectStandAlone &hltMetClean, const vector<T> &tracks, const string &channel, const string &trigger) const
{
  for (const auto &met : mets)
    {
      oneDHists_.at (trigger).at (channel + "_metDir/metPt")->Fill (met.pt ());

      twoDHists_.at (trigger).at (channel + "_metDir/pfMETNoMuVsPFMET")->Fill (met.pt (), metNoMu.Mod ());
      twoDHists_.at (trigger).at (channel + "_metDir/hltMetVsPFMET")->Fill (met.pt (), hltMet.pt ());
      twoDHists_.at (trigger).at (channel + "_metDir/hltMetCleanVsPFMET")->Fill (met.pt (), hltMetClean.pt ());
    }
  oneDHists_.at (trigger).at (channel + "_metDir/pfMETNoMuPt")->Fill (metNoMu.Mod ());

  twoDHists_.at (trigger).at (channel + "_metDir/hltMetVsPFMETNoMu")->Fill (metNoMu.Mod (), hltMet.pt ());
  twoDHists_.at (trigger).at (channel + "_metDir/hltMetCleanVsPFMETNoMu")->Fill (metNoMu.Mod (), hltMetClean.pt ());

  for (const auto &track : tracks)
    oneDHists_.at (trigger).at (channel + "_muonDir/muonPt")->Fill (track.pt ());
}

template<class T> const pat::TriggerObjectStandAlone &
TriggerEfficiency<T>::getHLTMET (const edm::TriggerNames &triggerNames, const vector<pat::TriggerObjectStandAlone> &triggerObjs, const string &collection) const
{
  unsigned i = 0;
  for (auto triggerObj : triggerObjs)
    {
      triggerObj.unpackPathNames (triggerNames);
      if (triggerObj.collection () == (collection + "::HLT"))
        return triggerObjs.at (i);
      i++;
    }

  pat::TriggerObjectStandAlone *dummy = new pat::TriggerObjectStandAlone ();
  return *dummy;
}

template<class T> bool
TriggerEfficiency<T>::passesTriggerFilter (const edm::TriggerNames &triggerNames, const vector<pat::TriggerObjectStandAlone> &triggerObjs, const string &filter) const
{
  for (auto triggerObj : triggerObjs)
    {
      triggerObj.unpackPathNames (triggerNames);
      for (const auto &filterLabel : triggerObj.filterLabels ())
        {
          if (filterLabel == filter)
            return true;
        }
    }
  return false;
}

template<class T> bool
TriggerEfficiency<T>::passesTrigger (const edm::TriggerNames &triggerNames, const edm::TriggerResults &triggerBits, const string &path) const
{
  for (unsigned i = 0; i < triggerNames.size (); i++)
    {
      string name = triggerNames.triggerName (i);
      bool pass = triggerBits.accept (i);
      if (name.find (path) == 0)
        return pass;
    }
  return false;
}

template<class T> double
TriggerEfficiency<T>::trackIsolation (const reco::Track &track, const vector<reco::Track> &tracks, const double outerDeltaR, const double innerDeltaR) const
{
  double sumPt = 0.0;

  for (const auto &t : tracks)
    {
      double dR = deltaR (track, t);
      if (dR < outerDeltaR && dR > innerDeltaR)
        sumPt += t.pt ();
    }

  return sumPt;
}

template<class T> bool
TriggerEfficiency<T>::genMatched (const T &track, const vector<reco::GenParticle> &genParticles, const int pdgId, const int status, const double maxDeltaR) const
{
  for (const auto &genParticle : genParticles)
    {
      if (abs (genParticle.pdgId ()) != abs (pdgId))
        continue;
      if (genParticle.status () != status)
        break;
      if (deltaR (track, genParticle) > maxDeltaR)
        continue;
      return true;
    }
  return false;
}

template<class T> bool
TriggerEfficiency<T>::hasGoodMuon (const vector<pat::Muon> &muons, const reco::Vertex &pv) const
{
  for (const auto &muon : muons)
    {
      if (fabs (muon.eta ()) > 2.1)
        continue;
      if (muon.pt () < 25.0)
        continue;
      if (!muon.isTightMuon (pv))
        continue;

      const reco::MuonPFIsolation &iso = muon.pfIsolationR03 ();
      if ((iso.sumChargedHadronPt + max (0.0, iso.sumNeutralHadronEt + iso.sumPhotonEt - 0.5 * iso.sumPUPt)) > 0.15 * muon.pt ())
        continue;

      return true;
    }
  return false;
}

template<> bool
TriggerEfficiency<reco::Track>::isGoodTrack (const reco::Track &track, const reco::Vertex &pv, const vector<reco::Track> &tracks) const
{
  if (fabs (track.eta ()) > 2.5)
    return false;
  if (track.normalizedChi2 () > 10.0)
    return false;
  if (fabs (track.dxy (pv.position ())) > 0.2)
    return false;
  if (fabs (track.dz (pv.position ())) > 0.5)
    return false;
  if (track.hitPattern ().numberOfValidPixelHits () == 0)
    return false;
  if (track.hitPattern ().trackerLayersWithMeasurement () <= 5)
    return false;
  if (track.hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::MISSING_INNER_HITS) > 0)
    return false;
  if (track.hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::TRACK_HITS) > 0)
    return false;
  if (trackIsolation (track, tracks, 0.3, 1.0e-12) > 0.01 * track.pt ())
    return false;
  return true;
}

template<> bool
TriggerEfficiency<reco::Track>::isGoodTrack (const reco::Track &track, const reco::Vertex &pv, const vector<reco::Track> &tracks, const vector<reco::GenParticle> &genParticles) const
{
  if (!isGoodTrack (track, pv, tracks))
    return false;
  if (!genMatched (track, genParticles, 1000024, 3, 0.1))
    return false;
  return true;
}

template<> bool
TriggerEfficiency<pat::Muon>::isGoodTrack (const pat::Muon &muon, const reco::Vertex &pv, const vector<pat::Muon> &muons) const
{
  if (fabs (muon.eta ()) > 2.1)
    return false;
  if (!muon.isGlobalMuon ())
    return false;
  if (!muon.isPFMuon ())
    return false;
  if (muon.globalTrack ()->normalizedChi2 () > 10.0)
    return false;
  if (muon.globalTrack ()->hitPattern ().numberOfValidMuonHits () == 0)
    return false;
  if (muon.numberOfMatchedStations () <= 1)
    return false;
  if (fabs (muon.muonBestTrack ()->dxy (pv.position ())) > 0.2)
    return false;
  if (fabs (muon.muonBestTrack ()->dz (pv.position ())) > 0.5)
    return false;
  if (muon.innerTrack ()->hitPattern ().numberOfValidPixelHits () == 0)
    return false;
  if (muon.innerTrack ()->hitPattern ().trackerLayersWithMeasurement () <= 5)
    return false;
  if (muon.innerTrack ()->hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::MISSING_INNER_HITS) > 0)
    return false;
  if (muon.innerTrack ()->hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::TRACK_HITS) > 0)
    return false;
  if ((muon.isolationR03 ().sumPt / muon.pt ()) > 0.01)
    return false;
  return true;
}

template<> bool
TriggerEfficiency<pat::Muon>::isGoodTrack (const pat::Muon &muon, const reco::Vertex &pv, const vector<pat::Muon> &muons, const vector<reco::GenParticle> &genParticles) const
{
  return isGoodTrack (muon, pv, muons);
}

typedef TriggerEfficiency<reco::Track> TriggerEfficiencyWithTracks;
typedef TriggerEfficiency<pat::Muon> TriggerEfficiencyWithMuons;

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(TriggerEfficiencyWithTracks);
DEFINE_FWK_MODULE(TriggerEfficiencyWithMuons);
