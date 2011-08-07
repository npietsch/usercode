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

vector<TFile*> BackgroundFiles;
vector<TFile*> SignalFiles;
vector<TFile*> DataFiles;

vector<string> BackgroundNames;
vector<string> SignalNames;
vector<string> DataNames;

vector<double> BackgroundWeights;
vector<double> SignalWeights;
vector<double> DataWeights;

vector<TString> Selections;

int ABCD_Tables()
{
  //--------------------------------------------------------------------------------------------------------
  // Define ABCD regions
  //
  // NOTE: Numbers of events in region A will calculated by hist->Intagral(xmin, xmid-1,         ymin, ymin-1)
  //       numbers of events in region B will calculated by hist->Intagral(xmid, x overflow-bin, ymin, ymin-1)
  //       numbers of events in region C will calculated by hist->Intagral(xmin, xmid-1,         ymid, y overflow-bin)
  //       numbers of events in region D will calculated by hist->Intagral(xmid, x overflow-bin, ymid, y overflow-bin)
  //
  //--------------------------------------------------------------------------------------------------------

  // Set xmin and xmid
  double xmin=3;
  double xmid=10;

  double ymin=6;
  double ymid=12;

  std::cout << "Read background files" << std::endl;

  /// push back files to vector vector<TFile*> BackgroundFiles
  BackgroundFiles.push_back (new TFile("TTJets.root","READ"));
  BackgroundFiles.push_back (new TFile("WJets.root","READ"));
  BackgroundFiles.push_back (new TFile("ZJets.root","READ"));
  BackgroundFiles.push_back (new TFile("SingleTop.root","READ"));
  BackgroundFiles.push_back (new TFile("QCD.root", "READ"));

  std::cout << "Read signal files" << std::endl;

  /// push back files to vector vector<TFile*> SignalFiles
  SignalFiles.push_back (new TFile("LM3.root","READ"));
  SignalFiles.push_back (new TFile("LM8.root","READ"));
  SignalFiles.push_back (new TFile("LM9.root","READ"));
  SignalFiles.push_back (new TFile("LM13.root","READ"));

  std::cout << "Read data files" << std::endl;

  /// push back files to vector vector<TFile*> DataFiles
  DataFiles.push_back (new TFile("MuHad.root","READ"));
  DataFiles.push_back (new TFile("ElectronHad.root","READ"));

  /// push back names to vector<string> BackgroundNames
  BackgroundNames.push_back("Ttbar");
  BackgroundNames.push_back("W+Jets");
  BackgroundNames.push_back("Z+Jets");
  BackgroundNames.push_back("Single top");
  BackgroundNames.push_back("QCD");

  /// push back names to vector<string> SignalNames
  SignalNames.push_back("LM3");
  SignalNames.push_back("LM8");
  SignalNames.push_back("LM9");
  SignalNames.push_back("LM13");

  /// push back names to vector<string> DataNames
  DataNames.push_back("MuHad");
  DataNames.push_back("ElHad");

  /// luminosity
  Int_t Luminosity=702;

  /// event weights
  Int_t NGQCD=1;
  Double_t XSQCD=1;
	
  Int_t NGTTJets=3091251;
  Double_t XSTTJets=158;

  Int_t NGZJets=34608520;
  Double_t XSZJets=3048;
  
  Int_t NGWJets=54362661;
  Double_t XSWJets=31314; 
  
  Int_t NGSingleTop=1; 
  Double_t XSSingleTop=1;
  
  Int_t NGLM3=36475;
  Double_t XSLM3=3.438;
  
  Int_t NGLM8=10595;
  Double_t XSLM8=0.73;
  
  Int_t NGLM9=79665;
  Double_t XSLM9=7.134;

  Int_t NGLM13=77000;
  Double_t XSLM13=6.899;
  
  Double_t WeightQCD=0.001*(Luminosity*(XSQCD))/NGQCD;
  Double_t WeightTTJets=(Luminosity*(XSTTJets))/NGTTJets;
  Double_t WeightZJets=(Luminosity*(XSZJets))/NGZJets;
  Double_t WeightWJets=(Luminosity*(XSWJets))/NGWJets;
  Double_t WeightSingleTop=0.001*Luminosity*XSSingleTop/NGSingleTop;
  Double_t WeightLM3=(Luminosity*(XSLM3))/NGLM3;
  Double_t WeightLM8=(Luminosity*(XSLM8))/NGLM8;
  Double_t WeightLM9=(Luminosity*(XSLM9))/NGLM9;
  Double_t WeightLM13=(Luminosity*(XSLM13))/NGLM13;


  /// push back event weights to vector<double> BackgroundWeights;
  BackgroundWeights.push_back(WeightTTJets);
  BackgroundWeights.push_back(WeightWJets);
  BackgroundWeights.push_back(WeightZJets);
  BackgroundWeights.push_back(WeightSingleTop);
  BackgroundWeights.push_back(WeightQCD);

  /// push back event weights to vector<double> SignalWeights;
  SignalWeights.push_back(WeightLM3);
  SignalWeights.push_back(WeightLM8);
  SignalWeights.push_back(WeightLM9);
  SignalWeights.push_back(WeightLM13);

  /// push back event weights to vector<double> DataWeights;
  DataWeights.push_back(1);
  DataWeights.push_back(1);

  /// push back event selections vector<TString> Selections;
  Selections.push_back("analyzeSUSY1m_metSelection");
  Selections.push_back("analyzeSUSY1b1m_6");
  Selections.push_back("analyzeSUSY2b1m_6");
  Selections.push_back("analyzeSUSY3b1m_6");
  Selections.push_back("analyzeSUSY1e_metSelection");
  Selections.push_back("analyzeSUSY1b1e_6");
  Selections.push_back("analyzeSUSY2b1e_6");
  Selections.push_back("analyzeSUSY3b1e_6");

  // size of vector<TString> Selections divided by 2
  int Selhalf=0.5*Selections.size();

  std::cout << "Start to loop over event selections" << std::endl << std::endl;

  for(int sdx=0; sdx < Selections.size(); sdx++)
    {
      std::cout << "=================================" << std::endl;
      std::cout << Selections[sdx] << std::endl;
      std::cout << "=================================" << std::endl << std::endl;

      // name of output tex file
      char dateiname[100];
      if(sdx < (Selections.size())/2) sprintf(dateiname,"ABCD_%ib1m.tex",sdx);
      else sprintf(dateiname,"ABCD_%ib1e.tex",sdx-Selhalf);

      // open output file
      std::cout << "--- Open " << dateiname << " ---"<< std::endl << std::endl;
      fstream g;
      g.open(dateiname, ios::out);
      g << "\\begin{tabular}{|l|c|c|c|c|c|}" << endl;
      g << "\\hline" << endl;
      g << "Sample & A & B & C & D & $\\textmd{D}_\\textmd{exp}$ \\\\" << endl;
      g << "\\hline" << endl;
      g << "\\hline" << endl;

      /// histogram for ABCD method     
      int ddx;
      if(sdx < Selhalf) ddx=0;
      else ddx=1;
      TH2F* ABCD_=(TH2F*)DataFiles[ddx]->Get(Selections[sdx]+"/HT_SigMET");

      /// ABCD regions
      double XMax=ABCD_->GetNbinsX()+1;
      double YMax=ABCD_->GetNbinsY()+1;
      
      std::cout << "------------------------------------------------" << std::endl;
      std::cout << "Loop over " << BackgroundNames.size() << " background samples" << std::endl;
      std::cout << "------------------------------------------------" << std::endl;

      //--------------
      // Background
      //--------------

      double nA_SM=0;
      double nB_SM=0;
      double nC_SM=0;
      double nD_SM=0;

      for(int bdx=0; bdx < BackgroundNames.size(); bdx++)
	{
	  std::cout << "Calculate number of selected " << BackgroundNames[bdx] << " events" << std::endl;

	  /// histogram for ABCD method
	  TH2F* hist=(TH2F*)BackgroundFiles[bdx]->Get(Selections[sdx]+"/HT_SigMET");

	  double nA_background=BackgroundWeights[bdx]*(hist->Integral(xmin,xmid-1,ymin,ymid));
	  double nB_background=BackgroundWeights[bdx]*(hist->Integral(xmid,XMax,ymin,ymid));
	  double nC_background=BackgroundWeights[bdx]*(hist->Integral(xmin,xmid-1,ymid,YMax));
	  double nD_background=BackgroundWeights[bdx]*(hist->Integral(xmid,XMax,ymid,YMax));
	 
	  double nA_background_sigma=sqrt(nA_background);
	  double nB_background_sigma=sqrt(nB_background);
	  double nC_background_sigma=sqrt(nC_background);
	  double nD_background_sigma=sqrt(nD_background);
	  
	  double nD_background_exp=(nB_background/nA_background)*nC_background;
	  double nD_background_exp_sigma=sqrt(pow((nB_background/nA_background)*nC_background_sigma,2)+pow((nB_background_sigma/nA_background)*nC_background,2)+pow((nB_background/(nA_background*nA_background))*nC_background*nA_background_sigma,2));

	  std::cout << "nA_background: " << nA_background << std::endl;
	  std::cout << "nD_background: " << nD_background << std::endl;
	  std::cout << "nD_background_exp: " << nD_background_exp << std::endl;
	  std::cout << "nD_background_exp_sigma: " << nD_background_exp_sigma << std::endl;

	  g << BackgroundNames[bdx] << "&";
	  g << nA_background << " $\\pm$" << nA_background_sigma << "&";
	  g << nB_background << " $\\pm$" << nB_background_sigma << "&";
	  g << nC_background << " $\\pm$" << nC_background_sigma << "&";
	  g << nD_background << " $\\pm$" << nD_background_sigma << "&";
	  g << nD_background_exp << " $\\pm$" << nD_background_exp_sigma << "\\\\" << std::endl;

	  nA_SM=nA_SM+nA_background;
	  nB_SM=nB_SM+nB_background;
	  nC_SM=nC_SM+nC_background;
	  nD_SM=nD_SM+nD_background;
	}

      g << "\\hline" << endl;

      std::cout << "------------------------------------------------" << std::endl;
      std::cout << "Loop over " << SignalNames.size() << " signal samples" << std::endl;
      std::cout << "------------------------------------------------" << std::endl;

      //--------------
      // Signal
      //--------------

      for(int bdx=0; bdx < SignalNames.size(); bdx++)
	{
	  std::cout << "Calculate number of selected " << SignalNames[bdx] << " events" << std::endl;

	  /// histogram for ABCD method
	  TH2F* hist=(TH2F*)SignalFiles[bdx]->Get(Selections[sdx]+"/HT_SigMET");

	  double nA_signal=SignalWeights[bdx]*(hist->Integral(xmin,xmid-1,ymin,ymid-1));
	  double nB_signal=SignalWeights[bdx]*(hist->Integral(xmid,XMax,ymin,ymid-1));
	  double nC_signal=SignalWeights[bdx]*(hist->Integral(xmin,xmid-1,ymid,YMax));
	  double nD_signal=SignalWeights[bdx]*(hist->Integral(xmid,XMax,ymid,YMax));
	 
	  double nA_signal_sigma=sqrt(nA_signal);
	  double nB_signal_sigma=sqrt(nB_signal);
	  double nC_signal_sigma=sqrt(nC_signal);
	  double nD_signal_sigma=sqrt(nD_signal);

	  double nD_signal_exp=(nB_signal/nA_signal)*nC_signal;
	  double nD_signal_exp_sigma=sqrt(pow((nB_signal/nA_signal)*nC_signal_sigma,2)+pow((nB_signal_sigma/nA_signal)*nC_signal,2)+pow((nB_signal/(nA_signal*nA_signal))*nC_signal*nA_signal_sigma,2));

	  std::cout << "SignalWeights[bdx]: " << SignalWeights[bdx] << std::endl;
	  std::cout << "A: hist->Integral(xmin,xmid-1,ymin,ymid-1): " << hist->Integral(xmin,xmid-1,ymin,ymid-1) << std::endl;
	  std::cout << "B: hist->Integral(xmid,XMax,ymin,ymid-1): " << hist->Integral(xmid,XMax,ymin,ymid-1) << std::endl;
	  std::cout << "C: hist->Integral(xmin,xmid-1,ymid,YMax): " << hist->Integral(xmin,xmid-1,ymid,YMax) << std::endl;
	  std::cout << "D: hist->Integral(xmid,XMax,ymid,YMax): " << hist->Integral(xmid,XMax,ymid,YMax) << std::endl;

	  std::cout << "nA_signal: " << nA_signal << std::endl;
	  std::cout << "nD_signal: " << nD_signal << std::endl;
	  std::cout << "nD_signal_exp: " << nD_signal_exp << std::endl;
	  std::cout << "nD_signal_exp_sigma: " << nD_signal_exp_sigma << std::endl;

	  g << SignalNames[bdx] << "&";
	  g << nA_signal << " $\\pm$" << nA_signal_sigma << "&";
	  g << nB_signal << " $\\pm$" << nB_signal_sigma << "&";
	  g << nC_signal << " $\\pm$" << nC_signal_sigma << "&";
	  g << nD_signal << " $\\pm$" << nD_signal_sigma << "&";
	  g << nD_signal_exp << " $\\pm$" << nD_signal_exp_sigma << "\\\\" << std::endl;
	}
      g << "\\hline" << endl;
      
      //--------------
      // All SM
      //--------------

      double nA_SM_sigma=sqrt(nA_SM);
      double nB_SM_sigma=sqrt(nB_SM);
      double nC_SM_sigma=sqrt(nC_SM);
      double nD_SM_sigma=sqrt(nD_SM);

      double nD_SM_exp=(nB_SM/nA_SM)*nC_SM;
      double nD_SM_exp_sigma=sqrt(pow((nB_SM/nA_SM)*nC_SM_sigma,2)+pow((nB_SM_sigma/nA_SM)*nC_SM,2)+pow((nB_SM/(nA_SM*nA_SM))*nC_SM*nA_SM_sigma,2));

      g << "Total SM MC" << "&";
      g << nA_SM << " $\\pm$" << nA_SM_sigma << "&";
      g << nB_SM << " $\\pm$" << nB_SM_sigma << "&";
      g << nC_SM << " $\\pm$" << nC_SM_sigma << "&";
      g << nD_SM << " $\\pm$" << nD_SM_sigma << "&";
      g << nD_SM_exp << " $\\pm$" << nD_SM_exp_sigma << "\\\\" << std::endl;

      std::cout << "------------------------------------------------" << std::endl;
      std::cout << DataNames[ddx] << " data stream" << std::endl;
      std::cout << "------------------------------------------------" << std::endl;

      //--------------
      // Data
      //--------------
      
      std::cout << "Calculate number of selected " << DataNames[ddx] << " events" << std::endl;
      
      double nA_data=DataWeights[ddx]*(ABCD_->Integral(xmin,xmid-1,ymin,ymid-1));
      double nB_data=DataWeights[ddx]*(ABCD_->Integral(xmid,XMax,ymin,ymid-1));
      double nC_data=DataWeights[ddx]*(ABCD_->Integral(xmin,xmid-1,ymid,YMax));
      double nD_data=DataWeights[ddx]*(ABCD_->Integral(xmid,XMax,ymid,YMax));
      
      double nA_data_sigma=sqrt(nA_data);
      double nB_data_sigma=sqrt(nB_data);
      double nC_data_sigma=sqrt(nC_data);
      double nD_data_sigma=sqrt(nD_data);
      
      double nD_data_exp=(nB_data/nA_data)*nC_data;
      double nD_data_exp_sigma=sqrt(pow((nB_data/nA_data)*nC_data_sigma,2)+pow((nB_data_sigma/nA_data)*nC_data,2)+pow((nB_data/(nA_data*nA_data))*nC_data*nA_data_sigma,2));

      std::cout << "nA_data: " << nA_data << std::endl;
      std::cout << "nD_data: " << nD_data << std::endl;
      std::cout << "nD_data_exp: " << nD_data_exp << std::endl;
      std::cout << "nD_data_exp_sigma: " << nD_data_exp_sigma << std::endl;
      
      g << DataNames[ddx] << "&";
      g << nA_data << " $\\pm$" << nA_data_sigma << "&";
      g << nB_data << " $\\pm$" << nB_data_sigma << "&";
      g << nC_data << " $\\pm$" << nC_data_sigma << "&";
      g << nD_data << " $\\pm$" << nD_data_sigma << "&";
      g << nD_data_exp << " $\\pm$" << nD_data_exp_sigma << "\\\\" << std::endl;
      
      
      g << "\\hline" << endl;
      g << "\\end{tabular}" << endl;
      
      std::cout << "" << std::endl;
      std::cout << "--- Close " << dateiname << " ---" << std::endl << std::endl;
      g.close();
    }

  std::cout << "" << std::endl;
  std::cout << "" << std::endl;
  std::cout << "Note: Statistical errors for MC are wrong as the refer to the number of weighted, but not to the number of unweighted events. This still has to corrected." << std::endl;

}
