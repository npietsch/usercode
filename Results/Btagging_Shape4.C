#include <vector>
#include <iostream>
#include <bitset>
#include <vector>
#include <fstream>
#include "TFile.h"
#include "TH1.h"
#include "TCanvas.h"
#include "TStyle.h"
#include "TLegend.h"

vector<TFile*> Files;
vector<TString> Names;
vector<TString> Algos;
vector<TString> Flavors;
vector<TString> Steps;
vector<TString> SelectionNames;

vector<unsigned int> LineColors;
vector<unsigned int> SampleColors;
vector<unsigned int> MarkerStyles;
vector<double> MarkerSizes;

vector<TH1F*> Histograms;

void addSample(TFile* sample, TString name; int lc; int ms; double msize);

void addSample(TFile* sample, TString name, int lc; int ms; double msize)
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
  TFile* TTJets=new TFile("TTJetsFall11.root","READ");
  TFile* WJetsHT=new TFile("WJetsHT.root","READ");

  // addSample(TFile* sample, TString name)
  addSample(TTJets,  "TTJets", 2, 21, 0.7);
  addSample(WJetsHT, "WJets",  4, 22, 0.7);

  // addAlgorithm(TString name)
  addAlgorithm("TCHEM");
  //addAlgorithm("SSVHEM");

  // addSelectionStep(TString name, int lc, TString sn);
  addSelectionStep("", 8, "MET < 300 GeV");

  // Flavors
  Flavors.push_back("B");
  Flavors.push_back("C");
  Flavors.push_back("L");

  gStyle->SetCanvasColor(10);
  gStyle->SetOptStat(0);
  gStyle->SetPalette(1);
  gStyle->SetTitleFillColor(0);

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
	       
	      // Define canvas., legend etc.
	      TCanvas *canvas =new TCanvas(SelectionNames[s]+"_"+Algos[a]+"_"+Flavors[flv]+"_Pt",SelectionNames[s]+"_"+Algos[a]+"_"+Flavors[flv]+"_Pt",1);

	      TLegend *leg = new TLegend(.5,.15,.88,.42);
	      leg->SetTextFont(42);
	      leg->SetFillColor(0);
	      leg->SetLineColor(0);
	      
	      TLegend *leg2 = new TLegend(.5,.15,.88,.42);
	      leg2->SetTextFont(42);
	      leg2->SetFillColor(0);
	      leg2->SetLineColor(0);

	      // loop over files
	      for(int f=0; f<(int)Files.size(); ++f)
		{
		  std::cout << Names[f] << std::endl;
		  std::cout << "------------" << std::endl;
		  
	      
		  std::cout << "bTagEffRA4bMu"+Algos[a]+Steps[s]+"/Num"+Flavors[flv]+"JetsPt" << std::endl;
		  
		  TH2F* Pt_=(TH2F*)Files[f]->Get("bTagEffRA4bMu"+Algos[a]+Steps[s]+"/Num"+Flavors[flv]+"JetsPtEta");
		  TH2F* Pt2_=(TH2F*)Files[f]->Get("bTagEffRA4bEl"+Algos[a]+Steps[s]+"/Num"+Flavors[flv]+"JetsPtEta");
		  Pt_->Add(Pt2_);

		  std::cout << "bTagEffRA4bMu"+Algos[a]+Steps[s]+"/Num"+Flavors[flv]+"JetsTaggedPtEta" << std::endl;

		  TH2F* TaggedPt_=(TH2F*)Files[f]->Get("bTagEffRA4bMu"+Algos[a]+Steps[s]+"/Num"+Flavors[flv]+"JetsTaggedPtEta");
		  TH2F* TaggedPt2_=(TH2F*)Files[f]->Get("bTagEffRA4bEl"+Algos[a]+Steps[s]+"/Num"+Flavors[flv]+"JetsTaggedPtEta");
		  TaggedPt_->Add(TaggedPt2_);

		  TaggedPt_->Divide(Pt_);
		  
		  //--------------------------------------
		  // Draw y errors
		  //--------------------------------------
		  
		  // define shift
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
		  double xbin=0;
		  for(int ibin=1; ibin<TaggedPt_->GetNbinsX(); ++ibin)
		    {
		      xbin=xbin+TaggedPt_->GetXaxis()->GetBinWidth(ibin);
		      if(TaggedPt_->GetXaxis()->GetBinWidth(ibin)>20) shift_=shift3_;

		      xbinsPtX[ibin]=xbin;
		      xbinsPt[ibin]=xbin+shift_;
		      std::cout << xbin[ibin] << std::endl;
		    }
		  //double xEndShift=shift_*(TaggedPt_->GetXaxis()->GetBinWidth(TaggedPt_->GetNbinsX()));
		  xbinsPt[TaggedPt_->GetNbinsX()]=TaggedPt_->GetBinLowEdge(TaggedPt_->GetNbinsX()+1)+shift_;
		  xbinsPtX[TaggedPt_->GetNbinsX()]=TaggedPt_->GetBinLowEdge(TaggedPt_->GetNbinsX()+1);

		  // define new histogram Temp_
		  char Tmp [70];
		  sprintf(Tmp,"%i_%i_%i_%i_Pt", f, a, flv, s);
		  TH1F* Tmp_=new TH1F(Tmp, "Tmp", nBins, xbinsPt);
		  TH1F* Tmp2_=new TH1F("Tmp2", "Tmp2", nBins, xbinsPtX);

		  // fill histogram Tmp_
		  for(int ibin=0; ibin<Tmp_->GetNbinsX()+1; ++ibin)
		    {
		      std::cout << "ibin: " << ibin << std::endl;
		      Tmp_->SetBinContent(ibin,TaggedPt_->GetBinContent(ibin,1));
		      std::cout << "bin content: " << TaggedPt_->GetBinContent(ibin,1) << std::endl;
		      Tmp_->SetBinError(ibin,TaggedPt_->GetBinError(ibin,1));
		      std::cout << "bin error: " << TaggedPt_->GetBinError(ibin,1) << std::endl;

		      Tmp2_->SetBinContent(ibin,TaggedPt_->GetBinContent(ibin,1));
		      Tmp2_->SetBinError(ibin,0.0000000001);
		    }
		  
		  // draw histogram Tmp_
		  Tmp_->SetTitle("TCHEM b-tag efficiency for "+Flavors[flv]+"-Jets");
		  if(Flavors[flv]=="L") Tmp_->SetTitle("TCHEM b-tag efficiency for other jets");
		  Tmp_->GetXaxis()->SetTitle("p_{T} [GeV]");
		  Tmp_->GetXaxis()->SetTitleOffset(1.1);
		  Tmp_->GetXaxis()->CenterTitle();
		  Tmp_->GetYaxis()->SetTitle("b-tag efficiency");
		  Tmp_->GetYaxis()->SetTitleOffset(1.25);
		  Tmp_->GetYaxis()->CenterTitle();

		  Tmp_->SetLineColor(SampleColors[f]);
		  if(f==0) Tmp_->Draw("E x0");
		  else Tmp_->Draw("same E x0");
		  
		  std::cout << "Test" << std::endl;

		  //--------------------------------------
		  // Draw x errors
		  //--------------------------------------
		  
		  // draw histogram Tmp2_    
		  Tmp2_->SetLineColor(SampleColors[f]);
		  Tmp2_->Draw("same");
		  
		  leg->AddEntry(Tmp_,Names[f],"l");
		  
		}
	      leg->Draw("box");
	      canvas->SaveAs(Algos[a]+Steps[s]+"_"+Flavors[flv]+"jetsEff_MuPt.pdf");
	      
	    }
	}
    }
  std::cout << "" << std::endl;
  
  return 0;
}
