#ifndef TRACK_COLLECTION_ANALYZER
#define TRACK_COLLECTION_ANALYZER

#include "TTree.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/PatCandidates/interface/IsolatedTrack.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

#include "DataFormats/Math/interface/deltaR.h"

#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/PatCandidates/interface/Jet.h"

#include "DisappTrks/CandidateTrackProducer/interface/CandidateTrack.h"

using namespace std;

class TrackCollectionAnalyzer : public edm::EDAnalyzer {
public:
    explicit TrackCollectionAnalyzer(const edm::ParameterSet &);
    ~TrackCollectionAnalyzer();

private:
    void analyze(const edm::Event &, const edm::EventSetup &);

    const bool disappearingTrackSelection(const CandidateTrack &, 
                                          const reco::Vertex &,
                                          const vector<pat::Jet> &,
                                          const vector<pat::Electron> &,
                                          const vector<pat::Muon> &,
                                          const vector<pat::Tau> &) const;

    edm::InputTag generalTracks_;
    edm::InputTag packedCandidates_;
    edm::InputTag lostTracks_;
    edm::InputTag isolatedTracks_;

    edm::InputTag genParticles_;

    edm::InputTag vertices_, electrons_, muons_, taus_, jets_;

    edm::EDGetTokenT<vector<CandidateTrack> > generalTracksToken_;
    edm::EDGetTokenT<pat::PackedCandidateCollection> packedCandidatesToken_;
    edm::EDGetTokenT<pat::PackedCandidateCollection> lostTracksToken_;
    edm::EDGetTokenT<vector<pat::IsolatedTrack> > isolatedTracksToken_;

    edm::EDGetTokenT<vector<reco::GenParticle> > genParticlesToken_;

    edm::EDGetTokenT<vector<reco::Vertex> >  verticesToken_;
    edm::EDGetTokenT<vector<pat::Electron> > electronsToken_;
    edm::EDGetTokenT<vector<pat::Muon> >     muonsToken_;
    edm::EDGetTokenT<vector<pat::Tau> >      tausToken_;
    edm::EDGetTokenT<vector<pat::Jet> >      jetsToken_;

    edm::Service<TFileService> fs_;
    TTree * tree_;

    vector<bool> isInPackedCandidates;
    vector<bool> isInLostTracks;
    vector<bool> isInIsolatedTracks;

    vector<double> pt, eta, phi;
    vector<double> vx, vy, vz;
    vector<double> d0Error, dzError;
    vector<int> charge;

    vector<double> trackIsoNoPUDRp3;

    vector<bool> passesSelection;

    vector<double> genMatchDR;
    vector<int> genMatchID;
};

TrackCollectionAnalyzer::TrackCollectionAnalyzer(const edm::ParameterSet &cfg) :
    generalTracks_   (cfg.getParameter<edm::InputTag>("tracks")),
    packedCandidates_(cfg.getParameter<edm::InputTag>("packedCandidates")),
    lostTracks_      (cfg.getParameter<edm::InputTag>("lostTracks")),
    isolatedTracks_  (cfg.getParameter<edm::InputTag>("isolatedTracks")),
    genParticles_    (cfg.getParameter<edm::InputTag>("genParticles")),
    vertices_        (cfg.getParameter<edm::InputTag>("vertices")),
    electrons_       (cfg.getParameter<edm::InputTag>("electrons")),
    muons_           (cfg.getParameter<edm::InputTag>("muons")),
    taus_            (cfg.getParameter<edm::InputTag>("taus")),
    jets_            (cfg.getParameter<edm::InputTag>("jets"))
{
    generalTracksToken_    = consumes<vector<CandidateTrack> >       (generalTracks_);
    packedCandidatesToken_ = consumes<pat::PackedCandidateCollection>(packedCandidates_);
    lostTracksToken_       = consumes<pat::PackedCandidateCollection>(lostTracks_);
    isolatedTracksToken_   = consumes<vector<pat::IsolatedTrack> >   (isolatedTracks_);

    genParticlesToken_ = consumes<vector<reco::GenParticle> >(genParticles_);

    verticesToken_     = consumes<vector<reco::Vertex> > (vertices_);
    electronsToken_    = consumes<vector<pat::Electron> >(electrons_);
    muonsToken_        = consumes<vector<pat::Muon> >    (muons_);
    tausToken_         = consumes<vector<pat::Tau> >     (taus_);
    jetsToken_         = consumes<vector<pat::Jet> >     (jets_);

    tree_ = fs_->make<TTree>("tree", "tree");

    tree_->Branch("isInPackedCandidates", &isInPackedCandidates);
    tree_->Branch("isInLostTracks", &isInLostTracks);
    tree_->Branch("isInIsolatedTracks", &isInIsolatedTracks);

    tree_->Branch("pt", &pt);
    tree_->Branch("eta", &eta);
    tree_->Branch("phi", &phi);

    tree_->Branch("vx", &vx);
    tree_->Branch("vy", &vy);
    tree_->Branch("vz", &vz);
    tree_->Branch("d0Error", &d0Error);
    tree_->Branch("dzError", &dzError);

    tree_->Branch("charge", &charge);

    tree_->Branch("trackIsoNoPUDRp3", &trackIsoNoPUDRp3);

    tree_->Branch("passesSelection", &passesSelection);

    tree_->Branch("genMatchDR", &genMatchDR);
    tree_->Branch("genMatchID", &genMatchID);
}

