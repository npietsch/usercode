#include "TH1D.h"
#include "TH2D.h"
#include "THStack.h"
#include "TCanvas.h"
#include "TStyle.h"
#include "TLegend.h"
#include <algorithm>
#include "TPaveText.h"
#include "TDRStyle_BtagEfficienciesAllEta.h"

class plotSet {
 private:
  TString Name;
  //  vector<TH1*> histos;

  static double global_event_weight;// = 1.;

  double hist_maximum(TH1*);
  double hist_minimum(TH1*);
  void setBounds(std::vector<TH1*>&, bool, bool);

  double hist_maximum2(TH2*);
  double hist_minimum2(TH2*);
  void setBounds2(std::vector<TH2*>&, bool, bool);

  map<TString, TCanvas*>      Canvases;
  map<TString, vector<TH1*> > HistosForCanvas;
  //map<TString, THStack* >     StackForCanvas;
  map<TString, vector<TString> > HistosToStack; //TStrings: Name of canvas, name of hist
  map<TString, vector<TH2*> > Histos2ForCanvas;
  map<TString, TString>       HistToHighlight;
  //vector<TString>             allHistos;
  map<TString, TString>       XaxisTitle;
  map<TString, TString>       YaxisTitle;
  map<TString, unsigned>      fixColors;
  map<TString, TString>       fixDrawStyles;
  map<TString, TString>       invisible;
  map<TString, TString>       signals;
  vector<TString>             logHistos;

  //unscaling not yet included:
  vector<TString>             HistosNotToScale;

  vector<pair<TString,TString> > HistosToRatio;
  bool ratiosDone;
  void doRatios();

  //STYLS:
  TString drawStyle;
  unsigned colors[10];
  unsigned lineWidth;

  TString HighlightedDrawStyle;
  unsigned HighlightedColor;
  unsigned HighlightedLineWidth;
  pair<unsigned, unsigned> CanvasSize;
  float PadMargins[4];
  unsigned fontStyle;
  float labelFontSize, titleFontSize;
  bool yLogScale, xLogScale, noHead, noStack;

  bool isNewCanvas(TString);
  bool isNewHisto(TString,TString);
  bool isNewHisto(TString h) { return isNewHisto(h,h); }
  bool isNewCanvas2(TString);
  bool isNewHisto2(TString,TString);

 public:

  plotSet(TString n) {
    Name = n;
    TH1* se = new TH1();
    se->SetDefaultSumw2(kTRUE);
    ratiosDone=false;
  }
  plotSet() {plotSet("");}

  TH1* touchThis(TString);

  //void setGlobalEventWeight( double w ) { global_event_weight = w; }

  void addPlot( TString,   TString,   int,   double,   double,   double,   double   );
  void addPlot( TString h, TString c, int b, double l, double u, double v           ) {
    addPlot(h,c,b,l,u,v,plotSet::global_event_weight); }

  void addPlot( TString h,            int b, double l, double u, double v, double w ) { 
    addPlot(h,h,b,l,u,v,w); }
  void addPlot( TString h,            int b, double l, double u, double v           ) { 
    addPlot(h,h,b,l,u,v,plotSet::global_event_weight); }

  void addPlot( TString h, TString c, int b, double l, double u, double v, double w, bool high) {
    if( high && isNewHisto(h,c) ) HighlightThis(h,c);
    addPlot(h,c,b,l,u,v,w); }
  void addPlot( TString h, TString c, int b, double l, double u, double v,           bool high) {
    addPlot(h,c,b,l,u,v,plotSet::global_event_weight,high); }

  void addPlot( TString h, TString c, int b, double l, double u, double v, double w, bool high, TString XT, TString YT ) {
    if( isNewHisto(h,c) ) SetAxesTitles(c,XT,YT);
    addPlot(h,c,b,l,u,v,w,high); }
  void addPlot( TString h, TString c, int b, double l, double u, double v,           bool high, TString XT, TString YT ) {
    addPlot(h,c,b,l,u,v,plotSet::global_event_weight,high,XT,YT); }

  void addPlot( TString h, TString c, int b, double l, double u, double v, double w,            TString XT, TString YT ) {
    if( isNewHisto(h,c) ) SetAxesTitles(c,XT,YT);
    addPlot(h,c,b,l,u,v,w); }
  void addPlot( TString h, TString c, int b, double l, double u, double v,                      TString XT, TString YT ) {
    addPlot(h,c,b,l,u,v,plotSet::global_event_weight,XT,YT); }

