#include <TROOT.h>
#include "TFile.h"
#include "TH1.h"
#include "TH2.h"
#include "TTree.h"
#include "TKey.h"
#include "TF1.h"
#include <iostream>
#include <fstream>
#include <sstream>

// main function
int Gluino()
{
  TFile* Daniel=new TFile("Bjets.root","READ");

  TH1F* Mjj_=(TH1F*)Daniel->Get("analyzeGluino/mjj");

  //gStyle->SetErrorX(0);

  TCanvas *c1 =new TCanvas( "LM9" , "LM9" ,1);
  Mjj_->Draw("L");

}
