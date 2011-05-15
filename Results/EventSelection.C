#include <TROOT.h>
#include "TFile.h"
#include "TH1.h"
#include "TTree.h"
#include "TKey.h"
#include "TF1.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <Plot.h>

vector<TFile*> Files;
vector<string> Names;
vector<double> Scales;
vector<unsigned int> Colors;
vector<unsigned int> FillColors;
vector<unsigned int> Styles;
vector<TString> selection;

int EventSelection()
{
  Files.push_back (new TFile("Bjets_QCDMu.root", "READ"));
  Files.push_back (new TFile("Bjets_Zjets.root", "READ"));
  Files.push_back (new TFile("Bjets_Wjets.root", "READ"));
  Files.push_back (new TFile("Bjets_TTJets.root", "READ"));
  //Files.push_back (new TFile("Bjets_TTJetsSemiMuon.root", "READ"));
  Files.push_back (new TFile("Bjets_Mu.root", "READ"));
  //Files.push_back (new TFile("Bjets_LM1.root", "READ"));
  Files.push_back (new TFile("Bjets_LM3.root", "READ"));
  //Files.push_back (new TFile("Bjets_LM8.root", "READ"));
  //Files.push_back (new TFile("Bjets_LM7.root", "READ"));
  //Files.push_back (new TFile("Bjets_LM9.root", "READ"));
  //Files.push_back (new TFile("Bjets_LM12.root", "READ"));
  //Files.push_back (new TFile("Bjets_Mu.root", "READ"));
  //Files.push_back (new TFile("Bjets_tbGluinoOSET400.root", "READ"));
  //Files.push_back (new TFile("Bjets_GluinoOSET450.root", "READ"));
  Files.push_back (new TFile("Bjets_tbGluinoOSET500.root", "READ"));
  //Files.push_back (new TFile("Bjets_GluinoOSET550.root", "READ"));
  //Files.push_back (new TFile("Bjets_GluinoOSET600.root", "READ"));
  //Files.push_back (new TFile("Bjets_GluinoOSET650.root", "READ"));
  //Files.push_back (new TFile("Bjets_GluinoOSET700.root", "READ"));
  //Files.push_back (new TFile("Bjets_GluinoOSET750.root", "READ"));
  //Files.push_back (new TFile("Bjets_GluinoOSET800.root", "READ"));
  
  int f=Files.size();
  
  Names.push_back("QCD #mu");
  Names.push_back("Z+Jets");
  Names.push_back("W+Jets");
  Names.push_back("t#bar{t}");
  //Names.push_back("t#bar{t} semilep. #mu");
  Names.push_back("2011 Data");
  //Names.push_back("LM1");
  Names.push_back("LM3");
  //Names.push_back("LM8");
  //Names.push_back("LM7");
  //Names.push_back("LM9");
  //Names.push_back("LM12");
  //Names.push_back("G400LSP10");
  //Names.push_back("G450LSP40");
  Names.push_back("G500LSP140");
  //Names.push_back("G550LSP10");
  //Names.push_back("G600LSP190");
  //Names.push_back("G650LSP290");
  //Names.push_back("G700LSP10");
  //Names.push_back("G750LSP340");
  //Names.push_back("G800LSP440");

  // lumi in fb-1
  //double lumi=0.0359;
  //double lumi=0.25;
  double lumi=0.181;

  // cross-sections
  double xsecQCDMu=296900000*0.00037;
  double xsecZjets=3048;
  double xsecWjets=31314;
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
  Scales.push_back(sZjets);
  Scales.push_back(sWjets);
  //Scales.push_back(sTTJets);
  Scales.push_back(sTTJets);
  Scales.push_back(sData);
  //Scales.push_back(sLM1);  
  Scales.push_back(sLM3);
  //Scales.push_back(sLM8);
  //Scales.push_back(sLM7);  
  //Scales.push_back(sLM9);
  //Scales.push_back(sLM12);
  //Scales.push_back(sData);
  //Scales.push_back(sG400);  
  //Scales.push_back(sG450);
  Scales.push_back(sG500);
  //Scales.push_back(sG550);  
  //Scales.push_back(sG600);
  //Scales.push_back(sG650);
  //Scales.push_back(sG700);  
  //Scales.push_back(sG750);
  //Scales.push_back(sG800);

  //Colors.push_back(38);
  //Colors.push_back(10);
  //Colors.push_back(45);
  //Colors.push_back(42);
  //Colors.push_back(42);
  //Colors.push_back(42);
  //Colors.push_back(42);
  Colors.push_back(17);
  Colors.push_back(7);
  Colors.push_back(48);
  Colors.push_back(3);
  //Colors.push_back(38);
  Colors.push_back(1);
  Colors.push_back(2);
  Colors.push_back(4);
  Colors.push_back(1);

  //Styles.push_back(1101);
  //Styles.push_back(1101);
  //Styles.push_back(1101);
  //Styles.push_back(1101);
  //Styles.push_back(1101);
  //Styles.push_back(1101);
  //Styles.push_back(1101);
  //Styles.push_back(1101);
  Styles.push_back(1101);
  Styles.push_back(1101);
  Styles.push_back(1101);
  Styles.push_back(1101);
  //Styles.push_back(1101);
  Styles.push_back(0);
  Styles.push_back(0);
  Styles.push_back(0);
  Styles.push_back(0);

  //FillColors.push_back(38);
  //FillColors.push_back(10);
  //FillColors.push_back(45);
  //FillColors.push_back(42);
  //FillColors.push_back(42);
  //FillColors.push_back(42);
  FillColors.push_back(17);
  FillColors.push_back(7);
  FillColors.push_back(48);
  FillColors.push_back(3);
  FillColors.push_back(38);
  FillColors.push_back(0);
  FillColors.push_back(0);
  FillColors.push_back(0);
  FillColors.push_back(0);

  //selection.push_back("1l_noCuts");
  //selection.push_back("1l_preselection");
  //selection.push_back("1l_oneGoodMuon");
  //selection.push_back("1l_fourGoodJets");
  //selection.push_back("1l_oneTightJet");
  //selection.push_back("1l_twoMediumJets");
  //selection.push_back("1l_HTSelection");
  //selection.push_back("1l_metSelection");


  //selection.push_back("1l");
  //selection.push_back("1b1l");
  //selection.push_back("2b1l");
  //selection.push_back("3b1l");
  //selection.push_back("4b1l");
  //selection.push_back("2l");
  //selection.push_back("1b2l");
  //selection.push_back("2b2l");
  //selection.push_back("3b2l");
  //selection.push_back("4b2l");

  int s=selection.size();

  //--------------------
  // Create histograms
  //--------------------

  plotSet plots("Name");

  for(int j=0; j<1; ++j)
    {
      std::cout << "Start creating histograms" << std::endl;

      for(int i=0; i<f; ++i)
	{
	  // Event Selection
	  //------------------

	  // plots.addPlot((TH1F*)Files[i]->Get("analyzeSUSY1l_preselection/nMuons"),Names[i],"nMuons_1l_preselection",Scales[i],Colors[i],Styles[i],FillColors[i]);
// 	  plots.SetAxesTitles("nMuons_1l_preselection","Number of isolated Muons", "");
// 	  plots.addPlot((TH1F*)Files[i]->Get("analyzeSUSY1l_oneGoodMuon/nMuons"),Names[i],"nMuons_1l_oneGoodMuon",Scales[i],Colors[i],Styles[i],FillColors[i]);
// 	  plots.SetAxesTitles("nMuons_1l_oneGoodMuon","Number of isolated Muons", "");

// 	  plots.addPlot((TH1F*)Files[i]->Get("analyzeSUSY1l_oneGoodMuon/nJets"),Names[i],"nJets_1l_oneGoodMuon",Scales[i],Colors[i],Styles[i],FillColors[i]);
// 	  plots.SetAxesTitles("nJets_1l_oneGoodMuon","Number of good Jets", "");
// 	  plots.addPlot((TH1F*)Files[i]->Get("analyzeSUSY1l_fourGoodJets/nJets"),Names[i],"nJets_1l_fourGoodJets",Scales[i],Colors[i],Styles[i],FillColors[i]);
// 	  plots.SetAxesTitles("nJets_1l_fourGoodJets","Number of good Jets", "");

	 //  plots.addPlot((TH1F*)Files[i]->Get("analyzeSUSY1l_fourGoodJets/Jet0_Et"),Names[i],"Jet0_Et_1l_fourGoodJets",Scales[i],Colors[i],Styles[i],FillColors[i]);
// 	  plots.SetAxesTitles("Jet0_Et_1l_fourGoodJets","E_{T} leading Jet [GeV]", "");
// 	  plots.addPlot((TH1F*)Files[i]->Get("analyzeSUSY1l_oneTightJet/Jet0_Et"),Names[i],"Jet0_Et_1l_oneTightJet",Scales[i],Colors[i],Styles[i],FillColors[i]);
// 	  plots.SetAxesTitles("Jet0_Et_1l_oneTightJet","E_{T} leading Jet [GeV]", "");

	  // plots.addPlot((TH1F*)Files[i]->Get("analyzeSUSY1l_fourGoodJets/Jet1_Et"),Names[i],"Jet1_Et_1l_fourGoodJets",Scales[i],Colors[i],Styles[i],FillColors[i]);
// 	  plots.SetAxesTitles("Jet1_Et_1l_fourGoodJets","E_{T} 2^{nd} leading Jet [GeV]", "");
// 	  plots.addPlot((TH1F*)Files[i]->Get("analyzeSUSY1l_oneTightJet/Jet1_Et"),Names[i],"Jet1_Et_1l_oneTightJet",Scales[i],Colors[i],Styles[i],FillColors[i]);
// 	  plots.SetAxesTitles("Jet1_Et_1l_oneTightJet","E_{T} 2^{nd} leading Jet [GeV]", "");
// 	  plots.addPlot((TH1F*)Files[i]->Get("analyzeSUSY1l_twoMediumJets/Jet1_Et"),Names[i],"Jet1_Et_1l_twoMediumJets",Scales[i],Colors[i],Styles[i],FillColors[i]);
// 	  plots.SetAxesTitles("Jet1_Et_1l_twoMediumJets","E_{T} 2^{nd} leading Jet [GeV]", "");

 // 	  plots.addPlot((TH1F*)Files[i]->Get("analyzeSUSY1b1l_1/Jet0_Et"),Names[i],"Jet0_Et_analyzeSUSY1b1l_1",Scales[i],Colors[i],Styles[i],FillColors[i]);
//  	  plots.SetAxesTitles("Jet0_Et_analyzeSUSY1b1l_1","E_{T} leading Jet [GeV]", "");
//  	  plots.addPlot((TH1F*)Files[i]->Get("analyzeSUSY1b1l_1/Jet1_Et"),Names[i],"Jet1_Et_analyzeSUSY1b1l_1",Scales[i],Colors[i],Styles[i],FillColors[i]);
//  	  plots.SetAxesTitles("Jet1_Et_analyzeSUSY1b1l_1","E_{T} 2^{nd} leading Jet [GeV]", "");

	 //  plots.addPlot((TH1F*)Files[i]->Get("analyzeBjets1l_twoMediumJets/nLooseBjetsTrackHighPur"),Names[i],"nLooseBjetsTrackHighPur_1l_twoMediumJets",Scales[i],Colors[i],Styles[i],FillColors[i]);
// 	  plots.SetAxesTitles("nLooseBjetsTrackHighPur_1l_twoMediumJets","#Jets with bdisc > 1.19 (TrackCountingHighPur)", "");
// 	  plots.addPlot((TH1F*)Files[i]->Get("analyzeBjets1l_twoMediumJets/nMediumBjetsTrackHighPur"),Names[i],"nMediumBjetsTrackHighPur_1l_twoMediumJets",Scales[i],Colors[i],Styles[i],FillColors[i]);
// 	  plots.SetAxesTitles("nMediumBjetsTrackHighPur_1l_twoMediumJets","#Jets with bdisc > 1.93 (TrackCountingHighPur)", "");
// 	  plots.addPlot((TH1F*)Files[i]->Get("analyzeBjets1l_twoMediumJets/nTightBjetsTrackHighPur"),Names[i],"nTightBjetsTrackHighPur_1l_twoMediumJets",Scales[i],Colors[i],Styles[i],FillColors[i]);
// 	  plots.SetAxesTitles("nTightBjetsTrackHighPur_1l_twoMediumJets","#Jets with bdisc > 3.41 (TrackCountingHighPur)", "");
// 	  plots.addPlot((TH1F*)Files[i]->Get("analyzeBjets1l_twoMediumJets/nLooseBjetsTrackHighEff"),Names[i],"nLooseBjetsTrackHighEff_1l_twoMediumJets",Scales[i],Colors[i],Styles[i],FillColors[i]);
// 	  plots.SetAxesTitles("nLooseBjetsTrackHighEff_1l_twoMediumJets","#Jets with bdisc > 1.7 (TrackCountingHighEff)", "");
	  // plots.addPlot((TH1F*)Files[i]->Get("analyzeBjets1l_twoMediumJets/nMediumBjetsTrackHighEff"),Names[i],"nMediumBjetsTrackHighEff_1l_twoMediumJets",Scales[i],Colors[i],Styles[i],FillColors[i]);
// 	  plots.SetAxesTitles("nMediumBjetsTrackHighEff_1l_twoMediumJets","#Jets with bdisc > 3.3 (TrackCountingHighEff)", "");
	  plots.addPlot((TH1F*)Files[i]->Get("analyzeBjets1l_twoMediumJets/nTightBjetsTrackHighEff"),Names[i],"nTightBjetsTrackHighEff_1l_twoMediumJets",Scales[i],Colors[i],Styles[i],FillColors[i]);
	  plots.SetAxesTitles("nTightBjetsTrackHighEff_1l_twoMediumJets","#Jets with bdisc > 10.21 (TrackCountingHighEff)", "");


// 	  plots.addPlot((TH1F*)Files[i]->Get("analyzeSUSY1l_twoMediumJets/HT"),Names[i],"HT_1l_twoMediumJets",Scales[i],Colors[i],Styles[i],FillColors[i]);
// 	  plots.SetAxesTitles("HT_1l_twoMediumJets","HT [GeV]", "");
// 	  plots.addPlot((TH1F*)Files[i]->Get("analyzeSUSY1l_twoMediumJets/MET"),Names[i],"MET_1l_twoMediumJets",Scales[i],Colors[i],Styles[i],FillColors[i]);
// 	  plots.SetAxesTitles("MET_1l_twoMediumJets","MET [GeV]", "");
	  // plots.addPlot((TH1F*)Files[i]->Get("analyzeSUSY1b1l_1/MET"),Names[i],"MET_analyzeSUSY1b1l_1",Scales[i],Colors[i],Styles[i],FillColors[i]);
// 	  plots.SetAxesTitles("MET_analyzeSUSY1b1l_1","MET [GeV]", "");
// plots.addPlot((TH1F*)Files[i]->Get("analyzeSUSY1b1l_1/HT"),Names[i],"HT_analyzeSUSY1b1l_1",Scales[i],Colors[i],Styles[i],FillColors[i]);
// 	  plots.SetAxesTitles("HT_analyzeSUSY1b1l_1","HT [GeV]", "");


//  	  plots.addPlot((TH1F*)Files[i]->Get("analyzeSUSY1l_1/HT"),Names[i],"HT_1l_1",Scales[i],Colors[i],Styles[i],FillColors[i]);
//  	  plots.SetAxesTitles("HT_1l_1","HT [GeV]", "");

// 	  plots.addPlot((TH1F*)Files[i]->Get("analyzeBjets1l_1/nLooseBjetsTrackHighPur"),Names[i],"nLooseBjetsTrackHighPur_1l_1",Scales[i],Colors[i],Styles[i],FillColors[i]);
// 	  plots.SetAxesTitles("nLooseBjetsTrackHighPur_1l_1","#Jets with bdisc > 1.19 (TrackCountingHighPur)", "");
// 	  plots.addPlot((TH1F*)Files[i]->Get("analyzeBjets1l_1/nMediumBjetsTrackHighPur"),Names[i],"nMediumBjetsTrackHighPur_1l_1",Scales[i],Colors[i],Styles[i],FillColors[i]);
// 	  plots.SetAxesTitles("nMediumBjetsTrackHighPur_1l_1","#Jets with bdisc > 1.93 (TrackCountingHighPur)", "");
// 	  plots.addPlot((TH1F*)Files[i]->Get("analyzeBjets1l_1/nTightBjetsTrackHighPur"),Names[i],"nTightBjetsTrackHighPur_1l_1",Scales[i],Colors[i],Styles[i],FillColors[i]);
// 	  plots.SetAxesTitles("nTightBjetsTrackHighPur_1l_1","#Jets with bdisc > 3.41 (TrackCountingHighPur)", "");
// 	  plots.addPlot((TH1F*)Files[i]->Get("analyzeBjets1l_1/nLooseBjetsTrackHighEff"),Names[i],"nLooseBjetsTrackHighEff_1l_1",Scales[i],Colors[i],Styles[i],FillColors[i]);
// 	  plots.SetAxesTitles("nLooseBjetsTrackHighEff_1l_1","#Jets with bdisc > 1.7 (TrackCountingHighEff)", "");
// 	  plots.addPlot((TH1F*)Files[i]->Get("analyzeBjets1l_1/nMediumBjetsTrackHighEff"),Names[i],"nMediumBjetsTrackHighEff_1l_1",Scales[i],Colors[i],Styles[i],FillColors[i]);
// 	  plots.SetAxesTitles("nMediumBjetsTrackHighEff_1l_1","#Jets with bdisc > 3.3 (TrackCountingHighEff)", "");
	 //  plots.addPlot((TH1F*)Files[i]->Get("analyzeBjets1l_1/nTightBjetsTrackHighEff"),Names[i],"nTightBjetsTrackHighEff_1l_1",Scales[i],Colors[i],Styles[i],FillColors[i]);
// 	  plots.SetAxesTitles("nTightBjetsTrackHighEff_1l_1","#Jets with bdisc > 10.21 (TrackCountingHighEff)", "");

// 	  plots.addPlot((TH1F*)Files[i]->Get("analyzeSUSY1l_1/MET"),Names[i],"MET_1l_1",Scales[i],Colors[i],Styles[i],FillColors[i]);
// 	  plots.SetAxesTitles("MET_1l_1","MET [GeV]", "");
// 	  plots.addPlot((TH1F*)Files[i]->Get("analyzeSUSY1l_2/MET"),Names[i],"MET_1l_2",Scales[i],Colors[i],Styles[i],FillColors[i]);
// 	  plots.SetAxesTitles("MET_1l_2","MET[GeV]", "");

// 	  plots.addPlot((TH1F*)Files[i]->Get("analyzeBjets1l_2/nLooseBjetsTrackHighPur"),Names[i],"nLooseBjetsTrackHighPur_1l_2",Scales[i],Colors[i],Styles[i],FillColors[i]);
// 	  plots.SetAxesTitles("nLooseBjetsTrackHighPur_1l_2","#Jets with bdisc > 1.19 (TrackCountingHighPur)", "");
// 	  plots.addPlot((TH1F*)Files[i]->Get("analyzeBjets1l_2/nMediumBjetsTrackHighPur"),Names[i],"nMediumBjetsTrackHighPur_1l_2",Scales[i],Colors[i],Styles[i],FillColors[i]);
// 	  plots.SetAxesTitles("nMediumBjetsTrackHighPur_1l_2","#Jets with bdisc > 1.93 (TrackCountingHighPur)", "");
// 	  plots.addPlot((TH1F*)Files[i]->Get("analyzeBjets1l_2/nTightBjetsTrackHighPur"),Names[i],"nTightBjetsTrackHighPur_1l_2",Scales[i],Colors[i],Styles[i],FillColors[i]);
// 	  plots.SetAxesTitles("nTightBjetsTrackHighPur_1l_2","#Jets with bdisc > 3.41 (TrackCountingHighPur)", "");
// 	  plots.addPlot((TH1F*)Files[i]->Get("analyzeBjets1l_2/nLooseBjetsTrackHighEff"),Names[i],"nLooseBjetsTrackHighEff_1l_2",Scales[i],Colors[i],Styles[i],FillColors[i]);
// 	  plots.SetAxesTitles("nLooseBjetsTrackHighEff_1l_2","#Jets with bdisc > 1.7 (TrackCountingHighEff)", "");
// 	  plots.addPlot((TH1F*)Files[i]->Get("analyzeBjets1l_2/nMediumBjetsTrackHighEff"),Names[i],"nMediumBjetsTrackHighEff_1l_2",Scales[i],Colors[i],Styles[i],FillColors[i]);
// 	  plots.SetAxesTitles("nMediumBjetsTrackHighEff_1l_2","#Jets with bdisc > 3.3 (TrackCountingHighEff)", "");
// 	  plots.addPlot((TH1F*)Files[i]->Get("analyzeBjets1l_2/nTightBjetsTrackHighEff"),Names[i],"nTightBjetsTrackHighEff_1l_2",Scales[i],Colors[i],Styles[i],FillColors[i]);
// 	  plots.SetAxesTitles("nTightBjetsTrackHighEff_1l_2","#Jets with bdisc > 10.21 (TrackCountingHighEff)", "");



	  // n-1 Plots
	  //------------------

// 	  plots.addPlot((TH1F*)Files[i]->Get("analyzeSUSY1l_nminus1_oneGoodMuon/nMuons"),Names[i],"nMuons_1lnminus1_oneGoodMuon",Scales[i],Colors[i],Styles[i],FillColors[i]);
// 	  plots.SetAxesTitles("nMuons_1lnminus1_oneGoodMuon","Number of isolated Muons", "");
	  
// 	  plots.addPlot((TH1F*)Files[i]->Get("analyzeSUSY1l_nminus1_fourGoodJets/nJets"),Names[i],"nJets_1lnminus1_fourGoodJets",Scales[i],Colors[i],Styles[i],FillColors[i]);
// 	  plots.SetAxesTitles("nJets_1nminus1l_fourGoodJets","Number of good Jets", "");

// 	  plots.addPlot((TH1F*)Files[i]->Get("analyzeSUSY1l_nminus1_oneTightJet/Jet0_Et"),Names[i],"Jet0_Et_1lnminus1_oneTightJet",Scales[i],Colors[i],Styles[i],FillColors[i]);
// 	  plots.SetAxesTitles("Jet0_Et_1lnminus1_oneTightJet","E_{T} leading Jet [GeV]", "");

// 	  plots.addPlot((TH1F*)Files[i]->Get("analyzeSUSY1l_nminus1_twoMediumJets/Jet1_Et"),Names[i],"Jet1_Et_1lnminus1_twoMediumJets",Scales[i],Colors[i],Styles[i],FillColors[i]);
// 	  plots.SetAxesTitles("Jet1_Et_1nminus1l_twoMediumJets","E_{T} 2^{nd} leading Jet [GeV]", "");

// 	  plots.addPlot((TH1F*)Files[i]->Get("analyzeSUSY1l_nminus1_HTSelection/HT"),Names[i],"HT_1lnminus1_HTSelection",Scales[i],Colors[i],Styles[i],FillColors[i]);
// 	  plots.SetAxesTitles("HT_1lnminus1_HTSelection","HT [GeV]", "");

// 	  plots.addPlot((TH1F*)Files[i]->Get("analyzeSUSY1l_nminus1_2/MET"),Names[i],"MET_1lnminus1_2",Scales[i],Colors[i],Styles[i],FillColors[i]);
// 	  plots.SetAxesTitles("MET_1lnminus1_2","MET [GeV]", "");

	}
    }
  plots.printAll("ylog");  
}
