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
#include "TDRStyle.h"

vector<TFile*> Files;
vector<TString> Names;
vector<unsigned int> SampleColors;
vector<unsigned int> MarkerStyles;
vector<double> MarkerSizes;
vector<unsigned int> FitStyles;

vector<TString> Algos;

vector<TString> Flavors;

vector<TString> Steps;
vector<unsigned int> LineColors;
vector<TString> SelectionNames;

vector<TH1F*> Histograms;
vector<TF1*> FitFunctions;

void addSample(TFile* sample, TString name, int lc, int ms, double msize, int fs);

void addSample(TFile* sample, TString name, int lc, int ms, double msize, int fs)
{
  Files.push_back(sample);
  Names.push_back(name);
  SampleColors.push_back(lc);
  MarkerStyles.push_back(ms);
  MarkerSizes.push_back(msize);
  FitStyles.push_back(fs);
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

int BtagEfficiencies()
{
  // Define sample
  TFile* TTJets    = new TFile("TTJetsFall11.root" , "READ");
  TFile* WJetsHT   = new TFile("WJetsHT.root"      , "READ");
  TFile* SingleTop = new TFile("SingleTop.root"    , "READ");

  // addSample(TFile* sample, TString name)
  addSample(TTJets,    "t#bar{t}+Jets", kRed,     21, 0.9, 7);
  addSample(SingleTop, "single top",    kBlue,    20, 1.0, 7);
  addSample(WJetsHT,   "W+Jets",        kGreen+2, 23, 1.1, 7);
  //addSample(SingleTop, "single top",    kBlue,  24, 1,   7);
  //addSample(WJetsHT,   "W+Jets",        kGreen, 25, 1,   7);


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
	       
	      // Define canvas and legend/afs/desy.de/user/n/npietsch
	      TCanvas *canvas =new TCanvas(SelectionNames[s]+"_"+Algos[a]+"_"+Flavors[flv]+"_Pt",SelectionNames[s]+"_"+Algos[a]+"_"+Flavors[flv]+"_Pt",1);

	      TLegend *leg = new TLegend(.64,.18,.91,.35);
	      leg->SetTextFont(42);
	      leg->SetFillColor(0);
	      leg->SetLineColor(1);
	      
	      TPaveText *label = new TPaveText(0.14,0.91,0.6,0.99,"NDC");
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
		  // Draw x and y errors
		  //--------------------------------------
		  
		  // define shifts
		  double shift_=4*(f-1);
		  double shift2_=5*(f-1);
		  double shift3_=6*(f-1);
		  
		  // define array xbinsPt
		  Int_t nBins=TaggedPt_->GetNbinsX();
		  double xbinsPt[18];
		  double xbinsPtX[18];

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

		  // define new histograms
		  char Tmp [70];
		  char Tmp2 [70];
		  sprintf(Tmp,"%i_%i_%i_%i_Pt", f, a, flv, s);
		  sprintf(Tmp2,"%i_%i_%i_%i_Pt2", f, a, flv, s);
		  TH1F* Tmp_=new TH1F(Tmp, Tmp, nBins, xbinsPt);
		  TH1F* Tmp2_=new TH1F(Tmp2, Tmp2, nBins, xbinsPtX);

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

		  //--------------------------------------
		  // Draw histogram
		  //--------------------------------------

		  // draw histogram Tmp2_
		  if(Flavors[flv]=="B") Tmp2_->SetMaximum(1.05*0.947686);
		  if(Flavors[flv]=="C") Tmp2_->SetMaximum(1.05*0.388437);
		  if(Flavors[flv]=="L") Tmp2_->SetMaximum(1.05*0.0880499);
		  Tmp2_->SetMinimum(0);
		  Tmp2_->SetTitle("");
		  if(Flavors[flv]=="B") Tmp2_->GetXaxis()->SetTitle("b-jet p_{T} [GeV]");
		  if(Flavors[flv]=="C") Tmp2_->GetXaxis()->SetTitle("c-jet p_{T} [GeV]");
		  if(Flavors[flv]=="L") Tmp2_->GetXaxis()->SetTitle("light quark jet p_{T} [GeV]");
		  Tmp2_->GetXaxis()->SetTitleOffset(1.35);
		  //Tmp2_->GetXaxis()->CenterTitle();
		  Tmp2_->GetYaxis()->SetTitle("b-tag efficiency");
		  Tmp2_->GetYaxis()->SetTitleOffset(1.35);
		  //Tmp2_->GetYaxis()->CenterTitle();
		  Tmp2_->SetLineColor(SampleColors[f]);
		  Tmp2_->SetLineWidth(2);
		  if(f==0) Tmp2_->Draw("");
		  else Tmp2_->Draw("same");

// 		  TF1 *myfit1 = new TF1("myfit1","[0]+[1]*x", 40, 160);
// 		  myfit1->SetLineWidth(2);
// 		  myfit1->SetLineColor(SampleColors[f]);

// 		  Tmp2_->Fit("myfit1","0EMR"); // "0" = do NOT automatically draw "hist"
// 		  Tmp2_->GetFunction("myfit1")->ResetBit(1<<9); // make "fitname" visible

// 		  TF1 *myfit2 = new TF1("myfit2","[0]+[1]*x", 160, 670);
// 		  myfit2->SetLineWidth(2);
// 		  myfit2->SetLineColor(SampleColors[f]);

// 		  Tmp2_->Fit("myfit2","0EMR+"); // "0" = do NOT automatically draw "hist"
// 		  Tmp2_->GetFunction("myfit2")->ResetBit(1<<9); // make "fitname" visible
		  
		  // fit functions
// 		  Double_t par[6];

// 		  if(Flavors[flv] == "B")
// 		    {
// 		      TF1 *g1 = new TF1("g1","[1]+[2]*x+[3]*x**2",40,160);
// 		      g1->SetLineColor(SampleColors[f]);
// 		      Tmp2_->Fit(g1,"0EMR");
// 		      Tmp2_->GetFunction("g1")->ResetBit(1<<9);
		      
// 		      TF1 *g2 = new TF1("g2","[4]+[5]*x",160,670);
// 		      g2->SetLineColor(SampleColors[f]);
// 		      Tmp2_->Fit(g2,"0EMR+");
// 		      Tmp2_->GetFunction("g2")->ResetBit(1<<9);
// 		    }


// 		  if(Flavors[flv] == "C" || Flavors[flv] == "L")
// 		    {
// 		      TF1 *g1 = new TF1("g1","[1]+[2]*x+[3]*x**2",40,670);
// 		      g1->SetLineColor(SampleColors[f]);
// 		      g1->SetLineWidth(2);
// 		      Tmp2_->Fit(g1,"0EMR");
// 		      Tmp2_->GetFunction("g1")->ResetBit(1<<9);
// 		    }

// 		  TF1 *total = new TF1("total","[0]+[1]*x+[2]*x**2+[3]+[4]*x",40,670);
// 		  total->SetLineColor(SampleColors[f]);

// 		  g1->GetParameters(&par[0]);
// 		  g2->GetParameters(&par[3]);

// 		  total->SetParameters(par);
		  
// 		  Tmp2_->Fit("total","0EMR+"); // "0" = do NOT automatically draw "hist"
// 		  Tmp2_->GetFunction("total")->ResetBit(1<<9); // make "fitname" visible

		  // draw histogram Tmp_
		  Tmp_->SetLineColor(SampleColors[f]);
		  Tmp_->SetLineWidth(2);

		  Tmp_->SetMarkerStyle(MarkerStyles[f]);
		  Tmp_->SetMarkerColor(SampleColors[f]);
		  Tmp_->SetMarkerSize(MarkerSizes[f]);

		  Tmp_->Draw("same E x0");

		  leg->AddEntry(Tmp_,Names[f],"l P");
		  
		}
	      std::cout << "==============================" << std::endl;
	      std::cout << "Maximum: " << Maximum << std::endl;
	      std::cout << "==============================" << std::endl;

	      leg->SetShadowColor(0);
	      leg->Draw();
	      label->Draw();
	      label2->Draw();

	      canvas->SaveAs(Algos[a]+Steps[s]+"_"+Flavors[flv]+"jetsEff_MuPt_08.pdf");
	      
	    }
	}
    }
  std::cout << "" << std::endl;
  
  return 0;
}

