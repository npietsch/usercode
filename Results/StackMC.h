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
      h->SetLineColor(0);
      h->SetMarkerColor(0);
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
    }
    
    void DrawClone(){
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
      frame->SetTitleOffset(1.0, "x");
      frame->SetTitleOffset(1.0, "y");
      frame->SetYTitle(yStackTitle);
      frame->GetXaxis()->SetRangeUser(xmin, xmax);
      //dk
      frame->GetXaxis()->SetTitleSize(0.05);
      frame->GetYaxis()->SetTitleSize(0.05);
      
      if(stackYmin!=stackYmax){
	frame->GetYaxis()->SetRangeUser(stackYmin, stackYmax);
      }
      
      frame->Draw();
      theStack->DrawClone("histsame");
      // extra lines
      for(int i=0;i<extra.GetEntries();i++) extra[i]->DrawClone("samehist");
      theData->DrawClone("sameaxis");
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