  void addPlot( TString h,            int b, double l, double u, double v, double w,            TString XT, TString YT ) {
    //if( isNewHisto(h,h) ) SetAxesTitles(h,XT,YT);
    addPlot(h,h,b,l,u,v,w,XT,YT); }
  void addPlot( TString h,            int b, double l, double u, double v,                      TString XT, TString YT ) {
    addPlot(h,h,b,l,u,v,plotSet::global_event_weight,XT,YT); }



  //void addPlot( TH1* );
  void addPlot( TH1*, TString, TString );

  void addPlot( TH1* h, TString n, TString t, double w) {
    h->Scale(w);
    addPlot(h,n,t);
  }

  void addPlot( TH1* h, TString n, TString t, double w, unsigned lc, unsigned fs){
    h->Scale(w);
    //h->SetFillColor(lc);
    //h->SetFillStyle(fs);
    //if(n=="G800") h->SetLineStyle(2);
    addPlot(h,n,t,lc);
      }

  void addPlot( TH1* h, TString n, TString t, unsigned fc ) {
    addPlot(h,n,t);
    fixColors[n] = fc;
  }
  void addPlot( TH2*, TString, TString );

  void addToStack( TH1* h, TString n, TString t) {
    addPlot(h,n,t);

    HistosToStack[t].push_back(n);
  }

  void addToStack( TH1* h, TString n, TString t, double w) {
    addPlot(h,n,t,w);
    HistosToStack[t].push_back(n);
  }

  void addToStack( TH1* h, TString n, TString t, unsigned fc ) {
    addPlot(h,n,t,fc);
    HistosToStack[t].push_back(n);
  }

  void addToStack( TH1* h, TString n, TString t,  double w, unsigned lc, unsigned fs, unsigned fc) {
    h->Scale(w);
    h->SetFillStyle(fs);
    h->SetFillColor(fc);
    addPlot(h,n,t,lc);
    HistosToStack[t].push_back(n);
  }

  void addPlot( TH1* h, TString n, TString t,  double w, unsigned lc, unsigned fs, unsigned fc) {
    if (fs==1101) addToStack(h,n,t,w,lc,fs,fc);
    else addPlot(h,n,t,w,lc,fs);
    if(w==1) fixDrawStyles[n]="P E";
    if(fc==0) signals[n]="n";
    if(lc==10) invisible[n]="n";
  }

  void scale(TString, TString, double);

  //2d:
  void addPlot( TString,
		int, double, double, double,
		int, double, double, double, double );
  void addPlot( TString h,
		int xb, double xl, double xu, double xv,
		int yb, double yl, double yu, double yv) {
    addPlot(h,xb,xl,xu,xv,
	    yb,yl,yu,yv,plotSet::global_event_weight); }
  void addPlot( TString h,
		int xb, double xl, double xu, double xv,
		int yb, double yl, double yu, double yv, double w, TString XT, TString YT ) {
    addPlot(h,xb,xl,xu,xv,
	    yb,yl,yu,yv,w);
    if( isNewHisto2(h,h) ) SetAxesTitles(h,XT,YT);
  }
  void addPlot( TString h,
		int xb, double xl, double xu, double xv,
		int yb, double yl, double yu, double yv, TString XT, TString YT ) {
    addPlot(h,xb,xl,xu,xv,
	    yb,yl,yu,yv,plotSet::global_event_weight);
    if( isNewHisto2(h,h) ) SetAxesTitles(h,XT,YT);
  }

  void ratioOf(TString, TString);

  void HighlightThis(TString, TString);

  void SetAxesTitles(TString, TString, TString);

  void SetLog(TString h) { logHistos.push_back(h); }

  //void loadHisto(TH1* h) { histos.push_back(h); }

  //void setRange()    { setBounds( histos, false, false ); }
  //void setLogRange() { setBounds( histos,  true, false ); }

  void printAll(TString);
  void printAll() {printAll("");}
  int print1D(map<TString, vector<TH1*> >::iterator);
  int print2D(map<TString, vector<TH2*> >::iterator);
  void saveAll(TString);

  void loadStyle(TString);
  template <typename T>
    void setStyles( T*&, TString );
};

double plotSet::global_event_weight=1.;

TH1* plotSet::touchThis(TString h) {
  for (map<TString, vector<TH1*> >::iterator ci=HistosForCanvas.begin(); ci!=HistosForCanvas.end(); ++ci) {
    for (size_t hi=0; hi<ci->second.size(); ++hi) {
      //cout<<"plotSet::touchThis: search for "<<h<<" found "<<ci->second.at(hi)->GetName()<<endl;
      if (ci->second.at(hi)->GetName() == h)
	return ci->second.at(hi);
    }
  }
  cout<<"plotSet::touchThis: histogram "<<h<<" not found!"<<endl;
  TH1* null = new TH1("null","null",10,0,10);
  return null;
}

