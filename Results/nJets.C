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
vector<string> Names;
vector<double> Scales;
vector<unsigned int> Colors;
vector<unsigned int> FillColors;
vector<unsigned int> Styles;

int nJets()
{

  Files.push_back (new TFile("TTJets350.root", "READ"));
  Files.push_back (new TFile("LM3350.root", "READ"));

// lumi in fb-1
  //double lumi=0.0359;
  //double lumi=0.25;
  double lumi=1;

  // cross-sections
  double xsecQCDMu=296900000*0.00037;
  double xsecZjets=3048;
  double xsecWjets=3131;
  double xsecTTJets=158;
  double xsecLM1=4.888;
  double xsecLM3=3.438;
  double xsecLM8=0.73;
  double xsecLM7=1.209;
  double xsecLM9=7.134;
  double xsecLM12=4.414;
  double xsecG400=19.3944;
  double xsecG450=8.31098;
  double xsecG500=1.86744;
  double xsecG550=0.967942;
  double xsecG600=0.507335;
  double xsecG650=0.28241;
  double xsecG700=0.157907;
  double xsecG750=0.0902996;
  double xsecG800=0.0526242;

  // number of events
  double nQCD=29034562;
  double nZjets=2543706;
  double nWjets=10822996;
  double nTTJets=1286491;
  double nLM1=219190;
  double nLM3=220000;
  double nLM8=220000;
  double nLM7=220000;
  double nLM9=220000;
  double nLM12=219595;
  double nG400=10000;
  double nG450=10000;
  double nG500=10000;
  double nG550=10000;
  double nG600=10000;
  double nG650=10000;
  double nG700=10000;
  double nG750=10000;
  double nG800=10000;

  // weights
  double sQCDMu=lumi*1000*xsecQCDMu/(nQCD);  //3.72322;
  double sZjets=lumi*1000*xsecZjets/(nZjets);  //1.19824;
  double sWjets=lumi*1000*xsecWjets/(nWjets);  //2.11502;
  double sTTJets=lumi*1000*xsecTTJets/(nTTJets);  //0.13623;
  double sLM1=lumi*1000*xsecLM1/(nLM1);  //0.02230;
  double sLM3=lumi*1000*xsecLM3/(nLM3);  //0.01563;
  double sLM8=lumi*1000*xsecLM8/(nLM8);  //0.00332;
  double sLM7=lumi*1000*xsecLM7/(nLM7);
  double sLM9=lumi*1000*xsecLM9/(nLM9);
  double sLM12=lumi*1000*xsecLM12/(nLM12);
  double sData=1;
  double sG400=lumi*1000*xsecG400/(nG400);  //0.02230;
  double sG450=lumi*1000*xsecG450/(nG450);  //0.02230;
  double sG500=lumi*1000*xsecG500/(nG500);  //0.01563;
  double sG550=lumi*1000*xsecG550/(nG550);  //0.02230;
  double sG600=lumi*1000*xsecG600/(nG600);  //0.02230;
  double sG650=lumi*1000*xsecG650/(nG650);  //0.01563;
  double sG700=lumi*1000*xsecG700/(nG700);  //0.02230;
  double sG750=lumi*1000*xsecG750/(nG750);  //0.02230;
  double sG800=lumi*1000*xsecG800/(nG800);  //0.01563;

  //Scales.push_back(sQCDMu);
  //Scales.push_back(sWjets);
  //Scales.push_back(sZjets);
  Scales.push_back(sTTJets);
  //Scales.push_back(sData);
  Scales.push_back(sLM3);  
  //Scales.push_back(sG500);
  //Scales.push_back(sLM9);

  //TH1F* hist1=(TH1F*)Files[0]->Get("analyzeSUSY1l_metSelection/nJets");
  //TH1F* hist2=(TH1F*)Files[0]->Get("analyzeSUSY1l_metSelection/nJets_control");
  //TH1F* hist3=(TH1F*)Files[1]->Get("analyzeSUSY1l_metSelection/nJets");

  TH1F* hist1=(TH1F*)Files[0]->Get("analyzeSUSY2b1l_3/nJets");
  TH1F* hist2=(TH1F*)Files[0]->Get("analyzeSUSY2b1l_3/nJets_control");
  TH1F* hist3=(TH1F*)Files[1]->Get("analyzeSUSY2b1l_3/nJets");
  TH1F* hist4=(TH1F*)Files[1]->Get("analyzeSUSY2b1l_3/nJets_control");

  double hist1Int=hist1->Integral(4,hist1->GetNbinsX());
  double hist2Int=hist2->Integral(4,hist2->GetNbinsX());

  hist1->Scale(Scales[0]);
  hist2->Scale(Scales[0]);
  hist3->Scale(Scales[1]);
  hist4->Scale(Scales[1]);

  hist2->Add(hist4);

  double AllBins= hist1Int/hist2Int;

  //double nJetsBin2= Scales[0]*(hist1->GetBinContent(3));
  //double nJetsBin3= Scales[0]*(hist1->GetBinContent(4));
  //double nJetsBin4= Scales[0]*(hist1->GetBinContent(5));

  double nJetsBin2= Scales[0]*(hist1->GetBinContent(3))+Scales[1]*(hist3->GetBinContent(3));
  double nJetsBin3= Scales[0]*(hist1->GetBinContent(4))+Scales[1]*(hist3->GetBinContent(3));
  double nJetsBin4= Scales[0]*(hist1->GetBinContent(5))+Scales[1]*(hist3->GetBinContent(3));

  double nJetsControlBin2= Scales[0]*(hist2->GetBinContent(3));
  double nJetsControlBin3= Scales[0]*(hist2->GetBinContent(4));
  double nJetsControlBin4= Scales[0]*(hist2->GetBinContent(5));

  //double nJetsControlBin2= Scales[0]*(hist2->GetBinContent(3))+Scales[4]*(hist4->GetBinContent(3));
  //double nJetsControlBin3= Scales[0]*(hist2->GetBinContent(4))+Scales[4]*(hist4->GetBinContent(3));
  //double nJetsControlBin4= Scales[0]*(hist2->GetBinContent(5))+Scales[4]*(hist4->GetBinContent(3));

  double Bin2=nJetsBin2/nJetsControlBin2;
  double Bin3=nJetsBin3/nJetsControlBin3;
  double Bin4=nJetsBin4/nJetsControlBin4;

  //hist1->Scale(1/hist1Int);
  //hist2->Scale(1/hist2Int);

  hist2->Scale(Bin3);

  std::cout << "TTbar MC truth: " << hist1->Integral(8,hist1->GetNbinsX()) << " events" << std::endl;
  std::cout << "TTbar estimate: " << hist2->Integral(8,hist2->GetNbinsX()) << " events" << std::endl;
  std::cout << "LM9 MC truth: " << hist3->Integral(8,hist3->GetNbinsX()) << " events" << std::endl;

  double significance=((hist3->Integral(8,hist3->GetNbinsX()))/(sqrt(hist2->Integral(8,hist2->GetNbinsX())+hist3->Integral(8,hist3->GetNbinsX()))));

  std::cout << "Significance: " << significance << std::endl; 

  hist1->SetLineColor(7);
  hist2->SetLineColor(2);
  hist3->SetLineColor(1);

  hist1->SetFillColor(7);
  hist2->SetLineWidth(2);
  hist3->SetLineWidth(2);
 
 //hist1->SetMaximum(0.09);
  //hist1->SetMinimum(0);

  TCanvas *c1 =new TCanvas( "TTJets" , "TTJets" ,1);
  hist1->Draw("");
  hist1->GetXaxis()->SetTitle("number of good Jets (Et > 40 GeV)");
  hist1->GetXaxis()->CenterTitle();
  hist1->GetYaxis()->SetTitle("# events normalized to bin3 of all Ttbar");
  hist1->GetYaxis()->CenterTitle();
  hist2->Draw("same");
  hist3->Draw("same");

  gPad->SetLogy();

  TLegend *leg = new TLegend(.62,.65,.99,.99);
  leg->SetTextFont(42);
  leg->SetFillColor(0);
  leg->SetLineColor(0);

  leg->AddEntry(hist1,"all Ttbar" ,"l");
  leg->AddEntry(hist2,"Ttbar estimate" ,"l");
  leg->AddEntry(hist3,"all LM3" ,"l");

  leg->SetFillColor(10);
  leg->Draw("box");

  c1->SaveAs("LM3corrected.pdf");

  return 0;
  
}
