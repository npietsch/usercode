#include <iostream>
#include "TROOT.h"
#include "TH1D.h"
#include "TFile.h"


void PU() {
  //TDirectory* keep = gDirectory->GetDirectory("");
  TFile* ORGPUDIST = new TFile("temp.root");

  cout<<"file read"<<endl;

  TH1D* orgpuT = (TH1D*) ORGPUDIST->Get("analyzeSUSY1m_noCuts/nPU"); //->Clone("puorg");
  TH1D* orgpu = (TH1D*) orgpuT->Clone("puorg");
  cout<<"histo cloned"<<endl;

  //delete orgpuT;
  //keep->cd();
  //ORGPUDIST->Close();

  TH1D* rebpu = new TH1D("pileup2","pileup", 71, -0.5, 70.5);

  for(int i=1; i<=orgpu->GetXaxis()->GetNbins(); i++) {
    cout<<i<<"    "<<orgpu->GetBinContent(i)<<endl;
    rebpu->SetBinContent(i,orgpu->GetBinContent(i+1));
    rebpu->SetBinError(i,orgpu->GetBinError(i+1));
  }
  for(int i2=orgpu->GetXaxis()->GetNbins()+1; i2<=rebpu->GetXaxis()->GetNbins(); i2++) {
    cout<<i2<<"    "<<0<<endl;
    
    rebpu->SetBinContent(i2,0);
  }

  //  orgpu->Delete();
  //ORGPUDIST->Close();

   rebpu->SetName("pileup");

   rebpu->Draw();

   TFile* REBPUDIST = new TFile("PU_Fall11_WJetsHT300.root","RECREATE");
   rebpu->Write();
   REBPUDIST->Close();
   //   ORGPUDIST->Close();
}
