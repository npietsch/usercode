#include <iostream>
#include "TROOT.h"
#include "TH1D.h"
#include "TFile.h"

vector<TString> Names;

void PU70() {

  Names.push_back("TTJetsFall11");
  Names.push_back("WJetsHT");
  Names.push_back("WJetsHT250");
  Names.push_back("WJetsHT300");
  Names.push_back("LM3");
  Names.push_back("LM8");
  Names.push_back("LM13");

  for(int sdx=0; sdx<(int)Names.size(); ++sdx)
    {
      
      TFile* file = new TFile(Names[sdx]+".root");
      
      cout<< "Read file" <<endl;
      
      TH1D* nPU = (TH1D*) file->Get("analyzeSUSY1m_noCuts/nPU_noWgt");
      
      cout<<"Clone file"<<endl;
      
      TH1D* nPU_new = (TH1D*) nPU->Clone("pileup");
 
      nPU_new->Draw();
      
      TFile* file_new = new TFile("PU_"+Names[sdx]+".root","RECREATE");
      nPU_new->Write();
      file_new->Close();
    }
}