void plotSet::HighlightThis(TString h, TString c) {
  //cout<<"......."<<endl;
  if( HistToHighlight.find(c) != HistToHighlight.end() )
    if( HistToHighlight.find(c)->second != h ) {
      cout<<"Highlighting in canvas "<<c<<" overwritten:"<<endl;
      cout<<"  "<<HistToHighlight.find(c)->second<<"  -->  "<<h<<endl;
    }
  HistToHighlight[c]=h; 
}

void plotSet::scale(TString h, TString c, double w) {
  if( HistosForCanvas.find(c) != HistosForCanvas.end() ) {
    for(unsigned i=0; i<HistosForCanvas[c].size(); ++i) {
      if(HistosForCanvas[c].at(i)->GetName() == h)
	HistosForCanvas[c].at(i)->Scale(w);
    }
  }
}


void plotSet::addPlot(TString name, TString can, int bins, double low, double up, double value, double weight) {

  if(isNewCanvas(can)) {
    TH1D* tmpH = new TH1D(name,can,bins,low,up);
    //tmpH->Sumw2();
    tmpH->Fill( value, weight );
    vector<TH1*> tmpV;
    tmpV.push_back( tmpH );
    HistosForCanvas[can] = tmpV;
  }
  else {
    int histNo = -1;
    for( size_t h = 0; h < HistosForCanvas[can].size() && histNo == -1; ++h)
      if( HistosForCanvas[can][h]->GetName() == name )
	histNo = h;

    if(histNo==-1) {// = Is New
      TH1D* tmpH = new TH1D(name,can,bins,low,up);
      tmpH->Sumw2();
      tmpH->Fill(value, weight);
      HistosForCanvas[can].push_back(tmpH);
    }
    else
      HistosForCanvas[can][histNo]->Fill(value, weight);
  }
}

void plotSet::addPlot(TH1* hist, TString histN, TString can) {
  hist->SetName(histN);
  hist->SetTitle("");
  if(isNewCanvas(can)) {
    vector<TH1*> tmpV;
    tmpV.push_back( hist );
    HistosForCanvas[can] = tmpV;
  }
  else {
    HistosForCanvas[can].push_back(hist);
  }
}

//TH2
void plotSet::addPlot(TH2* hist, TString histN, TString can) {
  hist->SetName(histN);
  hist->SetTitle(can);
  if(isNewCanvas2(can)) {
    vector<TH2*> tmpV;
    tmpV.push_back( hist );
    Histos2ForCanvas[can] = tmpV;
  }
  else {
    Histos2ForCanvas[can].push_back(hist);
  }
}

void plotSet::addPlot(TString name,
		      int xbins, double xlow, double xup, double xvalue, 
		      int ybins, double ylow, double yup, double yvalue, double weight ) {
  TString can = name;
  if(isNewCanvas2(can)) {
    TH2D* tmpH = new TH2D(name,name,xbins,xlow,xup,ybins,ylow,yup);
    tmpH->Fill( xvalue , yvalue, weight );
    vector<TH2*> tmpV;
    tmpV.push_back( tmpH );
    Histos2ForCanvas[can] = tmpV;
  }
  else {
    int histNo = -1;
    for( size_t h = 0; h < Histos2ForCanvas[can].size() && histNo == -1; ++h)
      if( Histos2ForCanvas[can][h]->GetTitle() == name )
	histNo = h;

    if(histNo==-1) {// = Is New
      TH2D* tmpH = new TH2D(name,name,xbins,xlow,xup,ybins,ylow,yup);
      tmpH->Fill( xvalue, yvalue, weight );
      Histos2ForCanvas[can].push_back(tmpH);
    }
    else
      Histos2ForCanvas[can][histNo]->Fill( xvalue, yvalue, weight );
  }
}

bool plotSet::isNewCanvas(TString c) {
  return (HistosForCanvas.find(c) == HistosForCanvas.end());
}

bool plotSet::isNewCanvas2(TString c) {
  return (Histos2ForCanvas.find(c) == Histos2ForCanvas.end());
}

bool plotSet::isNewHisto(TString h, TString c) {
  //  cout<<"new Can: "<<isNewCanvas(c)<<endl;
  if( isNewCanvas(c) ) return true;
  for( size_t i=0; i<HistosForCanvas[c].size(); ++i )
    if( HistosForCanvas[c].at(i)->GetTitle() == h ) return false;
  return true;
}

bool plotSet::isNewHisto2(TString h, TString c) {
  //  cout<<"new Can: "<<isNewCanvas(c)<<endl;
  if( isNewCanvas2(c) ) return true;
  for( size_t i=0; i<Histos2ForCanvas[c].size(); ++i )
    if( Histos2ForCanvas[c].at(i)->GetTitle() == h ) return false;
  return true;
}

