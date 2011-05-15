#include <vector>
#include <iostream>
#include <bitset>
#include <vector>
#include <fstream>
#include "TFile.h"
#include "TH1.h"
#include "TCanvas.h"
#include "TStyle.h"

vector<TFile*> Files;
vector<string> Names;
vector<double> Scales;
vector<unsigned int> Colors;
vector<unsigned int> FillColors;
vector<unsigned int> Styles;

int Plot1()
{
  std::cout << "Lese Files" << std::endl;

  Files.push_back (new TFile("Bjets_QCDMu.root", "READ"));
  Files.push_back (new TFile("Bjets_Wjets.root", "READ"));
  Files.push_back (new TFile("Bjets_Zjets.root", "READ"));
  Files.push_back (new TFile("Bjets_TTJets.root", "READ"));
  //Files.push_back (new TFile("Bjets_Mu.root", "READ"));
  //Files.push_back (new TFile("Bjets_LM1.root", "READ"));
  Files.push_back (new TFile("Bjets_tbGluinoOSET550.root", "READ"));
  Files.push_back (new TFile("Bjets_LM8.root", "READ"));

  // lumi in fb-1
  //double lumi=0.0359;
  //double lumi=0.25;
  double lumi=0.181;

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

  Scales.push_back(sQCDMu);
  Scales.push_back(sWjets);
  Scales.push_back(sZjets);
  Scales.push_back(sTTJets);
  //Scales.push_back(sData);
  //Scales.push_back(sLM1);  
  Scales.push_back(sG500);
  Scales.push_back(sLM8);

  //--------------------
  // Fuelle Histogramme
  //--------------------

  std::cout << "Fuelle Histogramme" << std::endl;

  TH1F* hist1=(TH1F*)Files[0]->Get("analyzeSUSY1b1l_1/HTidxMETidx");
  TH1F* hist2=(TH1F*)Files[1]->Get("analyzeSUSY1b1l_1/HTidxMETidx");
  TH1F* hist3=(TH1F*)Files[2]->Get("analyzeSUSY1b1l_1/HTidxMETidx");
  TH1F* hist4=(TH1F*)Files[3]->Get("analyzeSUSY1b1l_1/HTidxMETidx");

  TH1F* hist5=(TH1F*)Files[4]->Get("analyzeSUSY1b1l_1/HTidxMETidx");
  TH1F* hist6=(TH1F*)Files[5]->Get("analyzeSUSY1b1l_1/HTidxMETidx");

  hist1->Scale(Scales[0]);
  hist2->Scale(Scales[1]);
  hist3->Scale(Scales[2]);
  hist4->Scale(Scales[3]);
  hist5->Scale(Scales[4]);
  hist6->Scale(Scales[5]);

  hist1->SetMaximum(8);
  hist2->SetMaximum(8);
  hist3->SetMaximum(8);
  hist4->SetMaximum(400);
  hist5->SetMaximum(35);
  hist6->SetMaximum(12);

  hist1->SetMinimum(0);
  hist2->SetMinimum(0);
  hist3->SetMinimum(0);
  hist4->SetMinimum(0);
  hist5->SetMinimum(0);
  hist6->SetMinimum(0);

  //TH1F* QCDWjets=hist1->Add(hist2);
  TH1F *QCD = (TH1F*)hist1->Clone("QCD");
  TH1F *Wjets = (TH1F*)hist2->Clone("Wjets");
  TH1F *Zjets = (TH1F*)hist3->Clone("Zjets");
  TH1F *TTJets = (TH1F*)hist4->Clone("TTJets");

  QCD->Add(Wjets);
  QCD->Add(Zjets);
  QCD->SetMinimum(0);
  QCD->SetMaximum(8);

  TH1F *AllSM = (TH1F*)QCD->Clone("AllSM");
  AllSM->Add(TTJets);
  AllSM->SetMinimum(0);
  AllSM->SetMaximum(400);

  TH1F *AllSMLM3 = (TH1F*)AllSM->Clone("AllSMLM3");
  TH1F *AllSMLM8 = (TH1F*)AllSM->Clone("AllSMLM8");

  TH1F *LM3 = (TH1F*)hist5->Clone("LM3");
  TH1F *LM8 = (TH1F*)hist6->Clone("LM8");

  LM3->Divide(AllSMLM3);
  LM8->Divide(AllSMLM8);

  LM3->SetMinimum(0);
  LM3->SetMaximum(1.);

  LM8->SetMinimum(0);
  LM8->SetMaximum(0.2);

  //TH1F* OtherSM=QCDWjets->Add(hist3);

  //TH1F* allSM=hist4->Add(OtherSM);

  //hist1->Add(hist2);
  //hist2->Add(hist3);
  //hist3->Add(hist4);
  
  //hist5->Divide(hist3);
  
  //std::cout << hist5->GetNbinsX() << std::endl;
  
//   for(int j=1; j<hist5->GetNbinsX(); ++j)
//     {
//       std::cout << "bin " << j << std::endl;
//       //hist5->Integral(j,hist5->GetNbinsX());
//       std::cout << "S/B " << (hist5->Integral(j,hist5->GetNbinsX()))/(hist3->Integral(j,hist3->GetNbinsX())) << std::endl;
//     }
  
//===============================================================define styles: mystyle2==================================================

  TStyle *mystyle2 = new TStyle("mystyle2","mystyle2");

  //canvases
  //   mystyle2->SetCanvasColor(0);
  //   mystyle2->SetPalette         (1,0);
  //   mystyle2->SetCanvasBorderMode(1);
  mystyle2->SetCanvasColor(10);
  mystyle2->SetPalette(1);

  //pads
  mystyle2->SetPadTopMargin   (0.03);
  mystyle2->SetPadBottomMargin(0.15);
  mystyle2->SetPadLeftMargin  (0.14);
  mystyle2->SetPadRightMargin (0.16);
//   mystyle2->SetPadBorderMode  (0);
  
  //options
//   mystyle2->SetStatBorderSize(3);
  mystyle2->SetOptStat       (0);
//   mystyle2->SetOptTitle      (0);
//   mystyle2->SetStatW         (0.4);
//   mystyle2->SetStatH         (0.4);
//   mystyle2->SetDrawOption("colz");
  
  //titles
  mystyle2->SetTitleFillColor (0);
  //mystyle2->SetTitleBorderSize(3 );
  //  mystyle2->SetTitleH         (0.06);
//   mystyle2->SetTitleSize      (0.06, "X");
//   mystyle2->SetTitleSize      (0.06, "Y");
//   mystyle2->SetTitleSize      (0.06, "Z");
//   mystyle2->SetTitleOffset    (1,  "X");
//   mystyle2->SetTitleOffset    (1,  "Y");
//   mystyle2->SetTitleOffset    (1,  "Z");
  //mystyle2->SetTitleFont      (62,   "X");
  //mystyle2->SetTitleFont      (62,   "Y");
  //mystyle2->SetTitleFont      (62,   "Z");
  
  //labels
//   mystyle2->SetLabelSize(0.05,   "X");
//   mystyle2->SetLabelSize(0.05,   "Y");
//   mystyle2->SetLabelSize(0.05,   "Z");
//   mystyle2->SetLabelOffset(0.01, "X");
//   mystyle2->SetLabelOffset(0.01, "Y");
//   mystyle2->SetLabelOffset(0.01, "Z");
//   mystyle2->SetLabelFont(62,     "X");
//   mystyle2->SetLabelFont(62,     "Y");
//   mystyle2->SetLabelFont(62,     "Z");
  
  //Frames
//   mystyle2->SetFrameFillStyle (0);
//   mystyle2->SetFrameFillColor (kWhite);
//   mystyle2->SetFrameLineColor (kBlack);
//   mystyle2->SetFrameLineStyle (0);
//   mystyle2->SetFrameLineWidth (2);
//   mystyle2->SetFrameBorderMode(0);
  
  //histograms
//   mystyle2->SetHistFillColor(8);
//   mystyle2->SetHistFillStyle(5);
//   mystyle2->SetHistLineColor(kBlack);
//   mystyle2->SetHistLineStyle(0);
//   mystyle2->SetHistLineWidth(2);
//   mystyle2->SetNdivisions   (10, "X");
//   mystyle2->SetNdivisions   (5, "Y");
//   mystyle2->SetNdivisions   (5, "Z");
  
  // lines
//   mystyle2->SetLineColor(kBlack);
//   mystyle2->SetLineStyle(1);
//   mystyle2->SetLineWidth(2);
  
  //markers
//   mystyle2->SetMarkerStyle(kFullCircle);
//   mystyle2->SetMarkerStyle(3);
//   mystyle2->SetMarkerSize (0.5);
  
  //functions
//   mystyle2->SetFuncColor(kBlack);
//   mystyle2->SetFuncStyle(0);
//   mystyle2->SetFuncWidth(2);
  
  //ticks
//   mystyle2->SetTickLength(0.03);
  
  //statistics box
//   mystyle2->SetStatFont (62);
//   mystyle2->SetStatColor(0);
//   mystyle2->SetStatH    (0.20);
//   mystyle2->SetStatW    (0.30);
//   mystyle2->SetStatX    (0.965);
//   mystyle2->SetStatY    (0.95);
  
  gROOT->SetStyle("mystyle2");

  TCanvas *c1 =new TCanvas( "QCD" , "QCD" ,1);
  hist1->Draw("colz");
  hist1->GetXaxis()->SetTitle("HT [GeV]");
  hist1->GetXaxis()->CenterTitle();
  hist1->GetYaxis()->SetTitle("MET [GeV]");
  hist1->GetYaxis()->CenterTitle();
  hist1->GetZaxis()->SetTitle("# of events");
  hist1->GetZaxis()->CenterTitle();
  hist1->GetXaxis()->SetTitleSize(0.06);
  hist1->GetYaxis()->SetTitleSize(0.06);
  hist1->GetZaxis()->SetTitleSize(0.06);
  hist1->GetXaxis()->SetTitleOffset(1.1);
  hist1->GetYaxis()->SetTitleOffset(1);
  hist1->GetZaxis()->SetTitleOffset(0.8);
  hist1->SetTitle("QCD");
  //gPad->SetLogz();
  c1->SaveAs("QCD_1b.pdf");

  TCanvas *c2 =new TCanvas( "Wjets" , "Wjets" ,1);
  hist2->Draw("colz");
  hist2->GetXaxis()->SetTitle("HT [GeV]");
  hist2->GetXaxis()->CenterTitle();
  hist2->GetYaxis()->SetTitle("MET [GeV]");
  hist2->GetYaxis()->CenterTitle();
  hist2->GetZaxis()->SetTitle("# of events");
  hist2->GetZaxis()->CenterTitle();
  hist2->GetXaxis()->SetTitleSize(0.06);
  hist2->GetYaxis()->SetTitleSize(0.06);
  hist2->GetZaxis()->SetTitleSize(0.06);
  hist2->GetXaxis()->SetTitleOffset(1.1);
  hist2->GetYaxis()->SetTitleOffset(1);
  hist2->GetZaxis()->SetTitleOffset(0.8);
  hist2->SetTitle("Wjets");
  //gPad->SetLogz();
  c2->SaveAs("Wjets_1b.pdf");

  TCanvas *c3 =new TCanvas( "Zjets" , "Zjets" ,1);
  hist3->Draw("colz");
  hist3->GetXaxis()->SetTitle("HT [GeV]");
  hist3->GetXaxis()->CenterTitle();
  hist3->GetYaxis()->SetTitle("MET [GeV]");
  hist3->GetYaxis()->CenterTitle();
  hist3->GetZaxis()->SetTitle("# of events");
  hist3->GetZaxis()->CenterTitle();
  hist3->GetXaxis()->SetTitleSize(0.06);
  hist3->GetYaxis()->SetTitleSize(0.06);
  hist3->GetZaxis()->SetTitleSize(0.06);
  hist3->GetXaxis()->SetTitleOffset(1.1);
  hist3->GetYaxis()->SetTitleOffset(1);
  hist3->GetZaxis()->SetTitleOffset(0.8);
  hist3->SetTitle("Zjets");
  //gPad->SetLogz();
  c3->SaveAs("Zjets_1b.pdf");

  TCanvas *c4 =new TCanvas("ttbar" , "ttbar" ,1);
  hist4->Draw("colz");
  hist4->GetXaxis()->SetTitle("HT [GeV]");
  hist4->GetXaxis()->CenterTitle();
  hist4->GetYaxis()->SetTitle("MET [GeV]");
  hist4->GetYaxis()->CenterTitle();
  hist4->GetZaxis()->SetTitle("# of events");
  hist4->GetZaxis()->CenterTitle();
  hist4->GetXaxis()->SetTitleSize(0.06);
  hist4->GetYaxis()->SetTitleSize(0.06);
  hist4->GetZaxis()->SetTitleSize(0.06);
  hist4->GetXaxis()->SetTitleOffset(1.1);
  hist4->GetYaxis()->SetTitleOffset(1);
  hist4->GetZaxis()->SetTitleOffset(0.8);
  hist4->SetTitle("ttbar");
  //gPad->SetLogz();
  c4->SaveAs("TTJets_1b.pdf");

  TCanvas *c5 =new TCanvas("LM3" , "LM3" ,1);
  hist5->Draw("colz");
  hist5->GetXaxis()->SetTitle("HT [GeV]");
  hist5->GetXaxis()->CenterTitle();
  hist5->GetYaxis()->SetTitle("MET [GeV]");
  hist5->GetYaxis()->CenterTitle();
  hist5->GetZaxis()->SetTitle("# of events");
  hist5->GetZaxis()->CenterTitle();
  hist5->GetXaxis()->SetTitleSize(0.06);
  hist5->GetYaxis()->SetTitleSize(0.06);
  hist5->GetZaxis()->SetTitleSize(0.06);
  hist5->GetXaxis()->SetTitleOffset(1.1);
  hist5->GetYaxis()->SetTitleOffset(1);
  hist5->GetZaxis()->SetTitleOffset(0.8);
  hist5->SetTitle("LM3");
  //gPad->SetLogz();
  c5->SaveAs("LM3_1b.pdf");
  
  TCanvas *c6 =new TCanvas("Other SM" , "Other SM" ,1);
  hist6->Draw("colz");
  hist6->GetXaxis()->SetTitle("HT [GeV]");
  hist6->GetXaxis()->CenterTitle();
  hist6->GetYaxis()->SetTitle("MET [GeV]");
  hist6->GetYaxis()->CenterTitle();
  hist6->GetZaxis()->SetTitle("# of events");
  hist6->GetZaxis()->CenterTitle();
  hist6->GetXaxis()->SetTitleSize(0.06);
  hist6->GetYaxis()->SetTitleSize(0.06);
  hist6->GetZaxis()->SetTitleSize(0.06);
  hist6->GetXaxis()->SetTitleOffset(1.1);
  hist6->GetYaxis()->SetTitleOffset(1);
  hist6->GetZaxis()->SetTitleOffset(0.8);
  hist6->SetTitle("Other SM");
  //gPad->SetLogz();
  c6->SaveAs("OtherSM_1b.pdf");

  TCanvas *c7 =new TCanvas( "All SM" , "All SM" ,1);
  AllSM->Draw("colz");
  AllSM->GetXaxis()->SetTitle("HT [GeV]");
  AllSM->GetXaxis()->CenterTitle();
  AllSM->GetYaxis()->SetTitle("MET [GeV]");
  AllSM->GetYaxis()->CenterTitle();
  AllSM->GetZaxis()->SetTitle("# of events");
  AllSM->GetZaxis()->CenterTitle();
  AllSM->GetXaxis()->SetTitleSize(0.06);
  AllSM->GetYaxis()->SetTitleSize(0.06);
  AllSM->GetZaxis()->SetTitleSize(0.06);
  AllSM->GetXaxis()->SetTitleOffset(1.1);
  AllSM->GetYaxis()->SetTitleOffset(1);
  AllSM->GetZaxis()->SetTitleOffset(0.8);
  AllSM->SetTitle("All SM");
  //gPad->SetLogz();
  c7->SaveAs("AllSM_1b.pdf");

  TCanvas *c8 =new TCanvas("LM8" , "LM8" ,1);
  hist6->Draw("colz");
  hist6->GetXaxis()->SetTitle("HT [GeV]");
  hist6->GetXaxis()->CenterTitle();
  hist6->GetYaxis()->SetTitle("MET [GeV]");
  hist6->GetYaxis()->CenterTitle();
  hist6->GetZaxis()->SetTitle("# of events");
  hist6->GetZaxis()->CenterTitle();
  hist6->GetXaxis()->SetTitleSize(0.06);
  hist6->GetYaxis()->SetTitleSize(0.06);
  hist6->GetZaxis()->SetTitleSize(0.06);
  hist6->GetXaxis()->SetTitleOffset(1.1);
  hist6->GetYaxis()->SetTitleOffset(1);
  hist6->GetZaxis()->SetTitleOffset(0.8);
  hist6->SetTitle("LM8");
  //gPad->SetLogz();
  c8->SaveAs("LM8_1b.pdf");

  TCanvas *c9 =new TCanvas("LM3Sig" , "LM3Sig" ,1);
  LM3->Draw("colz");
  LM3->GetXaxis()->SetRangeUser(250,600);
  LM3->GetXaxis()->SetTitle("HT [GeV]");
  LM3->GetXaxis()->CenterTitle();
  LM3->GetYaxis()->SetTitle("MET [GeV]");
  LM3->GetYaxis()->CenterTitle();
  LM3->GetZaxis()->SetTitle("signal over background");
  LM3->GetZaxis()->CenterTitle();
  LM3->GetXaxis()->SetTitleSize(0.06);
  LM3->GetYaxis()->SetTitleSize(0.06);
  LM3->GetZaxis()->SetTitleSize(0.06);
  LM3->GetXaxis()->SetTitleOffset(1.1);
  LM3->GetYaxis()->SetTitleOffset(1);
  LM3->GetZaxis()->SetTitleOffset(0.8);
  LM3->SetTitle("OSET/SM");
  //gPad->SetLogz();
  c9->SaveAs("OSETSig_1b.pdf");

  TCanvas *c10 =new TCanvas("LM8Sig" , "LM8Sig" ,1);
  LM8->Draw("colz");
  LM8->GetXaxis()->SetTitle("HT [GeV]");
  LM8->GetXaxis()->CenterTitle();
  LM8->GetYaxis()->SetTitle("MET [GeV]");
  LM8->GetYaxis()->CenterTitle();
  LM8->GetZaxis()->SetTitle("signal over background");
  LM8->GetZaxis()->CenterTitle();
  LM8->GetXaxis()->SetTitleSize(0.06);
  LM8->GetYaxis()->SetTitleSize(0.06);
  LM8->GetZaxis()->SetTitleSize(0.06);
  LM8->GetXaxis()->SetTitleOffset(1.1);
  LM8->GetYaxis()->SetTitleOffset(1);
  LM8->GetZaxis()->SetTitleOffset(0.8);
  LM8->SetTitle("LM8/SM");
  //gPad->SetLogz();
  c10->SaveAs("LM8Sig_1b.pdf");
 
  return 0;
  
}
