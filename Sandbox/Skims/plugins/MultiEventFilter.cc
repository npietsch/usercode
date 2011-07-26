#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/Parse.h"


class MultiEventFilter : public edm::EDFilter {

  class Event {
    public:
      Event(unsigned int r, unsigned int l, unsigned int e) : run(r), lumi(l), event(e) {}
      unsigned int run;
      unsigned int lumi;
      unsigned int event;
  };

  public:

    explicit MultiEventFilter(const edm::ParameterSet & iConfig);
    ~MultiEventFilter() {}

  private:

    virtual bool filter(edm::Event & iEvent, const edm::EventSetup & iSetup);
    
    std::vector<Event> events_;

};


MultiEventFilter::MultiEventFilter(const edm::ParameterSet & iConfig) {
  std::vector<std::string> eventList = iConfig.getParameter<std::vector<std::string> >("EventList");
  for (unsigned int i = 0; i < eventList.size(); ++i) {
    std::vector<std::string> tokens = edm::tokenize(eventList[i], ":");
    if(tokens.size() != 3) {
      throw edm::Exception(edm::errors::Configuration) << "Incorrect event specification";
      continue;
    }
    events_.push_back(Event(atoi(tokens[0].c_str()), atoi(tokens[1].c_str()), atoi(tokens[2].c_str())));
  }
}


bool MultiEventFilter::filter(edm::Event & iEvent, const edm::EventSetup & iSetup) {

  for (unsigned int i = 0; i < events_.size(); ++i) {
    if (events_[i].event == iEvent.id().event() &&
        events_[i].run == iEvent.id().run() &&
        events_[i].lumi == iEvent.id().luminosityBlock()) return false;
  }
  return true;

}


#include "FWCore/Framework/interface/MakerMacros.h"

DEFINE_FWK_MODULE(MultiEventFilter);
