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
  //TFile* ElHad=new TFile("ElHad.root","READ");

  //--------------------------------------------------------------------------
  // Specify luminosity, numbers of events and cross-sections
  //--------------------------------------------------------------------------

  // Lumi for MuHad in fb^-1
  Double_t Lumi=4.123723;

  // Lumi for ElHad in fb^-1
  //Double_t Lumi=4.190583;
  
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
  
  Double_t WeightQCD=(Lumi*(XSQCD))/NGQCD;
  Double_t WeightTTJets=(Lumi*(XSTTJets))/NGTTJets;
  Double_t WeightDY=(Lumi*(XSDY))/NGDY;
  Double_t WeightWJets=(Lumi*(XSWJets))/NGWJets;
  Double_t WeightSingleTop=(Lumi*XSSingleTop)/NGSingleTop;
  Double_t WeightSM=(Lumi*XSSM)/NGSM;
  Double_t WeightLM3=(Lumi*(XSLM3))/NGLM3;
  Double_t WeightLM8=(Lumi*(XSLM8))/NGLM8;
  Double_t WeightLM9=(Lumi*(XSLM9))/NGLM9;

  //--------------------------------------------------------------------------
  // Specify selection steps and histograms
  //--------------------------------------------------------------------------

  Selections.push_back("analyzeBtagsMuTCHEM3highPt");
  Selections.push_back("analyzeBtagsMuTCHEM3highPtdilep");

  DataSelections.push_back("analyzeBtagsMuTCHEM3highPt");
  DataSelections.push_back("analyzeBtagsMuTCHEM3highPtdilep");

  Histograms1.push_back("BtagsWeight_1btags");

  Histograms2.push_back("BtagsWeight_2btags");

  DataHistograms.push_back("NrHighPtBtags");

  //--------------------------------------------------------------------------
  // gStyle
  //--------------------------------------------------------------------------

  gStyle->SetCanvasColor(10);
  gStyle->SetOptStat(0);
  gStyle->SetPalette(1);
  gStyle->SetTitleFillColor(0);

  //--------------------------------------------------------------------------
  // Plot histograms
  //--------------------------------------------------------------------------

  TString labels[]={"-0.5","","-04","","-0.3","","-0.2","","-0.1","","SF","","+0.1","","+0.2","","+0.3","","+0.4","","+0.5"};

  double LumiSF=1;

  for(int sel=0; sel<(int)Selections.size(); ++sel)
    {
      for(int h=0; h<(int)Histograms1.size(); ++h)
	{
	  // MC
	  TH1F* SF1=(TH1F*)SM->Get(Selections[sel]+"/"+Histograms1[h]);
	  TH1F* SF2=(TH1F*)SM->Get(Selections[sel]+"/"+Histograms2[h]);
	  
	  SF1->Scale(WeightSM);
	  SF2->Scale(WeightSM);

	  TH1F* SF1Clone=(TH1F*)SF1->Clone("SF1Clone");
	  TH1F* SF2Clone=(TH1F*)SF2->Clone("SF2Clone");
	  
	  // data
	  TH1F* NrBtags=(TH1F*)MuHad->Get(DataSelections[sel]+"/"+DataHistograms[h]);
	  
	  double bin1=LumiSF*(NrBtags->GetBinContent(2)+NrBtags->GetBinContent(3)+NrBtags->GetBinContent(4));
	  double bin2=LumiSF*(NrBtags->GetBinContent(3)+NrBtags->GetBinContent(4));
	  
	  std::cout << bin1 << std::endl;
	  std::cout << bin2 << std::endl;

	  double ratio=bin2/bin1;
	  double ratioErr=sqrt(bin2)/bin1+bin2*sqrt(bin1)/(bin1*bin1);
	  
	  TH1F* RatioData=new TH1F("ElHad","ElHad", 21, 0., 21.);
	  RatioData->SetBinContent(11, ratio);
	  RatioData->SetBinError(11, ratioErr);
	  
	  std::cout << "Ratio: "<< ratio << " +- " << ratioErr << std::endl;
	  
	  SF2Clone->Divide(SF1Clone);
	  
	  // canvas 1
	  char canvas_name1[30];
	  sprintf(canvas_name1, "%i_%i_SF", sel, h);
	  TCanvas *c1 =new TCanvas(canvas_name1,canvas_name1 ,1);

	  SF1->SetMinimum(0.1);
	  SF1->Draw("");
	  SF2->Scale(10);
	  SF2->Draw("same");
	  
	  c1->SaveAs(Selections[sel]+"_"+Histograms1[h]+"_SF2.pdf");
	  
	  // canvas 2
	  char canvas_name2[30];
	  sprintf(canvas_name2, "%i_%i_Ratio", sel, h);
	  TCanvas *c2 =new TCanvas(canvas_name2,canvas_name2 ,1);

	  // histograms
	  SF2Clone->SetTitle("r(2b/1b)");
	  SF2Clone->GetXaxis()->SetTitle("B-tag efficiency scale factor");
	  SF2Clone->GetXaxis()->CenterTitle();
	  SF2Clone->GetYaxis()->SetTitle("events");
	  SF2Clone->GetYaxis()->CenterTitle();
	  SF2Clone->GetYaxis()->SetTitleOffset(1.25);
	  SF2Clone->SetLineColor(4);

	  SF2Clone->SetTitle("Loose RA4b selection");
	  SF2Clone->GetXaxis()->SetTitle("b-tag efficiency scale factor");
	  SF2Clone->GetXaxis()->CenterTitle();
	  SF2Clone->GetYaxis()->SetTitle("ratio (2b/1b)");
	  SF2Clone->GetYaxis()->CenterTitle();

	  RatioData->SetLineColor(2);

	  // change labels
	  for(int ibin=0; ibin<=20; ++ibin)
	    {
	      SF2Clone->GetXaxis()->SetBinLabel(ibin+1,labels[ibin]);
	    }

	  //draw hisograms
	  SF2Clone->Draw("");
	  RatioData->Draw("same");
	  
	  // TLine
	  TLine * line = new TLine(4.5, 0.039, 4.5,.065 );
	  //TLine * line = new TLine(7.5, 0.063, 7.5, 0.1 );
	  line->SetLineWidth(2);
	  line->SetLineStyle(7);
	  line->SetLineColor(1);
	  line->Draw("same");
	  
	  TLine * line2 = new TLine(14.5, 0.039, 14.5, 0.115 );
	  //TLine * line2 = new TLine(18.5, 0.063, 18.5, 0.16 );
	  line2->SetLineWidth(2);
	  line2->SetLineStyle(7);
	  line2->SetLineColor(1);
	  line2->Draw("same");
	  
	  TLegend *leg = new TLegend(.5,.75,.8,.96);
	  leg->SetTextFont(42);
	  leg->SetFillColor(0);
	  leg->SetLineColor(0);
	  
	  leg->AddEntry(SF2Clone,"All SM MC","l E");
	  leg->AddEntry(RatioData,"MuHad","l E");

	  leg->Draw("same");

	  TPaveText *label = new TPaveText(0.15,0.78,0.45,0.88,"NDC");
	  label->SetFillColor(0);
	  label->SetTextFont(42);
	  label->SetBorderSize(1);
	  TText *text=label->AddText("L=4.124 fb^{-1}");
	  text->SetTextAlign(22);
	  label->Draw("same");

	  c2->SaveAs(Selections[sel]+"_"+Histograms1[h]+"_Ratio2.pdf");
	}
    }

//   TH1F* NrBtagsDiLep=(TH1F*)SM->Get("analyzeBtagsTCHEM3sf2/NrHighPtBtags");

//   TCanvas *c3 =new TCanvas( "c3" , "c3" ,1);
//   NrBtagsDiLep->Scale(WeightSM*LumiSF);
//   NrBtagsDiLep->Draw("");
//   gPad->SetLogy();

//   c3->SaveAs("NrBtags_emu_channel_3fb.pdf");

  return 0;
}
