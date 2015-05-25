import FWCore.ParameterSet.Config as cms

ggll = cms.EDAnalyzer('GammaGammaLL',
    SqrtS = cms.double(13000.),
    #HLTMenuLabel = cms.string("HLT"),
    HLTMenuLabel = cms.string("NOHLT"),
    LeptonsType = cms.InputTag('electron', 'muon'),
    maxExtraTracks = cms.untracked.uint32(10000),
    isoValInputTags = cms.VInputTag(
        cms.InputTag('elPFIsoValueCharged03PFIdPFIso'),
        cms.InputTag('elPFIsoValueGamma03PFIdPFIso'),
        cms.InputTag('elPFIsoValueNeutral03PFIdPFIso')
    ),
    beamSpotInputTag = cms.InputTag('offlineBeamSpot'),
    conversionsInputTag = cms.InputTag('allConversions'),
    rhoIsoInputTag = cms.InputTag('kt6PFJetsForIsolation', 'rho'),
    JetCollectionLabel = cms.InputTag('selectedPatJetsPFlow'),
    MetLabel = cms.InputTag('pfMETPFlow'),
    GlobalMuonCollectionLabel = cms.untracked.InputTag('selectedPatMuonsPFlow'), 
    GlobalEleCollectionLabel = cms.untracked.InputTag('selectedPatElectronsPFlow'),
    RunOnMC = cms.untracked.bool(True),
    MCAcceptPtCut = cms.untracked.double(0.),
    MCAcceptEtaCut = cms.untracked.double(-1.),
    GenParticlesCollectionLabel = cms.InputTag('genParticles'),
    PrintCandidates = cms.untracked.bool(False),
    mcpufile = cms.untracked.string(""),
    datapufile = cms.untracked.string(""),
)
