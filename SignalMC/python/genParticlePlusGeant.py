import FWCore.ParameterSet.Config as cms

def customizeKeep (process):
  outputTypes = ["RAWSIM", "RECOSIM", "AODSIM", "MINIAODSIM"]
  for a in outputTypes:
    b = a + "output"
    if hasattr (process, b):
      getattr (process, b).outputCommands.append ("keep *_genParticlePlusGeant_*_*")

  return process


def customizeProduce (process):
    process.genParticlePlusGeant = cms.EDProducer("GenPlusSimParticleProducer",
                                                  src = cms.InputTag("g4SimHits"),            # use "famosSimHits" for FAMOS
                                                  setStatus = cms.int32(8),                   # set status = 8 for GEANT GPs 
                                                  filter = cms.vstring("pt > 10.0"),          # just for testing (optional) 
                                                  genParticles = cms.InputTag("genParticles") # original genParticle list 
                                                  )  

    if hasattr (process, "simulation_step") and hasattr(process, "psim"):
      getattr(process, "simulation_step")._seq = getattr(process,"simulation_step")._seq * process.genParticlePlusGeant   

    return process 