TrackCollectionAnalyzer::~TrackCollectionAnalyzer() 
{
}

void TrackCollectionAnalyzer::analyze(const edm::Event &event, const edm::EventSetup &setup)
{
    edm::Handle<vector<CandidateTrack> >        generalTracks;
    edm::Handle<pat::PackedCandidateCollection> packedCandidates;   
    edm::Handle<pat::PackedCandidateCollection> lostTracks; 
    edm::Handle<vector<pat::IsolatedTrack> >    isolatedTracks;

    edm::Handle<vector<reco::GenParticle> > genParticles;

    edm::Handle<vector<reco::Vertex> > vertices;
    edm::Handle<vector<pat::Electron> > electrons;
    edm::Handle<vector<pat::Muon> > muons;
    edm::Handle<vector<pat::Tau> > taus;
    edm::Handle<vector<pat::Jet> > jets;

    event.getByToken(generalTracksToken_,    generalTracks);
    event.getByToken(packedCandidatesToken_, packedCandidates);
    event.getByToken(lostTracksToken_,       lostTracks);
    event.getByToken(isolatedTracksToken_,   isolatedTracks);

    event.getByToken(genParticlesToken_, genParticles);

    event.getByToken(verticesToken_, vertices);
    event.getByToken(electronsToken_, electrons);
    event.getByToken(muonsToken_, muons);
    event.getByToken(tausToken_, taus);
    event.getByToken(jetsToken_, jets);

    isInPackedCandidates.clear();
    isInLostTracks.clear();
    isInIsolatedTracks.clear();

    pt.clear();
    eta.clear();
    phi.clear();

    vx.clear();
    vy.clear();
    vz.clear();
    d0Error.clear();
    dzError.clear();

    charge.clear();

    trackIsoNoPUDRp3.clear();

    passesSelection.clear();

    genMatchDR.clear();
    genMatchID.clear();

    for(unsigned int i = 0; i < generalTracks->size(); i++) {

        const CandidateTrack &gentk = (*generalTracks)[i];
        //reco::TrackRef tkref = reco::TrackRef(generalTracks, i);
        edm::Ref<vector<CandidateTrack> > tkref = edm::Ref<vector<CandidateTrack> >(generalTracks, i);

        bool this_inPackedCandidates = false;
        for(const auto& pc : *packedCandidates) {
            double dR = deltaR(gentk, pc);
            if(dR < 0.001) {
                this_inPackedCandidates = true;
                break;
            }
        }
        isInPackedCandidates.push_back(this_inPackedCandidates);

        bool this_inLostTracks = false;
        for(const auto& lt : *lostTracks) {
            double dR = deltaR(gentk, lt);
            if(dR < 0.001) {
                this_inLostTracks = true;
                break;
            }
        }
        isInLostTracks.push_back(this_inLostTracks);

        bool this_isInIsolatedTracks = false;
        for(const auto& isoTrack : *isolatedTracks) {
            double dR = deltaR(gentk, isoTrack);
            if(dR < 0.001) {
                this_isInIsolatedTracks = true;
                break;
            }
        }
        isInIsolatedTracks.push_back(this_isInIsolatedTracks);

        pt.push_back(gentk.pt());
        eta.push_back(gentk.eta());
        phi.push_back(gentk.phi());

        vx.push_back(gentk.vx());
        vy.push_back(gentk.vy());
        vz.push_back(gentk.vz());
        d0Error.push_back(gentk.d0Error());
        dzError.push_back(gentk.dzError());

        charge.push_back(gentk.charge());

        trackIsoNoPUDRp3.push_back(gentk.trackIsoNoPUDRp3());

        passesSelection.push_back(disappearingTrackSelection(gentk, vertices->at(0), *jets, *electrons, *muons, *taus));

        double this_genMatchDR = -1;
        int this_genMatchID = 0;

        if(genParticles.isValid()) {
            for(const auto& genParticle : *genParticles) {
                if(!genParticle.isPromptFinalState() && !genParticle.isDirectPromptTauDecayProductFinalState()) {
                    continue;
                }
                double dR = deltaR(gentk, genParticle);
                if(this_genMatchDR < 0 || dR < this_genMatchDR) {
                    this_genMatchID = genParticle.pdgId();
                    this_genMatchDR = dR;
                }
            }
        }

        genMatchDR.push_back(this_genMatchDR);
        genMatchID.push_back(this_genMatchID);
    }

    tree_->Fill();

}

