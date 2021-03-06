import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/user/pakhotin/DarkSUSY_mH_125_mGammaD_1000_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_125_mGammaD_1000_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/d7ec853f1412ed77b3135ca95d8b3a46/output_9_1_WWX.root',
       '/store/user/pakhotin/DarkSUSY_mH_125_mGammaD_1000_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_125_mGammaD_1000_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/d7ec853f1412ed77b3135ca95d8b3a46/output_8_1_HHy.root',
       '/store/user/pakhotin/DarkSUSY_mH_125_mGammaD_1000_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_125_mGammaD_1000_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/d7ec853f1412ed77b3135ca95d8b3a46/output_7_1_bA2.root',
       '/store/user/pakhotin/DarkSUSY_mH_125_mGammaD_1000_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_125_mGammaD_1000_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/d7ec853f1412ed77b3135ca95d8b3a46/output_6_1_Ncm.root',
       '/store/user/pakhotin/DarkSUSY_mH_125_mGammaD_1000_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_125_mGammaD_1000_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/d7ec853f1412ed77b3135ca95d8b3a46/output_5_1_Zwm.root',
       '/store/user/pakhotin/DarkSUSY_mH_125_mGammaD_1000_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_125_mGammaD_1000_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/d7ec853f1412ed77b3135ca95d8b3a46/output_4_1_jUF.root',
       '/store/user/pakhotin/DarkSUSY_mH_125_mGammaD_1000_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_125_mGammaD_1000_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/d7ec853f1412ed77b3135ca95d8b3a46/output_3_1_7th.root',
       '/store/user/pakhotin/DarkSUSY_mH_125_mGammaD_1000_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_125_mGammaD_1000_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/d7ec853f1412ed77b3135ca95d8b3a46/output_2_1_A8N.root',
       '/store/user/pakhotin/DarkSUSY_mH_125_mGammaD_1000_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_125_mGammaD_1000_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/d7ec853f1412ed77b3135ca95d8b3a46/output_1_1_zsO.root',
       '/store/user/pakhotin/DarkSUSY_mH_125_mGammaD_1000_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_125_mGammaD_1000_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/d7ec853f1412ed77b3135ca95d8b3a46/output_16_1_qTy.root',
       '/store/user/pakhotin/DarkSUSY_mH_125_mGammaD_1000_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_125_mGammaD_1000_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/d7ec853f1412ed77b3135ca95d8b3a46/output_15_1_627.root',
       '/store/user/pakhotin/DarkSUSY_mH_125_mGammaD_1000_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_125_mGammaD_1000_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/d7ec853f1412ed77b3135ca95d8b3a46/output_14_1_nnO.root',
       '/store/user/pakhotin/DarkSUSY_mH_125_mGammaD_1000_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_125_mGammaD_1000_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/d7ec853f1412ed77b3135ca95d8b3a46/output_13_1_Qse.root',
       '/store/user/pakhotin/DarkSUSY_mH_125_mGammaD_1000_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_125_mGammaD_1000_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/d7ec853f1412ed77b3135ca95d8b3a46/output_12_1_h68.root',
       '/store/user/pakhotin/DarkSUSY_mH_125_mGammaD_1000_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_125_mGammaD_1000_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/d7ec853f1412ed77b3135ca95d8b3a46/output_11_1_pnU.root',
       '/store/user/pakhotin/DarkSUSY_mH_125_mGammaD_1000_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_GEN_v2/DarkSUSY_mH_125_mGammaD_1000_ctauExp_05_8TeV-madgraph452_bridge224_LHE_pythia6_537p4_PAT_v1/d7ec853f1412ed77b3135ca95d8b3a46/output_10_1_g4k.root' ] );


secFiles.extend( [
               ] )
