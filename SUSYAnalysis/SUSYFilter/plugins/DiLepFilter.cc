#include "SUSYAnalysis/SUSYFilter/plugins/DiLepFilter.h"

#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"

/// default constructor
DiLepFilter::DiLepFilter ( const edm::ParameterSet& cfg ) :
    goodElectrons_  (cfg.getParameter<edm::InputTag> ("goodElectrons" ) ),
    goodMuons_      (cfg.getParameter<edm::InputTag> ("goodMuons" ) ),
    looseElectrons_ (cfg.getParameter<edm::InputTag> ("looseElectrons" ) ),
    looseMuons_     (cfg.getParameter<edm::InputTag> ("looseMuons" ) ),

    isVeto_         (cfg.getParameter<bool>                 ("isVeto") ),
    Cut_            (cfg.getParameter<std::vector<double> > ("Cut") ),
    fltrChrg_       (cfg.getParameter<int>                  ("filterCharge") )
{
}

/// default destructor
DiLepFilter::~DiLepFilter()
{
}

/// sanity check
void
DiLepFilter::beginJob()
{
    if ( Cut_.size() !=2 )  edm::LogError ( "DiLepFilter" ) << "Cut has wrong size. Size has to be 2!\n";
    if ( Cut_[0]>Cut_[1] ) edm::LogError ( "DiLepFilter" ) << "Lower cut value is higher than upper one!\n";
}