const bool TrackCollectionAnalyzer::disappearingTrackSelection(
    const CandidateTrack        &track, 
    const reco::Vertex          &pv,
    const vector<pat::Jet>      &jets,
    const vector<pat::Electron> &electrons,
    const vector<pat::Muon>     &muons,
    const vector<pat::Tau>      &taus) const {

    // d0 wrt pv (2d) = (vertex - pv) cross p / |p|
    double d0 = ((track.vx() - pv.x()) * track.py() - (track.vy() - pv.y()) * track.px()) / track.pt(); 
  
    // dz wrt pv (2d) = (v_z - pv_z) - p_z * [(vertex - pv) dot p / |p|^2]
    double dz = track.vz() - pv.z() -
      ((track.vx() - pv.x()) * track.px() + (track.vy() - pv.y()) * track.py()) * track.pz() / track.pt() / track.pt();

    bool passes = (track.pt() > 55 &&
                   fabs(track.eta()) < 2.1 &&
                   // skip fiducial selections
                   !(fabs(track.dz()) < 0.5 && fabs(M_PI_2 - track.theta()) < 1.0e-3) &&
                   !(fabs(track.eta()) >= 1.42 && fabs(track.eta()) <= 1.65) &&
                   !(fabs(track.eta()) >= 0.15 && fabs(track.eta()) <= 0.35) &&
                   !(fabs(track.eta()) >= 1.55 && fabs(track.eta()) <= 1.85) &&
                   track.hitPattern().numberOfValidPixelHits() >= 4 &&
                   track.hitPattern().numberOfValidHits() >= 4 &&
                   track.missingInnerHits_() == 0 &&
                   track.missingMiddleHits_() == 0 &&
                   // track isolation under study
                   fabs(d0) < 0.02 &&
                   fabs(dz) < 0.5);

    if(!passes) return false;

    double deltaRToClosestElectron = -1;
    for(const auto &electron : electrons) {
      double thisDR = deltaR(electron, track);
      if(deltaRToClosestElectron < 0 || thisDR < deltaRToClosestElectron) deltaRToClosestElectron = thisDR;
    }
    if(fabs(deltaRToClosestElectron) <= 0.15) return false;

    double deltaRToClosestMuon = -1;
    for(const auto &muon : muons) {
      double thisDR = deltaR(muon, track);
      if(deltaRToClosestMuon < 0 || thisDR < deltaRToClosestMuon) deltaRToClosestMuon = thisDR;
    }
    if(fabs(deltaRToClosestMuon) <= 0.15) return false;

    double deltaRToClosestTauHad = -1;
    for(const auto &tau : taus) {
      if(tau.isTauIDAvailable("againstElectronLooseMVA5")) {
        if(tau.tauID("decayModeFinding") <= 0.5 ||
           tau.tauID("againstElectronLooseMVA5") <= 0.5 ||
           tau.tauID("againstMuonLoose3") <= 0.5) {
          continue;
        }
      }
      else if(tau.isTauIDAvailable("againstElectronLooseMVA6")) {
        if(tau.tauID("decayModeFinding") <= 0.5 ||
           tau.tauID("againstElectronLooseMVA6") <= 0.5 ||
           tau.tauID("againstMuonLoose3") <= 0.5) {
          continue;
        }
      }
      else {
        continue;
      }

      double thisDR = deltaR(tau, track);
      if(deltaRToClosestTauHad < 0 || thisDR < deltaRToClosestTauHad) deltaRToClosestTauHad = thisDR;
    }
    if(fabs(deltaRToClosestTauHad) <= 0.15) return false;

    double dRMinJet = -1;
    for(const auto &jet : jets) {
      if(jet.pt() > 30 &&
         fabs(jet.eta()) < 4.5 &&
         (((jet.neutralHadronEnergyFraction()<0.90 && jet.neutralEmEnergyFraction()<0.90 && (jet.chargedMultiplicity() + jet.neutralMultiplicity())>1 && jet.muonEnergyFraction()<0.8) && ((fabs(jet.eta())<=2.4 && jet.chargedHadronEnergyFraction()>0 && jet.chargedMultiplicity()>0 && jet.chargedEmEnergyFraction()<0.90) || fabs(jet.eta())>2.4) && fabs(jet.eta())<=3.0)
            || (jet.neutralEmEnergyFraction()<0.90 && jet.neutralMultiplicity()>10 && fabs(jet.eta())>3.0))) {
        double dR = deltaR(track, jet);
        if(dRMinJet < 0 || dR < dRMinJet) dRMinJet = dR;
      }
    }
    if(fabs(dRMinJet) <= 0.5) return false;

    if(track.missingOuterHits_() < 3) return false;
    if(track.hitPattern().trackerLayersWithMeasurement() < 4) return false;

    return true;
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(TrackCollectionAnalyzer);

#endif
