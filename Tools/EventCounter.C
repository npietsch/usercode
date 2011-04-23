#include <vector>
#include <iostream>
#include <iomanip>
#include <bitset>
#include <vector>
#include <fstream>
#include <TROOT.h>
#include "TFile.h"
#include "TH1.h"

vector<TFile*> bgFiles;
vector<string> bgNames;
vector<double> bgScales;
TH1F* bgHists[20][20][20];
int bgEvents[20][20][20];
int allSM[20][20];

vector<TFile*> sgFiles;
vector<string> sgNames;
vector<double> sgScales;
TH1F* sgHists[20][20][20];
int sgEvents[20][20][20];
double significance[20][20][20];

vector<TString> selection;
vector<TString> steps;

int EventCounter()
{
  // files
  bgFiles.push_back (new TFile("Bjets_TTJets.root", "READ"));
  bgFiles.push_back (new TFile("Bjets_Wjets.root", "READ"));
  bgFiles.push_back (new TFile("Bjets_Zjets.root", "READ"));
  bgFiles.push_back (new TFile("Bjets_QCDMu.root", "READ"));
  int bf=bgFiles.size();

  //sgFiles.push_back (new TFile("Bjets_Mu.root", "READ"));
  sgFiles.push_back (new TFile("Bjets_LM1.root", "READ"));
  sgFiles.push_back (new TFile("Bjets_LM3.root", "READ"));
  sgFiles.push_back (new TFile("Bjets_LM8.root", "READ"));
  int sf=sgFiles.size();
  
  // names
  bgNames.push_back("ttbar");
  bgNames.push_back("W+Jets");
  bgNames.push_back("Z+Jets");
  bgNames.push_back("QCD Mu");

  //sgNames.push_back("Run2010 Mu");
  sgNames.push_back("LM1");
  sgNames.push_back("LM3");
  sgNames.push_back("LM8");

  // lumi in fb-1
  //double lumi=0.0359;
  double lumi=0.25;

  // cross-sections
  double xsecQCDMu=296900000*0.00037;
  double xsecZjets=3048;
  double xsecWjets=31314;
  double xsecTTJets=158;
  double xsecLM1=4.888;
  double xsecLM3=3.438;
  double xsecLM8=0.73;
  double xsecG400=8.31098;
  double xsecG500=1.87644;
  double xsecG700=0.157907;
  double xsecG800=0.0526242;

  // number of events
  double nQCD=29504866;
  double nZjets=2543727;
  double nWjets=14805546;
  double nTTJets=1156119;
  double nLM1=219190;
  double nLM3=220000;
  double nLM8=220000;
  double nG400=10000;
  double nG500=10000;
  double nG700=10000;
  double nG800=10000;

  // weights
  double sQCDMu=lumi*1000*xsecQCDMu/(nQCD);  //3.72322;
  double sZjets=lumi*1000*xsecZjets/(nZjets);  //1.19824;
  double sWjets=lumi*1000*xsecWjets/(nWjets);  //2.11502;
  double sTTJets=lumi*1000*xsecTTJets/(nTTJets);  //0.13623;
  double sLM1=lumi*1000*xsecLM1/(nLM1);  //0.02230;
  double sLM3=lumi*1000*xsecLM3/(nLM3);  //0.01563;
  double sLM8=lumi*1000*xsecLM8/(nLM8);  //0.00332;
  double sG400=lumi*1000*xsecG400/(nG400);  //0.02230;
  double sG500=lumi*1000*xsecG500/(nG500);  //0.02230;
  double sG700=lumi*1000*xsecG700/(nG700);  //0.01563;
  double sG800=lumi*1000*xsecG800/(nG800);  //0.00332;
  double sData=1;

  bgScales.push_back(sTTJets);
  bgScales.push_back(sWjets);
  bgScales.push_back(sZjets);
  bgScales.push_back(sQCDMu);

  //sgScales.push_back(sData);
  sgScales.push_back(sLM1);  
  sgScales.push_back(sLM3);
  sgScales.push_back(sLM8);

  // selection
  selection.push_back("1l");
  //selection.push_back("2l";)
  selection.push_back("1b1l");
  //selection.push_back("1b2l");
  selection.push_back("2b1l");
  //selection.push_back("2b2l");
  //selection.push_back("3b");
  selection.push_back("3b1l");
  //selection.push_back("3b2l");
  //selection.push_back("4b");
  selection.push_back("4b1l");
  //selection.push_back("4b2l");
  
  int s=selection.size();

  // number of selection steps
  steps.push_back("1");  
  //steps.push_back("ZVeto");
  //steps.push_back("MET");

  int h=steps.size();
  int lastStep=h-1;

  //---------------------------------
  // Create histograms
  //---------------------------------
  
  std::cout << "Create histograms" << std::endl;
  
  for(int i=0; i<s; ++i)
    {
      for(int j=0; j<bf; ++j)
	{
	  //bgHists[i][0][j]=(TH1F*)bgFiles[j]->Get("analyzeSUSY"+selection[i]+"_1/nLeptons");
	  bgHists[i][0][j]=(TH1F*)bgFiles[j]->Get("analyzeSUSY"+selection[i]+"_1/nLeptons");
	  //bgHists[i][1][j]=(TH1F*)bgFiles[j]->Get("analyzeSUSY"+selection[i]+"_2/nLeptons");
	  //bgHists[i][2][j]=(TH1F*)bgFiles[j]->Get("analyzeSUSY"+selection[i]+"_5/nLeptons");
	  	  	}
      for(int k=0; k<sf; ++k)
	{
	  //sgHists[i][0][k]=(TH1F*)sgFiles[k]->Get("analyzeSUSY"+selection[i]+"_1/nLeptons");
	  sgHists[i][0][k]=(TH1F*)sgFiles[k]->Get("analyzeSUSY"+selection[i]+"_1/nLeptons");
	  //sgHists[i][1][k]=(TH1F*)sgFiles[k]->Get("analyzeSUSY"+selection[i]+"_2/nLeptons");
	  //sgHists[i][2][k]=(TH1F*)sgFiles[k]->Get("analyzeSUSY"+selection[i]+"_5/nLeptons");
	}
    }

  //---------------------------------
  // Count events
  //---------------------------------

  std::cout << "Count events" << std::endl;

  int events=0;

  for(int i=0; i<s; ++i)
    {
      for(int l=0; l<h; ++l)
	{
	  for(int j=0; j<bf; ++j)
	    {
	      //std::cout << bgHists[i][l][j]->Integral(0,bgHists[i][l][j]->GetNbinsX()) << std::endl;
	      bgEvents[i][l][j]=bgScales[j] * (bgHists[i][l][j]->Integral(1,bgHists[i][l][j]->GetNbinsX()));
	    }
	  for(int k=0; k<sf; ++k)
	    {
	      //std::cout << sgHists[i][l][k]->Integral(0,sgHists[i][l][k]->GetNbinsX()) << std::endl;
	      sgEvents[i][l][k]=sgScales[k] * (sgHists[i][l][k]->Integral(1,sgHists[i][l][k]->GetNbinsX()));
	    }
	}
    }
  
  //---------------------------------
  // Calculate significance
  //---------------------------------

  for(int i=0; i<s; ++i)
    {
      for(int l=0; l<h; ++l)
	{
	  double allSMEvt=0;
 	  for(int j=0; j<bf; ++j)
 	    {
	      allSMEvt=allSMEvt+bgEvents[i][l][j];
 	    }
	  allSM[i][l]=allSMEvt;
	  for(int k=0; k<sf; ++k)
 	    {
	      double signif=(sgEvents[i][l][k])/(sqrt(allSMEvt+sgEvents[i][l][k]));
	      significance[i][l][k]=0.1*round(10*signif);
	    }
	}
    }


  //---------------------------------
  // Display cutflow
  //---------------------------------

  for(int i=0; i<s; ++i)
    {
      std::cout << " " << std::endl;
      std::cout << "==================" << std::endl;
      std::cout << " Selection: " << selection[i] << std::endl;
      std::cout << "==================" << std::endl;
      std::cout << " " << std::endl;
      
      // background table header
      std::cout << "Cut";
      for(int j=0; j<bf; ++j)
	{
	  std::cout << setw(8) << "\t" << bgNames[j];
	}
      std::cout << setw(8) << "\t"  << "all SM" << std::endl;
      std::cout << "--------------------------------";
      for(int j=0; j<bf; ++j)
	{
	  std::cout << "----------------";
	}
      std::cout << "" << std::endl;

      // background cutflow
      for(int l=0; l<h; ++l)
	{
	  double allSM=0;
	  std::cout << steps[l] << ":";
 	  for(int j=0; j<bf; ++j)
 	    {
 	      std::cout << setw(8) << "\t" << bgEvents[i][l][j];
	      allSM=allSM+bgEvents[i][l][j];
 	    }
	  std::cout << setw(8) << "\t" << allSM;

 	  std::cout << "" << std::endl;
	}
      std::cout << "" << std::endl;

      // signal table header
      std::cout << "Cut";
      for(int k=0; k<sf; ++k)
	{
	  std::cout << setw(8) << "\t" << sgNames[k];
	}
      for(int k=0; k<sf; ++k)
	{
	  std::cout << setw(8) << "\t" << "s(" << sgNames[k] << ")";
	}

      std::cout << "" << std::endl;
      std::cout << "----------------";
           for(int k=0; k<sf; ++k)
	{
	  std::cout << "--------------------------------";
	}
      std::cout << "" << std::endl;

      // signal cutflow
      for(int l=0; l<h; ++l)
	{
	  std::cout << steps[l] << ":";
 	  for(int k=0; k<sf; ++k)
 	    {
 	      std::cout << setw(8) << "\t" << sgEvents[i][l][k];
 	    }
 	  for(int k=0; k<sf; ++k)
 	    {
 	      std::cout << setw(8) << "\t" << significance[i][l][k];
 	    }
 	  std::cout << "" << std::endl;
	}
    }

  //---------------------------------
  // Display cutflow for latex
  //---------------------------------

  for(int i=0; i<s; ++i)
    {
      std::cout << " " << std::endl;
      std::cout << "==================" << std::endl;
      std::cout << " Selection: " << selection[i] << std::endl;
      std::cout << "==================" << std::endl;
      std::cout << " " << std::endl;

      //------------------
      // background table
      //------------------
     
      std::cout << "\\begin{table}[h!]" << std::endl;
      std::cout << "\\begin{changemargin}{-2cm}{-2cm}" << std::endl;
      std::cout << "\\centering" << std::endl;
      std::cout << "\\begin{tabular}{|l|";
      for(int k=0; k<bf; ++k)
	{
	  std::cout << " c";
	}
      std::cout << " c";
      std::cout << "|}" << std::endl;
      std::cout << "\\hline" << std::endl;

      // background table header
      std::cout << "Cut";
      for(int j=0; j<bf; ++j)
	{
	  std::cout <<"&" << bgNames[j];
	}
      std::cout <<"&"  << "all SM";
      std::cout << "\\" << "\\"  << std::endl;
      std::cout << "\\hline \\hline" << std::endl;

      // background cutflow
      for(int l=0; l<h; ++l)
	{
	  double allSM=0;
	  std::cout << steps[l];
 	  for(int j=0; j<bf; ++j)
 	    {
 	      std::cout <<"&" << bgEvents[i][l][j];
	      allSM=allSM+bgEvents[i][l][j];
 	    }
	  std::cout <<"&" << allSM;

 	  std::cout << "\\" << "\\" << std::endl;
	}
      std::cout << "\\hline" << std::endl;
      std::cout << "\\end{tabular}" << std::endl;
      std::cout << "\\end{changemargin}" << std::endl;
      std::cout << "\\end{table}" << std::endl;

      //------------------
      // signal table
      //------------------
      std::cout << "" << std::endl;

      std::cout << "\\begin{table}[h!]" << std::endl;
      std::cout << "\\begin{changemargin}{-2cm}{-2cm}" << std::endl;
      std::cout << "\\centering" << std::endl;
      std::cout << "\\begin{tabular}{|l|";
      for(int k=0; k<sf; ++k)
	{
	  std::cout << " c c";
	}
      std::cout << "|}" << std::endl;
      std::cout << "\\hline" << std::endl;

      // signal table header
      std::cout << "Cut";
      for(int k=0; k<sf; ++k)
	{
	  std::cout <<"&" << sgNames[k];
	}
      for(int k=0; k<sf; ++k)
	{
	  std::cout <<"&" << "s(" << sgNames[k] << ")";
	}
      std::cout << "\\" << "\\" << std::endl;
      std::cout << "\\hline \\hline" << std::endl; 

      // signal cutflow
      for(int l=0; l<h; ++l)
	{
	  std::cout << steps[l];
 	  for(int k=0; k<sf; ++k)
 	    {
 	      std::cout <<"&" << sgEvents[i][l][k];
 	    }
 	  for(int k=0; k<sf; ++k)
 	    {
 	      std::cout <<"&" << significance[i][l][k];
 	    }
 	  std::cout << "\\" << "\\" << std::endl;
	}
      std::cout << "\\hline" << std::endl;
      std::cout << "\\end{tabular}" << std::endl;
      std::cout << "\\end{changemargin}" << std::endl;
      std::cout << "\\end{table}" << std::endl;
    }

  //---------------------------------
  // Display summary 1
  //---------------------------------

  std::cout << " " << std::endl;
  std::cout << "==================" << std::endl;
  std::cout << " Summary 1: " << std::endl;
  std::cout << "==================" << std::endl;
  std::cout << " " << std::endl;
  
  // header
  std::cout << "Selection";

  for(int k=0; k<bf; ++k)
    {
      std::cout << "\t" << bgNames[k] << setw(8);
    }
  std::cout << "\t"  << "all SM";
  std::cout << "" << std::endl;
  std::cout << "--------------------------------";
  for(int j=0; j<bf; ++j)
    {
      std::cout << "----------------";
    }
  std::cout << "" << std::endl;
  
  for(int i=0; i<s; ++i)
    {
      std::cout << selection[i];
      for(int k=0; k<bf; ++k)
	{
	  std::cout << setw(8) << "\t"  << bgEvents[i][lastStep][k];
	}
      std::cout << setw(8) << "\t"  << allSM[i][lastStep];
      std::cout << " " << std::endl;
    }


  //---------------------------------
  // Display summary 2
  //---------------------------------

  std::cout << " " << std::endl;
  std::cout << "==================" << std::endl;
  std::cout << " Summary 2: " << std::endl;
  std::cout << "==================" << std::endl;
  std::cout << " " << std::endl;
  
  // header
  std::cout << "Selection" << "\t";
  for(int k=0; k<sf; ++k)
    {
      std::cout << sgNames[k] << setw(8) << "\t";
    }
  for(int k=0; k<sf; ++k)
    {
      std::cout << "S/B(" << sgNames[k] << ")" << setw(8) << "\t";
    }

  std::cout << "" << std::endl;
  std::cout << "----------------";
  for(int j=0; j<sf; ++j)
    {
      std::cout << "----------------" << "----------------";
    }
  std::cout << "" << std::endl;
  
  for(int i=0; i<s; ++i)
    {
      std::cout << selection[i];
      for(int k=0; k<sf; ++k)
	{
	  std::cout << setw(8) << "\t"  << sgEvents[i][lastStep][k];
	}

      for(int k=0; k<sf; ++k)
	{
	  
	  if(allSM[i][lastStep]>0) std::cout << setw(8) << "\t" << 0.01 * round((float)(100*(sgEvents[i][lastStep][k])/(allSM[i][lastStep])));
	  else std::cout << setw(8) << "\t" << sgEvents[i][lastStep][k];
	}

      std::cout << " " << std::endl;
    }

  //---------------------------------
  // Display summary 3
  //---------------------------------

  std::cout << " " << std::endl;
  std::cout << "==================" << std::endl;
  std::cout << " Summary 3: " << std::endl;
  std::cout << "==================" << std::endl;
  std::cout << " " << std::endl;
  
  // header
  std::cout << "Selection";
  std::cout << "\t"  << "all SM";
  for(int k=0; k<sf; ++k)
    {
      std::cout << setw(8) << "\t" << sgNames[k];
    }
  for(int k=0; k<sf; ++k)
    {
      std::cout << setw(8) << "\t" << "S/B(" << sgNames[k] << ")";
    }

  std::cout << "" << std::endl;
  std::cout << "--------------------------------";
  for(int j=0; j<sf; ++j)
    {
      std::cout << "----------------" << "----------------";
    }
  std::cout << "" << std::endl;
  
  for(int i=0; i<s; ++i)
    {
      std::cout << selection[i];
      std::cout << setw(8) << "\t"  << allSM[i][lastStep];
      for(int k=0; k<sf; ++k)
	{
	  std::cout << setw(8) << "\t"  << sgEvents[i][lastStep][k];
	}

      for(int k=0; k<sf; ++k)
	{
	  
	  if(allSM[i][lastStep]>0) std::cout << setw(8) << "\t" << 0.01 * round((float)(100*(sgEvents[i][lastStep][k])/(allSM[i][lastStep])));
	  else std::cout << setw(8) << "\t" << sgEvents[i][lastStep][k];
	}

      std::cout << " " << std::endl;
    }
  
  //---------------------------------
  // Display summary 4
  //---------------------------------

  std::cout << " " << std::endl;
  std::cout << "==================" << std::endl;
  std::cout << " Summary 4: " << std::endl;
  std::cout << "==================" << std::endl;
  std::cout << " " << std::endl;
  
  // header
  std::cout << "Selection";
  if(sf>0) std::cout << "\t" << "S/B(" << sgNames[0] << ")" << setw(8) << "\t" << "s(" << sgNames[0] << ")";
  for(int k=1; k<sf; ++k)
    {
      std::cout << setw(8) << "\t" << "S/B(" << sgNames[k] << ")" << setw(8) << "\t" << "s(" << sgNames[k] << ")";
    }
  std::cout << "" << std::endl;
  std::cout << "------------------------------------------------";
  for(int k=1; k<sf; ++k)
    {
      std::cout << "--------------------------------";
    }
  std::cout << "" << std::endl;
  
  for(int i=0; i<s; ++i)
    {
      std::cout << selection[i];
      for(int k=0; k<sf; ++k)
	{
	  if(allSM[i][lastStep]>0) std::cout << setw(8) << "\t" << 0.01 * round((float)(100*(sgEvents[i][lastStep][k])/(allSM[i][lastStep]))) << setw(8) << "\t" <<  significance[i][lastStep][k];
	  else std::cout << setw(8) << "\t" << sgEvents[i][lastStep][k] << setw(8) << "\t"  << significance[i][lastStep][k];
	}
      std::cout << " " << std::endl;
    }

  //---------------------------------
  // Display summary 1 for latex
  //---------------------------------

  std::cout << " " << std::endl;
  std::cout << "%==================" << std::endl;
  std::cout << "% Summary 1: " << std::endl;
  std::cout << "%==================" << std::endl;
  std::cout << " " << std::endl;
  
  std::cout << "\\begin{frame}" << std::endl;
  std::cout << "\\begin{table}[h!]" << std::endl;
  std::cout << "\\begin{changemargin}{-2cm}{-2cm}" << std::endl;
  std::cout << "\\centering" << std::endl;
  std::cout << "\\begin{tabular}{|l|";
  for(int k=0; k<bf; ++k)
    {
      std::cout << " c";
    }

  std::cout << " c";
  std::cout << "|}" << std::endl;
  std::cout << "\\hline" << std::endl;

  // header
  std::cout << "Sel.";
  for(int k=0; k<bf; ++k)
    {
      std::cout <<"&" << bgNames[k];
    }

  std::cout << "&"  << "all SM";

  std::cout << "\\" << "\\";
  std::cout << "" << std::endl;

  std::cout << "\\hline \\hline" << std::endl;
  
  for(int i=0; i<s; ++i)
    {
      std::cout << selection[i];
      for(int k=0; k<bf; ++k)
	{
	  std::cout <<"&"  << bgEvents[i][lastStep][k];
	}

      std::cout <<"&"  << allSM[i][lastStep];
      std::cout << "\\" << "\\";
      std::cout << " " << std::endl;
    }
  std::cout << "\\hline" << std::endl;
  std::cout << "\\end{tabular}" << std::endl;
  std::cout << "\\end{changemargin}" << std::endl;
  std::cout << "\\end{table}" << std::endl;
  std::cout << "\\end{frame}" << std::endl;

  //---------------------------------
  // Display summary 2 for latex
  //---------------------------------

  std::cout << " " << std::endl;
  std::cout << "%==================" << std::endl;
  std::cout << "% Summary 2: " << std::endl;
  std::cout << "%==================" << std::endl;
  std::cout << " " << std::endl;
  
  std::cout << "\\begin{frame}" << std::endl;
  std::cout << "\\begin{table}[h!]" << std::endl;
  std::cout << "\\begin{changemargin}{-2cm}{-2cm}" << std::endl;
  std::cout << "\\centering" << std::endl;
  std::cout << "\\begin{tabular}{|l|";
  for(int k=0; k<sf; ++k)
    {
      std::cout << " c";
    }
  for(int k=0; k<sf; ++k)
    {
      std::cout << " c";
    }
  std::cout << "|}" << std::endl;
  std::cout << "\\hline" << std::endl;

  // header
  std::cout << "Sel.";
  for(int k=0; k<sf; ++k)
    {
      std::cout <<"&" << sgNames[k];
    }
  for(int k=0; k<sf; ++k)
    {
      std::cout << "&" << "S/B(" << sgNames[k] << ")";
    }

  std::cout << "\\" << "\\";
  std::cout << "" << std::endl;

  std::cout << "\\hline \\hline" << std::endl;
  
  for(int i=0; i<s; ++i)
    {
      std::cout << selection[i];
      for(int k=0; k<sf; ++k)
	{
	  
	  std::cout << "&" << sgEvents[i][lastStep][k];
	}

      for(int k=0; k<sf; ++k)
	{

	  if(allSM[i][lastStep]>0) std::cout <<"&" << 0.01 * round((float)(100*(sgEvents[i][lastStep][k])/(allSM[i][lastStep])));
	  else std::cout <<"&" << sgEvents[i][lastStep][k];
	}
      std::cout << "\\" << "\\";
      std::cout << " " << std::endl;
    }
  std::cout << "\\hline" << std::endl;
  std::cout << "\\end{tabular}" << std::endl;
  std::cout << "\\end{changemargin}" << std::endl;
  std::cout << "\\end{table}" << std::endl;
  std::cout << "\\end{frame}" << std::endl;

  //---------------------------------
  // Display summary 3 for latex
  //---------------------------------

  std::cout << " " << std::endl;
  std::cout << "%==================" << std::endl;
  std::cout << "% Summary 3: " << std::endl;
  std::cout << "%==================" << std::endl;
  std::cout << " " << std::endl;
  
  std::cout << "\\begin{frame}" << std::endl;
  std::cout << "\\begin{table}[h!]" << std::endl;
  std::cout << "\\begin{changemargin}{-2cm}{-2cm}" << std::endl;
  std::cout << "\\centering" << std::endl;
  std::cout << "\\begin{tabular}{|l|";
  for(int k=0; k<sf; ++k)
    {
      std::cout << " c";
    }
  for(int k=0; k<sf; ++k)
    {
      std::cout << " c";
    }

  std::cout << " c";
  std::cout << "|}" << std::endl;
  std::cout << "\\hline" << std::endl;

  // header
  std::cout << "Sel.";
  std::cout << "&"  << "all SM";
  for(int k=0; k<sf; ++k)
    {
      std::cout <<"&" << sgNames[k];
    }
  for(int k=0; k<sf; ++k)
    {
      std::cout << "&" << "S/B(" << sgNames[k] << ")";
    }

  std::cout << "\\" << "\\";
  std::cout << "" << std::endl;

  std::cout << "\\hline \\hline" << std::endl;
  
  for(int i=0; i<s; ++i)
    {
      std::cout << selection[i];
      std::cout <<"&"  << allSM[i][lastStep];
      for(int k=0; k<sf; ++k)
	{
	  std::cout <<"&"  << sgEvents[i][lastStep][k];
	}
      for(int k=0; k<sf; ++k)
	{

	  if(allSM[i][lastStep]>0) std::cout <<"&" << 0.01 * round((float)(100*(sgEvents[i][lastStep][k])/(allSM[i][lastStep])));
	  else std::cout <<"&" << sgEvents[i][lastStep][k];

	}

      std::cout << "\\" << "\\";
      std::cout << " " << std::endl;
    }
  std::cout << "\\hline" << std::endl;
  std::cout << "\\end{tabular}" << std::endl;
  std::cout << "\\end{changemargin}" << std::endl;
  std::cout << "\\end{table}" << std::endl;
  std::cout << "\\end{frame}" << std::endl;

  //---------------------------------
  // Display summary 4 for latex
  //---------------------------------

  std::cout << " " << std::endl;
  std::cout << "%==================" << std::endl;
  std::cout << "% Summary 4: " << std::endl;
  std::cout << "%==================" << std::endl;
  std::cout << " " << std::endl;
  
  std::cout << "\\begin{frame}" << std::endl;
  std::cout << "\\begin{table}[h!]" << std::endl;
  std::cout << "\\begin{changemargin}{-2cm}{-2cm}" << std::endl;
  std::cout << "\\centering" << std::endl;  std::cout << "\\begin{tabular}{|l|";
  for(int k=0; k<sf; ++k)
    {
      std::cout << " c c";
    }
  std::cout << "|}" << std::endl;
  std::cout << "\\hline" << std::endl;

  // header
  std::cout << "Sel.";
  if(sf>0) std::cout << "&" << "S/B(" << sgNames[0] << ")" <<"&" << "s(" << sgNames[0] << ")";
  for(int k=1; k<sf; ++k)
    {
      std::cout <<"&" << "S/B(" << sgNames[k] << ")" <<"&" << "s(" << sgNames[k] << ")";
    }
  std::cout << "\\" << "\\";

  std::cout << "" << std::endl;

  std::cout << "\\hline \\hline" << std::endl;
  
  for(int i=0; i<s; ++i)
    {
      std::cout << selection[i];
      for(int k=0; k<sf; ++k)
	{
	  if(allSM[i][lastStep]>0) std::cout <<"&" << 0.01 * round((float)(100*(sgEvents[i][lastStep][k])/(allSM[i][lastStep]))) <<"&" <<  significance[i][lastStep][k];
	  else std::cout <<"&" << sgEvents[i][lastStep][k] <<"&"  << significance[i][lastStep][k];
	}
      std::cout << "\\" << "\\";
      std::cout << " " << std::endl;
    }
  std::cout << "\\hline" << std::endl;
  std::cout << "\\end{tabular}" << std::endl;
  std::cout << "\\end{changemargin}" << std::endl;
  std::cout << "\\end{table}" << std::endl;
  std::cout << "\\end{frame}" << std::endl;
  std::cout << " " << std::endl;
  std::cout << " " << std::endl;

  return 0;
}
