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


int PU()
{
  // define sample
  TFile* ElHad_ =new TFile("ElHad.root", "READ");

  // get histograms
  TH1F* nBtags1PV_=(TH1F*)ElHad_->Get("analyzeBtagsRA4bElTCHEM3/nbtags_1PU");
  TH1F* nBtags5PV_=(TH1F*)ElHad_->Get("analyzeBtagsRA4bElTCHEM3/nbtags_5PU");
  TH1F* nBtags9PV_=(TH1F*)ElHad_->Get("analyzeBtagsRA4bElTCHEM3/nbtags_7PU");
  TH1F* nBtags13PV_=(TH1F*)ElHad_->Get("analyzeBtagsRA4bElTCHEM3/nbtags_10PU");

  // normaliz histograms to unit area
  nBtags1PV_->Scale(1/(nBtags1PV_->Integral()));
  nBtags5PV_->Scale(1/(nBtags5PV_->Integral()));
  nBtags9PV_->Scale(1/(nBtags9PV_->Integral()));
  nBtags13PV_->Scale(1/(nBtags13PV_->Integral()));

  // set gStyle
  gStyle->SetCanvasColor(10);
  gStyle->SetOptStat(0);
  gStyle->SetPalette(1);
  gStyle->SetTitleFillColor(0);

  // histogram and marker style
  nBtags1PV_->SetLineColor(8);
  nBtags1PV_->SetMarkerStyle(20);
  nBtags1PV_->SetMarkerColor(8);
  nBtags1PV_->SetMarkerSize(1.3);
  nBtags1PV_->SetTitle("");
  nBtags1PV_->GetXaxis()->SetTitle("number of b-tagged jets");
  nBtags1PV_->GetXaxis()->CenterTitle();
  nBtags1PV_->GetYaxis()->SetTitle("a.u.");
  nBtags1PV_->GetYaxis()->CenterTitle();

  nBtags5PV_->SetLineColor(2);
  nBtags5PV_->SetMarkerStyle(21);
  nBtags5PV_->SetMarkerColor(2);
  nBtags5PV_->SetMarkerSize(1.3);

  nBtags9PV_->SetLineColor(4);
  nBtags9PV_->SetMarkerStyle(22);
  nBtags9PV_->SetMarkerColor(4);
  nBtags9PV_->SetMarkerSize(1.3);

  nBtags13PV_->SetLineColor(1);
  nBtags13PV_->SetMarkerStyle(23);
  nBtags13PV_->SetMarkerColor(1);
  nBtags13PV_->SetMarkerSize(1.3);

  TLegend *leg = new TLegend(.73,.55,.88,.88);
  leg->SetTextFont(42);
  leg->SetFillColor(0);
  leg->SetLineColor(0);
  
  leg->AddEntry(nBtags1PV_,"1-4 PV","l P");
  leg->AddEntry(nBtags5PV_,"5-8 PV","l P");
  leg->AddEntry(nBtags9PV_,"9-12 PV","l P");
  leg->AddEntry(nBtags13PV_,"> 13 PV","l P");

  TCanvas *c1 =new TCanvas("c1","c1",1);

  nBtags1PV_->Draw("");
  nBtags5PV_->Draw("same");
  nBtags9PV_->Draw("same");
  nBtags13PV_->Draw("same");
  leg->Draw("box");

  TPaveText *label = new TPaveText(0.16,0.16,0.43,0.27,"NDC");
  label->SetFillColor(0);
  label->SetTextFont(42);
  label->SetBorderSize(1);
  TText *text=label->AddText("L=4.13 fb^{-1}");
  text->SetTextAlign(22);
  label->Draw("same");

  c1->SaveAs("PV_El.pdf");

//   //double xbins[5]={0.1,1.1,2.1,3.1,4.1};


// //   for(int ibin=1; ibin<Tag0gedPt_->GetNbinsX(); ++ibin)
// //     {
// //       xbin=xbin+TaggedPt_->GetXaxis()->GetBinWidth(ibin);
// //       if(TaggedPt_->GetXaxis()->GetBinWidth(ibin)>20) shift_=shift3_;
// //       xbinsPt[ibin]=xbin+shift_;
// //       std::cout << xbin[ibin] << std::endl;
// //     }
  
//   // define new histogram

//   TH1F* nBtags5PV_New_= new TH1F("nBtags5PV_New", "nBtags5PV_New", 4, 0.1, 4.1);

//   for(int i=0; i<5; ++i)
//     {
//       nBtags5PV_New_->SetBinContent(i,nBtags5PV_->GetBinContent(i));
//     }
//   TCanvas *c1 =new TCanvas("c1" ,"c1" ,1);

//   nBtags5PV_->SetFillColor

//   //nBtags1PV_->Draw("");
//   nBtags5PV_->Draw("");
//   nBtags5PV_New_->Draw("same");
//   //nBtags9PV_->Draw("same");
//   //nBtags13PV_->Draw("same");





// 		  // define shift
// 		  double shift_=2*s;
// 		  double shift2_=4*s;
// 		  double shift3_=6*s;

// 		  // define array xbinsPt
// 		  Int_t nBins=TaggedPt_->GetNbinsX();
// 		  double xbinsPt[11];
		  
// 		  // fill array xbinsPt
// 		  double xbin0=TaggedPt_->GetBinLowEdge(1);
// 		  xbinsPt[0]=xbin0;
// 		  std::cout << xbin0 << std::endl;
// 		  // 
// 		  double xbin=0;
// 		  for(int ibin=1; ibin<TaggedPt_->GetNbinsX(); ++ibin)
// 		    {
// 		      xbin=xbin+TaggedPt_->GetXaxis()->GetBinWidth(ibin);
// 		      //if(TaggedPt_->GetXaxis()->GetBinWidth(ibin)>10) shift_=shift2_;
// 		      if(TaggedPt_->GetXaxis()->GetBinWidth(ibin)>20) shift_=shift3_;
// 		      //xbinsPt[ibin]=xbin+shift_*(TaggedPt_->GetXaxis()->GetBinWidth(ibin));
// 		      xbinsPt[ibin]=xbin+shift_;
// 		      std::cout << xbin[ibin] << std::endl;
// 		    }
// 		  //double xEndShift=shift_*(TaggedPt_->GetXaxis()->GetBinWidth(TaggedPt_->GetNbinsX()));
// 		  xbinsPt[TaggedPt_->GetNbinsX()]=TaggedPt_->GetBinLowEdge(TaggedPt_->GetNbinsX()+1)+shift_;
		  
// 		  // define new histogram TaggePt_
// 		  char Tmp [70];
// 		  sprintf(Tmp,"%i_%i_%i_%i_Pt", f, a, flv, s);
// 		  TH1F* Tmp_=new TH1F(Tmp, "Tmp", nBins, xbinsPt);

// 		  // fill histogram TaggedPt_
// 		  for(int ibin=0; ibin<Tmp_->GetNbinsX()+1; ++ibin)
// 		    {
// 		      std::cout << ibin << std::endl;
// 		      Tmp_->SetBinContent(ibin,TaggedPt_->GetBinContent(ibin));
// 		      Tmp_->SetBinError(ibin,TaggedPt_->GetBinError(ibin));
// 		    }

// 		  // draw histogram Tmp_
// 		  Tmp_->SetTitle(Flavors[flv]+"Jets tag efficiency "+Algos[a]);
// 		  Tmp_->GetXaxis()->SetTitle("p_{T} [GeV]");
// 		  Tmp_->GetXaxis()->CenterTitle();
// 		  Tmp_->GetYaxis()->SetTitle("b-tag efficiency");
// 		  Tmp_->GetYaxis()->CenterTitle();
// 		  Tmp_->SetLineColor(LineColors[s]);
// 		  if(s==0) Tmp_->Draw("E x0");
// 		  else Tmp_->Draw("same E x0");

// 		  //--------------------------------------
// 		  // Draw x errors
// 		  //--------------------------------------

// 		  // draw histogram TaggePt_    
// 		  TaggedPt_->SetLineColor(LineColors[s]);
// 		  for(int ibin=0; ibin<TaggedPt_->GetNbinsX()+1; ++ibin)
// 		    {
// 		      TaggedPt_->SetBinError(ibin,0.0000000001);
// 		    }

// 		  TaggedPt_->Draw("same");
		  
// 		  leg->AddEntry(TaggedPt_,SelectionNames[s],"l");
		  
// 		}
// 	      leg->Draw("box");
// 	      canvas->SaveAs(Names[f]+"_"+Algos[a]+"_"+Flavors[flv]+"jetsEff_ElPt.pdf");

  return 0;
  
}
