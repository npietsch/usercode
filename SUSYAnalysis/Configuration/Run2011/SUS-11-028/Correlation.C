#include <vector>
#include <iostream>
#include <bitset>
#include <fstream>
#include "TFile.h"
#include "TH1.h"
#include "TH2.h"
#include "TProfile2D.h"
#include "TCanvas.h"
#include "TStyle.h"
#include "TLegend.h"
#include "TPaveText.h"

int Correlation()
{
  // Define file
  TFile* TTJets = new TFile("TTJetsFall11.root" , "READ");

  // Read from file
  //TH2F* HT_MET=(TH2F*)TTJets->Get("analyzeTtGenEvent_noCuts_1m/HT_MET_acceptance");
  //TH2F* HT_MET=(TH2F*)TTJets->Get("analyzeTtGenEvent_leptonSelection_1m/HT_MET_acceptance");
  //TH2F* ttbarMass_HT  = (TH2F*)TTJets->Get("analyzeTtGenEvent_noCuts_1m/ttbarMass_HT");
  //TH2F* ttbarMass_MET = (TH2F*)TTJets->Get("analyzeTtGenEvent_noCuts_1m/ttbarMass_MET");
  TH2F* qScale_HT = (TH2F*)TTJets->Get("analyzeTtGenEvent_noCuts_1m/qScale_HT");
  TH2F* PDFScale_HT = (TH2F*)TTJets->Get("analyzeTtGenEvent_noCuts_1m/PDFScale_HT");

  TCanvas *canvas =new TCanvas("c1","c1",1);

  TProfile2D* qScale =(TProfile2D*)qScale_HT->ProfileX();
  TProfile2D* PDFScale =(TProfile2D*)PDFScale_HT->ProfileX();
  //TProfile2D* MET=(TProfile2D*)ttbarMass_MET->ProfileX();

  qScale->Draw("");
  PDFScale->Draw("same");

}