void plotSet::SetAxesTitles(TString c, TString xt, TString yt) {
  if( XaxisTitle.find(c) != XaxisTitle.end() ) {
    if( XaxisTitle[c] != xt ) {
      cout<<"Title for x axis in canvas "<<c<<" overwritten:"<<endl;
      cout<<"  "<<XaxisTitle[c]<<"  -->  "<<xt<<endl;
      XaxisTitle[c] = xt;
    }
  }
  else
    XaxisTitle[c] = xt;

  if( YaxisTitle.find(c) != YaxisTitle.end() ) {
    if( YaxisTitle[c] != yt ) {
      cout<<"Title for y axis in canvas "<<c<<" overwritten:"<<endl;
      cout<<"  "<<YaxisTitle[c]<<"  -->  "<<yt<<endl;
      YaxisTitle[c] = yt;
    }
  }
  else
    YaxisTitle[c] = yt;
}


void plotSet::ratioOf(TString h1, TString h2) {
  pair<TString,TString> out;
  out.first = h1;
  out.second = h2;
  bool inR = false;
  for (size_t r=0; r<HistosToRatio.size(); ++r) {
    if (HistosToRatio.at(r).first==h1 && HistosToRatio.at(r).second==h2)
      inR = true;
  }
  if(!inR)
    HistosToRatio.push_back(out);
}

void plotSet::doRatios() {
  for (size_t r=0; r<HistosToRatio.size(); ++r) {
    TH1* hist1 = touchThis(HistosToRatio.at(r).first);
    TH1* hist2 = touchThis(HistosToRatio.at(r).second);
    TString rn = hist1->GetName();
    rn+= " over ";
    rn+= hist2->GetName();
    TString rt = hist1->GetTitle();
    rt+= " over ";
    rt+= hist2->GetTitle(); 
    TH1D* rhist = new TH1D();
    rhist = (TH1D*) hist1->Clone(rn);
    rhist->Divide(hist1,hist2,1,1);

    addPlot( rhist, rn, rt);

    HistosNotToScale.push_back(rn);
  }
}
void plotSet::printAll(TString style) {

  //any ratios?
  if(!ratiosDone)
    doRatios();
  ratiosDone=true;

  loadStyle(style);

  for( map<TString, vector<TH1*> >::iterator c = HistosForCanvas.begin(); c != HistosForCanvas.end(); ++c ) {
    print1D(c);
  }

  for( map<TString, vector<TH2*> >::iterator c = Histos2ForCanvas.begin(); c != Histos2ForCanvas.end(); ++c ) {
    print2D(c);
  }

}

void plotSet::saveAll(TString DSname) {

  TString fname = DSname;
  fname += "_";
  fname += Name;
  fname += ".root";
  TFile *outputFile = new TFile(fname, "RECREATE");
  
  //any ratios?
  if(!ratiosDone)
    doRatios();
  ratiosDone=true;


  for( map<TString, vector<TH1*> >::iterator c = HistosForCanvas.begin(); c != HistosForCanvas.end(); ++c )
    for( size_t h = 0; h < c->second.size(); ++h ) {
      if( XaxisTitle.find(c->first) != XaxisTitle.end() )
	c->second.at(h)->GetXaxis()->SetTitle( XaxisTitle[c->first] );
      if( YaxisTitle.find(c->first) != YaxisTitle.end() )
	c->second.at(h)->GetYaxis()->SetTitle( YaxisTitle[c->first] );
      c->second.at(h)->Write();
    }
  
  for( map<TString, vector<TH2*> >::iterator c = Histos2ForCanvas.begin(); c != Histos2ForCanvas.end(); ++c )
    for( size_t h = 0; h < c->second.size(); ++h )
      c->second.at(h)->Write();
  
  outputFile->Close();
}

