#include <vector>
#include <iostream>
#include <bitset>
#include <vector>
#include <fstream>
#include "TFile.h"
#include "TH1.h"
#include "TH2.h"
#include "TF1.h"
#include "TCanvas.h"
#include "TStyle.h"
#include "TLegend.h"
#include "TPaveText.h"
#include "TDRStyle_BtagEfficienciesAllEta.h"

vector<TFile*> Files;
vector<TString> Labels;
vector<unsigned int> SampleColors;
vector<unsigned int> MarkerStyles;
vector<double> MarkerSizes;
vector<unsigned int> FitStyles;

vector<TString> Steps;
vector<unsigned int> LineColors;
vector<TString> SelectionNames;

vector<TH1F*> Histograms;

// function addSample
void addSample(TFile* sample, TString label, int lc, int ms, double msize, int fs);

void addSample(TFile* sample, TString label, int lc, int ms, double msize, int fs)
{
  Files.push_back(sample);
  Labels.push_back(label);
  SampleColors.push_back(lc);
  MarkerStyles.push_back(ms);
  MarkerSizes.push_back(msize);
  FitStyles.push_back(fs);
}

int BtagEfficiencyWeighting()
{
  //-----------------------------------------------------
  // Define samples
  //-----------------------------------------------------

  TFile* TTJets    = new TFile("TTJetsFall11.root",   "READ");
  TFile* WJetsHT   = new TFile("WJetsHT.root",        "READ");
  TFile* SingleTop = new TFile("SingleTop.root",      "READ");

  TFile* ZJets     = new TFile("ZJets.root",          "READ");
  TFile* QCD       = new TFile("QCD.root",            "READ");

  //TFile* LM3       = new TFile("LM3.root",            "READ");
  //TFile* LM8       = new TFile("LM8.root",            "READ");
  //TFile* LM13      = new TFile("LM13.root",           "READ");

  //----------------------------------------------------------------------------------
  // addSample(TFile* sample, TString label, int lc, int ms, double msize, int fs);
  //----------------------------------------------------------------------------------

  addSample(TTJets,    "t#bar{t}+Jets", kRed+2,   21, 1.1, 7);
  addSample(SingleTop, "Single Top",    kRed,     22, 1.4, 7);
  addSample(WJetsHT,   "W+Jets",        1,        23, 1.4, 7);

  addSample(ZJets,     "Z+Jets",        kGreen+2, 21, 0.9, 7);
  addSample(QCD,       "QCD",           kBlue,    21, 0.9, 7);

//   addSample(LM3,  "LM3",  kRed,     20, 1.1, 7);
//   addSample(LM8,  "LM8",  kBlue,    21, 0.9, 7);
//   addSample(LM13, "LM13", kGreen+2, 22, 1.2, 7);

  //-----------------------------------------------------
  // set Style
  //-----------------------------------------------------

  setTDRStyle();
 
  //-----------------------------------------------------
  // Make plots
  //-----------------------------------------------------

  // loop over files
  for(int f=0; f<(int)Files.size(); ++f)
    {
      std::cout << "File: " << Labels[f] <<  std::endl;
      
      // Define canvas, legend and labels
      TCanvas *canvas =new TCanvas(Labels[f],Labels[f],1);
      
      TLegend *leg = new TLegend(.50,.18,.90,.42);
      leg->SetTextFont(42);
      leg->SetFillColor(0);
      leg->SetLineColor(1);
      leg->SetShadowColor(0);
      leg->SetLineColor(0);
      
      TPaveText *label = new TPaveText(0.16,0.85,0.85,0.93,"NDC");
      label->SetFillColor(0);
      label->SetTextFont(42);
      label->SetTextSize(0.042);
      label->SetBorderSize(0);
      label->SetTextAlign(12);
      TText *text=label->AddText("Simulation, #sqrt{s} = 7 TeV, muon channel");
      
      TPaveText *label2 = new TPaveText(0.33,0.23,0.53,0.33,"NDC");
      label2->SetFillColor(0);
      label2->SetTextFont(62);
      label2->SetBorderSize(0);
      TText *text2=label2->AddText("0 < |#eta| < 2.4");
      
      TH1F* weights_=(TH1F*)Files[f]->Get("monitorBtagWeightingMu/btagWeights_noWgt");
      TH1F* cuts_=(TH1F*)Files[f]->Get("monitorBtagWeightingMu/nbjets");
      
      // define shifts of markers in x direction
      double shift_=0.05;
      
      // define int nBins and array xbins and xbins2
      Int_t nBins=weights_->GetNbinsX();
      double xbins[5];
      double xbins2[5];

      // fill arrays xbins and xbins2
      double xbin0=weights_->GetBinLowEdge(1);
      xbins[0] =xbin0;
      xbins2[0]=xbin0;

      std::cout << "Test1" << std::endl;

      double ibinX=0;
      for(int xbin=1; xbin<weights_->GetNbinsX(); ++xbin)
	{
	  std::cout << "Test2" << xbin << std::endl;

	  ibinX=ibinX+1;
	  
	  xbins[xbin] =ibinX;
	  xbins2[xbin]=ibinX+shift_;

	  std::cout << xbins[xbin] << std::endl;
	  std::cout << xbins2[xbin] << std::endl;
	}
      //std::cout << weights_->GetNbinsX()+1 << std::endl;
      //std::cout << weights_->GetBinLowEdge(weights_->GetNbinsX()+1) << std::endl;

      xbins[4]=4;
      xbins2[4]=4;
      
//       std::cout << "Test3" << std::endl;

//       std::cout << xbins[0] << std::endl;
//       std::cout << xbins[1] << std::endl;
//       std::cout << xbins[2] << std::endl;
//       std::cout << xbins[3] << std::endl;
//       std::cout << xbins[4] << std::endl;
//       std::cout << xbins2[0] << std::endl;
//       std::cout << xbins2[1] << std::endl;
//       std::cout << xbins2[2] << std::endl;
//       std::cout << xbins2[3] << std::endl;
//       std::cout << xbins2[4] << std::endl;

      // define new histograms Tmp_ and Tmp2_
      char Tmp [70];
      char Tmp2 [70];
      sprintf(Tmp,"%i",    f);
      sprintf(Tmp2,"%i_2", f);
      TH1F* Tmp_ =new TH1F(Tmp,  Tmp,  nBins, xbins );
      TH1F* Tmp2_=new TH1F(Tmp2, Tmp2, nBins, xbins2);
      
      std::cout << "Test4" << std::endl;

      // fill histogramw Tmp_ and Tmp2_
      for(int xbin=0; xbin<Tmp_->GetNbinsX()+1; ++xbin)
	{
	  Tmp_->SetBinContent(xbin,weights_->GetBinContent(xbin));
	  Tmp_->SetBinError(xbin,weights_->GetBinError(xbin));
	  
	  Tmp2_->SetBinContent(xbin,weights_->GetBinContent(xbin));
	  Tmp2_->SetBinError(xbin,0.0000001);
	  
	}
      
      //--------------------------------------
      // Define and draw histograms
      //--------------------------------------
      
      // Draw x-errors
      Tmp2_->SetTitle("");
     
      Tmp2_->SetMinimum(0);
      Tmp2_->GetXaxis()->SetTitle("No. of b-jets");
      Tmp2_->GetYaxis()->SetTitle("# events");
      
//       Tmp2_->GetXaxis()->SetTitleOffset(1.2); 
//       Tmp2_->GetYaxis()->SetTitleOffset(1.4);
      
//       Tmp2_->SetLineColor(SampleColors[f]);
//       Tmp2_->SetLineWidth(1);
//       if(f==0) Tmp2_->Draw("");
//       else Tmp2_->Draw("same");
      
//       // Draw markers
//       Tmp_->SetLineColor(SampleColors[f]);
//       Tmp_->SetLineWidth(1);
//       Tmp_->SetMarkerStyle(MarkerStyles[f]);
//       Tmp_->SetMarkerColor(SampleColors[f]);
//       Tmp_->SetMarkerSize(MarkerSizes[f]);
//       Tmp_->Draw("same E x0");
      
      //leg->AddEntry(Tmp_,Labels[f],"l P");

  leg->Draw();
  label->Draw();
  
//   canvas->SaveAs(Algos[a]+"_"+Flavors[flv]+"jetsEfficiency_Mu.eps");
    }


  return 0;
}
