#include <vector>
#include <iostream>
#include <bitset>
#include <vector>
#include <fstream>
#include "TFile.h"
#include "TH1.h"
#include "TH2.h"
#include "TCanvas.h"
#include "TStyle.h"
#include "TLegend.h"
#include "TPaveText.h"
#include "TDRStyle.h"

vector<TFile*> Files;
vector<TString> Names;
vector<unsigned int> SampleColors;
vector<unsigned int> MarkerStyles;
vector<double> MarkerSizes;

vector<TString> Algos;

vector<TString> Flavors;

vector<TString> Steps;
vector<unsigned int> LineColors;
vector<TString> SelectionNames;

vector<TH1F*> Histograms;

void addSample(TFile* sample, TString name, int lc, int ms, double msize);

void addSample(TFile* sample, TString name, int lc, int ms, double msize)
{
  Files.push_back(sample);
  Names.push_back(name);
  SampleColors.push_back(lc);
  MarkerStyles.push_back(ms);
  MarkerSizes.push_back(msize);
}

void addAlgorithm(TString name);

void addAlgorithm(TString name)
{
  Algos.push_back(name);
}


void addSelectionStep(TString name, int lc, TString sn);

void addSelectionStep(TString name, int lc, TString sn)
{
  Steps.push_back(name);
  LineColors.push_back(lc);
  SelectionNames.push_back(sn);
}

