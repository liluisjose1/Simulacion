///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Mar  1 2018)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#ifndef __NONAME_H__
#define __NONAME_H__

#include <wx/artprov.h>
#include <wx/xrc/xmlres.h>
#include <wx/string.h>
#include <wx/stattext.h>
#include <wx/gdicmn.h>
#include <wx/font.h>
#include <wx/colour.h>
#include <wx/settings.h>
#include <wx/textctrl.h>
#include <wx/button.h>
#include <wx/sizer.h>
#include <wx/frame.h>

///////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////
/// Class MyFrame1
///////////////////////////////////////////////////////////////////////////////
class MyFrame1 : public wxFrame 
{
	private:
	
	protected:
		wxStaticText* m_staticText3;
		wxTextCtrl* txt1;
		wxStaticText* m_staticText31;
		wxTextCtrl* txt2;
		wxStaticText* m_staticText311;
		wxTextCtrl* txt3;
		wxStaticText* m_staticText3111;
		wxTextCtrl* txtr;
		wxButton* m_button2;
		wxButton* m_button3;
		
		// Virtual event handlers, overide them in your derived class
		virtual void evenProcesar( wxCommandEvent& event ) { event.Skip(); }
		virtual void evetSalir( wxCommandEvent& event ) { event.Skip(); }
		
	
	public:
		
		MyFrame1( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxEmptyString, const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 250,300 ), long style = wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL );
		
		~MyFrame1();
	
};

#endif //__NONAME_H__