/// event veto
bool
DiLepFilter::filter ( edm::Event& event, const edm::EventSetup& setup )
{
    enum channel_t { kMM, kEM, kEE };

    // fetch the input collections from the event content
    edm::Handle<std::vector<pat::Electron> > goodElectrons;
    event.getByLabel (goodElectrons_, goodElectrons );
    edm::Handle<std::vector<pat::Muon> > goodMuons;
    event.getByLabel (goodMuons_, goodMuons );
    edm::Handle<std::vector<pat::Electron> > looseElectrons;
    event.getByLabel (looseElectrons_, looseElectrons );
    edm::Handle<std::vector<pat::Muon> > looseMuons;
    event.getByLabel (looseMuons_, looseMuons );

    // skip events with less than two loose
    if ( looseElectrons->size() + looseMuons->size() < 2 ) return false;

    // skip events with less than one good lepton
    if ( goodElectrons->size() + goodMuons->size() < 1 ) return false;

    double maxsumpt = -1;
    const reco::RecoCandidate *lep1 = 0, *lep2 = 0;
    channel_t channel;
    
    //--------------------------------------------------------------------------------------------------------
    // Loop over all possible combinations of two good leptons
    //--------------------------------------------------------------------------------------------------------

    //mumu combinations
    for (std::vector<pat::Muon>::const_iterator goodMuon1 = goodMuons->begin(); goodMuon1 != goodMuons->end(); ++goodMuon1)
      {
        for (std::vector<pat::Muon>::const_iterator goodMuon2 = goodMuon1+1; goodMuon2 != goodMuons->end(); ++goodMuon2)
	  {
            if (! fltrChrg_ || goodMuon1->charge()*goodMuon2->charge() == fltrChrg_)
	      {
                double sumpt = goodMuon1->pt() + goodMuon2->pt();
                if (sumpt > maxsumpt)
		  {
                    //we have found a better solution
                    maxsumpt = sumpt;
                    lep1 = &(*goodMuon1);
                    lep2 = &(*goodMuon2);
                    channel = kMM;
		  } else break;
	      }
	  }
      }
    
    //emu combinations
    for (std::vector<pat::Muon>::const_iterator goodMuon = goodMuons->begin(); goodMuon != goodMuons->end(); ++goodMuon)
      {
        for (std::vector<pat::Electron>::const_iterator goodElec = goodElectrons->begin(); goodElec != goodElectrons->end(); ++goodElec)
	  {
	    if (! fltrChrg_ || goodMuon->charge()*goodElec->charge() == fltrChrg_)
	      {
		double sumpt = goodMuon->pt() + goodElec->pt();
		if (sumpt > maxsumpt)
		  {
		    //we have found a better solution
		    maxsumpt = sumpt;
		    lep1 = &(*goodMuon);
		    lep2 = &(*goodElec);

		    channel = kEM;
		  } else break;
	      }
	  }
      }

    //ee combinations
    for (std::vector<pat::Electron>::const_iterator goodElec1 = goodElectrons->begin(); goodElec1 != goodElectrons->end(); ++goodElec1) 
      {
        for (std::vector<pat::Electron>::const_iterator goodElec2 = goodElec1+1; goodElec2 != goodElectrons->end(); ++goodElec2)
	  {
            if (! fltrChrg_ || goodElec1->charge()*goodElec2->charge() == fltrChrg_)
	      {
		double sumpt = goodElec1->pt() + goodElec2->pt();
		if (sumpt > maxsumpt)
		  {
		    //we have found a better solution
		    maxsumpt = sumpt;
		    lep1 = &(*goodElec1);
		    lep2 = &(*goodElec2);
		    channel = kEE;
		  } else break;
	      }
	  }
      }
    
    //---------------------------------------------------------------------------------------------------------
    // If no combination found yet: Loop over all possible combinations of one good and one loose lepton
    //---------------------------------------------------------------------------------------------------------

    if(maxsumpt < 0)
      {
	//mumu combinations
	for(std::vector<pat::Muon>::const_iterator goodMuon = goodMuons->begin(); goodMuon != goodMuons->end(); ++goodMuon)
	  {
	    for(std::vector<pat::Muon>::const_iterator looseMuon = looseMuons->begin(); looseMuon != looseMuons->end(); ++looseMuon)
	      {
		if (goodMuon->pt() != looseMuon->pt() && (! fltrChrg_ || goodMuon->charge()*looseMuon->charge() == fltrChrg_) )
		  {
		    double sumpt = goodMuon->pt() + looseMuon->pt();
		    if (sumpt > maxsumpt)
		      {
			//we have found a better solution
			maxsumpt = sumpt;
			lep1 = &(*goodMuon);
			lep2 = &(*looseMuon);
			channel = kMM;
		      } else break;
		  }
	      }
	  }
	
	//mue combinations
	for (std::vector<pat::Muon>::const_iterator goodMuon = goodMuons->begin(); goodMuon != goodMuons->end(); ++goodMuon)
	  {
	    for (std::vector<pat::Electron>::const_iterator looseElec = looseElectrons->begin(); looseElec != looseElectrons->end(); ++looseElec)
	      {
		if (! fltrChrg_ || goodMuon->charge()*looseElec->charge() == fltrChrg_)
		  {
		    double sumpt = goodMuon->pt() + looseElec->pt();
		    if (sumpt > maxsumpt)
		      {
			//we have found a better solution
			maxsumpt = sumpt;
			lep1 = &(*goodMuon);
			lep2 = &(*looseElec);
			channel = kEM;
		      } else break;
		  }
	      }
	  }
	
	//emu combinations
	for (std::vector<pat::Electron>::const_iterator goodElec = goodElectrons->begin(); goodElec != goodElectrons->end(); ++goodElec)
	  {
	    for (std::vector<pat::Muon>::const_iterator looseMuon = looseMuons->begin(); looseMuon != looseMuons->end(); ++looseMuon)
	      {
		if (! fltrChrg_ || goodElec->charge()*looseMuon->charge() == fltrChrg_)
		  {
		    double sumpt = goodElec->pt() + looseMuon->pt();
		    if (sumpt > maxsumpt)
		      {
			//we have found a better solution
			maxsumpt = sumpt;
			lep1 = &(*goodElec);
			lep2 = &(*looseMuon);
			channel = kEM;
		      } else break;
		  }
	      }
	  }
	
	//ee combinations
	for (std::vector<pat::Electron>::const_iterator goodElec = goodElectrons->begin(); goodElec != goodElectrons->end(); ++goodElec) 
	  {
	    for (std::vector<pat::Elctron>::const_iterator looseElec = goodElec+1; looseElec != goodElectrons->end(); ++looseElec)
	      {
		if (goodElec->pt() != looseElec->pt() && (! fltrChrg_ || goodElec->charge()*looseElec->charge() == fltrChrg_) )
		  {
		    double sumpt = goodElec->pt() + looseElec->pt();
		    if (sumpt > maxsumpt)
		      {
			//we have found a better solution
			maxsumpt = sumpt;
			lep1 = &(*goodElec);
			lep2 = &(*looseElec);
			channel = kEE;
		      } else break;
		  }
	      }
	  }
      }
    
    if (maxsumpt < 0) return false;

    double diLeptonMass = (lep1->p4() + lep2->p4()).M();
    
    // check if events in mass window are to be selected or vetoed
    if ( isVeto_ )
      {
        if ( diLeptonMass >= Cut_[0] && diLeptonMass <= Cut_[1] ) return false;
      } 
    else
      {
	if ( diLeptonMass < Cut_[0] || diLeptonMass > Cut_[1] ) return false;
      }
 
    return true;
}
