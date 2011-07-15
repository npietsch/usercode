#include <vector>
#include <iostream>
#include <bitset>
#include <vector>
#include <fstream>
#include "TFile.h"
#include "TH1.h"
#include "TCanvas.h"
#include "TStyle.h"
#include "TPaveText.h"

vector<TFile*> Files;
vector<string> Names;
vector<double> Scales;
vector<unsigned int> Colors;
vector<unsigned int> FillColors;
vector<unsigned int> Styles;

int Colz2()
{
  std::cout << "Lese Files" << std::endl;

  Files.push_back (new TFile("TTJets.root", "READ"));
  //Files.push_back (new TFile("LM3.root", "READ"));
  //Files.push_back (new TFile("LM8.root", "READ"));
  Files.push_back (new TFile("LM9.root", "READ"));

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
  //Scales.push_back(sLM1);  
  // Scales.push_back(sG500);
  //Scales.push_back(sLM3);
  //Scales.push_back(sLM8);
  Scales.push_back(sLM9);

  //--------------------
  // Fuelle Histogramme
  //--------------------

  std::cout << "Fuelle Histogramme" << std::endl;

  TH2F* hist1=(TH2F*)Files[0]->Get("analyzeSUSY1l_metSelection/mW_MT");
  TH2F* hist2=(TH2F*)Files[1]->Get("analyzeSUSY1l_metSelection/mW_MT");
  //TH2F* hist3=(TH2F*)Files[2]->Get("analyzeSUSY1b1l_3/mW_nJets");
  //TH2F* hist4=(TH2F*)Files[3]->Get("analyzeSUSY1b1l_3/mW_nJets");

  //TH2F* hist1=(TH2F*)Files[0]->Get("analyzeEventTopology1b1l_mediumTCHE_3/HT_dPhiLepMETMin");
  //TH2F* hist2=(TH2F*)Files[1]->Get("analyzeEventTopology1b1l_mediumTCHE_3/HT_dPhiLepMETMin");

  hist1->Scale(Scales[0]);
  hist2->Scale(Scales[1]);
  //hist3->Scale(Scales[2]);
  //hist4->Scale(Scales[3]);

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
  
  double A=hist1->Integral(1,  4, 12, hist1->GetNbinsY());
  double D=hist1->Integral(1,  4,  1, 11);
  
  double B=hist1->Integral(5, 10, 12, hist1->GetNbinsY());
  double E=hist1->Integral(5, 10,  1, 11);
  
  double C=hist1->Integral(11, hist1->GetNbinsX(), 12, hist1->GetNbinsY());
  double F=hist1->Integral(11, hist1->GetNbinsX(),  1, 11);

  double AD=A/D;
  double BE=B/E;
  double CF=C/F;
  
  std::cout << "A: " << A << std::endl;
  std::cout << "B: " << B << std::endl;
  std::cout << "C: " << C << std::endl;
  std::cout << "D: " << D << std::endl;
  std::cout << "E: " << E << std::endl;
  std::cout << "F: " << F << std::endl;

  std::cout << "----------" << std::endl;
  std::cout << "A/D: " << AD << std::endl;
  std::cout << "B/E: " << BE << std::endl;
  std::cout << "C/F: " << CF << std::endl;
  std::cout << "----------" << std::endl;


  //std::cout << "Estimate: " << Estimate << std::endl;

  gROOT->SetStyle("mystyle2");

  TCanvas *c1 =new TCanvas( "Ttbar" , "Ttbar" ,1);
  hist1->Draw("colz");
  hist1->GetXaxis()->SetTitle("mW [GeV]");
  hist1->GetXaxis()->CenterTitle();
  hist1->GetYaxis()->SetTitle("HT [GeV]");
  hist1->GetYaxis()->CenterTitle();
  hist1->GetYaxis()->SetRangeUser(350,2000);
  hist1->GetZaxis()->SetTitle("# of events");
  hist1->GetZaxis()->CenterTitle();
  hist1->GetXaxis()->SetTitleSize(0.06);
  hist1->GetYaxis()->SetTitleSize(0.06);
  hist1->GetZaxis()->SetTitleSize(0.06);
  hist1->GetXaxis()->SetTitleOffset(1.1);
  hist1->GetYaxis()->SetTitleOffset(1);
  hist1->GetZaxis()->SetTitleOffset(0.8);
  hist1->SetTitle("Ttbar");

  // TLine
  TLine * line = new TLine(50, 350, 50, 2000);
  line->SetLineWidth(3);
  line->SetLineStyle(1);
  line->SetLineColor(1);
  line->Draw("same");
  TLine * line2 = new TLine(100, 350, 100, 2000);
  line2->SetLineWidth(3);
  line2->SetLineStyle(1);
  line2->SetLineColor(1);
  line2->Draw("same");
  TLine * line3 = new TLine(0, 600, 200, 600);
  line3->SetLineWidth(3);
  line3->SetLineStyle(1);
  line3->SetLineColor(1);
  line3->Draw("same");

  //gPad->SetLogz();
  c1->SaveAs("HT_mW_Ttbar.pdf");

  TCanvas *c2 =new TCanvas( "LM9" , "LM9" ,1);
  hist2->Draw("colz");
  hist2->GetXaxis()->SetTitle("mW [GeV]");
  hist2->GetXaxis()->CenterTitle();
  hist2->GetYaxis()->SetTitle("HT [GeV]");
  hist2->GetYaxis()->CenterTitle();
  hist2->GetYaxis()->SetRangeUser(350,2000);
  hist2->GetZaxis()->SetTitle("# of events");
  hist2->GetZaxis()->CenterTitle();
  hist2->GetXaxis()->SetTitleSize(0.06);
  hist2->GetYaxis()->SetTitleSize(0.06);
  hist2->GetZaxis()->SetTitleSize(0.06);
  hist2->GetXaxis()->SetTitleOffset(1.1);
  hist2->GetYaxis()->SetTitleOffset(1);
  hist2->GetZaxis()->SetTitleOffset(0.8);
  hist2->SetTitle("LM9");

  line->Draw("same");
  line2->Draw("same");
  line3->Draw("same");

  //gPad->SetLogz();
  c2->SaveAs("HT_mW_LM9.pdf");

//   TCanvas *c3 =new TCanvas( "LM8" , "LM8" ,1);
//   hist3->Draw("colz");
//   hist3->GetXaxis()->SetTitle("mW [GeV]");
//   hist3->GetXaxis()->CenterTitle();
//   hist3->GetYaxis()->SetTitle("nJets [GeV]");
//   hist3->GetYaxis()->CenterTitle();
//   hist3->GetZaxis()->SetTitle("# of events");
//   hist3->GetZaxis()->CenterTitle();
//   hist3->GetXaxis()->SetTitleSize(0.06);
//   hist3->GetYaxis()->SetTitleSize(0.06);
//   hist3->GetZaxis()->SetTitleSize(0.06);
//   hist3->GetXaxis()->SetTitleOffset(1.1);
//   hist3->GetYaxis()->SetTitleOffset(1);
//   hist3->GetZaxis()->SetTitleOffset(0.8);
//   hist3->SetTitle("LM8");
//   //gPad->SetLogz();
//   c3->SaveAs("nJets_mW_LM8.pdf");

//   TCanvas *c4 =new TCanvas( "LM9" , "LM9" ,1);
//   hist4->Draw("colz");
//   hist4->GetXaxis()->SetTitle("mW [GeV]");
//   hist4->GetXaxis()->CenterTitle();
//   hist4->GetYaxis()->SetTitle("nJets [GeV]");
//   hist4->GetYaxis()->CenterTitle();
//   hist4->GetZaxis()->SetTitle("# of events");
//   hist4->GetZaxis()->CenterTitle();
//   hist4->GetXaxis()->SetTitleSize(0.06);
//   hist4->GetYaxis()->SetTitleSize(0.06);
//   hist4->GetZaxis()->SetTitleSize(0.06);
//   hist4->GetXaxis()->SetTitleOffset(1.1);
//   hist4->GetYaxis()->SetTitleOffset(1);
//   hist4->GetZaxis()->SetTitleOffset(0.8);
//   hist4->SetTitle("LM9");
//   //gPad->SetLogz();
//   c4->SaveAs("nJets_mW_LM9.pdf");

  return 0;
  
}
