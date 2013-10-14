#ifndef _StackWithRatio_h
#define _StackWithRatio_h

#include "TStyle.h"
#include "TH1D.h"
#include "THStack.h"
#include "TPad.h"
#include "TObjArray.h"

#define MAXBIN 1000

class StackWithRatio{
 public:
  
  int rebOff; // rebinning offset
  int rebN;   // # bins to rebin
  
  double lumi;
  double SF;  // additional MC scale factor
  
  bool band;     // draw errow band with stat(+)sys
  double relsys; // relative sys error
  
  double stackYmin;
  double stackYmax;
  double ratioYmin;
  double ratioYmax;
  double xmin;
  double xmax;
  
  TString xTitle;
  TString yStackTitle;
  TString yRatioTitle;
  TPad* pad1;
  TPad* pad2;
  
  TObjArray extra;
  
  StackWithRatio(double dataLumi=1,const char* xt="", const char* yst="Number of Events", const char* yrt="Data/MC"):
    rebN(0),rebOff(0),lumi(dataLumi),sumMC(0),theData(0),band(false),relsys(0)
    stackYmin(0),stackYmax(0),ratioYmin(0),ratioYmax(0),xmin(0),xmax(0),SF(1),
    xTitle(xt), yStackTitle(yst), yRatioTitle(yrt){
    theStack = new THStack("hs","");
  };
    
    ~StackWithRatio(){
      if(sumMC!=0) sumMC->Delete();
      if(theData!=0) theData->Delete();
    }
    
    // add MC histo to stack
    void Add(TH1D*& h, Color_t color, int nevts=1, double xsec=1){
      h->SetLineColor(1);
      h->SetFillColor(color);
      if(rebN>1) Rebin(h);
      double weight = SF*lumi*xsec/nevts;
      h->Scale(weight);
      if(!sumMC) sumMC = (TH1D*) h->Clone();
      else sumMC->Add(h);
      theStack->Add(h);
    }
    
    // add data histo
    void AddData(TH1D*& h){
      if(rebN>1) Rebin(h);
      h->SetMarkerStyle(20);
      h->SetLineWidth(1);
      h->SetMarkerSize(1);
      h->SetXTitle(xTitle);
      theData = (TH1D*)h->Clone();
    };
    
    // add extra histo
    void AddExtra(TH1D*& h, Color_t color=1, int nevts=1, double xsec=1, Style_t style=2, double width=2){
      if(rebN>1) Rebin(h);
      double weight = SF*lumi*xsec/nevts;
      h->Scale(weight);
      h->SetLineColor(color);
      h->SetLineStyle(style);
      h->SetLineWidth(width);
      extra.Add(h);
    };
    
    void SetStackYRange(double min,double max){
      stackYmin=min;
      stackYmax=max;
    }
    
    void SetRatioYRange(double min,double max){
      ratioYmin=min;
      ratioYmax=max;
    }
    
    void SetXRange(double min,double max){
      xmin=min;
      xmax=max;
    }
    
    void Rebin(TH1D*&h){
      //std::cout << "Test1" << std::endl;

      int nb = h->GetNbinsX();
      double width = h->GetBinWidth(1);
      TAxis* ax = h->GetXaxis();
      double xmin = ax->GetXmin();
      double xmax = ax->GetXmax();
      
      //std::cout << "Test2" << std::endl;

      const int n  = nb-rebOff+1;
      double bins[n];
      bins[0] = xmin;
      bins[1] = ax->GetBinLowEdge(rebOff+1);
      
      //std::cout << "Test3" << std::endl;

      int k=0;
      for(int i=2;i<n;i++){
	bins[i]=bins[i-1]+rebN*width;
	if(bins[i]>=xmax){
	  bins[i]=xmax;
	  k=i;
	  break;
	}
      }
      //for(int i=0;i<k;i++) cout<<bins[i]<<endl;
      TString name = h->GetName();
      TH1D* newH = h->Rebin(k-1,name+"_reb",bins);
      // delete h;
      h->Delete();// better for interpreter
      h=newH;

      //std::cout << "Test4" << std::endl;
    }
    
