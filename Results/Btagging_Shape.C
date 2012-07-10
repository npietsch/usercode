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

vector<TH1F*> Histograms;

void addSample(TFile* sample, TString name; int lc);

void addSample(TFile* sample, TString name, int lc)
{
  Files.push_back(sample);
  Names.push_back(name);
  SampleColors.push_back(lc);
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

int Btagging_Shape()
{
  // Define sample
  TFile* TTJets=new TFile("TTJetsFall11.root","READ");
  
  // addSample(TFile* sample, TString name)
    addSample(TTJets,   "TTJets",    2);

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
		  
		  TH1F* Pt_=(TH1F*)Files[f]->Get("bTagEffRA4bMu"+Algos[a]+Steps[s]+"/Num"+Flavors[flv]+"JetsPt");
		  TH1F* Pt2_=(TH1F*)Files[f]->Get("bTagEffRA4bEl"+Algos[a]+Steps[s]+"/Num"+Flavors[flv]+"JetsPt");
		  Pt_->Add(Pt2_);

		  TH1F* TaggedPt_=(TH1F*)Files[f]->Get("bTagEffRA4bMu"+Algos[a]+Steps[s]+"/Num"+Flavors[flv]+"JetsTaggedPt");
		  TH1F* TaggedPt2_=(TH1F*)Files[f]->Get("bTagEffRA4bEl"+Algos[a]+Steps[s]+"/Num"+Flavors[flv]+"JetsTaggedPt");
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
		  
		  // fill array xbinsPt
		  double xbin0=TaggedPt_->GetBinLowEdge(1);
		  xbinsPt[0]=xbin0;
		  std::cout << xbin0 << std::endl;
		  // 
		  double xbin=0;
		  for(int ibin=1; ibin<TaggedPt_->GetNbinsX(); ++ibin)
		    {
		      xbin=xbin+TaggedPt_->GetXaxis()->GetBinWidth(ibin);
		      //if(TaggedPt_->GetXaxis()->GetBinWidth(ibin)>10) shift_=shift2_;
		      if(TaggedPt_->GetXaxis()->GetBinWidth(ibin)>20) shift_=shift3_;
		      //xbinsPt[ibin]=xbin+shift_*(TaggedPt_->GetXaxis()->GetBinWidth(ibin));
		      xbinsPt[ibin]=xbin+shift_;
		      std::cout << xbin[ibin] << std::endl;
		    }
		  //double xEndShift=shift_*(TaggedPt_->GetXaxis()->GetBinWidth(TaggedPt_->GetNbinsX()));
		  xbinsPt[TaggedPt_->GetNbinsX()]=TaggedPt_->GetBinLowEdge(TaggedPt_->GetNbinsX()+1)+shift_;
		  
		  // define new histogram TaggePt_
		  char Tmp [70];
		  sprintf(Tmp,"%i_%i_%i_%i_Pt", f, a, flv, s);
		  TH1F* Tmp_=new TH1F(Tmp, "Tmp", nBins, xbinsPt);
		  
		  // fill histogram TaggedPt_
		  for(int ibin=0; ibin<Tmp_->GetNbinsX()+1; ++ibin)
		    {
		      std::cout << ibin << std::endl;
		      Tmp_->SetBinContent(ibin,TaggedPt_->GetBinContent(ibin));
		      Tmp_->SetBinError(ibin,TaggedPt_->GetBinError(ibin));
		      std::cout << "bin error: " << TaggedPt_->GetBinError(ibin) << std::endl;
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
		  
		  // draw histogram TaggePt_    
		  TaggedPt_->SetLineColor(SampleColors[f]);
		  for(int ibin=0; ibin<TaggedPt_->GetNbinsX()+1; ++ibin)
		    {
		      TaggedPt_->SetBinError(ibin,0.0000000001);
		    }
		  
		  TaggedPt_->Draw("same");
		  
		  leg->AddEntry(TaggedPt_,Names[f],"l");
		  
		}
	      leg->Draw("box");
	      canvas->SaveAs(Algos[a]+Steps[s]+"_"+Flavors[flv]+"jetsEff_MuPt.pdf");
	      
	      
	      //----------------------------------------------------------------------------------------------
	      //----------------------------------------------------------------------------------------------
	      //----------------------------------------------------------------------------------------------
	      
	      
	      // Define canvas2., legend etc.
	      TCanvas *canvas2 =new TCanvas(SelectionNames[s]+"_"+Algos[a]+"_"+Flavors[flv]+"_Eta",SelectionNames[s]+"_"+Algos[a]+"_"+Flavors[flv]+"_Eta",1);

	      leg->SetLineColor(0);
		  
	      for(int f=0; f<(int)Files.size(); ++f)
		{
		  std::cout << Names[f] << std::endl;
		  std::cout << "------------" << std::endl;

		  std::cout << "bTagEffRA4bMu"+Algos[a]+Steps[s]+"/Num"+Flavors[flv]+"JetsEta" << std::endl;
		  
		  TH1F* Eta_=(TH1F*)Files[f]->Get("bTagEffRA4bMu"+Algos[a]+Steps[s]+"/Num"+Flavors[flv]+"JetsEta");
		  TH1F* Eta2_=(TH1F*)Files[f]->Get("bTagEffRA4bEl"+Algos[a]+Steps[s]+"/Num"+Flavors[flv]+"JetsEta");
		  Eta_->Add(Eta2_);

		  TH1F* TaggedEta_=(TH1F*)Files[f]->Get("bTagEffRA4bMu"+Algos[a]+Steps[s]+"/Num"+Flavors[flv]+"JetsTaggedEta");
		   TH1F* TaggedEta2_=(TH1F*)Files[f]->Get("bTagEffRA4bEl"+Algos[a]+Steps[s]+"/Num"+Flavors[flv]+"JetsTaggedEta");
		   TaggedEta_->Add(TaggedEta2_);

		   TaggedEta_->Divide(Eta_);
		  
		  //--------------------------------------
		  // Draw y errors
		  //--------------------------------------
		  
		  // define shift
		  shift_=0.025*f;
		  
		  // define array xbinsEta
		  Int_t nBins=TaggedEta_->GetNbinsX();
		  double xbinsEta[8];
	      
		  // fill array xbinsEta
		  double xbin0=TaggedEta_->GetBinLowEdge(1);
		  xbinsEta[0]=xbin0;
		  std::cout << xbin0 << std::endl;
		  // 
		  xbin=0;
		  for(int ibin=1; ibin<TaggedEta_->GetNbinsX(); ++ibin)
		    {
		      xbin=xbin+TaggedEta_->GetXaxis()->GetBinWidth(ibin);
		      xbinsEta[ibin]=xbin+shift_;
		      std::cout << xbin[ibin] << std::endl;
		    }
		  xbinsEta[TaggedEta_->GetNbinsX()]=TaggedEta_->GetBinLowEdge(TaggedEta_->GetNbinsX()+1)+shift_;
		  
		  // define new histogram TaggeEta_
		  char TmpEta [70];
		  sprintf(TmpEta,"%i_%i_%i_%i_Eta", f, a, flv, s);
		  TH1F* TmpEta_=new TH1F(TmpEta, "TmpEta", nBins, xbinsEta);
		  
		  // fill histogram TaggedEta_
		  for(int ibin=0; ibin<TmpEta_->GetNbinsX()+1; ++ibin)
		    {
		      std::cout << ibin << std::endl;
		      TmpEta_->SetBinContent(ibin,TaggedEta_->GetBinContent(ibin));
		      TmpEta_->SetBinError(ibin,TaggedEta_->GetBinError(ibin));
		    }
		  
		  // draw histogram TmpEta_
		  TmpEta_->SetTitle("TCHEM b-tag efficiency for "+Flavors[flv]+"-Jets");
		  if(Flavors[flv]=="L") TmpEta_->SetTitle("TCHEM b-tag efficiency for other jets");
		  TmpEta_->GetXaxis()->SetTitle("|#eta|");
		  TmpEta_->GetXaxis()->SetTitleOffset(1.1);
		  TmpEta_->GetXaxis()->CenterTitle();
		  TmpEta_->GetYaxis()->SetTitle("b-tag efficiency");
		  TmpEta_->GetYaxis()->CenterTitle();
		  TmpEta_->GetYaxis()->SetTitleOffset(1.25);
		  TmpEta_->SetLineColor(SampleColors[f]);
		  if(f==0) TmpEta_->Draw("E x0");
		  else TmpEta_->Draw("same E x0");
		  
		  //--------------------------------------
		  // Draw x errors
		  //--------------------------------------
		  
		  // draw histogram TaggeEta_    
		  TaggedEta_->SetLineColor(SampleColors[f]);
		  for(int ibin=0; ibin<TaggedEta_->GetNbinsX()+1; ++ibin)
		    {
		      TaggedEta_->SetBinError(ibin,0.0000000001);
		    }
		  
		  TaggedEta_->Draw("same");
		  
		  leg2->AddEntry(TaggedEta_,Names[f],"l");
		  
		}
	      leg2->Draw("box");
	      canvas2->SaveAs(Algos[a]+Steps[s]+"_"+Flavors[flv]+"jetsEff_MuEta.pdf");
	    }
	}
    }
  std::cout << "" << std::endl;

  return 0;
}