int plotSet::print1D( map<TString, vector<TH1*> >::iterator c )
{
  gStyle->SetOptStat(0);

  TCanvas* tmpC = new TCanvas(c->first,c->first,CanvasSize.first,CanvasSize.second );
  Canvases[c->first] = tmpC;
  tmpC->cd();
  float legSize = .05 + (.05*min((int)c->second.size(),4));
  TLegend *leg = new TLegend(.65,.6,.99,.99);
  leg->SetTextFont(42);
  leg->SetFillColor(0);
  leg->SetLineColor(0);
  
  if(yLogScale) gPad->SetLogy();
  
  setBounds( c->second, yLogScale, false);
  
  PadMargins[1] = 0.03;
  PadMargins[3] = legSize + .02;
  
  gPad->SetMargin(PadMargins[0],PadMargins[1],PadMargins[2],PadMargins[3]);
  
  if( c->second.size()==0 ) return 0;
  
  TH1* nu = (TH1*) c->second.at(0)->Clone(c->first+"nu");
  //TH1* nu = new TH1();
  setStyles( nu , c->first );
  nu->Draw(drawStyle);
  
  bool theFirst=false;//true;
  bool theFirstInStack=true;
  THStack *tmpStk = new THStack(c->first, c->first);
  for( size_t h = 0; h < c->second.size(); ++h )
    {

      if(fixDrawStyles.find(c->second.at(h)->GetName()) != fixDrawStyles.end())
	{
	  drawStyle=fixDrawStyles[c->second.at(h)->GetName()];
	}      
      else drawStyle="HIST";
      
      if(c->second.at(h)->GetName() == HistToHighlight[c->first] )
	{
	  //WARUM STEHT HIER GetTitle() UND NICHT GetName()
	  c->second.at(h)->SetLineWidth(HighlightedLineWidth);
	  //c->second.at(h)->SetLineColor( HighlightedColor );
	}
      else
	c->second.at(h)->SetLineWidth(lineWidth);
      //if( find(fixColors.begin(), fixColors.end(),c->second.at(h)->GetName()) != fixColors.end())
      if( fixColors.find( c->second.at(h)->GetName() ) != fixColors.end())
	{
	  c->second.at(h)->SetLineColor(fixColors[c->second.at(h)->GetName()]);
	}	    
      else
	{
	  c->second.at(h)->SetLineColor( h<10 ? colors[h] : 1 );
	}

      //if(fixDrawStyles.find(c->second.at(h)->GetName()) == "P" )
      //if(fixDrawStyles.find(c->second.at(h)->GetName()) != fixDrawStyles.end()) drawStyle=fixDrawStyles[c->second.at(h)->GetName()];
      //	{
      //  std::cout << c->second.at(h)->GetName() << std::endl;
      //x}
/* 	{ */
/* 	  std::cout << "Hallo"  << std::endl; //drawStyle=fixDrawStyle[c->second.at(h)->GetName]; */
/* 	} */
      TString tmpName = c->second.at(h)->GetName();
      if( !noStack &&
	  find(HistosToStack[c->first].begin(),HistosToStack[c->first].end(),tmpName)
	  != HistosToStack[c->first].end() ) {
	tmpStk->Add(c->second.at(h));
	if( theFirstInStack ) theFirst ? tmpStk->Draw(drawStyle) : 
	  tmpStk->Draw(drawStyle+" sames");
	theFirst=false;
	theFirstInStack=false;
	/*       setStyles( tmpStk , c->first ); */
      }
      else {
	theFirst ? c->second.at(h)->Draw(drawStyle) :
	  c->second.at(h)->Draw(drawStyle+" sames");
	theFirst=false;
	//setStyles( c->second.at(h) , c->first );
      }
      if(invisible.find(c->second.at(h)->GetName()) == invisible.end())
	{
	  if(fixDrawStyles.find(c->second.at(h)->GetName()) != fixDrawStyles.end())
	    {
	      leg->AddEntry(c->second.at(h),c->second.at(h)->GetName(),"l E");
	    }
	  else if(signals.find(c->second.at(h)->GetName()) != signals.end())
	    {
	      leg->AddEntry(c->second.at(h),c->second.at(h)->GetName(),"l");
	    }      
	  else leg->AddEntry(c->second.at(h),c->second.at(h)->GetName(),"f");
	}
    }

  TPaveText *label = new TPaveText(0.15,0.81,0.45,0.9,"NDC");
  label->SetFillColor(0);
  label->SetTextFont(42);
  label->SetBorderSize(1);
  TText *text=label->AddText("L=4.98 fb^{-1}");
  text->SetTextAlign(22);
  label->Draw("same");

  gPad->RedrawAxis();

  leg->Draw();
  if( !theFirstInStack ) setStyles( tmpStk , c->first );
  //setStyles( c->second.at(0) , c->first );
  /*   if(yLogScale) gPad->SetLogy(); */
  
  /*   setBounds( c->second, yLogScale, false); */
  
  /*   PadMargins[1] = 0.03; */
  /*   PadMargins[3] = legSize + .02; */
  
  /*  
      gPad->SetMargin(PadMargins[0],PadMargins[1],PadMargins[2],PadMargins[3]); */
  //tmpC->Modified();
  //tmpC->Update();
  
  tmpC->SaveAs(c->first+"_tight.pdf");

  return 1;
}