    void DrawClone(){

      //std::cout << "Test5" << std::endl;

      //cout<<xmin<<"|"<<xmax<<endl;
      if(sumMC==0){
	cout<<"No histograms added!"<<endl;
	exit(0);
      }
      
      if(theData==0){
	cout<<"Data not yet defined!"<<endl;
	exit(0);
      }

      //std::cout << "Test6" << std::endl;

      if(gPad==0||!gPad->IsEditable()) gROOT->MakeDefCanvas();
      // upper pad - stack
      pad1 = new TPad("pad1","pad1",0,0.3,1,0.98);
      pad1->SetTickx(1);
      pad1->SetTicky(1);
      //pad1->SetLogy();
      pad1->SetBottomMargin(0);
      pad1->SetLeftMargin(0.12);
      // lower pad - ratio
      pad2 = new TPad("pad2","pad2",0,0,1,0.31);
      pad2->SetTickx(1);
      pad2->SetTicky(1);
      pad2->SetLogy(kFALSE);
      pad2->SetBottomMargin(0.35);
      pad2->SetTopMargin(0);
      pad2->SetLeftMargin(0.12);
      pad1->Draw();
      pad2->Draw();
      // stack
      pad1->cd();

      if(xmax!=xmin){
	theData->GetXaxis()->SetRangeUser(xmin, xmax);
      }

      else {
	xmin=theData->GetXaxis()->GetXmin();
	xmax=theData->GetXaxis()->GetXmax();
      }
      
      //std::cout << "Test7" << std::endl;

      TH1D* frame = theData->Clone();
      frame->Reset();
      frame->SetStats(0);
      frame->SetTitle("");
      frame->SetTitleOffset(1.1, "x");
      frame->SetTitleOffset(1.0, "y");
      frame->SetYTitle(yStackTitle);
      frame->GetXaxis()->SetRangeUser(xmin, xmax);
      frame->GetYaxis()->SetTitleSize(0.065);
      frame->GetYaxis()->SetTitleFont(62);
      //frame->GetYaxis()->SetLabelFont(42);
      //frame->GetXaxis()->SetLabelFont(42);
      
      if(stackYmin!=stackYmax){
	frame->GetYaxis()->SetRangeUser(stackYmin, stackYmax);
      }
      
      frame->Draw();
      theStack->DrawClone("histsame");
      //sumMC->DrawClone("same");
      // extra lines
      for(int i=0;i<extra.GetEntries();i++) extra[i]->DrawClone("samehist");
      theData->DrawClone("same");
      theData->DrawClone("sameaxis");

      //std::cout << "Test8" << std::endl;

      // ratio
      pad2->cd();
      //theData->SetNdivisions(11, "X");
      theData->SetTitleOffset(1.1, "x");
      theData->SetTitleOffset(0.6, "y");
      theData->SetYTitle(yRatioTitle);
      theData->GetXaxis()->SetTitleSize(0.14);
      theData->GetYaxis()->SetTitleSize(0.1);
      theData->GetYaxis()->SetLabelFont(62);
      theData->GetXaxis()->SetLabelFont(62);
      theData->GetYaxis()->SetLabelSize(0.1);
      theData->GetXaxis()->SetLabelSize(0.1 );
      
      if(ratioYmin!=ratioYmax){
	theData->GetYaxis()->SetRangeUser(ratioYmin, ratioYmax);
      }
      // mean ratio 
      double imc  =sumMC->Integral();
      double idata=theData->Integral();
      cout<<"Average ratio : "<<idata/imc<<endl;;
      theData->Divide(sumMC);
      theData->SetStats(0);
      theData->SetTitle("");
      theData->DrawClone("ep");
      
      //std::cout << "Test9" << std::endl;

      if(band) {
	DrawBand(theData,relsys);
	theData->DrawClone("sameep");
      }
      
      //dk: strange be carful
      cout<<xmin<<" "<<xmax<<endl;
      cout<<frame->GetXaxis()->GetXmin()<<" "<<frame->GetXaxis()->GetXmax()<<endl;
      TLine line(xmin, 1, xmax+1, 1);
      line.SetLineWidth(1);
      line.SetLineStyle(1);
      line.SetLineColor(1);
      line.DrawClone();

      //std::cout << "Test10" << std::endl;
    };
    
    void DrawBand(TH1D*h,double sys){
      double r2 = sys*sys;
      const int n=h->fN;
      double  x[MAXBIN];
      double  y[MAXBIN];
      double ey[MAXBIN];
      int k=0;
      for(int i=0;i<n;i++){
	y[k]=h->GetBinContent(i);
	if(y[k]!=0){
	  double e=h->GetBinError(i)/y[k];
	  ey[k]=sqrt(e*e+r2)*y[k];
	  x[k]=h->GetBinCenter(i);
	  k++;
	}
      }
      TGraphErrors g(k, x, y, 0, ey);
      g.SetFillColor(kYellow-10);
      g.DrawClone("samee3");
    }
    
 private:
    THStack* theStack;
    TH1D*       sumMC;
    TH1D*     theData;
};

#endif
