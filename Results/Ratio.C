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

vector<TString> MCMuSelections;
vector<TString> MCElSelections;

vector<TString> DataMuSelections;
vector<TString> DataElSelections;

vector<TString> MCHistograms;
vector<TString> DataHistograms;

int Ratio()
{
 
  //--------------------------------------------------------------------------
  // Define samples
  //--------------------------------------------------------------------------

  TFile* SM=new TFile("SM.root","READ");

  TFile* MuHad=new TFile("MuHad.root","READ");
  TFile* ElHad=new TFile("ElHad.root","READ");

  //--------------------------------------------------------------------------
  // Specify luminosity, numbers of events and cross-sections
  //--------------------------------------------------------------------------

  // Lumi for MuHad in fb^-1
  Double_t MuLumi=4.123723;

  // Lumi for ElHad in fb^-1
  Double_t ElLumi=4.190583;
  
  //--------------------------------------------------------------------------
  // Specify selection steps and histograms
  //--------------------------------------------------------------------------

  // selections
  MCMuSelections.push_back("analyzeBtagsMuTCHEM3highPtdilep");
  MCElSelections.push_back("analyzeBtagsElTCHEM3highPtdilep");

  DataMuSelections.push_back("analyzeBtagsMuTCHEM3highPtdilep");
  DataElSelections.push_back("analyzeBtagsElTCHEM3highPtdilep");

  //MCMuSelections.push_back("analyzeBtagsMuTCHEM3lowPtdilep");
  //MCElSelections.push_back("analyzeBtagsElTCHEM3lowPtdilep");

  //DataMuSelections.push_back("analyzeBtagsMuTCHEM3lowPtdilep");
  //DataElSelections.push_back("analyzeBtagsElTCHEM3lowPtdilep");

  // histograms
  MCHistograms.push_back("BtagsWeight_1btags");
  MCHistograms.push_back("BtagsWeight_2btags");

  DataHistograms.push_back("NrHighPtBtags");
  //DataHistograms.push_back("NrLowPtBtags");

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

  // Muon selection
  for(int sel=0; sel<(int)MCMuSelections.size(); ++sel)
    { 
      // data
      TH1F* NrBtagMu=(TH1F*)MuHad->Get(DataMuSelections[sel]+"/"+DataHistograms[sel]);
      
      double Nr1Btag=NrBtagMu->GetBinContent(2)+NrBtagMu->GetBinContent(3)+NrBtagMu->GetBinContent(4);
      double Nr2Btag=NrBtagMu->GetBinContent(3)+NrBtagMu->GetBinContent(4);
      
      std::cout << "Nr1Btag: " << Nr1Btag << std::endl;
      std::cout << "Nr2Btag: " << Nr2Btag << std::endl;
      
      double DataRatioMu=Nr2Btag/Nr1Btag;
      double DataRatioMuErr=sqrt(pow((sqrt(Nr2Btag))/Nr1Btag, 2)+pow(Nr2Btag*(sqrt(Nr1Btag))/(Nr1Btag*Nr1Btag), 2));
      
      std::cout << "DataRatioMu: "<< DataRatioMu << " +- " << DataRatioMuErr << std::endl;
	  
      TH1F* DataRatioMu_=new TH1F("DataRatioMu","DataRatioMu", 21, 0., 21.);
      DataRatioMu_->SetBinContent(11, DataRatioMu);
      DataRatioMu_->SetBinError(11, DataRatioMuErr);
	  
      // MC
      TH1F* SF1_=(TH1F*)SM->Get(MCMuSelections[sel]+"/"+MCHistograms[0]);
      TH1F* SF2_=(TH1F*)SM->Get(MCMuSelections[sel]+"/"+MCHistograms[1]);

      SF1_->Scale(MuLumi);
      SF2_->Scale(MuLumi);

      SF2_->Divide(SF1_);
	  
      // canvas
      char canvas_name1[30];
      sprintf(canvas_name1, "%i_RatioMu", sel);
      TCanvas *MuCanvas =new TCanvas(canvas_name1,canvas_name1 ,1);

      // Draw hisograms
      SF2_->SetTitle("r(2b/1b)");
      SF2_->GetXaxis()->SetTitle("B-tag efficiency scale factor");
      SF2_->GetXaxis()->CenterTitle();
      SF2_->GetYaxis()->SetTitle("events");
      SF2_->GetYaxis()->CenterTitle();
      SF2_->GetYaxis()->SetTitleOffset(1.25);
      SF2_->SetLineColor(4);
      
      SF2_->SetTitle("Loose RA4b selection");
      SF2_->GetXaxis()->SetTitle("b-tag efficiency scale factor");
      SF2_->GetXaxis()->CenterTitle();
      SF2_->GetYaxis()->SetTitle("ratio (2b/1b)");
      SF2_->GetYaxis()->CenterTitle();
      
      DataRatioMu_->SetLineColor(2);
      
      // change labels
      for(int ibin=0; ibin<=20; ++ibin)
	{
	  SF2_->GetXaxis()->SetBinLabel(ibin+1,labels[ibin]);
	}
      
      //draw hisograms
      SF2_->Draw("");
      DataRatioMu_->Draw("same");
      
      // TLine
      TLine * line = new TLine(8.5, 0.063, 8.5, 0.105 );
      
      line->SetLineWidth(2);
      line->SetLineStyle(7);
      line->SetLineColor(1);
      line->Draw("same");
	  
      TLine * line2 = new TLine(19.5, 0.063, 19.5, 0.169 );
      
      line2->SetLineWidth(2);
      line2->SetLineStyle(7);
      line2->SetLineColor(1);
      line2->Draw("same");
	  
      TLegend *leg = new TLegend(.5,.75,.8,.96);
      leg->SetTextFont(42);
      leg->SetFillColor(0);
      leg->SetLineColor(0);
      
      leg->AddEntry(SF2_,"All SM MC","l E");
      leg->AddEntry(DataRatioMu_,"MuHad","l E");
      
      leg->Draw("same");
      
      TPaveText *label = new TPaveText(0.15,0.78,0.45,0.88,"NDC");
      label->SetFillColor(0);
      label->SetTextFont(42);
      label->SetBorderSize(1);
      TText *text=label->AddText("L=4.124 fb^{-1}");
      text->SetTextAlign(22);
      label->Draw("same");
      
      MuCanvas->SaveAs(MCMuSelections[sel]+"_Ratio.pdf");
    }

  // Electron selection
  for(int sel=0; sel<(int)MCElSelections.size(); ++sel)
    { 
      // data
      TH1F* NrBtagEl=(TH1F*)ElHad->Get(DataElSelections[sel]+"/"+DataHistograms[sel]);
      
      double Nr1Btag=NrBtagEl->GetBinContent(2)+NrBtagEl->GetBinContent(3)+NrBtagEl->GetBinContent(4);
      double Nr2Btag=NrBtagEl->GetBinContent(3)+NrBtagEl->GetBinContent(4);
      
      std::cout << "Nr1Btag: " << Nr1Btag << std::endl;
      std::cout << "Nr2Btag: " << Nr2Btag << std::endl;
      
      double DataRatioEl=Nr2Btag/Nr1Btag;
      double DataRatioElErr=sqrt(pow((sqrt(Nr2Btag))/Nr1Btag, 2)+pow(Nr2Btag*(sqrt(Nr1Btag))/(Nr1Btag*Nr1Btag), 2));
      
      std::cout << "DataRatioEl: "<< DataRatioEl << " +- " << DataRatioElErr << std::endl;
	  
      TH1F* DataRatioEl_=new TH1F("DataRatioEl","DataRatioEl", 21, 0., 21.);
      DataRatioEl_->SetBinContent(11, DataRatioEl);
      DataRatioEl_->SetBinError(11, DataRatioElErr);
	  
      // MC
      TH1F* SF1_=(TH1F*)SM->Get(MCElSelections[sel]+"/"+MCHistograms[0]);
      TH1F* SF2_=(TH1F*)SM->Get(MCElSelections[sel]+"/"+MCHistograms[1]);

      SF1_->Scale(ElLumi);
      SF2_->Scale(ElLumi);

      SF2_->Divide(SF1_);
	  
      // canvas
      char canvas_name1[30];
      sprintf(canvas_name1, "%i_RatioEl", sel);
      TCanvas *ElCanvas =new TCanvas(canvas_name1,canvas_name1 ,1);

      // Draw hisograms
      SF2_->SetTitle("r(2b/1b)");
      SF2_->GetXaxis()->SetTitle("B-tag efficiency scale factor");
      SF2_->GetXaxis()->CenterTitle();
      SF2_->GetYaxis()->SetTitle("events");
      SF2_->GetYaxis()->CenterTitle();
      SF2_->GetYaxis()->SetTitleOffset(1.25);
      SF2_->SetLineColor(4);
      
      SF2_->SetTitle("Loose RA4b selection");
      SF2_->GetXaxis()->SetTitle("b-tag efficiency scale factor");
      SF2_->GetXaxis()->CenterTitle();
      SF2_->GetYaxis()->SetTitle("ratio (2b/1b)");
      SF2_->GetYaxis()->CenterTitle();
      
      DataRatioEl_->SetLineColor(2);
      
      // change labels
      for(int ibin=0; ibin<=20; ++ibin)
	{
	  SF2_->GetXaxis()->SetBinLabel(ibin+1,labels[ibin]);
	}
      
      //draw hisograms
      SF2_->Draw("");
      DataRatioEl_->Draw("same");
      
      // TLine
      TLine * line = new TLine(8.5, 0.053, 8.5, 0.101 );
      
      line->SetLineWidth(2);
      line->SetLineStyle(7);
      line->SetLineColor(1);
      line->Draw("same");
	  
      TLine * line2 = new TLine(19.5, 0.053, 19.5, 0.169 );
      
      line2->SetLineWidth(2);
      line2->SetLineStyle(7);
      line2->SetLineColor(1);
      line2->Draw("same");
	  
      TLegend *leg = new TLegend(.5,.75,.8,.96);
      leg->SetTextFont(42);
      leg->SetFillColor(0);
      leg->SetLineColor(0);
      
      leg->AddEntry(SF2_,"All SM MC","l E");
      leg->AddEntry(DataRatioEl_,"ElHad","l E");
      
      leg->Draw("same");
      
      TPaveText *label = new TPaveText(0.15,0.78,0.45,0.88,"NDC");
      label->SetFillColor(0);
      label->SetTextFont(42);
      label->SetBorderSize(1);
      TText *text=label->AddText("L=4.191 fb^{-1}");
      text->SetTextAlign(22);
      label->Draw("same");
      
      ElCanvas->SaveAs(MCElSelections[sel]+"_Ratio.pdf");
    }

  // Combined selection
  for(int sel=0; sel<(int)MCMuSelections.size(); ++sel)
    { 
      // data
      TH1F* NrBtagMu2_=(TH1F*)MuHad->Get(DataMuSelections[sel]+"/"+DataHistograms[sel]);
      

      double Nr1Btag=NrBtagMu2_->GetBinContent(2)+NrBtagMu2_->GetBinContent(3)+NrBtagMu2_->GetBinContent(4);
      double Nr2Btag=NrBtagMu2_->GetBinContent(3)+NrBtagMu2_->GetBinContent(4);
      
      std::cout << "Nr1Btag: " << Nr1Btag << std::endl;
      std::cout << "Nr2Btag: " << Nr2Btag << std::endl;
      
      double DataRatioMu=Nr2Btag/Nr1Btag;
      double DataRatioMuErr=sqrt(pow((sqrt(Nr2Btag))/Nr1Btag, 2)+pow(Nr2Btag*(sqrt(Nr1Btag))/(Nr1Btag*Nr1Btag), 2));
      
      std::cout << "DataRatioMu: "<< DataRatioMu << " +- " << DataRatioMuErr << std::endl;
	  
      TH1F* DataRatioMu_=new TH1F("DataRatioMu","DataRatioMu", 21, 0., 21.);
      DataRatioMu_->SetBinContent(11, DataRatioMu);
      DataRatioMu_->SetBinError(11, DataRatioMuErr);
	  
      // MC
      TH1F* SF1_=(TH1F*)SM->Get(MCMuSelections[sel]+"/"+MCHistograms[0]);
      TH1F* SF2_=(TH1F*)SM->Get(MCMuSelections[sel]+"/"+MCHistograms[1]);

      SF1_->Scale(MuLumi);
      SF2_->Scale(MuLumi);

      SF2_->Divide(SF1_);
	  
      // canvas
      char canvas_name1[30];
      sprintf(canvas_name1, "%i_RatioMu", sel);
      TCanvas *MuCanvas =new TCanvas(canvas_name1,canvas_name1 ,1);

      // Draw hisograms
      SF2_->SetTitle("r(2b/1b)");
      SF2_->GetXaxis()->SetTitle("B-tag efficiency scale factor");
      SF2_->GetXaxis()->CenterTitle();
      SF2_->GetYaxis()->SetTitle("events");
      SF2_->GetYaxis()->CenterTitle();
      SF2_->GetYaxis()->SetTitleOffset(1.25);
      SF2_->SetLineColor(4);
      
      SF2_->SetTitle("Loose RA4b selection");
      SF2_->GetXaxis()->SetTitle("b-tag efficiency scale factor");
      SF2_->GetXaxis()->CenterTitle();
      SF2_->GetYaxis()->SetTitle("ratio (2b/1b)");
      SF2_->GetYaxis()->CenterTitle();
      
      DataRatioMu_->SetLineColor(2);
      
      // change labels
      for(int ibin=0; ibin<=20; ++ibin)
	{
	  SF2_->GetXaxis()->SetBinLabel(ibin+1,labels[ibin]);
	}
      
      //draw hisograms
      SF2_->Draw("");
      DataRatioMu_->Draw("same");
      
      // TLine
      TLine * line = new TLine(8.5, 0.063, 8.5, 0.105 );
      
      line->SetLineWidth(2);
      line->SetLineStyle(7);
      line->SetLineColor(1);
      line->Draw("same");
	  
      TLine * line2 = new TLine(19.5, 0.063, 19.5, 0.169 );
      
      line2->SetLineWidth(2);
      line2->SetLineStyle(7);
      line2->SetLineColor(1);
      line2->Draw("same");
	  
      TLegend *leg = new TLegend(.5,.75,.8,.96);
      leg->SetTextFont(42);
      leg->SetFillColor(0);
      leg->SetLineColor(0);
      
      leg->AddEntry(SF2_,"All SM MC","l E");
      leg->AddEntry(DataRatioMu_,"MuHad","l E");
      
      leg->Draw("same");
      
      TPaveText *label = new TPaveText(0.15,0.78,0.45,0.88,"NDC");
      label->SetFillColor(0);
      label->SetTextFont(42);
      label->SetBorderSize(1);
      TText *text=label->AddText("L=4.124 fb^{-1}");
      text->SetTextAlign(22);
      label->Draw("same");
      
      MuCanvas->SaveAs(MCMuSelections[sel]+"_Ratio.pdf");
    }


  return 0;
}