//
/* int plotSet::print1D( map<TString, vector<TH1*> >::iterator c ) */
/* { */
/*   gStyle->SetOptStat(0); */

/*   TCanvas* tmpC = new TCanvas( c->first,c->first,CanvasSize.first,CanvasSize.second ); */
/*   Canvases[c->first] = tmpC; */
/*   tmpC->cd(); */
/*   float legSize = .05 + (.05*min((int)c->second.size(),4)); */
/*   TLegend *leg = new TLegend(.25,.99-legSize,.99,.99); */
/*   leg->SetTextFont(42); */
/*   leg->SetFillColor(0); */
/*   leg->SetLineColor(0); */
    
/*   if( c->second.size()==0 ) return 0; */


/*   bool theFirst=true; */
/*   bool theFirstInStack=true; */
/*   THStack *tmpStk = new THStack(c->first, c->first); */
/*   for( size_t h = 0; h < c->second.size(); ++h ) { */
/*     if(c->second.at(h)->GetName() == HistToHighlight[c->first] ) {// WARUM STEHT HIER GetTitle() UND NICHT GetName() */
/*       c->second.at(h)->SetLineWidth(HighlightedLineWidth); */
/*       //c->second.at(h)->SetLineColor( HighlightedColor ); */
/*     } else */
/*       c->second.at(h)->SetLineWidth(lineWidth); */
/*     //if( find(fixColors.begin(), fixColors.end(), c->second.at(h)->GetName()) != fixColors.end()) */
/*     if( fixColors.find( c->second.at(h)->GetName() ) != fixColors.end()) */
/*       c->second.at(h)->SetLineColor(fixColors[c->second.at(h)->GetName()]); */
/*     else */
/*       { */
/*  	c->second.at(h)->SetLineColor( h<10 ? colors[h] : 1 ); */
/* /\* 	c->second.at(h)->SetFillColor(h<10 ? colors[h] : 1 ); *\/ */
/* /\* 	c->second.at(h)->SetFillStyle(3004); *\/ */
/*       } */
/*     TString tmpName = c->second.at(h)->GetName(); */
/*     if( !noStack && find(HistosToStack[c->first].begin(),HistosToStack[c->first].end(),tmpName) != HistosToStack[c->first].end() ) { */
/*       tmpStk->Add(c->second.at(h)); */
/*       if( theFirstInStack ) theFirst ? tmpStk->Draw(drawStyle) :  tmpStk->Draw(drawStyle+" sames"); */
/*       theFirst=false; */
/*       theFirstInStack=false; */
/* /\*       setStyles( tmpStk , c->first ); *\/ */
/*     } */
/*     else { */
/*       theFirst ? c->second.at(h)->Draw(drawStyle) : c->second.at(h)->Draw(drawStyle+" sames"); */
/*       theFirst=false; */
/*       setStyles( c->second.at(h) , c->first ); */
/*     } */
/*     leg->AddEntry(c->second.at(h),c->second.at(h)->GetName(),"l"); */
/*   } */

/*   leg->Draw(); */
/*   if( !theFirstInStack ) setStyles( tmpStk , c->first ); */

/*   if(yLogScale) gPad->SetLogy(); */

/*   setBounds( c->second, yLogScale, false); */
 
/*   PadMargins[1] = 0.03; */
/*   PadMargins[3] = legSize + .02; */

/*   gPad->SetMargin(PadMargins[0],PadMargins[1],PadMargins[2],PadMargins[3]); */
/*   //tmpC->Modified(); */
/*   //tmpC->Update(); */

/*   tmpC->SaveAs(c->first+".pdf"); */

/*   return 1; */
/* } */

template <typename T>
void plotSet::setStyles(T*& hist, TString name) {
    
  if(noHead)
    hist->SetTitle("");

  if( XaxisTitle.find(name) != XaxisTitle.end() )
    hist->GetXaxis()->SetTitle( XaxisTitle[name] );
  //if( YaxisTitle.find(name) != YaxisTitle.end() )
  hist->GetYaxis()->SetTitle("events");
  hist->GetYaxis()->CenterTitle();
  hist->GetXaxis()->CenterTitle();

  hist->GetXaxis()->SetLabelSize(labelFontSize);
  hist->GetYaxis()->SetLabelSize(labelFontSize);
  
  hist->GetXaxis()->SetTitleSize(titleFontSize);
  hist->GetYaxis()->SetTitleSize(titleFontSize);
  
  hist->GetXaxis()->SetLabelFont(fontStyle);
  hist->GetYaxis()->SetLabelFont(fontStyle);
  
  hist->GetXaxis()->SetTitleFont(fontStyle);
  hist->GetYaxis()->SetTitleFont(fontStyle);
}

