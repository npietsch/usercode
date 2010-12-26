#ifndef SUSYObjects_SUSYEvent_h
#define SUSYObjects_SUSYEvent_h

#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

#include "DataFormats/PatCandidates/interface/Muon.h"

class SUSYEvent {

 public:

  /// empty constructor
  SUSYEvent(){};
  /// default destructor
  virtual ~SUSYEvent(){};

  /// return number of leptons
  int leptons() const;

/*  protected: */

/*   // reference to muon collection */
/*   std::vector<pat::Muon> muons_; */

};

#endif