int Btagging_Shape4()
{
  // Define sample
  TFile* TTJets    = new TFile("TTJetsFall11.root" , "READ");
  TFile* WJetsHT   = new TFile("WJetsHT.root"      , "READ");
  TFile* SingleTop = new TFile("SingleTop.root"    , "READ");

  // addSample(TFile* sample, TString name)
  addSample(TTJets,    "t#bar{t}+Jets", kRed-3,    21, 0.8);
  addSample(WJetsHT,   "W+Jets",        kYellow+1, 25, 0.8);
  addSample(SingleTop, "single top",    kOrange+4, 24, 0.8);

  // addAlgorithm(TString name)
  addAlgorithm("TCHEM");

  // addSelectionStep(TString name, int lc, TString sn);
  addSelectionStep("", 8, "RA4b");

  // Flavors
  Flavors.push_back("B");
  Flavors.push_back("C");
  Flavors.push_back("L");

  // global settings
//   gStyle->SetCanvasColor(10);
//   gStyle->SetOptStat(0);
//   gStyle->SetPalette(1);
//   gStyle->SetTitleFillColor(0);

  setTDRStyle();

  // loop over algorithms
  for(int a=0; a<Algos.size(); ++a)
    {
      std::cout << Algos[a] << std::endl;
      
      // loop over flavor	  
      for(int flv=0; flv<(int)Flavors.size(); ++flv)
	{
	  // loop over selection steps
	  for(int s=0; s < Steps.size(); ++s)
	    {
	      std::cout << "Selection step " << Steps[s] <<  std::endl;
	       
	      // Define canvas and legend
	      TCanvas *canvas =new TCanvas(SelectionNames[s]+"_"+Algos[a]+"_"+Flavors[flv]+"_Pt",SelectionNames[s]+"_"+Algos[a]+"_"+Flavors[flv]+"_Pt",1);

	      TLegend *leg = new TLegend(.64,.18,.91,.35);
	      leg->SetTextFont(42);
	      leg->SetFillColor(0);
	      leg->SetLineColor(1);
	      
	      TPaveText *label = new TPaveText(0.17,0.85,0.52,0.93,"NDC");
	      label->SetFillColor(0);
	      label->SetTextFont(42);
	      label->SetBorderSize(0);
	      TText *text=label->AddText("CMS Simulation, #sqrt{s}=7 TeV");
	      text->SetTextAlign(22);
	      
	      TPaveText *label2 = new TPaveText(0.33,0.23,0.53,0.33,"NDC");
	      label2->SetFillColor(0);
	      label2->SetTextFont(62);
	      label2->SetBorderSize(0);
	      TText *text2=label2->AddText("0 < |#eta| < 0.8");
	      text2->SetTextAlign(22);

	      // declare maximum and ybin
	      double Maximum=0;
	      double ybin=1;

	      // loop over files
	      for(int f=0; f<(int)Files.size(); ++f)
		{
		  TH2F* Pt_=(TH2F*)Files[f]->Get("bTagEffRA4bMu"+Algos[a]+Steps[s]+"/Num"+Flavors[flv]+"JetsPtEta");
		  TH2F* Pt2_=(TH2F*)Files[f]->Get("bTagEffRA4bEl"+Algos[a]+Steps[s]+"/Num"+Flavors[flv]+"JetsPtEta");
		  Pt_->Add(Pt2_);

		  TH2F* TaggedPt_=(TH2F*)Files[f]->Get("bTagEffRA4bMu"+Algos[a]+Steps[s]+"/Num"+Flavors[flv]+"JetsTaggedPtEta");
		  TH2F* TaggedPt2_=(TH2F*)Files[f]->Get("bTagEffRA4bEl"+Algos[a]+Steps[s]+"/Num"+Flavors[flv]+"JetsTaggedPtEta");
		  TaggedPt_->Add(TaggedPt2_);

		  TaggedPt_->Divide(Pt_);
		  
		  //--------------------------------------
		  // Draw y errors
		  //--------------------------------------
		  
		  // define shifts
		  double shift_=2*f;
		  double shift2_=4*f;
		  double shift3_=6*f;
		  
		  // define array xbinsPt
		  Int_t nBins=TaggedPt_->GetNbinsX();
		  double xbinsPt[11];
		  double xbinsPtX[11];

		  // fill array xbinsPt
		  double xbin0=TaggedPt_->GetBinLowEdge(1);
		  xbinsPt[0]=xbin0;
		  xbinsPtX[0]=xbin0;
		  std::cout << xbin0 << std::endl;

		  //
		  double ibinX=0;
		  for(int xbin=1; xbin<TaggedPt_->GetNbinsX(); ++xbin)
		    {
		      ibinX=ibinX+TaggedPt_->GetXaxis()->GetBinWidth(xbin);
		      if(TaggedPt_->GetXaxis()->GetBinWidth(xbin)>20) shift_=shift3_;

		      xbinsPtX[xbin]=ibinX;
		      xbinsPt[xbin]=ibinX+shift_;
		    }
		  xbinsPt[TaggedPt_->GetNbinsX()]=TaggedPt_->GetBinLowEdge(TaggedPt_->GetNbinsX()+1)+shift_;
		  xbinsPtX[TaggedPt_->GetNbinsX()]=TaggedPt_->GetBinLowEdge(TaggedPt_->GetNbinsX()+1);

		  // define new histogram Temp_
		  char Tmp [70];
		  sprintf(Tmp,"%i_%i_%i_%i_Pt", f, a, flv, s);
		  TH1F* Tmp_=new TH1F(Tmp, "Tmp", nBins, xbinsPt);
		  TH1F* Tmp2_=new TH1F("Tmp2", "Tmp2", nBins, xbinsPtX);

		  // fill histogram Tmp_
		  for(int xbin=0; xbin<Tmp_->GetNbinsX()+1; ++xbin)
		    {
		      Tmp_->SetBinContent(xbin,TaggedPt_->GetBinContent(xbin, ybin));
		      Tmp_->SetBinError(xbin,TaggedPt_->GetBinError(xbin, ybin));
		      
		      Tmp2_->SetBinContent(xbin,TaggedPt_->GetBinContent(xbin, ybin));
		      Tmp2_->SetBinError(xbin,0.0000001);

		      if(TaggedPt_->GetBinContent(xbin, ybin)+TaggedPt_->GetBinError(xbin, ybin) > Maximum)
			{
			  Maximum=TaggedPt_->GetBinContent(xbin, ybin)+TaggedPt_->GetBinError(xbin, ybin);
			}
		    }

		  // draw histogram Tmp_
		  if(Flavors[flv]=="B") Tmp_->SetMaximum(1.05*0.951668);
		  if(Flavors[flv]=="C") Tmp_->SetMaximum(1.05*0.373941);
		  if(Flavors[flv]=="L") Tmp_->SetMaximum(1.05*0.0727985);
		  Tmp_->SetTitle("");
		  if(Flavors[flv]=="B") Tmp_->GetXaxis()->SetTitle("b-jet p_{T} [GeV]");
		  if(Flavors[flv]=="C") Tmp_->GetXaxis()->SetTitle("c-jet p_{T} [GeV]");
		  if(Flavors[flv]=="L") Tmp_->GetXaxis()->SetTitle("light quark jet p_{T} [GeV]");
		  Tmp_->GetXaxis()->SetTitleOffset(1.35);
		  //Tmp_->GetXaxis()->CenterTitle();
		  Tmp_->GetYaxis()->SetTitle("b-tag efficiency");
		  Tmp_->GetYaxis()->SetTitleOffset(1.35);
		  //Tmp_->GetYaxis()->CenterTitle();
		  Tmp_->SetLineColor(SampleColors[f]);
		  Tmp_->SetLineWidth(1);

		  Tmp_->SetMarkerStyle(MarkerStyles[f]);
		  Tmp_->SetMarkerColor(SampleColors[f]);
		  Tmp_->SetMarkerSize(MarkerSizes[f]);

		  if(f==0) Tmp_->Draw("E x0");
		  else Tmp_->Draw("same E x0");


		  //--------------------------------------
		  // Draw x errors
		  //--------------------------------------
		  
		  // draw histogram Tmp2_   
		  Tmp2_->SetLineColor(SampleColors[f]);
		  Tmp2_->SetLineWidth(1);
		  Tmp2_->Draw("same");

		  leg->AddEntry(Tmp_,Names[f],"l P");
		  
		}
	      std::cout << "==============================" << std::endl;
	      std::cout << "Maximum: " << Maximum << std::endl;
	      std::cout << "==============================" << std::endl;

	      leg->SetShadowColor(0);
	      leg->Draw();
	      label->Draw();
	      label2->Draw();

	      canvas->SaveAs(Algos[a]+Steps[s]+"_"+Flavors[flv]+"jetsEff_MuPt.pdf");
	      
	    }
	}
    }
  std::cout << "" << std::endl;
  
  return 0;
}