int plotSet::print2D(map<TString, vector<TH2*> >::iterator c) {


    TCanvas* tmpC = new TCanvas( c->first,c->first,CanvasSize.first,CanvasSize.second );
    Canvases[c->first] = tmpC;
    tmpC->cd();
    float legSize = .05 + (.05* min((int)c->second.size(),4));
    TLegend *leg = new TLegend(.25,.5,.95,.99);
    leg->SetTextFont(42);
    leg->SetFillColor(0);
    leg->SetLineColor(0);
    
    if( c->second.size()==0 ) return 0;
    for( size_t h = 0; h < c->second.size(); ++h ) {

      if(c->second.at(h)->GetTitle() == HistToHighlight[c->first] ) {
	c->second.at(h)->SetLineWidth(HighlightedLineWidth);
	c->second.at(h)->SetLineColor( HighlightedColor );
      } else {
	c->second.at(h)->SetLineWidth(lineWidth);
	c->second.at(h)->SetLineColor( h<10 ? colors[h] : 1 );
      }
      h==0 ? c->second.at(h)->Draw(drawStyle) : c->second.at(h)->Draw(drawStyle+" sames");
      leg->AddEntry(c->second.at(h),c->second.at(h)->GetName(),"l");
    }

    leg->Draw();

    if(yLogScale) {
      setBounds2( c->second, true, false);
      gPad->SetLogy();
    }
    else setBounds2( c->second, false, false);

    if(noHead)
      c->second.at(0)->SetTitle("");

    if( XaxisTitle.find(c->first) != XaxisTitle.end() )
      c->second.at(0)->GetXaxis()->SetTitle( XaxisTitle[c->first] );
    if( YaxisTitle.find(c->first) != YaxisTitle.end() )
      c->second.at(0)->GetYaxis()->SetTitle( YaxisTitle[c->first] );

    c->second.at(0)->GetXaxis()->SetLabelSize(labelFontSize);
    c->second.at(0)->GetYaxis()->SetLabelSize(labelFontSize);

    c->second.at(0)->GetXaxis()->SetTitleSize(titleFontSize);
    c->second.at(0)->GetYaxis()->SetTitleSize(titleFontSize);

    c->second.at(0)->GetXaxis()->SetLabelFont(fontStyle);
    c->second.at(0)->GetYaxis()->SetLabelFont(fontStyle);

    c->second.at(0)->GetXaxis()->SetTitleFont(fontStyle);
    c->second.at(0)->GetYaxis()->SetTitleFont(fontStyle);

    PadMargins[1] = 0.03;
    PadMargins[3] = legSize + .02;

    gPad->SetMargin(PadMargins[0],PadMargins[1],PadMargins[2],PadMargins[3]);
    return 1;
}

	      
double plotSet::hist_maximum(TH1* h) { const int i = h->GetMaximumBin();   return h->GetBinContent(i) + h->GetBinError(i);}

double plotSet::hist_minimum(TH1* h) { 
  int min_bin=h->GetMaximumBin(); 
  for(int x=0; x<=h->GetNbinsX()+1; x++) {
    for(int y=0; y<=h->GetNbinsY(); y++) {
      int bin = h->GetBin(x,y);
      if( h->GetBinContent(bin) !=0 && h->GetBinContent(bin) < h->GetBinContent(min_bin) )
        min_bin = bin;
    }
  }
  return h->GetBinContent(min_bin);
}

void plotSet::setBounds(std::vector<TH1*>& hist, bool log, bool twoD) {
  if (hist.empty()) return;

  size_t i_max(0),i_min(0);

  for(size_t i=0; i<hist.size(); i++) {
    if(!hist[i_max] || (hist[i] && hist_maximum(hist[i]) > hist_maximum(hist[i_max] )) ) i_max=i;
    if( !hist[i_min] || (hist[i] && hist_minimum(hist[i]) < hist_minimum(hist[i_min])) ) i_min=i;
  }

  // In the case of empty histograms, set an arbitrary range.
  // Otherwise this can cause a TPad::Range exception when drawing.
  double Max = hist_maximum(hist[i_max])*(log? 2.5 : 1.05);
  double min = log ? 0.5 * (max(hist_minimum(hist[i_min]), 0.4)) : 0;
  //double min = log ? 0.1 : 0;
  if (Max <= min)   Max = min + 1;


  for(unsigned i=0; i<hist.size(); i++) {
    if(hist[i]) hist[i]->SetMaximum(Max);
    if(hist[i]) hist[i]->SetMinimum(min);
  }
}


double plotSet::hist_maximum2(TH2* h) { const int i = h->GetMaximumBin();   return h->GetBinContent(i) + h->GetBinError(i);}

