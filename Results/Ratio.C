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

vector<TString> Selections;
vector<TString> DataSelections;

vector<TString> Histograms1;
vector<TString> Histograms2;
vector<TString> DataHistograms;

int Ratio()
{
 
  //--------------------------------------------------------------------------
  // Define samples
  //--------------------------------------------------------------------------

  TFile* TTJets=new TFile("TTJets.root","READ");
  TFile* SingleTop=new TFile("SingleTop.root","READ");
  TFile* WJets=new TFile("WJets.root","READ");
  TFile* DY=new TFile("DY.root","READ");
  TFile* QCD=new TFile("QCD.root","READ");
  TFile* SM=new TFile("SM.root","READ");

  TFile* MuHad=new TFile("MuHad.root","READ");

  //--------------------------------------------------------------------------
  // Specify luminosity, numbers of events and cross-sections
  //--------------------------------------------------------------------------

  // Luminosity for MuHad
  Int_t Luminosity=2960;
  
  // Luminosity for ElHad
  //Int_t Luminosity=2166;
  
  Int_t NGQCD=1;
  Double_t XSQCD=0.001;
  
  Int_t NGTTJets=3701947;
  Double_t XSTTJets=157.5;
  
  Int_t NGDY=36277961;
  Double_t XSDY=3048;
  
  Int_t NGWJets=81352581;
  Double_t XSWJets=31314; 
  
  Int_t NGSingleTop=1; 
  Double_t XSSingleTop=0.001;
  
  Int_t NGSM=1; 
  Double_t XSSM=0.001;

  Int_t NGLM3=36475;
  Double_t XSLM3=3.438;
  
  Int_t NGLM8=10595;
  Double_t XSLM8=0.73;
  
  Int_t NGLM9=79665;
  Double_t XSLM9=7.134;
  
  Double_t WeightQCD=(Luminosity*(XSQCD))/NGQCD;
  Double_t WeightTTJets=(Luminosity*(XSTTJets))/NGTTJets;
  Double_t WeightDY=(Luminosity*(XSDY))/NGDY;
  Double_t WeightWJets=(Luminosity*(XSWJets))/NGWJets;
  Double_t WeightSingleTop=(Luminosity*XSSingleTop)/NGSingleTop;
  Double_t WeightSM=(Luminosity*XSSM)/NGSM;
  Double_t WeightLM3=(Luminosity*(XSLM3))/NGLM3;
  Double_t WeightLM8=(Luminosity*(XSLM8))/NGLM8;
  Double_t WeightLM9=(Luminosity*(XSLM9))/NGLM9;

  //--------------------------------------------------------------------------
  // Specify selection steps and histograms
  //--------------------------------------------------------------------------

  Selections.push_back("analyzeBtagsTCHEM3sf");

  DataSelections.push_back("analyzeBtagsTCHEM3sf");

  Histograms1.push_back("BtagsWeight_1btags");

  Histograms2.push_back("BtagsWeight_2btags");

  DataHistograms.push_back("NrHighPtBtags");

  //--------------------------------------------------------------------------
  // Plot histograms
  //--------------------------------------------------------------------------

  double LumiSF=1;

  for(int sel=0; sel<(int)Selections.size(); ++sel)
    {
      for(int h=0; h<(int)Histograms1.size(); ++h)
	{
	  // MC
	  TH1F* SF1=(TH1F*)SM->Get(Selections[sel]+"/"+Histograms1[h]);
	  TH1F* SF2=(TH1F*)SM->Get(Selections[sel]+"/"+Histograms2[h]);
	  
	  TH1F* SF1Clone=(TH1F*)SF1->Clone("SF1Clone");
	  TH1F* SF2Clone=(TH1F*)SF2->Clone("SF2Clone");
	  
	  // data
	  TH1F* NrBtags=(TH1F*)MuHad->Get(DataSelections[sel]+"/"+DataHistograms[h]);
	  
	  double bin1=LumiSF*(NrBtags->GetBinContent(2)+NrBtags->GetBinContent(3)+NrBtags->GetBinContent(4));
	  double bin2=LumiSF*(NrBtags->GetBinContent(3)+NrBtags->GetBinContent(4));
	  
	  double ratio=bin2/bin1;
	  double ratioErr=sqrt(bin2)/bin1+bin2*sqrt(bin1)/(bin1*bin1);
	  
	  TH1F* RatioData=new TH1F("MuHad","MuHad", 21, 0., 21.);
	  RatioData->SetBinContent(11, ratio);
	  RatioData->SetBinError(11, ratioErr);
	  
	  std::cout << "Ratio: "<< ratio << " +- " << ratioErr << std::endl;
	  
	  SF2Clone->Divide(SF1Clone);
	  
	  TCanvas *c1 =new TCanvas( "c1" , "c1" ,1);
	  SF1->SetMinimum(0.1);
	  SF1->Draw("");
	  SF2->Scale(10);
	  SF2->Draw("same");
	  
	  c1->SaveAs(Selections[sel]+"_"+Histograms1[h]+"_SF.pdf");
	  
	  TCanvas *c2 =new TCanvas( "c2" , "c2" ,1);
	  SF2Clone->Draw("");
	  RatioData->Draw("same");
	  
	  // TLine
	  TLine * line = new TLine(0.5, 0.024,
				   0.5, 0.026 );
	  line->SetLineWidth(2);
	  line->SetLineStyle(7);
	  line->SetLineColor(1);
	  line->Draw("same");
	  
	  TLine * line2 = new TLine(17.5, 0.024,
				    17.5, 0.06 );
	  line2->SetLineWidth(2);
	  line2->SetLineStyle(7);
	  line2->SetLineColor(1);
	  line2->Draw("same");
	  
	  c2->SaveAs(Selections[sel]+"_"+Histograms1[h]+"_Ratio.pdf");
	}
    }
  return 0;
}