double plotSet::hist_minimum2(TH2* h) { 
  int min_bin(h->GetMaximumBin());
  for(int x=0; x<=h->GetNbinsX()+1; x++) {
    for(int y=0; y<=h->GetNbinsY(); y++) {
      int bin = h->GetBin(x,y);
      if( h->GetBinContent(bin) !=0 && h->GetBinContent(bin) < h->GetBinContent(min_bin) )
        min_bin = bin;
    }
  }
  return h->GetBinContent(min_bin);
}

void plotSet::setBounds2(std::vector<TH2*>& hist, bool log, bool twoD) {
  if (hist.empty()) return;

  size_t i_max(0),i_min(0);
  for(size_t i=0; i<hist.size(); i++) {
    if(!hist[i_max] || (hist[i] && hist_maximum(hist[i]) > hist_maximum(hist[i_max])) ) i_max=i;
    if(!hist[i_min] || (hist[i] && hist_minimum(hist[i]) < hist_minimum(hist[i_min])) ) i_min=i;
  }

  // In the case of empty histograms, set an arbitrary range.
  // Otherwise this can cause a TPad::Range exception when drawing.
  double max = hist_maximum(hist[i_max]) * (log? 2.5 : 1.15);
  //  double min = log ? 0.05 * hist_minimum(hist[i_min]) : 0;
  double min = log ? 0.1 : 0;
  if (max <= min)   max = min + 1;


  for(unsigned i=0; i<hist.size(); i++) {
    if(hist[i]) hist[i]->SetMaximum(max);
    if(hist[i]) hist[i]->SetMinimum(min);
  }
}

void plotSet::loadStyle(TString style) {
  gROOT->SetStyle("Plain");
  gStyle->SetPalette(1);
  drawStyle="HIST";
  colors[0] = 1;
  colors[1] = 2;
  colors[2] = 3;
  colors[3] = 4;
  colors[4] = 5;
  colors[5] = 6;
  colors[6] = 7;
  colors[7] = 8;
  colors[8] = 9;
  colors[9] = 10;

  lineWidth=2;
  HighlightedDrawStyle="";
  HighlightedColor=1;
  HighlightedLineWidth=4;
  CanvasSize.first=700;
  CanvasSize.second=700;
  PadMargins[0]=.1;//left
  PadMargins[1]=.1;//right
  PadMargins[2]=.1;//bottom
  PadMargins[3]=.1;//top

  fontStyle=42;
  labelFontSize =.04;
  titleFontSize =.045; 

  yLogScale = false;
  noHead    = false;
  noStack   = false;
 
  vector<TString> allStyles;
  int pos_beg = 0;
  int pos_end = 0;

  while( pos_beg < style.Sizeof() ) {
    int p;
    for( p=pos_beg; p<style.Sizeof(); ++p ) {
      if( style(p,1) == " " ) break;
    }
    //cout << " ******** " << p <<endl;

    pos_end = p;

    allStyles.push_back( style( pos_beg, pos_end-pos_beg ) );
    pos_beg = pos_end+1;
  }

  for(size_t i=0; i<allStyles.size(); ++i)
    if( allStyles.at(i) == "kcolor") {
      colors[0] = kBlack;
      colors[1] = kRed+1;
      colors[2] = kSpring-6;
      colors[3] = kBlue-4;
      colors[4] = kCyan+1;
      colors[5] = kMagenta-7;
      colors[6] = kGreen-6;
      colors[7] = kGray+1;
      colors[8] = kBlue+2;
      colors[9] = kRed-7;
    }
    else if (allStyles.at(i) == "ylog")
      yLogScale=true;
    else if (allStyles.at(i) == "noHead")
      noHead=true;
    else if (allStyles.at(i) == "noStack")
      noStack=true;
    else if (allStyles.at(i) == "COLZ")
      drawStyle="COLZ";
    else if (allStyles.at(i) == "BOX")
      drawStyle="BOX";
    else cout<<" +++ Style "<<allStyles.at(i)<<" not known."<<endl;
}



template<typename T>
void plotAllThese(vector<T*> hist) {
  int colors[10] = {1,2,3,4,5,6,7,8,9,10};

//   TCanvas* eeMassLEADEID3 = new TCanvas("eeMassLEADEID3","eeMassLEADEID3",800,800);
//   eeMassLEADEID3->cd();
//   gPad->SetLogy();



  for( size_t i=0; i<hist.size(); ++i )
    {
      hist.at(i)->SetLineColor(colors[i]);
      hist.at(i)->SetLineWidth(2);
      if(i==0) hist.at(i)->Draw();
      else hist.at(i)->Draw("sames");
    }

}
